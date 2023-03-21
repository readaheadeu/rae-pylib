"""Accessors for the Hetzner DNS API

This module wraps the DNS related functionality of the Hetzner cloud API. The
DNS functionality is entirely separated from the other APIs and thus can be
used as stand-alone API.
"""

import typing
import urllib.parse

import requests


class ApiConfiguration(typing.NamedTuple):
    """Global Configuration for the API

    All global configuration parameters to the API are controlled via this
    configuration tuple. The individual fields are:

    token - Optional string used as API authentication token. If not provided,
            No authentication is used.
    url - URL of the API. Make sure to use a trailing slash. The default is
            is the official Hetzner URL 'https://dns.hetzner.com/api/v1/'.
    """

    token: typing.Optional[str] = None
    url: str = "https://dns.hetzner.com/api/v1/"


class RequestError(Exception):
    """An HTTP request failed unexpectedly"""

    response: requests.Response

    def __init__(self, response: requests.Response):
        """Initialize the request-error"""

        self.response = response


class UnauthorizedError(RequestError):
    """Not authorized to access this API"""


class Api:
    """
    """

    _conf: ApiConfiguration

    def __init__(
        self,
        *,
        configuration: typing.Optional[ApiConfiguration] = None,
    ):
        """
        """

        self._conf = configuration or ApiConfiguration()

    def list_zones(
        self,
        *,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        search_name: typing.Optional[str] = None,
    ):
        """
        """

        # Configure the HTTP header.
        headers = {}
        if self._conf.token is not None:
            headers["Auth-API-Token"] = self._conf.token

        # Assemble the API arguments.
        params = {}
        if name is not None:
            params["name"] = name
        if page is not None:
            params["page"] = str(page)
        if per_page is not None:
            params["per_page"] = str(per_page)
        if search_name is not None:
            params["search_name"] = search_name

        # Prepare the request URL.
        url = urllib.parse.urljoin(self._conf.url, "zones")

        # Submit the API request.
        _r = requests.get(
            headers=headers,
            params=params,
            url=url,
        )
        if _r.status_code == 401:
            raise UnauthorizedError(_r)
        elif _r.status_code != 200:
            raise RequestError(_r)
