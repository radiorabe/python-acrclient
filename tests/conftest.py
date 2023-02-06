from functools import reduce
from operator import concat

from pytest import fixture, skip

from acrclient import Client


def pytest_addoption(parser):
    parser.addoption(
        "--acr-bearer-token",
        action="store",
        default=None,
        help="Bearer token for ACRCloud, used for acceptance testing.",
    )


@fixture(name="bearer_token", scope="session")
def bearer_token_fixture(request):
    """ "ACRCloud API Key used for acceptance testing."""
    bearer_token = request.config.getoption("--acr-bearer-token")
    if not bearer_token:
        skip(
            reason="provide an ACRCloud bearer token with"
            + " --acr-bearer-token to run acceptance testing."
        )
    return bearer_token


@fixture(name="client", scope="session")
def client_fixture(bearer_token):
    return Client(bearer_token=bearer_token)


@fixture(name="project_ids", scope="session")
def project_ids_fixture(client):
    return [p.id for p in client.list_bm_cs_projects()]


@fixture(name="project_stream_ids", scope="session")
def project_stream_ids_fixture(client, project_ids):
    return reduce(
        concat,
        [
            [
                (p, s.stream_id, s.created_at)
                for s in client.list_bm_cs_projects_streams(p)
            ]
            for p in project_ids
        ],
    )
