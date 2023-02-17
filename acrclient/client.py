from __future__ import annotations

from typing import Any, Optional, Union

from requests import Session
from requests.adapters import HTTPAdapter, Retry
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

    >>> bearer_token = "bearer-token"
    >>> config = Client.Config(retries= 5, backoff_factor= 0.1)
    >>> client = Client(bearer_token, config=config)

    :param str bearer_token
        The bearer token for ACRCloud.
    """

    class Config:
        """Configuration for acrclient.

        :param int retries
            Total number of retries to allow.

        :param float backoff_factor
            A backoff factor to apply between attempts after the second try
            (most errors are resolved immediately by a second try without a
            delay). urllib3 will sleep for::
                {backoff factor} * (2 ** ({number of total retries} - 1))
            seconds. If the backoff_factor is 0.1, then :func:`Retry.sleep` will sleep
            for [0.0s, 0.2s, 0.4s, ...] between retries. It will never be longer
            than `backoff_max`.
            By default, backoff is disabled (set to 0).
        """

        def __init__(
            self,
            retries: Union[bool | int | None] = 5,
            backoff_factor: float = 0.1,
        ):
            self._retries: Union[bool | int | None] = retries
            self._backoff_factor: float = backoff_factor

        @property
        def retries(self):
            return self._retries

        @property
        def backoff_factor(self):
            return self._backoff_factor

    def __init__(
        self,
        bearer_token: str,
        base_url: str = "https://eu-api-v2.acrcloud.com",
        config: Optional[Config] = None,
    ):
        self.base_url: str = base_url

        self._config: Optional[Client.Config] = config or Client.Config()
        self._auth: _Auth = _Auth(bearer_token=bearer_token)
        self._session = Session()
        self._session.mount(
            "https://",
            HTTPAdapter(
                max_retries=Retry(
                    total=self._config.retries,
                    backoff_factor=self._config.backoff_factor,
                )
            ),
        )

    def get(self, path: str, params: Any = None, **kwargs) -> Response:
        """Fetch JSON data from ACRCloud API with set Access Key param."""
        url = f"{self.base_url}{path}"
        if not kwargs.get("timeout"):
            kwargs["timeout"] = 60

        # pylint: disable-next=missing-timeout
        response = self._session.get(url=url, auth=self._auth, params=params, **kwargs)
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
