import boto3

class BaseAwsClient:
    service = None
    
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def client(self):
        return boto3.client(service)

    