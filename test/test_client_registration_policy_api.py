# coding: utf-8

"""
    My Project

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.client_registration_policy_api import ClientRegistrationPolicyApi  # noqa: E501
from openapi_client.rest import ApiException


class TestClientRegistrationPolicyApi(unittest.TestCase):
    """ClientRegistrationPolicyApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.client_registration_policy_api.ClientRegistrationPolicyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_realms_realm_client_registration_policy_providers_get(self):
        """Test case for admin_realms_realm_client_registration_policy_providers_get

        Base path for retrieve providers with the configProperties properly filled  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()