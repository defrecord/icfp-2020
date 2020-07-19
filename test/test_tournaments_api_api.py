# coding: utf-8

"""
    ICFP Contest 2020 API

    See <a href='https://github.com/icfpcontest2020/aliens-proxy-protocol' target='_blank'>https://github.com/icfpcontest2020/aliens-proxy-protocol<a/>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.tournaments_api_api import TournamentsApiApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTournamentsApiApi(unittest.TestCase):
    """TournamentsApiApi unit test stubs"""

    def setUp(self):
        self.api = api.tournaments_api_api.TournamentsApiApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tournaments_current_get(self):
        """Test case for tournaments_current_get

        """
        pass

    def test_tournaments_get(self):
        """Test case for tournaments_get

        """
        pass

    def test_tournaments_tournament_id_get(self):
        """Test case for tournaments_tournament_id_get

        """
        pass


if __name__ == '__main__':
    unittest.main()