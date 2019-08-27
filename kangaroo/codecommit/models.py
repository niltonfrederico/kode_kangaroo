from sqlalchemy_utils.types.choice import ChoiceType
from sqlalchemy_utils.types.uuid import UUIDType
from kommon.models import BaseModel
from sqlalchemy import Column, String


class IssueModel(BaseModel):

    TYPES = ["open", "closed"]

    repository_id = Column(UUIDType(binary=False), primary_key=True)
    name = Column(String)
    text = Column(String)
    status = Column(ChoiceType(TYPES))
