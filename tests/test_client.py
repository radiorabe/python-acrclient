import requests_mock

import acrclient


def test_client():
    client = acrclient.Client("bearer-token")
    assert isinstance(client, acrclient.Client)
    assert client.bearer_token == "bearer-token"
    assert client.base_url == "https://eu-api-v2.acrcloud.com"


def test_request():
    client = acrclient.Client("bearer-token")
    with requests_mock.Mocker() as mock:
        mock.get("https://eu-api-v2.acrcloud.com/foo", json={})
        client.request("/foo")


def test_get_bm_cs_projects_results():
    client = acrclient.Client("bearer-token")
    with requests_mock.Mocker() as mock:
        mock.get(
            f"{client.base_url}/api/bm-cs-projects/project-id/streams/stream-id/results",
            json={"data": {}},
        )
        client.get_bm_cs_projects_results("project-id", "stream-id")
