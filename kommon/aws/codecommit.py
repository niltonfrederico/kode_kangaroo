from ..decorators import snakecase_dict

from ..clients import BaseAwsClient
from ..choices import Choices


SORT_BY = Choices(
    ("repositoryName", "REPOSITORY_NAME", "repositoryName"),
    ("lastModifiedDate", "LAST_MODIFIED_DATE", "lastModifiedDate"),
)

ORDER = Choices(
    ("ascending", "ASCENDING", "ascending"), ("descending", "DESCENDING", "descending")
)


class CodeCommitClient(BaseAwsClient):

    service = "codecommit"

    @snakecase_dict
    def list_repositories(
        self, next_token=None, sort_by=SORT_BY.REPOSITORY_NAME, order_by=ORDER.ASCENDING
    ):
        data = self._prepare_args(
            **{"nextToken": next_token, "sortBy": sort_by, "order": order_by}
        )
        response = self.client.list_repositories(**data)

        return response.get("repositories")
