# coding: utf-8

"""
    My Project

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import
import re  # noqa: F401
import sys  # noqa: F401

import six  # noqa: F401
import nulltype  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    int,
    none_type,
    str,
    validate_get_composed_info,
)
try:
    from openapi_client.models import credential_representation
except ImportError:
    credential_representation = sys.modules[
        'openapi_client.models.credential_representation']
try:
    from openapi_client.models import federated_identity_representation
except ImportError:
    federated_identity_representation = sys.modules[
        'openapi_client.models.federated_identity_representation']
try:
    from openapi_client.models import membership_type
except ImportError:
    membership_type = sys.modules[
        'openapi_client.models.membership_type']
try:
    from openapi_client.models import social_link_representation
except ImportError:
    social_link_representation = sys.modules[
        'openapi_client.models.social_link_representation']
try:
    from openapi_client.models import user_consent_representation
except ImportError:
    user_consent_representation = sys.modules[
        'openapi_client.models.user_consent_representation']
try:
    from openapi_client.models import user_profile_metadata
except ImportError:
    user_profile_metadata = sys.modules[
        'openapi_client.models.user_profile_metadata']


class MemberRepresentation(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    @cached_property
    def openapi_types():
        """
        This must be a class method so a model may have properties that are
        of type self, this ensures that we don't create a cyclic import

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'id': (str,),  # noqa: E501
            'username': (str,),  # noqa: E501
            'first_name': (str,),  # noqa: E501
            'last_name': (str,),  # noqa: E501
            'email': (str,),  # noqa: E501
            'email_verified': (bool,),  # noqa: E501
            'attributes': ({str: ([str],)},),  # noqa: E501
            'user_profile_metadata': (user_profile_metadata.UserProfileMetadata,),  # noqa: E501
            '_self': (str,),  # noqa: E501
            'origin': (str,),  # noqa: E501
            'created_timestamp': (int,),  # noqa: E501
            'enabled': (bool,),  # noqa: E501
            'totp': (bool,),  # noqa: E501
            'federation_link': (str,),  # noqa: E501
            'service_account_client_id': (str,),  # noqa: E501
            'credentials': ([credential_representation.CredentialRepresentation],),  # noqa: E501
            'disableable_credential_types': ([str],),  # noqa: E501
            'required_actions': ([str],),  # noqa: E501
            'federated_identities': ([federated_identity_representation.FederatedIdentityRepresentation],),  # noqa: E501
            'realm_roles': ([str],),  # noqa: E501
            'client_roles': ({str: ([str],)},),  # noqa: E501
            'client_consents': ([user_consent_representation.UserConsentRepresentation],),  # noqa: E501
            'not_before': (int,),  # noqa: E501
            'application_roles': ({str: ([str],)},),  # noqa: E501
            'social_links': ([social_link_representation.SocialLinkRepresentation],),  # noqa: E501
            'groups': ([str],),  # noqa: E501
            'access': ({str: (bool,)},),  # noqa: E501
            'membership_type': (membership_type.MembershipType,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        'id': 'id',  # noqa: E501
        'username': 'username',  # noqa: E501
        'first_name': 'firstName',  # noqa: E501
        'last_name': 'lastName',  # noqa: E501
        'email': 'email',  # noqa: E501
        'email_verified': 'emailVerified',  # noqa: E501
        'attributes': 'attributes',  # noqa: E501
        'user_profile_metadata': 'userProfileMetadata',  # noqa: E501
        '_self': 'self',  # noqa: E501
        'origin': 'origin',  # noqa: E501
        'created_timestamp': 'createdTimestamp',  # noqa: E501
        'enabled': 'enabled',  # noqa: E501
        'totp': 'totp',  # noqa: E501
        'federation_link': 'federationLink',  # noqa: E501
        'service_account_client_id': 'serviceAccountClientId',  # noqa: E501
        'credentials': 'credentials',  # noqa: E501
        'disableable_credential_types': 'disableableCredentialTypes',  # noqa: E501
        'required_actions': 'requiredActions',  # noqa: E501
        'federated_identities': 'federatedIdentities',  # noqa: E501
        'realm_roles': 'realmRoles',  # noqa: E501
        'client_roles': 'clientRoles',  # noqa: E501
        'client_consents': 'clientConsents',  # noqa: E501
        'not_before': 'notBefore',  # noqa: E501
        'application_roles': 'applicationRoles',  # noqa: E501
        'social_links': 'socialLinks',  # noqa: E501
        'groups': 'groups',  # noqa: E501
        'access': 'access',  # noqa: E501
        'membership_type': 'membershipType',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_from_server',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, _visited_composed_classes=(), **kwargs):  # noqa: E501
        """member_representation.MemberRepresentation - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _from_server (bool): True if the data is from the server
                                False if the data is from the client (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): [optional]  # noqa: E501
            username (str): [optional]  # noqa: E501
            first_name (str): [optional]  # noqa: E501
            last_name (str): [optional]  # noqa: E501
            email (str): [optional]  # noqa: E501
            email_verified (bool): [optional]  # noqa: E501
            attributes ({str: ([str],)}): [optional]  # noqa: E501
            user_profile_metadata (user_profile_metadata.UserProfileMetadata): [optional]  # noqa: E501
            _self (str): [optional]  # noqa: E501
            origin (str): [optional]  # noqa: E501
            created_timestamp (int): [optional]  # noqa: E501
            enabled (bool): [optional]  # noqa: E501
            totp (bool): [optional]  # noqa: E501
            federation_link (str): [optional]  # noqa: E501
            service_account_client_id (str): [optional]  # noqa: E501
            credentials ([credential_representation.CredentialRepresentation]): [optional]  # noqa: E501
            disableable_credential_types ([str]): [optional]  # noqa: E501
            required_actions ([str]): [optional]  # noqa: E501
            federated_identities ([federated_identity_representation.FederatedIdentityRepresentation]): [optional]  # noqa: E501
            realm_roles ([str]): [optional]  # noqa: E501
            client_roles ({str: ([str],)}): [optional]  # noqa: E501
            client_consents ([user_consent_representation.UserConsentRepresentation]): [optional]  # noqa: E501
            not_before (int): [optional]  # noqa: E501
            application_roles ({str: ([str],)}): [optional]  # noqa: E501
            social_links ([social_link_representation.SocialLinkRepresentation]): [optional]  # noqa: E501
            groups ([str]): [optional]  # noqa: E501
            access ({str: (bool,)}): [optional]  # noqa: E501
            membership_type (membership_type.MembershipType): [optional]  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in six.iteritems(kwargs):
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)