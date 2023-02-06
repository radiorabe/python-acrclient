from typing import Any, Optional

from requests import get
from requests.auth import AuthBase
from requests.models import PreparedRequest, Response

from .models import GetBmCsProjectsResultsParams


class _Auth(AuthBase):  # pylint: disable=too-few-public-methods
    """Bearer token style auth for ACRCloud."""

    def __init__(self, bearer_token: str) -> None:
        self.bearer_token = bearer_token

    def __call__(self, request: PreparedRequest) -> PreparedRequest:
        request.headers["Authorization"] = f"Bearer {self.bearer_token}"
        return request


class Client:
    """ACRCloud client to fetch metadata.

    Args:
        bearer_token: The bearer token for ACRCloud.
    """

    def __init__(self, bearer_token: str, base_url="https://eu-api-v2.acrcloud.com"):
        self.base_url = base_url
        self.auth = _Auth(bearer_token=bearer_token)

    def get(self, path: str, params: Any = None, **kwargs) -> Response:
        """Fetch JSON data from ACRCloud API with set Access Key param."""
        url = f"{self.base_url}{path}"
        if not kwargs.get("timeout"):
            kwargs["timeout"] = 10

        # pylint: disable-next=missing-timeout
        response = get(url=url, auth=self.auth, params=params, **kwargs)
        response.raise_for_status()
        return response

    def json(self, path: str, params: Any = None, **kwargs) -> Any:
        response = self.get(path, params=params, **kwargs)
        return response.json()

    def get_bm_cs_projects_results(
        self,
        project_id: int,
        stream_id: str,
        params: Optional[GetBmCsProjectsResultsParams] = None,
        **kwargs,
    ) -> Any:
        return self.json(
            path=f"/api/bm-cs-projects/{project_id}/streams/{stream_id}/results",
            params=params,
            **kwargs,
        ).get("data")
