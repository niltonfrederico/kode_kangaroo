from datetime import datetime

import pytest

from kommon.db import session
from kangaroo.codecommit.models import IssueModel, ISSUE_STATUS


@pytest.fixture(name="issue_model")
def fixture_issue_model():
    model = IssueModel()
    model.respository_uid = "fake_uid"
    model.name = "fake_name"
    model.text = "fake_text"
    model.status = ISSUE_STATUS.open
    session.add(model)
    session.commit()

    return model


def test_issue_model_create(issue_model):
    assert issue_model.__tablename__ == "issuemodel"
    assert type(issue_model.id) == int

    assert type(issue_model.repository_uid) == "fake_uid"
    assert type(issue_model.name) == "fake_name"
    assert type(issue_model.text) == "fake_text"
    assert type(issue_model.status) == ISSUE_STATUS.open

    assert type(issue_model.created_at) == datetime
    assert issue_model.updated_at is None
