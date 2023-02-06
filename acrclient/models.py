# pylint: disable=too-few-public-methods,too-many-locals,too-many-arguments,too-many-instance-attributes
from typing import Optional, TypedDict


class Bucket:
    """Bucket with ACR data."""

    # pylint: disable=redefined-builtin,invalid-name
    def __init__(
        self,
        id: int,
        uid: int,
        name: str,
        type: str,
        state: int,
        region: str,
        metadata_template: str,
        labels: list[str],
        net_type: int,
        tracker: int,
        created_at: str,
        updated_at: str,
        num: int,
        size: str | int,
        access_permission: str,
        *args,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.id: int = id
        self.uid: int = uid
        self.name: str = name
        self.type: str = type
        self.state: int = state
        self.region: str = region
        self.metadata_template: str = metadata_template
        self.labels: list[str] = labels
        self.net_type: int = net_type
        self.tracker: int = tracker
        self.created_at: str = created_at
        self.updated_at: str = updated_at
        self.num: int = num
        self.size: str | int = size
        self.access_permission: str = access_permission


class Artist:
    """Artist for Music record."""

    # pylint: disable=redefined-builtin,invalid-name
    def __init__(
        self,
        name: str,
        *args,
        id: Optional[str | int | dict] = None,
        seokey: Optional[str] = None,
        isni: Optional[str] = None,
        role: Optional[str] = None,
        roles: Optional[list] = None,
        langs: Optional[list] = None,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.name: str = name
        self.id: Optional[str | int | dict] = id
        self.seokey: Optional[str] = seokey
        self.isni: Optional[str] = isni
        self.role: Optional[str] = role
        self.roles: Optional[list] = roles
        self.langs: Optional[list] = langs


class Album:
    """Album for Music record."""

    # pylint: disable=redefined-builtin,invalid-name
    def __init__(
        self,
        *args,
        id: Optional[str | int] = None,
        name: Optional[str] = None,
        image: Optional[str] = None,
        langs: Optional[dict] = None,
        cd_id: Optional[str] = None,
        type: Optional[str] = None,
        upc: Optional[str] = None,
        release_date: Optional[str] = None,
        **kwargs,
    ) -> None:
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.id: Optional[str | int] = id
        self.name: Optional[str] = name
        self.image: Optional[str] = image
        self.cd_id: Optional[str] = cd_id
        self.type: Optional[str] = type
        self.upc: Optional[str] = upc
        self.release_date: Optional[str] = release_date

        self.langs: Optional[list[Lang]] = None
        if langs:
            self.langs = [Lang(*l) for l in langs]


class Contributors:
    """Contributors for Music record."""

    def __init__(
        self,
        *args,
        composers: Optional[list[str]] = None,
        lyricists: Optional[list[str]] = None,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.composers: Optional[list[str]] = composers
        self.lyricists: Optional[list[str]] = lyricists


class ExternalIds:
    """External IDs for Music record."""

    def __init__(
        self,
        *args,
        isrc: Optional[str | list[str]] = None,
        upc: Optional[str | list[str]] = None,
        iswc: Optional[str] = None,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.isrc: Optional[str | list[str]] = isrc
        self.upc: Optional[str | list[str]] = upc
        self.iswc: Optional[str] = iswc


class ExternalMetadataDeezer:
    """External metadata from Deezer."""

    def __init__(
        self,
        album: dict,
        track: dict,
        artists: list[dict],
        *args,
        **kwargs,
    ) -> None:
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.album = album
        self.track = track
        self.artists = artists


class ExternalMetadataSpotify:
    """External metadata from Spotify."""

    def __init__(
        self,
        album: dict,
        track: dict,
        artists: list[dict],
        *args,
        **kwargs,
    ) -> None:
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.album = album
        self.track = track
        self.artists = artists


class ExternalMetadataYoutube:
    """External metadata from Youtube."""

    def __init__(
        self,
        vid: str,
        *args,
        **kwargs,
    ) -> None:
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.vid: str = vid


class ExternalMetadataMusicBrainz:
    """MusicBrainz external metadata for Music record."""

    def __init__(
        self,
        track,
        *args,
        **kwargs,
    ) -> None:
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.track = track


class ExternalMetadataLyricFind:
    """Lyricfind external metadata for Music record."""

    def __init__(
        self,
        lfid: str,
        *args,
        **kwargs,
    ) -> None:
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.lfid: str = lfid


class MusicStoryData:
    """Musicstory data part for external metadata in Music record."""

    # pylint: disable=redefined-builtin,invalid-name
    def __init__(
        self,
        *args,
        id,
        **kwargs,
    ) -> None:
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.id = id


class ExternalMetadataMusicStory:
    """Musicstory external metadata for Music record."""

    def __init__(
        self,
        track,
        *args,
        album=None,
        release=None,
        **kwargs,
    ) -> None:
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.track: MusicStoryData = MusicStoryData(**track)
        self.album: Optional[MusicStoryData]
        if album:
            self.album = MusicStoryData(**album)
        self.release: Optional[MusicStoryData] = None
        if release:
            self.release = MusicStoryData(**release)


class ExternalMetadata:
    """External metadata for Music record."""

    def __init__(
        self,
        *args,
        deezer: list = None,
        spotify: list = None,
        youtube: list = None,
        musicstory: Optional[list | dict] = None,
        lyricfind: Optional[list | dict] = None,
        musicbrainz: Optional[list] = None,
        **kwargs,
    ) -> None:
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"

        if deezer:
            self.deezer = [
                deezer
                if not isinstance(deezer, list)
                else [ExternalMetadataDeezer(**d) for d in deezer]
            ]
        if spotify:
            self.spotify = [
                spotify
                if not isinstance(spotify, list)
                else [ExternalMetadataSpotify(**s) for s in spotify]
            ]
        if youtube:
            self.youtube = [
                youtube
                if not isinstance(youtube, list)
                else [ExternalMetadataYoutube(**y) for y in youtube]
            ]

        self.musicstory: Optional[
            list[ExternalMetadataMusicStory] | ExternalMetadataMusicStory
        ] = None
        if musicstory:
            self.musicstory = (
                ExternalMetadataMusicStory(**musicstory)
                if not isinstance(musicstory, list)
                else [ExternalMetadataMusicStory(**m) for m in musicstory]
            )
        self.lyricfind: Optional[
            list[ExternalMetadataLyricFind] | ExternalMetadataLyricFind
        ] = None
        if lyricfind:
            self.lyricfind = (
                ExternalMetadataLyricFind(**lyricfind)
                if not isinstance(lyricfind, list)
                else [ExternalMetadataLyricFind(**l) for l in lyricfind]
            )
        self.musicbrianz: Optional[list[ExternalMetadataMusicBrainz | str]] = None
        if musicbrainz:
            self.musicbrainz = [
                mb if isinstance(mb, str) else ExternalMetadataMusicBrainz(**mb)
                for mb in musicbrainz
            ]


class Genre:
    """Genre of Music record."""

    # pylint: disable=redefined-builtin,invalid-name
    def __init__(
        self,
        name: str,
        *args,
        id: Optional[int | str] = None,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.name: str = name
        self.id: Optional[int | str] = id


class WorkCreator:
    """Creator of work in Music record."""

    def __init__(
        self,
        ipi: int,
        name: str,
        *args,
        affiliation: Optional[dict] = None,
        last_name: Optional[str] = None,
        role: Optional[str] = None,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.ipi: int = ipi
        self.name: str = name
        self.affiliation: Optional[dict] = affiliation
        self.last_name: Optional[str] = last_name
        self.role: Optional[str] = role


class WorkWorkAgency:
    """Agency in work of work in Music record."""

    def __init__(
        self,
        code: str,
        *args,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.code: str = code


class WorkWork:
    """Work part of work in Music record."""

    def __init__(
        self,
        code: str,
        agency,
        *args,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.code: str = code
        self.agency = WorkWorkAgency(**agency)


class Work:
    """Work part of Music record."""

    # pylint: disable=redefined-builtin,invalid-name
    def __init__(
        self,
        id,
        name: str,
        iswc,
        creators,
        *args,
        other_names=None,
        works=None,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.id = id
        self.name = name
        self.iswc = iswc
        self.creators = [WorkCreator(**c) for c in creators]

        self.other_names = other_names

        self.works = None
        if works:
            self.works = [WorkWork(**w) for w in works]


class Lang:
    """Lang part of Music record."""

    def __init__(
        self,
        code: str,
        name: str,
        *args,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.code: str = code
        self.name: str = name


class ReleaseByTerritories:
    """ReleaseByTerritories part of Music record."""

    def __init__(
        self,
        territories: list[str],
        release_date: str,
        *args,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.territories: list[str] = territories
        self.release_date: str = release_date


class Music:
    """ACR abstraction of a "Music" resource."""

    def __init__(
        self,
        title: str,
        acrid: str,
        score: int,
        result_from: int,
        duration_ms: int,
        sample_begin_time_offset_ms: int,
        sample_end_time_offset_ms: int,
        db_begin_time_offset_ms: int,
        db_end_time_offset_ms: int,
        play_offset_ms: int,
        external_ids,
        external_metadata,
        album,
        *args,
        artists: Optional[list[dict]] = None,
        release_date: Optional[str] = None,
        label: Optional[str] = None,
        language: Optional[str] = None,
        exids: Optional[str] = None,
        source: Optional[str] = None,
        ppm: Optional[str] = None,
        bpm: Optional[str | bool] = None,
        rights_claim_policy: Optional[str] = None,
        updated_at: Optional[str] = None,
        langs=None,
        contributors=None,
        rights_claim=None,
        lyrics=None,
        genres=None,
        works=None,
        release_by_territories=None,
        **kwargs,
    ):
        # remove fields that should not be in the top-level of a music record
        # can we report these to ACRCloud as part of auto-remediation?
        for field in [
            "163",
            "amco",
            "andyou",
            "anghami",
            "artstis",
            "awa",
            "base_score",
            "bugs",
            "deezer",
            "disco_3453684",
            "joox",
            "kkbox",
            "lyricfind",
            "merlin",
            "musicbrainz",
            "musicstory",
            "mwg",
            "nct",
            "omusic",
            "partner",
            "partners",
            "qqmusic",
            "rec_times",
            "rights_owners",
            "sme",
            "Soundcharts",
            "spotify",
            "trackitdown",
            "umg",
            "wmg",
            "works_ids",
            "youtube",
        ]:
            kwargs.pop(field, None)

        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.title: str = title
        self.acrid: str = acrid

        self.score: int = score
        self.duration_ms: int = duration_ms
        self.result_from: int = result_from

        self.sample_begin_time_offset_ms: int = sample_begin_time_offset_ms
        self.sample_end_time_offset_ms: int = sample_end_time_offset_ms
        self.db_begin_time_offset_ms: int = db_begin_time_offset_ms
        self.db_end_time_offset_ms: int = db_end_time_offset_ms
        self.play_offset_ms: int = play_offset_ms

        self.external_ids: ExternalIds = ExternalIds(**external_ids)
        self.external_metadata: ExternalMetadata | list[ExternalMetadata] = (
            [ExternalMetadata(*e) for e in external_metadata]
            if isinstance(external_metadata, list)
            else ExternalMetadata(**external_metadata)
        )
        self.album: Album = Album(**album)

        self.artists: list[Artist] = [Artist(**a) for a in artists] if artists else []
        self.release_date: Optional[str] = release_date
        self.label: Optional[str] = label
        self.language: Optional[str] = language
        self.exids: Optional[str] = exids
        self.source: Optional[str] = source
        self.ppm: Optional[str] = ppm
        self.bpm: Optional[str | bool] = bpm
        self.rights_claim_policy: Optional[str] = rights_claim_policy
        self.updated_at: Optional[str] = updated_at

        self.contributors: Optional[Contributors] = None
        if contributors:
            self.contributors = Contributors(**contributors)

        self.rights_claim: Optional[dict] = None
        if rights_claim:
            self.rights_claim = rights_claim

        self.lyrics: Optional[dict] = None
        if lyrics:
            self.lyrics = lyrics

        self.langs: Optional[list[Lang | str]] = None
        if langs:
            self.langs = [l if isinstance(l, str) else Lang(**l) for l in langs]

        self.genres: Optional[list[Genre]] = None
        if genres:
            self.genres = [Genre(**g) for g in genres]

        self.works: Optional[list[Work]] = None
        if works:
            self.works = [Work(**w) for w in works]

        self.release_by_territories: Optional[list] = None
        if release_by_territories:
            self.release_by_territories = [
                ReleaseByTerritories(**rbt) for rbt in release_by_territories
            ]


class CustomFile:
    """CustomFile record."""

    # pylint: disable=redefined-builtin,invalid-name,redefined-outer-name
    def __init__(
        self,
        title: str,
        acrid: str,
        bucket_id: str,
        count: int,
        score: int,
        duration_ms: int,
        sample_begin_time_offset_ms: int,
        sample_end_time_offset_ms: int,
        db_begin_time_offset_ms: int,
        db_end_time_offset_ms: int,
        play_offset_ms: int,
        *args,
        album: Optional[str] = None,
        artists: Optional[str] = None,
        isrc: Optional[str] = None,
        label: Optional[str] = None,
        release_date: Optional[str] = None,
        Artist: Optional[str] = None,
        Artists: Optional[str] = None,
        Title: Optional[str] = None,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.title: str = title
        self.acrid: str = acrid
        self.bucket_id: str = bucket_id

        self.count: int = count
        self.score: int = score
        self.duration_ms: int = duration_ms

        self.sample_begin_time_offset_ms: int = sample_begin_time_offset_ms
        self.sample_end_time_offset_ms: int = sample_end_time_offset_ms
        self.db_begin_time_offset_ms: int = db_begin_time_offset_ms
        self.db_end_time_offset_ms: int = db_end_time_offset_ms
        self.play_offset_ms: int = play_offset_ms

        self.album: Optional[str] = album
        self.artists: Optional[str] = artists
        self.isrc: Optional[str] = isrc
        self.label: Optional[str] = label
        self.release_date: Optional[str] = release_date

        self.Artist: Optional[str] = Artist
        self.Artists: Optional[str] = Artists
        self.Title: Optional[str] = Title


class ListBmCsProjectsParams(TypedDict):
    """Parameters for listing base projects."""

    region: str
    """eu-west-1,us-west-2,ap-southeast-1"""
    type: str
    """AVR,LCD,HR"""
    page: str
    """Page number"""
    per_page: str
    """The results number per page"""


class BmCsProjectsConfig:
    """Configuration in a ProjectsStreamsRecord."""

    # pylint: disable=redefined-builtin,invalid-name
    def __init__(
        self,
        record: dict,
        *args,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.record = record


class ListBmCsProjectsResponseRecord:
    """Project record in base proects response."""

    # pylint: disable=redefined-builtin,invalid-name
    def __init__(
        self,
        id: int,
        name: str,
        uid: int,
        type: str,
        region: str,
        state: int,
        access_key: str,
        bucket_group: str,
        noise: int,
        created_at: str,
        updated_at: str,
        iswc: int,
        buckets: list,
        status_check: int,
        external_ids: list[str],
        metadata_template: str,
        result_callback_url: str,
        result_callback_send_type: str,
        result_callback_send_noresult: str,
        state_notification_url: str,
        state_notification_email: str,
        state_notification_email_frequency: str,
        state_notification_email_custom_interval: int,
        result_callback_retry: int,
        monitoring_num: int,
        config: dict,
        *args,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.id: int = id
        self.name: str = name
        self.uid: int = uid
        self.type: str = type
        self.region: str = region
        self.state: int = state
        self.access_key: str = access_key
        self.bucket_group: str = bucket_group
        self.noise: int = noise
        self.created_at: str = created_at
        self.updated_at: str = updated_at
        self.iswc: int = iswc
        self.buckets: list[Bucket] = [Bucket(**b) for b in buckets]
        self.status_check: int = status_check
        self.external_ids: list = external_ids
        self.metadata_template: str = metadata_template
        self.result_callback_url: str = result_callback_url
        self.result_callback_send_type: str = result_callback_send_type
        self.result_callback_send_noresult: str = result_callback_send_noresult
        self.state_notification_url: str = state_notification_url
        self.state_notification_email: str = state_notification_email
        self.state_notification_email_frequency: str = (
            state_notification_email_frequency
        )
        self.state_notification_email_custom_interval: int = (
            state_notification_email_custom_interval
        )
        self.result_callback_retry: int = result_callback_retry
        self.monitoring_num: int = monitoring_num
        self.config: BmCsProjectsConfig = BmCsProjectsConfig(**config)


ListBmCsProjectsResponse = list[ListBmCsProjectsResponseRecord]


class ListBmCsProjectsStreamsParams(TypedDict):
    """Parameters for listing base projects."""

    timemap: int
    """0 or 1"""
    state: str
    """All,Running,Timeout,Paused,Invalid URL,Mute,Other. Default is All."""
    search_value: str
    """Search by Name, StreamID, URL, User-defind, Remark"""
    sort: str
    """sort by 'created_at', 'stream_id', 'name', Default is 'created_at'"""
    order: str
    """order by desc or asc, default is desc."""


class BmCsProjectsStreamsConfig:
    """Configuration in a ProjectsStreamsRecord."""

    # pylint: disable=redefined-builtin,invalid-name
    def __init__(
        self,
        id: int,
        name: str,
        uid: int,
        rec_length: int,
        interval: int,
        rec_timeout: int,
        monitor_timeout: int,
        noise: int,
        delay: int,
        record: dict,
        created_at: str,
        updated_at: str,
        *args,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.id: int = id
        self.name: str = name
        self.uid: int = uid
        self.rec_length: int = rec_length
        self.interval: int = interval
        self.rec_timeout: int = rec_timeout
        self.monitor_timeout: int = monitor_timeout
        self.noise: int = noise
        self.delay: int = delay
        self.record: dict = record
        self.created_at: str = created_at
        self.updated_at: str = updated_at


class ListBmCsProjectsStreamsResponseRecord:
    """Project record in base proects response."""

    def __init__(
        self,
        stream_id: str,
        uid: int,
        mcp_id: int,
        stream_type: str,
        name: str,
        state: str,
        code: int,
        stream_urls: list[str],
        current_url: str,
        region: str,
        pitch_shift: int,
        check_pitch_shift: int,
        remark: str,
        created_at: str,
        updated_at: str,
        record_video: int,
        stream_rec_type: int,
        epg: str,
        add_recordings: int,
        config: dict,
        timemap: int,
        ucf: int,
        *args,
        user_defined: Optional[str] = None,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.stream_id: str = stream_id
        self.uid: int = uid
        self.mcp_id: int = mcp_id
        self.stream_type: str = stream_type
        self.name: str = name
        self.state: str = state
        self.code: int = code
        self.stream_urls: list[str] = stream_urls
        self.current_url: str = current_url
        self.region: str = region
        self.pitch_shift: int = pitch_shift
        self.check_pitch_shift: int = check_pitch_shift
        self.remark: str = remark
        self.created_at: str = created_at
        self.updated_at: str = updated_at
        self.record_video: int = record_video
        self.stream_rec_type: int = stream_rec_type
        self.epg: str = epg
        self.add_recordings: int = add_recordings
        self.timemap: int = timemap
        self.ucf: int = ucf
        self.user_defined: Optional[str] = user_defined
        self.config: BmCsProjectsStreamsConfig = BmCsProjectsStreamsConfig(**config)


ListBmCsProjectsStreamsResponse = list[ListBmCsProjectsStreamsResponseRecord]


class GetBmCsProjectsResultsParams(TypedDict):
    """Parameters for getting BM projects custom streams results."""

    type: str
    """last: get the last results, day: get the day results, Default is day"""
    date: str
    """Get all the results on this date. The format is YYYYmmdd (E.g. 20210201)"""
    min_duration: int
    """Return the results of played_duration >= min_duration seconds (default: 0)"""
    max_duration: int
    """Return the results with played_duration <= max_duration seconds (default: 3600)"""
    isrc_country: str
    """Only return results that match the isrc country code (E.g. DE, FR, IT, US)"""


class GetBmCsProjectsResultsResponseRecordStatus:
    """Status part of a BM Project's custom stream result record."""

    def __init__(self, msg: str, version: str, code: int, *args, **kwargs):
        assert (len(args) + len(kwargs)) == 0
        self.msg: str = msg
        self.version: str = version
        self.code: int = code


class GetBmCsProjectsResultsResponseRecordMetadata:
    """Metadata part of a BM Project's custom stream result record."""

    # pylint: disable=redefined-builtin
    def __init__(
        self,
        type: str,
        timestamp_utc: str,
        played_duration: int,
        *args,
        record_timestamp: Optional[str] = None,
        music: Optional[list] = None,
        custom_files: Optional[list] = None,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.type: str = type
        self.timestamp_utc: str = timestamp_utc

        self.played_duration: int = played_duration

        self.record_timestamp: Optional[str] = record_timestamp

        self.music: Optional[list[Music]] = None
        if music:
            self.music = [Music(**m) for m in music]
        self.custom_files: Optional[list[CustomFile]] = None
        if custom_files:
            self.custom_files = [CustomFile(**m) for m in custom_files]


class GetBmCsProjectsResultsResponseRecord:
    """Record in a BM Project's custom stream results response."""

    def __init__(
        self,
        status: dict,
        metadata: dict,
        *args,
        result_type: Optional[int] = None,
        service_type: Optional[str] = None,
        **kwargs,
    ):
        assert (len(args) + len(kwargs)) == 0, f"{self.__class__}: {args=} {kwargs=}"
        self.status = GetBmCsProjectsResultsResponseRecordStatus(**status)
        self.metadata = GetBmCsProjectsResultsResponseRecordMetadata(**metadata)
        self.result_type: Optional[int] = result_type
        self.service_type: Optional[str] = service_type


GetBmCsProjectsResultsResponse = list[GetBmCsProjectsResultsResponseRecord]
