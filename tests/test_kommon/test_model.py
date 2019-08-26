from datetime import datetime

from kommon.db import session
from kommon.models import BaseModel


def test_base_model():
    model = BaseModel()
    session.add(model)
    session.commit()

    assert type(model.id) == int
    assert type(model.created_at) == datetime
    assert model.updated_at is None
    assert model.__tablename__ == "basemodel"
