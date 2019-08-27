import re
import boto3

# TODO: Move me to kommon.utils
first_cap_re = re.compile("(.)([A-Z][a-z]+)")
all_cap_re = re.compile("([a-z0-9])([A-Z])")


class BaseAwsClient:
    service = None

    def __init__(self, *args, **kwargs):
        pass

    @property
    def client(self):
        return boto3.client(self.service)

    def _prepare_args(self, **kwargs):
        return {k: v for k, v in kwargs.items() if v is not None}

    def _prepare_response(self, response):
        converted_dict = {}
        for k, v in response.items():
            new_v = v
            if isinstance(v, dict):
                new_v = self._prepare_response(v)
            elif isinstance(v, list):
                new_v = list()
                for x in v:
                    new_v.append(self._prepare_response(x))
            converted_dict[self._convert_camelcase_to_snakecase(k)] = new_v
        return converted_dict

    # TODO: Move me to kommon.utils
    def _convert_camelcase_to_snakecase(self, string):
        s1 = first_cap_re.sub(r"\1_\2", string)
        return all_cap_re.sub(r"\1_\2", s1).lower()
