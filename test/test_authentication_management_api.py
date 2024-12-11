# coding: utf-8

"""
    My Project

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import keycloak_admin_client
from keycloak_admin_client.api.authentication_management_api import AuthenticationManagementApi  # noqa: E501
from keycloak_admin_client.rest import ApiException


class TestAuthenticationManagementApi(unittest.TestCase):
    """AuthenticationManagementApi unit test stubs"""

    def setUp(self):
        self.api = keycloak_admin_client.api.authentication_management_api.AuthenticationManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_realms_realm_authentication_authenticator_providers_get(self):
        """Test case for admin_realms_realm_authentication_authenticator_providers_get

        Get authenticator providers Returns a stream of authenticator providers.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_client_authenticator_providers_get(self):
        """Test case for admin_realms_realm_authentication_client_authenticator_providers_get

        Get client authenticator providers Returns a stream of client authenticator providers.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_config_description_provider_id_get(self):
        """Test case for admin_realms_realm_authentication_config_description_provider_id_get

        Get authenticator provider's configuration description  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_config_id_delete(self):
        """Test case for admin_realms_realm_authentication_config_id_delete

        Delete authenticator configuration  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_config_id_get(self):
        """Test case for admin_realms_realm_authentication_config_id_get

        Get authenticator configuration  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_config_id_put(self):
        """Test case for admin_realms_realm_authentication_config_id_put

        Update authenticator configuration  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_config_post(self):
        """Test case for admin_realms_realm_authentication_config_post

        Create new authenticator configuration  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_executions_execution_id_config_id_get(self):
        """Test case for admin_realms_realm_authentication_executions_execution_id_config_id_get

        Get execution's configuration  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_executions_execution_id_config_post(self):
        """Test case for admin_realms_realm_authentication_executions_execution_id_config_post

        Update execution with new configuration  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_executions_execution_id_delete(self):
        """Test case for admin_realms_realm_authentication_executions_execution_id_delete

        Delete execution  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_executions_execution_id_get(self):
        """Test case for admin_realms_realm_authentication_executions_execution_id_get

        Get Single Execution  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_executions_execution_id_lower_priority_post(self):
        """Test case for admin_realms_realm_authentication_executions_execution_id_lower_priority_post

        Lower execution's priority  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_executions_execution_id_raise_priority_post(self):
        """Test case for admin_realms_realm_authentication_executions_execution_id_raise_priority_post

        Raise execution's priority  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_executions_post(self):
        """Test case for admin_realms_realm_authentication_executions_post

        Add new authentication execution  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_flows_flow_alias_copy_post(self):
        """Test case for admin_realms_realm_authentication_flows_flow_alias_copy_post

        Copy existing authentication flow under a new name The new name is given as 'newName' attribute of the passed JSON object  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_flows_flow_alias_executions_execution_post(self):
        """Test case for admin_realms_realm_authentication_flows_flow_alias_executions_execution_post

        Add new authentication execution to a flow  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_flows_flow_alias_executions_flow_post(self):
        """Test case for admin_realms_realm_authentication_flows_flow_alias_executions_flow_post

        Add new flow with new execution to existing flow  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_flows_flow_alias_executions_get(self):
        """Test case for admin_realms_realm_authentication_flows_flow_alias_executions_get

        Get authentication executions for a flow  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_flows_flow_alias_executions_put(self):
        """Test case for admin_realms_realm_authentication_flows_flow_alias_executions_put

        Update authentication executions of a Flow  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_flows_get(self):
        """Test case for admin_realms_realm_authentication_flows_get

        Get authentication flows Returns a stream of authentication flows.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_flows_id_delete(self):
        """Test case for admin_realms_realm_authentication_flows_id_delete

        Delete an authentication flow  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_flows_id_get(self):
        """Test case for admin_realms_realm_authentication_flows_id_get

        Get authentication flow for id  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_flows_id_put(self):
        """Test case for admin_realms_realm_authentication_flows_id_put

        Update an authentication flow  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_flows_post(self):
        """Test case for admin_realms_realm_authentication_flows_post

        Create a new authentication flow  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_form_action_providers_get(self):
        """Test case for admin_realms_realm_authentication_form_action_providers_get

        Get form action providers Returns a stream of form action providers.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_form_providers_get(self):
        """Test case for admin_realms_realm_authentication_form_providers_get

        Get form providers Returns a stream of form providers.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_per_client_config_description_get(self):
        """Test case for admin_realms_realm_authentication_per_client_config_description_get

        Get configuration descriptions for all clients  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_register_required_action_post(self):
        """Test case for admin_realms_realm_authentication_register_required_action_post

        Register a new required actions  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_required_actions_alias_config_delete(self):
        """Test case for admin_realms_realm_authentication_required_actions_alias_config_delete

        Delete RequiredAction configuration  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_required_actions_alias_config_description_get(self):
        """Test case for admin_realms_realm_authentication_required_actions_alias_config_description_get

        Get RequiredAction provider configuration description  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_required_actions_alias_config_get(self):
        """Test case for admin_realms_realm_authentication_required_actions_alias_config_get

        Get RequiredAction configuration  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_required_actions_alias_config_put(self):
        """Test case for admin_realms_realm_authentication_required_actions_alias_config_put

        Update RequiredAction configuration  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_required_actions_alias_delete(self):
        """Test case for admin_realms_realm_authentication_required_actions_alias_delete

        Delete required action  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_required_actions_alias_get(self):
        """Test case for admin_realms_realm_authentication_required_actions_alias_get

        Get required action for alias  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_required_actions_alias_lower_priority_post(self):
        """Test case for admin_realms_realm_authentication_required_actions_alias_lower_priority_post

        Lower required action's priority  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_required_actions_alias_put(self):
        """Test case for admin_realms_realm_authentication_required_actions_alias_put

        Update required action  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_required_actions_alias_raise_priority_post(self):
        """Test case for admin_realms_realm_authentication_required_actions_alias_raise_priority_post

        Raise required action's priority  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_required_actions_get(self):
        """Test case for admin_realms_realm_authentication_required_actions_get

        Get required actions Returns a stream of required actions.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_authentication_unregistered_required_actions_get(self):
        """Test case for admin_realms_realm_authentication_unregistered_required_actions_get

        Get unregistered required actions Returns a stream of unregistered required actions.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
