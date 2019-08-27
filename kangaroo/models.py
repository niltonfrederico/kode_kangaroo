from sqlalchemy import Column, String
from sqlalchemy_utils.types.choice import ChoiceType
from sqlalchemy_utils.types.uuid import UUIDType

from kommon.db import BaseModel
from kommon.choices import Choices


ISSUE_STATUS = Choices(("closed", "closed"), ("open", "open"))


class IssueModel(BaseModel):  # noqa
    repository_uid = Column(UUIDType(binary=False), unique=True)
    name = Column(String)
    text = Column(String)
    status = Column(ChoiceType(ISSUE_STATUS))
