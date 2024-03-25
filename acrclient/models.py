"""Models for acr-client."""

from __future__ import annotations

from typing import NotRequired, TypedDict


class GetBmCsProjectsResultsParams(TypedDict):  # pragma: no cover
    """Parameters for getting BM projects custom streams results."""

    type: str
    """last: get the last results, day: get the day results, Default is day"""
    date: str
    """Get all the results on this date. The format is YYYYmmdd (E.g. 20210201)"""
    min_duration: NotRequired[int | None]
    """Return the results of played_duration >= min_duration seconds (default: 0)"""
    max_duration: NotRequired[int | None]
    """Return results with played_duration <= max_duration seconds (default: 3600)"""
    isrc_country: NotRequired[str | None]
    """Only return results that match the isrc country code (E.g. DE, FR, IT, US)"""
