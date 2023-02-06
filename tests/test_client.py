"""Unittests for ACRCloud client.

These are mostly trivial tests for coverage's sake.
Most of our real testing effort is in the acceptance
test suite which helps us ensure that the client
works for our real-world use case. Thus you should
not rely on the examples in here, but rather look
at the type hints or acceptance test suite to see
what you can expect from the API.
"""
import requests_mock

from acrclient import Client
from acrclient.client import _Auth
from acrclient.models import (
    GetBmCsProjectsResultsParams,
    ListBmCsProjectsParams,
    ListBmCsProjectsStreamsParams,
)


def test_client():
    client = Client(bearer_token="bearer-token")
    assert isinstance(client, Client)
    assert isinstance(client.auth, _Auth)
    assert client.base_url == "https://api-v2.acrcloud.com"


def test_client_get():
    client = Client(bearer_token="bearer-token")
    with requests_mock.Mocker() as mock:
        mock.get("https://api-v2.acrcloud.com/foo", json={})
        client.get("/foo")


def test_client_list_bm_cs_projects():
    client = Client(bearer_token="bearer-token")
    with requests_mock.Mocker() as mock:
        mock.get(
            f"{client.base_url}/api/bm-cs-projects",
            json={
                "data": [
                    {
                        "id": "",
                        "name": "",
                        "uid": "",
                        "type": "",
                        "region": "",
                        "state": "",
                        "access_key": "",
                        "bucket_group": "",
                        "noise": "",
                        "created_at": "",
                        "updated_at": "",
                        "iswc": "",
                        "buckets": [
                            {
                                "id": "",
                                "uid": "",
                                "name": "",
                                "type": "",
                                "state": "",
                                "region": "",
                                "metadata_template": "",
                                "labels": "",
                                "net_type": "",
                                "tracker": "",
                                "created_at": "",
                                "updated_at": "",
                                "num": "",
                                "size": "",
                                "access_permission": "",
                            },
                        ],
                        "status_check": "",
                        "external_ids": "",
                        "metadata_template": "",
                        "result_callback_url": "",
                        "result_callback_send_type": "",
                        "result_callback_send_noresult": "",
                        "state_notification_url": "",
                        "state_notification_email": "",
                        "state_notification_email_frequency": "",
                        "state_notification_email_custom_interval": "",
                        "result_callback_retry": "",
                        "monitoring_num": "",
                        "config": {
                            "record": {},
                        },
                    },
                ],
            },
        )
        client.list_bm_cs_projects(
            params=ListBmCsProjectsParams(),
        )


def test_client_list_bm_cs_projects_streams():
    client = Client(bearer_token="bearer-token")
    with requests_mock.Mocker() as mock:
        mock.get(
            f"{client.base_url}/api/bm-cs-projects/project-id/streams",
            json={
                "data": [
                    {
                        "stream_id": "",
                        "uid": "",
                        "mcp_id": "",
                        "stream_type": "",
                        "name": "",
                        "state": "",
                        "code": "",
                        "stream_urls": "",
                        "current_url": "",
                        "region": "",
                        "pitch_shift": "",
                        "check_pitch_shift": "",
                        "remark": "",
                        "created_at": "",
                        "updated_at": "",
                        "record_video": "",
                        "stream_rec_type": "",
                        "epg": "",
                        "add_recordings": "",
                        "timemap": "",
                        "ucf": "",
                        "config": {
                            "id": "",
                            "name": "",
                            "uid": "",
                            "rec_length": "",
                            "interval": "",
                            "rec_timeout": "",
                            "monitor_timeout": "",
                            "noise": "",
                            "delay": "",
                            "record": "",
                            "created_at": "",
                            "updated_at": "",
                        },
                    },
                ],
            },
        )
        client.list_bm_cs_projects_streams(
            "project-id",
            params=ListBmCsProjectsStreamsParams(),
        )


def test_client_get_bm_cs_projects_results():
    client = Client(bearer_token="bearer-token")
    with requests_mock.Mocker() as mock:
        mock.get(
            f"{client.base_url}/api/bm-cs-projects/project-id/streams/stream-id/results",
            json={
                "data": [
                    {
                        "status": {
                            "msg": "",
                            "version": "",
                            "code": "",
                        },
                        "metadata": {
                            "type": "",
                            "timestamp_utc": "",
                            "played_duration": "",
                            "music": [
                                {
                                    "title": "",
                                    "acrid": "",
                                    "score": 0,
                                    "result_from": 0,
                                    "duration_ms": 0,
                                    "sample_begin_time_offset_ms": 0,
                                    "sample_end_time_offset_ms": 0,
                                    "db_begin_time_offset_ms": 0,
                                    "db_end_time_offset_ms": 0,
                                    "play_offset_ms": 0,
                                    "external_ids": {},
                                    "external_metadata": {
                                        "musicstory": {
                                            "track": {
                                                "id": 0,
                                            },
                                            "album": {
                                                "id": 0,
                                            },
                                            "release": {
                                                "id": 0,
                                            },
                                        },
                                        "lyricfind": {
                                            "lfid": "",
                                        },
                                        "musicbrainz": [
                                            {
                                                "track": "",
                                            }
                                        ],
                                    },
                                    "artists": [
                                        {
                                            "name": "",
                                        }
                                    ],
                                    "album": {
                                        "langs": [
                                            {
                                                "code": "",
                                                "name": "",
                                            }
                                        ]
                                    },
                                    "contributors": {
                                        "composers": {},
                                        "lyricists": {},
                                    },
                                    "rights_claim": {
                                        "TODO": "shrug",
                                    },
                                    "lyrics": {
                                        "TODO": "shrug",
                                    },
                                    "langs": [
                                        {
                                            "code": "",
                                            "name": "",
                                        }
                                    ],
                                    "genres": [
                                        {
                                            "name": "",
                                        }
                                    ],
                                    "works": [
                                        {
                                            "id": "",
                                            "name": "",
                                            "iswc": "",
                                            "creators": [
                                                {
                                                    "ipi": 0,
                                                    "name": "",
                                                }
                                            ],
                                            "works": [
                                                {
                                                    "code": "",
                                                    "agency": {
                                                        "code": "",
                                                    },
                                                }
                                            ],
                                        }
                                    ],
                                    "release_by_territories": [
                                        {
                                            "territories": [""],
                                            "release_date": "",
                                        }
                                    ],
                                },
                            ],
                        },
                    },
                ]
            },
        )
        client.get_bm_cs_projects_results(
            "project-id",
            "stream-id",
            params=GetBmCsProjectsResultsParams(),
        )
