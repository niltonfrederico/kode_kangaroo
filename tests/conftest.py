import pytest
from kommon.db import BaseModel, engine


@pytest.yield_fixture(name="db", autouse=True, scope="module")
def fixture_db():
    engine.connect()
    BaseModel.metadata.create_all(engine)
    yield engine
    BaseModel.metadata.drop_all(engine)
