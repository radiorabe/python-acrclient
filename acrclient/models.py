from typing import Literal, TypedDict


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


class GetExternalMetadataTracksParams(TypedDict):
    """Parameters for getting music platforms metadata and links"""

    type: str
    """ACRCloud Music ID"""
    acr_id: str
    """1 or 0, if you set it to 1, the response metadata  will contain the contributors and works
    metadata if the tracks have"""
    include_works: Literal[0, 1]
