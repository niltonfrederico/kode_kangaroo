from uuid import uuid4, UUID
from datetime import datetime

import pytest

from kommon.db import session
from kangaroo.models import IssueModel, ISSUE_STATUS


@pytest.fixture(name="issue_model")
def fixture_issue_model():
    model = IssueModel()
    model.repository_uid = str(uuid4())
    model.name = "fake_name"
    model.text = "fake_text"
    model.status = ISSUE_STATUS.open
    session.add(model)
    session.commit()

    return model


def test_issue_model_create(issue_model):
    assert issue_model.__tablename__ == "issue"
    assert type(issue_model.id) == int

    assert type(issue_model.repository_uid) == UUID
    assert issue_model.name == "fake_name"
    assert issue_model.text == "fake_text"
    assert issue_model.status == ISSUE_STATUS.open

    assert type(issue_model.created_at) == datetime
    assert issue_model.updated_at is None
