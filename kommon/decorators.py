from .utils import dict_keys_to_snakecase


def snakecase_dict(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)

        if type(response) not in (dict, list):
            raise TypeError("Function return must be a dict or list of dicts.")

        if type(response) is list:
            return [dict_keys_to_snakecase(r) for r in response]

        return dict_keys_to_snakecase(response)

    return wrapper
