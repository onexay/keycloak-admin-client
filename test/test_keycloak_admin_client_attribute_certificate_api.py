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
from openapi_client.api.keycloak_admin_client_attribute_certificate_api import KeycloakAdminClientAttributeCertificateApi  # noqa: E501
from openapi_client.rest import ApiException


class TestKeycloakAdminClientAttributeCertificateApi(unittest.TestCase):
    """KeycloakAdminClientAttributeCertificateApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.keycloak_admin_client_attribute_certificate_api.KeycloakAdminClientAttributeCertificateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_realms_realm_clients_client_uuid_certificates_attr_download_post(self):
        """Test case for admin_realms_realm_clients_client_uuid_certificates_attr_download_post

        Get a keystore file for the client, containing private key and public certificate  # noqa: E501
        """
        pass

    def test_admin_realms_realm_clients_client_uuid_certificates_attr_generate_and_download_post(self):
        """Test case for admin_realms_realm_clients_client_uuid_certificates_attr_generate_and_download_post

        Generate a new keypair and certificate, and get the private key file  Generates a keypair and certificate and serves the private key in a specified keystore format. Only generated public certificate is saved in Keycloak DB - the private key is not.  # noqa: E501
        """
        pass

    def test_admin_realms_realm_clients_client_uuid_certificates_attr_generate_post(self):
        """Test case for admin_realms_realm_clients_client_uuid_certificates_attr_generate_post

        Generate a new certificate with new key pair  # noqa: E501
        """
        pass

    def test_admin_realms_realm_clients_client_uuid_certificates_attr_get(self):
        """Test case for admin_realms_realm_clients_client_uuid_certificates_attr_get

        Get key info  # noqa: E501
        """
        pass

    def test_admin_realms_realm_clients_client_uuid_certificates_attr_upload_certificate_post(self):
        """Test case for admin_realms_realm_clients_client_uuid_certificates_attr_upload_certificate_post

        Upload only certificate, not private key  # noqa: E501
        """
        pass

    def test_admin_realms_realm_clients_client_uuid_certificates_attr_upload_post(self):
        """Test case for admin_realms_realm_clients_client_uuid_certificates_attr_upload_post

        Upload certificate and eventually private key  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
