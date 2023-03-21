"""Tests for rae-hetzner

Basic functionality-testing for the rae-hetzner library.
"""

import rae_hetzner


def test_dns():
    conf = rae_hetzner.dns.ApiConfiguration(token="<foobar>")
    _api = rae_hetzner.dns.Api(configuration=conf)
    #api.list_zones()
