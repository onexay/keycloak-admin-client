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
    from openapi_client.models import multivalued_hash_map_string_string
except ImportError:
    multivalued_hash_map_string_string = sys.modules[
        'openapi_client.models.multivalued_hash_map_string_string']


class CredentialRepresentation(ModelNormal):
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
            'type': (str,),  # noqa: E501
            'user_label': (str,),  # noqa: E501
            'created_date': (int,),  # noqa: E501
            'secret_data': (str,),  # noqa: E501
            'credential_data': (str,),  # noqa: E501
            'priority': (int,),  # noqa: E501
            'value': (str,),  # noqa: E501
            'temporary': (bool,),  # noqa: E501
            'device': (str,),  # noqa: E501
            'hashed_salted_value': (str,),  # noqa: E501
            'salt': (str,),  # noqa: E501
            'hash_iterations': (int,),  # noqa: E501
            'counter': (int,),  # noqa: E501
            'algorithm': (str,),  # noqa: E501
            'digits': (int,),  # noqa: E501
            'period': (int,),  # noqa: E501
            'config': (multivalued_hash_map_string_string.MultivaluedHashMapStringString,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        'id': 'id',  # noqa: E501
        'type': 'type',  # noqa: E501
        'user_label': 'userLabel',  # noqa: E501
        'created_date': 'createdDate',  # noqa: E501
        'secret_data': 'secretData',  # noqa: E501
        'credential_data': 'credentialData',  # noqa: E501
        'priority': 'priority',  # noqa: E501
        'value': 'value',  # noqa: E501
        'temporary': 'temporary',  # noqa: E501
        'device': 'device',  # noqa: E501
        'hashed_salted_value': 'hashedSaltedValue',  # noqa: E501
        'salt': 'salt',  # noqa: E501
        'hash_iterations': 'hashIterations',  # noqa: E501
        'counter': 'counter',  # noqa: E501
        'algorithm': 'algorithm',  # noqa: E501
        'digits': 'digits',  # noqa: E501
        'period': 'period',  # noqa: E501
        'config': 'config',  # noqa: E501
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
        """credential_representation.CredentialRepresentation - a model defined in OpenAPI

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
            type (str): [optional]  # noqa: E501
            user_label (str): [optional]  # noqa: E501
            created_date (int): [optional]  # noqa: E501
            secret_data (str): [optional]  # noqa: E501
            credential_data (str): [optional]  # noqa: E501
            priority (int): [optional]  # noqa: E501
            value (str): [optional]  # noqa: E501
            temporary (bool): [optional]  # noqa: E501
            device (str): [optional]  # noqa: E501
            hashed_salted_value (str): [optional]  # noqa: E501
            salt (str): [optional]  # noqa: E501
            hash_iterations (int): [optional]  # noqa: E501
            counter (int): [optional]  # noqa: E501
            algorithm (str): [optional]  # noqa: E501
            digits (int): [optional]  # noqa: E501
            period (int): [optional]  # noqa: E501
            config (multivalued_hash_map_string_string.MultivaluedHashMapStringString): [optional]  # noqa: E501
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
