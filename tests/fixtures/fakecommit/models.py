from sqlalchemy import Column, String, Integer, Text
from datetime import datetime

from sqlalchemy_utils.types import UUIDType, URLType

from kommon.db import BaseModel


timestamp_now = datetime.now().timestamp()


class FakeRepository(BaseModel):  # noqa
    account_id = Column(Integer(), default="123456789")
    repository_id = Column(UUIDType(binary=False), primary_key=True)
    repository_name = Column(String())
    repository_description = Column(Text())
    default_branch = Column(String(), default="master")
    last_modified_date = Column(String(), default=timestamp_now)
    creation_date = Column(String(), default=timestamp_now)
    clone_url_http = Column(URLType(), default="https://fakeurl.fake")
    clone_url_ssh = Column(URLType(), default="ssh://fakeurl.fake")
    arn = Column(
        String(), default="arn:aws:codecommit:us-east-1:123456789:fake_repository"
    )
