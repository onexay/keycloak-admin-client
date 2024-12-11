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
from openapi_client.api.client_role_mappings_api import ClientRoleMappingsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestClientRoleMappingsApi(unittest.TestCase):
    """ClientRoleMappingsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.client_role_mappings_api.ClientRoleMappingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_realms_realm_groups_group_id_role_mappings_clients_client_id_available_get(self):
        """Test case for admin_realms_realm_groups_group_id_role_mappings_clients_client_id_available_get

        Get available client-level roles that can be mapped to the user or group  # noqa: E501
        """
        pass

    def test_admin_realms_realm_groups_group_id_role_mappings_clients_client_id_composite_get(self):
        """Test case for admin_realms_realm_groups_group_id_role_mappings_clients_client_id_composite_get

        Get effective client-level role mappings This recurses any composite roles  # noqa: E501
        """
        pass

    def test_admin_realms_realm_groups_group_id_role_mappings_clients_client_id_delete(self):
        """Test case for admin_realms_realm_groups_group_id_role_mappings_clients_client_id_delete

        Delete client-level roles from user or group role mapping  # noqa: E501
        """
        pass

    def test_admin_realms_realm_groups_group_id_role_mappings_clients_client_id_get(self):
        """Test case for admin_realms_realm_groups_group_id_role_mappings_clients_client_id_get

        Get client-level role mappings for the user or group, and the app  # noqa: E501
        """
        pass

    def test_admin_realms_realm_groups_group_id_role_mappings_clients_client_id_post(self):
        """Test case for admin_realms_realm_groups_group_id_role_mappings_clients_client_id_post

        Add client-level roles to the user or group role mapping  # noqa: E501
        """
        pass

    def test_admin_realms_realm_users_user_id_role_mappings_clients_client_id_available_get(self):
        """Test case for admin_realms_realm_users_user_id_role_mappings_clients_client_id_available_get

        Get available client-level roles that can be mapped to the user or group  # noqa: E501
        """
        pass

    def test_admin_realms_realm_users_user_id_role_mappings_clients_client_id_composite_get(self):
        """Test case for admin_realms_realm_users_user_id_role_mappings_clients_client_id_composite_get

        Get effective client-level role mappings This recurses any composite roles  # noqa: E501
        """
        pass

    def test_admin_realms_realm_users_user_id_role_mappings_clients_client_id_delete(self):
        """Test case for admin_realms_realm_users_user_id_role_mappings_clients_client_id_delete

        Delete client-level roles from user or group role mapping  # noqa: E501
        """
        pass

    def test_admin_realms_realm_users_user_id_role_mappings_clients_client_id_get(self):
        """Test case for admin_realms_realm_users_user_id_role_mappings_clients_client_id_get

        Get client-level role mappings for the user or group, and the app  # noqa: E501
        """
        pass

    def test_admin_realms_realm_users_user_id_role_mappings_clients_client_id_post(self):
        """Test case for admin_realms_realm_users_user_id_role_mappings_clients_client_id_post

        Add client-level roles to the user or group role mapping  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
