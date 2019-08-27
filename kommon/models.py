from datetime import datetime

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer, DateTime


class BaseModel:

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
