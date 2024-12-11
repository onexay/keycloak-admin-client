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
    from openapi_client.models import any_ofstringnull
except ImportError:
    any_ofstringnull = sys.modules[
        'openapi_client.models.any_ofstringnull']


class TenantVendorsResSchema(ModelNormal):
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
            'contact_fullname': (str,),  # noqa: E501
            'contact_mobile': (str,),  # noqa: E501
            'contact_email': (any_ofstringnull.AnyOfstringnull,),  # noqa: E501
            'tenant_id': (str,),  # noqa: E501
            'vendor_id': (str,),  # noqa: E501
            'created_ts': (datetime,),  # noqa: E501
            'updated_ts': (datetime,),  # noqa: E501
            'active': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        'contact_fullname': 'contact_fullname',  # noqa: E501
        'contact_mobile': 'contact_mobile',  # noqa: E501
        'contact_email': 'contact_email',  # noqa: E501
        'tenant_id': 'tenant_id',  # noqa: E501
        'vendor_id': 'vendor_id',  # noqa: E501
        'created_ts': 'created_ts',  # noqa: E501
        'updated_ts': 'updated_ts',  # noqa: E501
        'active': 'active',  # noqa: E501
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
    def __init__(self, contact_fullname, contact_mobile, contact_email, tenant_id, vendor_id, created_ts, updated_ts, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, _visited_composed_classes=(), **kwargs):  # noqa: E501
        """tenant_vendors_res_schema.TenantVendorsResSchema - a model defined in OpenAPI

        Args:
            contact_fullname (str): Contact Fullname
            contact_mobile (str): Contact Mobile
            contact_email (any_ofstringnull.AnyOfstringnull): Contact Email
            tenant_id (str): Tenant Id
            vendor_id (str): Vendor Id
            created_ts (datetime): Created Ts
            updated_ts (datetime): Updated Ts

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
            active (bool): Active. [optional] if omitted the server will use the default value of True  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.contact_fullname = contact_fullname
        self.contact_mobile = contact_mobile
        self.contact_email = contact_email
        self.tenant_id = tenant_id
        self.vendor_id = vendor_id
        self.created_ts = created_ts
        self.updated_ts = updated_ts
        for var_name, var_value in six.iteritems(kwargs):
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
