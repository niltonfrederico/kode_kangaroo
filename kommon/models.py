from datetime import datetime

from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy import Column, Integer, DateTime


@as_declarative()
class BaseModel:

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
