import pytest

from kode.codecommit import CodeCommitClient


@pytest.fixture(name="client")
def fixture_client():
    return CodeCommitClient()


def test_fetch_all_repositories(client):
    results = client.list_repositories()

    assert type(results) == list
    assert type(results[0]) == dict if len(results) > 0 else True


def test_fetch_get_repository(client):
    result = client.get_repository("old_town_road")

    assert type(result) is dict
    assert result["repository_name"] == "old_town_road"


def test_fetch_get_non_existing_repository(client):
    with pytest.raises(client.exceptions.RepositoryDoesNotExistException):
        client.get_repository("fake_repo")
