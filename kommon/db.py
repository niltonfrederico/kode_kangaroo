from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .models import BaseModel as DbBaseModel
from .settings import DATABASE_URI

Session = sessionmaker()

engine = create_engine(DATABASE_URI)

session = Session(bind=engine)
BaseModel = declarative_base(cls=DbBaseModel)
