from ..clients import BaseAwsClient
from ..choices import Choices


SORT_BY = Choices(
    ("REPOSITORY_NAME", "repositoryName", "repositoryName"),
    ("LAST_MODIFIED_DATE", "lastModifiedDate", "lastModifiedDate"),
)

ORDER = Choices(
    ("ASCENDING", "ascending", "ascending"), ("DESCENDING", "descending", "descending")
)


class CodeCommitClient(BaseAwsClient):
    def list_repositories(
        self, next_token=None, sort_by=SORT_BY.REPOSITORY_NAME, order_by=ORDER.ASCENDING
    ):
        return self.client(nextToken=next_token, sortBy=sort_by, order=order_by)
