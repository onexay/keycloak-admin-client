# openapi_client.IdentityProvidersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_realm_identity_provider_import_config_post**](IdentityProvidersApi.md#admin_realms_realm_identity_provider_import_config_post) | **POST** /admin/realms/{realm}/identity-provider/import-config | Import identity provider from JSON body
[**admin_realms_realm_identity_provider_instances_alias_delete**](IdentityProvidersApi.md#admin_realms_realm_identity_provider_instances_alias_delete) | **DELETE** /admin/realms/{realm}/identity-provider/instances/{alias} | Delete the identity provider
[**admin_realms_realm_identity_provider_instances_alias_export_get**](IdentityProvidersApi.md#admin_realms_realm_identity_provider_instances_alias_export_get) | **GET** /admin/realms/{realm}/identity-provider/instances/{alias}/export | Export public broker configuration for identity provider
[**admin_realms_realm_identity_provider_instances_alias_get**](IdentityProvidersApi.md#admin_realms_realm_identity_provider_instances_alias_get) | **GET** /admin/realms/{realm}/identity-provider/instances/{alias} | Get the identity provider
[**admin_realms_realm_identity_provider_instances_alias_management_permissions_get**](IdentityProvidersApi.md#admin_realms_realm_identity_provider_instances_alias_management_permissions_get) | **GET** /admin/realms/{realm}/identity-provider/instances/{alias}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**admin_realms_realm_identity_provider_instances_alias_management_permissions_put**](IdentityProvidersApi.md#admin_realms_realm_identity_provider_instances_alias_management_permissions_put) | **PUT** /admin/realms/{realm}/identity-provider/instances/{alias}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**admin_realms_realm_identity_provider_instances_alias_mapper_types_get**](IdentityProvidersApi.md#admin_realms_realm_identity_provider_instances_alias_mapper_types_get) | **GET** /admin/realms/{realm}/identity-provider/instances/{alias}/mapper-types | Get mapper types for identity provider
[**admin_realms_realm_identity_provider_instances_alias_mappers_get**](IdentityProvidersApi.md#admin_realms_realm_identity_provider_instances_alias_mappers_get) | **GET** /admin/realms/{realm}/identity-provider/instances/{alias}/mappers | Get mappers for identity provider
[**admin_realms_realm_identity_provider_instances_alias_mappers_id_delete**](IdentityProvidersApi.md#admin_realms_realm_identity_provider_instances_alias_mappers_id_delete) | **DELETE** /admin/realms/{realm}/identity-provider/instances/{alias}/mappers/{id} | Delete a mapper for the identity provider
[**admin_realms_realm_identity_provider_instances_alias_mappers_id_get**](IdentityProvidersApi.md#admin_realms_realm_identity_provider_instances_alias_mappers_id_get) | **GET** /admin/realms/{realm}/identity-provider/instances/{alias}/mappers/{id} | Get mapper by id for the identity provider
[**admin_realms_realm_identity_provider_instances_alias_mappers_id_put**](IdentityProvidersApi.md#admin_realms_realm_identity_provider_instances_alias_mappers_id_put) | **PUT** /admin/realms/{realm}/identity-provider/instances/{alias}/mappers/{id} | Update a mapper for the identity provider
[**admin_realms_realm_identity_provider_instances_alias_mappers_post**](IdentityProvidersApi.md#admin_realms_realm_identity_provider_instances_alias_mappers_post) | **POST** /admin/realms/{realm}/identity-provider/instances/{alias}/mappers | Add a mapper to identity provider
[**admin_realms_realm_identity_provider_instances_alias_put**](IdentityProvidersApi.md#admin_realms_realm_identity_provider_instances_alias_put) | **PUT** /admin/realms/{realm}/identity-provider/instances/{alias} | Update the identity provider
[**admin_realms_realm_identity_provider_instances_alias_reload_keys_get**](IdentityProvidersApi.md#admin_realms_realm_identity_provider_instances_alias_reload_keys_get) | **GET** /admin/realms/{realm}/identity-provider/instances/{alias}/reload-keys | Reaload keys for the identity provider if the provider supports it, \&quot;true\&quot; is returned if reload was performed, \&quot;false\&quot; if not.
[**admin_realms_realm_identity_provider_instances_get**](IdentityProvidersApi.md#admin_realms_realm_identity_provider_instances_get) | **GET** /admin/realms/{realm}/identity-provider/instances | List identity providers
[**admin_realms_realm_identity_provider_instances_post**](IdentityProvidersApi.md#admin_realms_realm_identity_provider_instances_post) | **POST** /admin/realms/{realm}/identity-provider/instances | Create a new identity provider
[**admin_realms_realm_identity_provider_providers_provider_id_get**](IdentityProvidersApi.md#admin_realms_realm_identity_provider_providers_provider_id_get) | **GET** /admin/realms/{realm}/identity-provider/providers/{provider_id} | Get the identity provider factory for that provider id


# **admin_realms_realm_identity_provider_import_config_post**
> {str: (str,)} admin_realms_realm_identity_provider_import_config_post(realm)

Import identity provider from JSON body

Import identity provider from uploaded JSON file

### Example

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IdentityProvidersApi(api_client)
    realm = 'realm_example' # str | 
    request_body = {'key': 'request_body_example'} # {str: (str,)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import identity provider from JSON body
        api_response = api_instance.admin_realms_realm_identity_provider_import_config_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_import_config_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import identity provider from JSON body
        api_response = api_instance.admin_realms_realm_identity_provider_import_config_post(realm, request_body=request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_import_config_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **request_body** | **{str: (str,)}**|  | [optional]

### Return type

**{str: (str,)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_identity_provider_instances_alias_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_identity_provider_instances_alias_delete(realm, alias)

Delete the identity provider

### Example

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IdentityProvidersApi(api_client)
    realm = 'realm_example' # str | 
    alias = 'alias_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete the identity provider
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_delete(realm, alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **alias** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_identity_provider_instances_alias_export_get**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_identity_provider_instances_alias_export_get(realm, alias)

Export public broker configuration for identity provider

### Example

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IdentityProvidersApi(api_client)
    realm = 'realm_example' # str | 
    alias = 'alias_example' # str | 
    format = 'format_example' # str | Format to use (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export public broker configuration for identity provider
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_export_get(realm, alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_export_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export public broker configuration for identity provider
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_export_get(realm, alias, format=format)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_export_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **alias** | **str**|  |
 **format** | **str**| Format to use | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_identity_provider_instances_alias_get**
> identity_provider_representation.IdentityProviderRepresentation admin_realms_realm_identity_provider_instances_alias_get(realm, alias)

Get the identity provider

### Example

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IdentityProvidersApi(api_client)
    realm = 'realm_example' # str | 
    alias = 'alias_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get the identity provider
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_get(realm, alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **alias** | **str**|  |

### Return type

[**identity_provider_representation.IdentityProviderRepresentation**](IdentityProviderRepresentation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_identity_provider_instances_alias_management_permissions_get**
> management_permission_reference.ManagementPermissionReference admin_realms_realm_identity_provider_instances_alias_management_permissions_get(realm, alias)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IdentityProvidersApi(api_client)
    realm = 'realm_example' # str | 
    alias = 'alias_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether client Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_management_permissions_get(realm, alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_management_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **alias** | **str**|  |

### Return type

[**management_permission_reference.ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_identity_provider_instances_alias_management_permissions_put**
> management_permission_reference.ManagementPermissionReference admin_realms_realm_identity_provider_instances_alias_management_permissions_put(realm, alias)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IdentityProvidersApi(api_client)
    realm = 'realm_example' # str | 
    alias = 'alias_example' # str | 
    management_permission_reference_management_permission_reference = openapi_client.ManagementPermissionReference() # management_permission_reference.ManagementPermissionReference |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether client Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_management_permissions_put(realm, alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_management_permissions_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return object stating whether client Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_management_permissions_put(realm, alias, management_permission_reference_management_permission_reference=management_permission_reference_management_permission_reference)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_management_permissions_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **alias** | **str**|  |
 **management_permission_reference_management_permission_reference** | [**management_permission_reference.ManagementPermissionReference**](ManagementPermissionReference.md)|  | [optional]

### Return type

[**management_permission_reference.ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_identity_provider_instances_alias_mapper_types_get**
> {str: (identity_provider_mapper_type_representation.IdentityProviderMapperTypeRepresentation,)} admin_realms_realm_identity_provider_instances_alias_mapper_types_get(realm, alias)

Get mapper types for identity provider

### Example

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IdentityProvidersApi(api_client)
    realm = 'realm_example' # str | 
    alias = 'alias_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get mapper types for identity provider
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_mapper_types_get(realm, alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_mapper_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **alias** | **str**|  |

### Return type

[**{str: (identity_provider_mapper_type_representation.IdentityProviderMapperTypeRepresentation,)}**](IdentityProviderMapperTypeRepresentation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_identity_provider_instances_alias_mappers_get**
> [identity_provider_mapper_representation.IdentityProviderMapperRepresentation] admin_realms_realm_identity_provider_instances_alias_mappers_get(realm, alias)

Get mappers for identity provider

### Example

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IdentityProvidersApi(api_client)
    realm = 'realm_example' # str | 
    alias = 'alias_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get mappers for identity provider
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_mappers_get(realm, alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_mappers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **alias** | **str**|  |

### Return type

[**[identity_provider_mapper_representation.IdentityProviderMapperRepresentation]**](IdentityProviderMapperRepresentation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_identity_provider_instances_alias_mappers_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_identity_provider_instances_alias_mappers_id_delete(id, realm, alias)

Delete a mapper for the identity provider

### Example

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IdentityProvidersApi(api_client)
    id = 'id_example' # str | Mapper id
    realm = 'realm_example' # str | 
    alias = 'alias_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete a mapper for the identity provider
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_mappers_id_delete(id, realm, alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_mappers_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Mapper id |
 **realm** | **str**|  |
 **alias** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_identity_provider_instances_alias_mappers_id_get**
> identity_provider_mapper_representation.IdentityProviderMapperRepresentation admin_realms_realm_identity_provider_instances_alias_mappers_id_get(id, realm, alias)

Get mapper by id for the identity provider

### Example

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IdentityProvidersApi(api_client)
    id = 'id_example' # str | 
    realm = 'realm_example' # str | 
    alias = 'alias_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get mapper by id for the identity provider
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_mappers_id_get(id, realm, alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_mappers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **realm** | **str**|  |
 **alias** | **str**|  |

### Return type

[**identity_provider_mapper_representation.IdentityProviderMapperRepresentation**](IdentityProviderMapperRepresentation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_identity_provider_instances_alias_mappers_id_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_identity_provider_instances_alias_mappers_id_put(id, realm, alias)

Update a mapper for the identity provider

### Example

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IdentityProvidersApi(api_client)
    id = 'id_example' # str | Mapper id
    realm = 'realm_example' # str | 
    alias = 'alias_example' # str | 
    identity_provider_mapper_representation_identity_provider_mapper_representation = openapi_client.IdentityProviderMapperRepresentation() # identity_provider_mapper_representation.IdentityProviderMapperRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a mapper for the identity provider
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_mappers_id_put(id, realm, alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_mappers_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a mapper for the identity provider
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_mappers_id_put(id, realm, alias, identity_provider_mapper_representation_identity_provider_mapper_representation=identity_provider_mapper_representation_identity_provider_mapper_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_mappers_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Mapper id |
 **realm** | **str**|  |
 **alias** | **str**|  |
 **identity_provider_mapper_representation_identity_provider_mapper_representation** | [**identity_provider_mapper_representation.IdentityProviderMapperRepresentation**](IdentityProviderMapperRepresentation.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_identity_provider_instances_alias_mappers_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_identity_provider_instances_alias_mappers_post(realm, alias)

Add a mapper to identity provider

### Example

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IdentityProvidersApi(api_client)
    realm = 'realm_example' # str | 
    alias = 'alias_example' # str | 
    identity_provider_mapper_representation_identity_provider_mapper_representation = openapi_client.IdentityProviderMapperRepresentation() # identity_provider_mapper_representation.IdentityProviderMapperRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a mapper to identity provider
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_mappers_post(realm, alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_mappers_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a mapper to identity provider
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_mappers_post(realm, alias, identity_provider_mapper_representation_identity_provider_mapper_representation=identity_provider_mapper_representation_identity_provider_mapper_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_mappers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **alias** | **str**|  |
 **identity_provider_mapper_representation_identity_provider_mapper_representation** | [**identity_provider_mapper_representation.IdentityProviderMapperRepresentation**](IdentityProviderMapperRepresentation.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_identity_provider_instances_alias_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_identity_provider_instances_alias_put(realm, alias)

Update the identity provider

### Example

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IdentityProvidersApi(api_client)
    realm = 'realm_example' # str | 
    alias = 'alias_example' # str | 
    identity_provider_representation_identity_provider_representation = openapi_client.IdentityProviderRepresentation() # identity_provider_representation.IdentityProviderRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the identity provider
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_put(realm, alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the identity provider
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_put(realm, alias, identity_provider_representation_identity_provider_representation=identity_provider_representation_identity_provider_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **alias** | **str**|  |
 **identity_provider_representation_identity_provider_representation** | [**identity_provider_representation.IdentityProviderRepresentation**](IdentityProviderRepresentation.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_identity_provider_instances_alias_reload_keys_get**
> bool admin_realms_realm_identity_provider_instances_alias_reload_keys_get(realm, alias)

Reaload keys for the identity provider if the provider supports it, \"true\" is returned if reload was performed, \"false\" if not.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IdentityProvidersApi(api_client)
    realm = 'realm_example' # str | 
    alias = 'alias_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Reaload keys for the identity provider if the provider supports it, \"true\" is returned if reload was performed, \"false\" if not.
        api_response = api_instance.admin_realms_realm_identity_provider_instances_alias_reload_keys_get(realm, alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_alias_reload_keys_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **alias** | **str**|  |

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_identity_provider_instances_get**
> [identity_provider_representation.IdentityProviderRepresentation] admin_realms_realm_identity_provider_instances_get(realm)

List identity providers

### Example

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IdentityProvidersApi(api_client)
    realm = 'realm_example' # str | 
    brief_representation = True # bool | Boolean which defines whether brief representations are returned (default: false) (optional)
first = 56 # int | Pagination offset (optional)
max = 56 # int | Maximum results size (defaults to 100) (optional)
realm_only = True # bool | Boolean which defines if only realm-level IDPs (not associated with orgs) should be returned (default: false) (optional)
search = 'search_example' # str | Filter specific providers by name. Search can be prefix (name*), contains (*name*) or exact (\"name\"). Default prefixed. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List identity providers
        api_response = api_instance.admin_realms_realm_identity_provider_instances_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List identity providers
        api_response = api_instance.admin_realms_realm_identity_provider_instances_get(realm, brief_representation=brief_representation, first=first, max=max, realm_only=realm_only, search=search)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **brief_representation** | **bool**| Boolean which defines whether brief representations are returned (default: false) | [optional]
 **first** | **int**| Pagination offset | [optional]
 **max** | **int**| Maximum results size (defaults to 100) | [optional]
 **realm_only** | **bool**| Boolean which defines if only realm-level IDPs (not associated with orgs) should be returned (default: false) | [optional]
 **search** | **str**| Filter specific providers by name. Search can be prefix (name*), contains (*name*) or exact (\&quot;name\&quot;). Default prefixed. | [optional]

### Return type

[**[identity_provider_representation.IdentityProviderRepresentation]**](IdentityProviderRepresentation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_identity_provider_instances_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_identity_provider_instances_post(realm)

Create a new identity provider

### Example

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IdentityProvidersApi(api_client)
    realm = 'realm_example' # str | 
    identity_provider_representation_identity_provider_representation = openapi_client.IdentityProviderRepresentation() # identity_provider_representation.IdentityProviderRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new identity provider
        api_response = api_instance.admin_realms_realm_identity_provider_instances_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new identity provider
        api_response = api_instance.admin_realms_realm_identity_provider_instances_post(realm, identity_provider_representation_identity_provider_representation=identity_provider_representation_identity_provider_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_instances_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **identity_provider_representation_identity_provider_representation** | [**identity_provider_representation.IdentityProviderRepresentation**](IdentityProviderRepresentation.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_identity_provider_providers_provider_id_get**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_identity_provider_providers_provider_id_get(provider_id, realm)

Get the identity provider factory for that provider id

### Example

```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IdentityProvidersApi(api_client)
    provider_id = 'provider_id_example' # str | The provider id to get the factory
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get the identity provider factory for that provider id
        api_response = api_instance.admin_realms_realm_identity_provider_providers_provider_id_get(provider_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling IdentityProvidersApi->admin_realms_realm_identity_provider_providers_provider_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| The provider id to get the factory |
 **realm** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

