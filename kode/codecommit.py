from kommon.decorators import snakecase_dict

from kommon.clients import BaseAwsClient
from kommon.choices import Choices


SORT_BY = Choices(
    ("repositoryName", "REPOSITORY_NAME", "repositoryName"),
    ("lastModifiedDate", "LAST_MODIFIED_DATE", "lastModifiedDate"),
)

ORDER = Choices(
    ("ascending", "ASCENDING", "ascending"), ("descending", "DESCENDING", "descending")
)


class CodeCommitClient(BaseAwsClient):

    service = "codecommit"

    @property
    def exceptions(self):
        return self.client.exceptions

    @snakecase_dict
    def list_repositories(
        self, next_token=None, sort_by=SORT_BY.REPOSITORY_NAME, order_by=ORDER.ASCENDING
    ):
        data = self._prepare_args(
            **{"nextToken": next_token, "sortBy": sort_by, "order": order_by}
        )
        response = self.client.list_repositories(**data)

        return response.get("repositories")

    @snakecase_dict
    def get_repository(self, name):
        """
        May raise botocore.errorfactory.RepositoryDoesNotExistException
        Capture with client.exceptions.RepositoryDoesNotExistException
        """
        response = self.client.get_repository(repositoryName=name)

        return response.get("repositoryMetadata")
