"""AcrCloud client."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from typing import Any, Self

    from requests.models import PreparedRequest, Response

    from .models import GetBmCsProjectsResultsParams

from requests import Session
from requests.adapters import HTTPAdapter, Retry
from requests.auth import AuthBase


class _Auth(AuthBase):  # pylint: disable=too-few-public-methods
    """Bearer token style auth for ACRCloud."""

    def __init__(self: Self, bearer_token: str) -> None:
        self.bearer_token = bearer_token

    def __call__(self: Self, request: PreparedRequest) -> PreparedRequest:
        request.headers["Authorization"] = f"Bearer {self.bearer_token}"
        return request


class Client:
    """Client class with various methods to call ACRCloud API v2 endpoints.

    Examples
    --------
        Create an instance with configuration.
        ```python
        >>> bearer_token = "bearer-token"
        >>> config = Client.Config(retries= 5, backoff_factor= 0.1)
        >>> client = Client(bearer_token, config=config)

        ```

    """

    class Config:
        """Configuration for acrclient."""

        def __init__(
            self: Self,
            *,
            retries: bool | int | None = 5,
            backoff_factor: float = 0.1,
        ) -> None:
            """Parameters

            retries: Total number of retries to allow.

            backoff_factor: A backoff factor to apply between attempts after the
                second try (most errors are resolved immediately by a second try
                without a delay). urllib3 will sleep for::
                    {backoff factor} * (2 ** ({number of total retries} - 1))
                seconds. If the backoff_factor is 0.1, then :func:`Retry.sleep`
                will sleep for [0.0s, 0.2s, 0.4s, ...] between retries. It will
                never be longer than `backoff_max`.
                By default, backoff is set to 0.1.

            """
            self._retries: bool | int | None = retries
            self._backoff_factor: float = backoff_factor

        @property
        def retries(self: Self) -> bool | int | None:
            """Get total number of allowed retries."""
            return self._retries

        @property
        def backoff_factor(self: Self) -> float:
            """Get backoff factor to applied between attempts."""
            return self._backoff_factor

    def __init__(
        self: Self,
        bearer_token: str,
        base_url: str = "https://eu-api-v2.acrcloud.com",
        config: Config | None = None,
    ) -> None:
        """Parameters

        bearer_token: The bearer token for ACRCloud.

        """
        self.base_url: str = base_url

        self._config: Client.Config | None = config or Client.Config()
        self._auth: _Auth = _Auth(bearer_token=bearer_token)
        self._session = Session()
        self._session.mount(
            "https://",
            HTTPAdapter(
                max_retries=Retry(
                    total=self._config.retries,
                    backoff_factor=self._config.backoff_factor,
                ),
            ),
        )

    def get(
        self: Self,
        path: str,
        params: Any = None,  # noqa: ANN401
        **kwargs: Any,  # noqa: ANN401
    ) -> Response:
        """Fetch JSON data from ACRCloud API with set Access Key param.

        Args:
        ----
            path: URL path
            params: Parameters for request (usually used as GET params)
            **kwargs: Get passed to `requests.get`

        Returns:
        -------
            Response object

        """
        url = f"{self.base_url}{path}"
        if not kwargs.get("timeout"):
            kwargs["timeout"] = 60

        # pylint: disable-next=missing-timeout
        response = self._session.get(url=url, auth=self._auth, params=params, **kwargs)
        response.raise_for_status()
        return response

    def json(
        self: Self,
        path: str,
        params: Any = None,  # noqa: ANN401
        **kwargs: Any,  # noqa: ANN401
    ) -> Any:  # noqa: ANN401
        """Get the json results of a get call.

        Args:
        ----
            path: URL path
            params: Parameters for request (usually used as GET params)
            **kwargs: Get passed to `requests.get`

        Returns:
        -------
            Data from API

        """
        response = self.get(path, params=params, **kwargs)
        return response.json()

    def get_bm_cs_projects_results(
        self: Self,
        project_id: int,
        stream_id: str,
        params: GetBmCsProjectsResultsParams | None = None,
        **kwargs: Any,  # noqa: ANN401
    ) -> Any:  # noqa: ANN401
        """Get Custom Broadcast Monitoring Streams Results from ACRCloud.

        Args:
        ----
            project_id: Custom Broadcast Monitoring Project ID
            stream_id: Custom Broadcast Monitoring Stream ID
            params: GET parameters for request
            **kwargs: Get passed to `requests.get`

        Returns:
        -------
            Data from API

        """
        return self.json(
            path=f"/api/bm-cs-projects/{project_id}/streams/{stream_id}/results",
            params=params,
            **kwargs,
        ).get("data")
