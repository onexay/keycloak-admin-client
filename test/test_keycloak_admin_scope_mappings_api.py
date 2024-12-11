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
from openapi_client.api.keycloak_admin_scope_mappings_api import KeycloakAdminScopeMappingsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestKeycloakAdminScopeMappingsApi(unittest.TestCase):
    """KeycloakAdminScopeMappingsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.keycloak_admin_scope_mappings_api.KeycloakAdminScopeMappingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_available_get(self):
        """Test case for admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_available_get

        The available client-level roles Returns the roles for the client that can be associated with the client's scope  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_composite_get(self):
        """Test case for admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_composite_get

        Get effective client roles Returns the roles for the client that are associated with the client's scope.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_delete(self):
        """Test case for admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_delete

        Remove client-level roles from the client's scope.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_get(self):
        """Test case for admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_get

        Get the roles associated with a client's scope Returns roles for the client.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_post(self):
        """Test case for admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_post

        Add client-level roles to the client's scope  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_scopes_client_scope_id_scope_mappings_get(self):
        """Test case for admin_realms_realm_client_scopes_client_scope_id_scope_mappings_get

        Get all scope mappings for the client  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_available_get(self):
        """Test case for admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_available_get

        Get realm-level roles that are available to attach to this client's scope  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_composite_get(self):
        """Test case for admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_composite_get

        Get effective realm-level roles associated with the client’s scope What this does is recurse any composite roles associated with the client’s scope and adds the roles to this lists.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_delete(self):
        """Test case for admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_delete

        Remove a set of realm-level roles from the client's scope  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_get(self):
        """Test case for admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_get

        Get realm-level roles associated with the client's scope  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_post(self):
        """Test case for admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_post

        Add a set of realm-level roles to the client's scope  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_available_get(self):
        """Test case for admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_available_get

        The available client-level roles Returns the roles for the client that can be associated with the client's scope  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_composite_get(self):
        """Test case for admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_composite_get

        Get effective client roles Returns the roles for the client that are associated with the client's scope.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_delete(self):
        """Test case for admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_delete

        Remove client-level roles from the client's scope.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_get(self):
        """Test case for admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_get

        Get the roles associated with a client's scope Returns roles for the client.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_post(self):
        """Test case for admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_post

        Add client-level roles to the client's scope  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_templates_client_scope_id_scope_mappings_get(self):
        """Test case for admin_realms_realm_client_templates_client_scope_id_scope_mappings_get

        Get all scope mappings for the client  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_available_get(self):
        """Test case for admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_available_get

        Get realm-level roles that are available to attach to this client's scope  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_composite_get(self):
        """Test case for admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_composite_get

        Get effective realm-level roles associated with the client’s scope What this does is recurse any composite roles associated with the client’s scope and adds the roles to this lists.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_delete(self):
        """Test case for admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_delete

        Remove a set of realm-level roles from the client's scope  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_get(self):
        """Test case for admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_get

        Get realm-level roles associated with the client's scope  # noqa: E501
        """
        pass

    def test_admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_post(self):
        """Test case for admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_post

        Add a set of realm-level roles to the client's scope  # noqa: E501
        """
        pass

    def test_admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_available_get(self):
        """Test case for admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_available_get

        The available client-level roles Returns the roles for the client that can be associated with the client's scope  # noqa: E501
        """
        pass

    def test_admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_composite_get(self):
        """Test case for admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_composite_get

        Get effective client roles Returns the roles for the client that are associated with the client's scope.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_delete(self):
        """Test case for admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_delete

        Remove client-level roles from the client's scope.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_get(self):
        """Test case for admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_get

        Get the roles associated with a client's scope Returns roles for the client.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_post(self):
        """Test case for admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_post

        Add client-level roles to the client's scope  # noqa: E501
        """
        pass

    def test_admin_realms_realm_clients_client_uuid_scope_mappings_get(self):
        """Test case for admin_realms_realm_clients_client_uuid_scope_mappings_get

        Get all scope mappings for the client  # noqa: E501
        """
        pass

    def test_admin_realms_realm_clients_client_uuid_scope_mappings_realm_available_get(self):
        """Test case for admin_realms_realm_clients_client_uuid_scope_mappings_realm_available_get

        Get realm-level roles that are available to attach to this client's scope  # noqa: E501
        """
        pass

    def test_admin_realms_realm_clients_client_uuid_scope_mappings_realm_composite_get(self):
        """Test case for admin_realms_realm_clients_client_uuid_scope_mappings_realm_composite_get

        Get effective realm-level roles associated with the client’s scope What this does is recurse any composite roles associated with the client’s scope and adds the roles to this lists.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_clients_client_uuid_scope_mappings_realm_delete(self):
        """Test case for admin_realms_realm_clients_client_uuid_scope_mappings_realm_delete

        Remove a set of realm-level roles from the client's scope  # noqa: E501
        """
        pass

    def test_admin_realms_realm_clients_client_uuid_scope_mappings_realm_get(self):
        """Test case for admin_realms_realm_clients_client_uuid_scope_mappings_realm_get

        Get realm-level roles associated with the client's scope  # noqa: E501
        """
        pass

    def test_admin_realms_realm_clients_client_uuid_scope_mappings_realm_post(self):
        """Test case for admin_realms_realm_clients_client_uuid_scope_mappings_realm_post

        Add a set of realm-level roles to the client's scope  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()