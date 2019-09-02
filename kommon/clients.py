import re
import boto3


class BaseAwsClient:
    service = None

    def __init__(self, *args, **kwargs):
        pass

    @property
    def client(self):
        return boto3.client(self.service)

    def _prepare_args(self, **kwargs):
        return {k: v for k, v in kwargs.items() if v is not None}
