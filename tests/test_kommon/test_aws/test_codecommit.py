import pytest

from kommon.aws.codecommit import CodeCommitClient


@pytest.fixture(name="client")
def fixture_client():
    return CodeCommitClient()


def test_fetch_all_repositories(client):
    results = client.list_repositories()

    assert type(results) == list
    assert type(results[0]) == dict if len(results) > 0 else True
