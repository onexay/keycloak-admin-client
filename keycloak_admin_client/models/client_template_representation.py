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
    from openapi_client.models import protocol_mapper_representation
except ImportError:
    protocol_mapper_representation = sys.modules[
        'openapi_client.models.protocol_mapper_representation']


class ClientTemplateRepresentation(ModelNormal):
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
            'name': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'protocol': (str,),  # noqa: E501
            'full_scope_allowed': (bool,),  # noqa: E501
            'bearer_only': (bool,),  # noqa: E501
            'consent_required': (bool,),  # noqa: E501
            'standard_flow_enabled': (bool,),  # noqa: E501
            'implicit_flow_enabled': (bool,),  # noqa: E501
            'direct_access_grants_enabled': (bool,),  # noqa: E501
            'service_accounts_enabled': (bool,),  # noqa: E501
            'public_client': (bool,),  # noqa: E501
            'frontchannel_logout': (bool,),  # noqa: E501
            'attributes': ({str: (str,)},),  # noqa: E501
            'protocol_mappers': ([protocol_mapper_representation.ProtocolMapperRepresentation],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        'id': 'id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'description': 'description',  # noqa: E501
        'protocol': 'protocol',  # noqa: E501
        'full_scope_allowed': 'fullScopeAllowed',  # noqa: E501
        'bearer_only': 'bearerOnly',  # noqa: E501
        'consent_required': 'consentRequired',  # noqa: E501
        'standard_flow_enabled': 'standardFlowEnabled',  # noqa: E501
        'implicit_flow_enabled': 'implicitFlowEnabled',  # noqa: E501
        'direct_access_grants_enabled': 'directAccessGrantsEnabled',  # noqa: E501
        'service_accounts_enabled': 'serviceAccountsEnabled',  # noqa: E501
        'public_client': 'publicClient',  # noqa: E501
        'frontchannel_logout': 'frontchannelLogout',  # noqa: E501
        'attributes': 'attributes',  # noqa: E501
        'protocol_mappers': 'protocolMappers',  # noqa: E501
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
        """client_template_representation.ClientTemplateRepresentation - a model defined in OpenAPI

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
            name (str): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            protocol (str): [optional]  # noqa: E501
            full_scope_allowed (bool): [optional]  # noqa: E501
            bearer_only (bool): [optional]  # noqa: E501
            consent_required (bool): [optional]  # noqa: E501
            standard_flow_enabled (bool): [optional]  # noqa: E501
            implicit_flow_enabled (bool): [optional]  # noqa: E501
            direct_access_grants_enabled (bool): [optional]  # noqa: E501
            service_accounts_enabled (bool): [optional]  # noqa: E501
            public_client (bool): [optional]  # noqa: E501
            frontchannel_logout (bool): [optional]  # noqa: E501
            attributes ({str: (str,)}): [optional]  # noqa: E501
            protocol_mappers ([protocol_mapper_representation.ProtocolMapperRepresentation]): [optional]  # noqa: E501
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
