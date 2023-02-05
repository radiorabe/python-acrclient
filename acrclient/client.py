import requests


class Client:
    """ACRCloud client to fetch metadata.

    Args:
        bearer_token: The bearer token for ACRCloud.
    """

    def __init__(self, bearer_token, base_url="https://eu-api-v2.acrcloud.com"):
        self.base_url = base_url
        self.bearer_token = bearer_token

    def request(self, path, headers=None, **kwargs):
        """Fetch JSON data from ACRCloud API with set Access Key param."""

        url_params = {
            **kwargs,
        }
        if not headers:
            headers = {}
        if self.bearer_token:
            headers["Authorization"] = f"Bearer {self.bearer_token}"

        response = requests.get(
            url=f"{self.base_url}{path}", params=url_params, headers=headers, timeout=10
        )
        response.raise_for_status()
        return response.json()

    def get_bm_cs_projects_results(self, project_id, stream_id, headers=None, **kwargs):
        return self.request(
            path=f"/api/bm-cs-projects/{project_id}/streams/{stream_id}/results",
            headers=headers,
            **kwargs,
        ).get("data")
