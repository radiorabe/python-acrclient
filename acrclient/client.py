from typing import Any, Optional

from requests import Session
from requests.adapters import HTTPAdapter, Retry
from requests.auth import AuthBase
from requests.models import PreparedRequest, Response

from .models import (
    GetBmCsProjectsResultsParams,
    GetBmCsProjectsResultsResponse,
    GetBmCsProjectsResultsResponseRecord,
    ListBmCsProjectsParams,
    ListBmCsProjectsResponse,
    ListBmCsProjectsResponseRecord,
    ListBmCsProjectsStreamsParams,
    ListBmCsProjectsStreamsResponse,
    ListBmCsProjectsStreamsResponseRecord,
)


class _Auth(AuthBase):  # pylint: disable=too-few-public-methods
    """Bearer token style auth for ACRCloud."""

    def __init__(self, bearer_token: str) -> None:
        self.bearer_token = bearer_token

    def __call__(self, request: PreparedRequest) -> PreparedRequest:
        request.headers["Authorization"] = f"Bearer {self.bearer_token}"
        return request


class Client:
    """ACRCloud client to fetch metadata."""
    def __init__(
        self,
        bearer_token: str,
        base_url: str = "https://api-v2.acrcloud.com",
        retries: int = 5,
        backoff_factor: float = 0.1,
    ):
        """
        Parameters:
            bearer_token: The bearer token for ACRCloud.
        """
        self.base_url = base_url
        self.auth = _Auth(bearer_token=bearer_token)
        self._session = Session()
        self._session.mount(
            "https://",
            HTTPAdapter(
                max_retries=Retry(
                    total=retries,
                    backoff_factor=backoff_factor,
                )
            ),
        )

    def get(
        self,
        path: str,
        params: Any = None,
        **kwargs,
    ) -> Response:
        """Fetch JSON data from ACRCloud API with set Access Key param."""
        url = f"{self.base_url}{path}"
        if not kwargs.get("timeout"):
            kwargs["timeout"] = 60

        # pylint: disable-next=missing-timeout
        response = self._session.get(url=url, auth=self.auth, params=params, **kwargs)
        response.raise_for_status()
        return response

    def json(
        self,
        path: str,
        params: Any = None,
        **kwargs,
    ) -> Any:
        response = self.get(path, params=params, **kwargs)
        return response.json()

    def list_bm_cs_projects(
        self,
        params: Optional[ListBmCsProjectsParams] = None,
        **kwargs,
    ) -> ListBmCsProjectsResponse:
        data = self.json(
            path="/api/bm-cs-projects",
            params=params,
            **kwargs,
        ).get("data")
        return [ListBmCsProjectsResponseRecord(**r) for r in data]

    def list_bm_cs_projects_streams(
        self,
        project_id: int,
        params: Optional[ListBmCsProjectsStreamsParams] = None,
        **kwargs,
    ) -> ListBmCsProjectsStreamsResponse:
        data = self.json(
            path=f"/api/bm-cs-projects/{project_id}/streams",
            params=params,
            **kwargs,
        ).get("data")
        return [ListBmCsProjectsStreamsResponseRecord(**r) for r in data]

    def get_bm_cs_projects_results(
        self,
        project_id: int,
        stream_id: str,
        params: Optional[GetBmCsProjectsResultsParams] = None,
        **kwargs,
    ) -> GetBmCsProjectsResultsResponse:
        data = self.json(
            path=f"/api/bm-cs-projects/{project_id}/streams/{stream_id}/results",
            params=params,
            **kwargs,
        ).get("data")
        return [GetBmCsProjectsResultsResponseRecord(**r) for r in data]
