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
from keycloak_admin_client.api.component_api import ComponentApi  # noqa: E501
from keycloak_admin_client.rest import ApiException


class TestComponentApi(unittest.TestCase):
    """ComponentApi unit test stubs"""

    def setUp(self):
        self.api = keycloak_admin_client.api.component_api.ComponentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_realms_realm_components_get(self):
        """Test case for admin_realms_realm_components_get

        /admin/realms/{realm}/components  # noqa: E501
        """
        pass

    def test_admin_realms_realm_components_id_delete(self):
        """Test case for admin_realms_realm_components_id_delete

        /admin/realms/{realm}/components/{id}  # noqa: E501
        """
        pass

    def test_admin_realms_realm_components_id_get(self):
        """Test case for admin_realms_realm_components_id_get

        /admin/realms/{realm}/components/{id}  # noqa: E501
        """
        pass

    def test_admin_realms_realm_components_id_put(self):
        """Test case for admin_realms_realm_components_id_put

        /admin/realms/{realm}/components/{id}  # noqa: E501
        """
        pass

    def test_admin_realms_realm_components_id_sub_component_types_get(self):
        """Test case for admin_realms_realm_components_id_sub_component_types_get

        List of subcomponent types that are available to configure for a particular parent component.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_components_post(self):
        """Test case for admin_realms_realm_components_post

        /admin/realms/{realm}/components  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
