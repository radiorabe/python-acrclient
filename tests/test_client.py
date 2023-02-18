import requests_mock

from acrclient import Client
from acrclient.client import _Auth


def test_client():
    client = Client(_Auth("bearer-token"))
    assert isinstance(client, Client)
    assert client.base_url == "https://eu-api-v2.acrcloud.com"


def test_client_get():
    client = Client(_Auth("bearer-token"))
    with requests_mock.Mocker() as mock:
        mock.get("https://eu-api-v2.acrcloud.com/foo", json={})
        client.get("/foo")


def test_client_get_bm_cs_projects_results():
    client = Client(_Auth("bearer-token"))
    with requests_mock.Mocker() as mock:
        mock.get(
            f"{client.base_url}/api/bm-cs-projects/project-id/streams/stream-id/results",
            json={"data": {}},
        )
        client.get_bm_cs_projects_results("project-id", "stream-id")
