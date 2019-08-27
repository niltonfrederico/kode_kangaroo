import pytest

from datetime import datetime

from kommon.db import session
from kommon.models import BaseModel


@pytest.mark.skip()
@pytest.fixture(name="base_model")
def fixture_base_model():
    model = BaseModel()
    session.add(model)
    session.commit()

    return model


@pytest.mark.skip()
def test_base_model(base_model):
    assert type(base_model.id) == int
    assert type(base_model.created_at) == datetime
    assert base_model.updated_at is None
    assert base_model.__tablename__ == "basemodel"
