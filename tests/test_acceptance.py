from functools import reduce
from operator import concat
from datetime import datetime, timedelta

from pytest import mark

from acrclient import Client
from acrclient.models import (
    Album,
    Artist,
    BmCsProjectsConfig,
    BmCsProjectsStreamsConfig,
    Contributors,
    ExternalIds,
    ExternalMetadata,
    Genre,
    Lang,
    Music,
    Work,
    WorkCreator,
    WorkWork,
    WorkWorkAgency,
)


def test_list_bm_cs_projects(client):
    data = client.list_bm_cs_projects()
    assert_is_list_bm_cs_projects(data)


def assert_is_list_bm_cs_projects(data):
    assert isinstance(data, list)
    assert len(data) > 0
    for record in data:
        assert isinstance(record.id, int)
        assert isinstance(record.name, str)
        assert isinstance(record.uid, int)
        assert isinstance(record.type, str)
        assert isinstance(record.region, str)
        assert isinstance(record.state, int)
        assert isinstance(record.access_key, str)
        assert isinstance(record.bucket_group, str)
        assert isinstance(record.noise, int)
        assert isinstance(record.created_at, str)
        assert isinstance(record.updated_at, str)
        assert isinstance(record.iswc, int)
        assert isinstance(record.status_check, int)
        assert isinstance(record.metadata_template, str)
        assert isinstance(record.result_callback_url, str)
        assert isinstance(record.result_callback_send_type, str)
        assert isinstance(record.result_callback_send_noresult, str)
        assert isinstance(record.state_notification_url, str)
        assert isinstance(record.state_notification_email, str)
        assert isinstance(record.state_notification_email_frequency, str)
        assert isinstance(record.state_notification_email_custom_interval, int)
        assert isinstance(record.result_callback_retry, int)
        assert isinstance(record.monitoring_num, int)

        assert isinstance(record.config, BmCsProjectsConfig)
        if record.config:
            assert isinstance(record.config.record, dict)

        assert isinstance(record.external_ids, list)
        for external_id in record.external_ids:
            assert isinstance(external_id, str)

        assert isinstance(record.buckets, list)
        for bucket in record.buckets:
            assert isinstance(bucket.id, int)
            assert isinstance(bucket.uid, int)
            assert isinstance(bucket.name, str)
            assert isinstance(bucket.type, str)
            assert isinstance(bucket.state, int)
            assert isinstance(bucket.region, str)
            assert isinstance(bucket.metadata_template, str)
            assert isinstance(bucket.net_type, int)
            assert isinstance(bucket.tracker, int)
            assert isinstance(bucket.created_at, str)
            assert isinstance(bucket.updated_at, str)
            assert isinstance(bucket.num, int)
            assert isinstance(bucket.size, (str, int))
            assert isinstance(bucket.access_permission, str)
            assert isinstance(bucket.labels, list)
            for label in bucket.labels:
                assert isinstance(label, str)


def test_list_bm_cs_projects_streams(client, project_ids):
    for project_id in project_ids:
        data = client.list_bm_cs_projects_streams(project_id=project_id)
        print("wat")
        assert_is_list_bm_cs_projects_streams(data)


def assert_is_list_bm_cs_projects_streams(data):
    assert isinstance(data, list)
    assert len(data) > 0
    for record in data:
        print(data)
        assert isinstance(record.stream_id, str)
        assert isinstance(record.uid, int)
        assert isinstance(record.mcp_id, int)
        assert isinstance(record.stream_type, str)
        assert isinstance(record.name, str)
        assert isinstance(record.state, str)
        assert isinstance(record.code, int)
        assert isinstance(record.current_url, str)
        assert isinstance(record.region, str)
        assert isinstance(record.pitch_shift, int)
        assert isinstance(record.check_pitch_shift, int)
        assert isinstance(record.remark, str)
        assert isinstance(record.created_at, str)
        assert isinstance(record.updated_at, str)
        assert isinstance(record.record_video, int)
        assert isinstance(record.stream_rec_type, int)
        assert isinstance(record.epg, str)
        assert isinstance(record.add_recordings, int)
        assert isinstance(record.timemap, int)
        assert isinstance(record.ucf, int)
        assert isinstance(record.stream_urls, list)
        assert isinstance(record.config, BmCsProjectsStreamsConfig)
        if record.config:
            assert isinstance(record.config.id, int)
            assert isinstance(record.config.name, str)
            assert isinstance(record.config.uid, int)
            assert isinstance(record.config.rec_length, int)
            assert isinstance(record.config.interval, int)
            assert isinstance(record.config.rec_timeout, int)
            assert isinstance(record.config.monitor_timeout, int)
            assert isinstance(record.config.noise, int)
            assert isinstance(record.config.delay, int)
            assert isinstance(record.config.record, dict)
            assert isinstance(record.config.created_at, str)
            assert isinstance(record.config.updated_at, str)

        for stream_url in record.stream_urls:
            assert isinstance(stream_url, str)
        if record.user_defined:
            # maybe it's a string?
            assert isinstance(record.user_defined, str)


def get_bm_cs_projects_results_params():
    client = Client(bearer_token=bearer_token)
    project_ids = [p.id for p in client.list_bm_cs_projects()]
    stream_id_and_created_ats = reduce(
        concat,
        [
            [
                (p, s.stream_id, s.created_at)
                for s in client.list_bm_cs_projects_streams(p)
            ]
            for p in project_ids
        ],
    )
    tests = []
    for project_id, stream_id, created_at in stream_id_and_created_ats:
        now = datetime.now().date()

        date = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S").date()
        while date < now - timedelta(days=1):
            date += timedelta(days=1)
            tests.append(
                (
                    project_id,
                    stream_id,
                    {
                        "date": datetime.strftime(date, "%Y%m%d"),
                    },
                )
            )
    return tests


@mark.parametrize("project_id, stream_id, params", get_bm_cs_projects_results_params())
def test_get_bm_cs_projects_results(project_id, stream_id, params, client):
    data = client.get_bm_cs_projects_results(
        project_id,
        stream_id,
        params=params,
    )
    assert_is_get_bm_cs_projects_result(data)


# pylint: disable=too-many-statements,too-many-branches,too-many-locals,too-many-nested-blocks
def assert_is_get_bm_cs_projects_result(data):
    assert isinstance(data, list)
    for record in data:
        assert record.status.code == 0
        assert record.status.msg == "Success"
        assert record.status.version == "1.0"

        if record.result_type:
            assert record.result_type == 0

        assert record.metadata.type == "delay"
        assert isinstance(record.metadata.timestamp_utc, str)
        assert record.metadata.played_duration >= 0

        if not record.metadata.music:
            # custom record was set so music is not
            record.metadata.music = []
        for music in record.metadata.music:
            assert isinstance(music, Music)
            assert isinstance(music.title, str)
            assert isinstance(music.acrid, str)
            if music.release_date:
                assert isinstance(music.release_date, str)
            if music.label:
                assert isinstance(music.label, str)
            if music.language:
                assert isinstance(music.language, str)
            if music.exids:
                assert isinstance(music.exids, str)
            if music.source:
                assert isinstance(music.source, str)
            if music.ppm:
                assert isinstance(music.ppm, str)

            assert isinstance(music.result_from, int)
            assert isinstance(music.sample_end_time_offset_ms, int)
            assert isinstance(music.duration_ms, int)
            assert isinstance(music.score, int)
            assert isinstance(music.db_begin_time_offset_ms, int)
            assert isinstance(music.db_end_time_offset_ms, int)
            assert isinstance(music.play_offset_ms, int)
            assert isinstance(music.sample_end_time_offset_ms, int)

            if music.contributors:
                assert isinstance(music.contributors, Contributors)
                if music.contributors.composers:
                    assert isinstance(music.contributors.composers, list)
                    for composer in music.contributors.composers:
                        assert isinstance(composer, str)
                if music.contributors.lyricists:
                    assert isinstance(music.contributors.lyricists, list)
                    for lyricist in music.contributors.lyricists:
                        assert isinstance(lyricist, str)
            if music.langs:
                assert isinstance(music.langs, list)
                for lang in music.langs:
                    assert isinstance(lang, (Lang, str))
                    if isinstance(lang, Lang):
                        assert isinstance(lang.code, str)
                        assert isinstance(lang.name, str)
            if music.genres:
                assert isinstance(music.genres, list)
                for genre in music.genres:
                    assert isinstance(genre, Genre)
                    assert isinstance(genre.name, str)
                    if genre.id:
                        assert isinstance(genre.id, (int, str))
            if music.works:
                assert isinstance(music.works, list)
                for work in music.works:
                    assert isinstance(work, Work)

                    assert isinstance(work.id, str)
                    assert isinstance(work.name, str)
                    assert isinstance(work.iswc, str)

                    assert isinstance(work.creators, list)
                    for creator in work.creators:
                        assert isinstance(creator, WorkCreator)
                        assert isinstance(creator.ipi, int)
                        assert isinstance(creator.name, str)
                        if creator.affiliation:
                            assert isinstance(creator.affiliation, dict)
                        if creator.last_name:
                            assert isinstance(creator.last_name, str)
                        if creator.role:
                            assert isinstance(creator.role, str)

                    if work.works:
                        assert isinstance(work.works, list)
                        for inner_work in work.works:
                            assert isinstance(inner_work, WorkWork)
                            assert isinstance(inner_work.code, str)
                            assert isinstance(inner_work.agency, WorkWorkAgency)
                            assert isinstance(inner_work.agency.code, str)
                    if work.other_names:
                        assert isinstance(work.other_names, list)
                        for other_name in work.other_names:
                            assert isinstance(other_name, str)

            assert isinstance(music.external_ids, ExternalIds)
            if music.external_ids.isrc:
                assert isinstance(music.external_ids.isrc, (str, list))
            if music.external_ids.upc:
                assert isinstance(music.external_ids.upc, (str, list))
            if music.external_ids.iswc:
                assert isinstance(music.external_ids.iswc, str)

            assert isinstance(music.external_metadata, (ExternalMetadata, list))
            if isinstance(music.external_metadata, list):
                for external_metadata in music.external_metadata:
                    assert isinstance(external_metadata, ExternalMetadata)
                    assert isinstance(external_metadata.spotify, str)
                    assert isinstance(external_metadata.deezer, str)
                    assert isinstance(external_metadata.youtube, str)

            assert isinstance(music.album, Album)
            if music.album.name:
                assert isinstance(music.album.name, str)
            if music.album.id:
                assert isinstance(music.album.id, (str, int))
            if music.album.image:
                assert isinstance(music.album.image, str)

            if music.artists:
                assert isinstance(music.artists, list)
                for artist in music.artists:
                    assert isinstance(artist, Artist)
                    assert isinstance(artist.name, str)
                    if artist.id:
                        assert isinstance(artist.id, (str, int, dict))
                    if artist.role:
                        assert isinstance(artist.role, str)
                    if artist.roles:
                        assert isinstance(artist.roles, list)
                    if artist.langs:
                        assert isinstance(artist.langs, list)
                    if artist.seokey:
                        assert isinstance(artist.seokey, str)
                    if artist.isni:
                        assert isinstance(artist.isni, str)
