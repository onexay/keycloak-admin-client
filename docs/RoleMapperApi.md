# openapi_client.RoleMapperApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_realm_groups_group_id_role_mappings_get**](RoleMapperApi.md#admin_realms_realm_groups_group_id_role_mappings_get) | **GET** /admin/realms/{realm}/groups/{group-id}/role-mappings | Get role mappings
[**admin_realms_realm_groups_group_id_role_mappings_realm_available_get**](RoleMapperApi.md#admin_realms_realm_groups_group_id_role_mappings_realm_available_get) | **GET** /admin/realms/{realm}/groups/{group-id}/role-mappings/realm/available | Get realm-level roles that can be mapped
[**admin_realms_realm_groups_group_id_role_mappings_realm_composite_get**](RoleMapperApi.md#admin_realms_realm_groups_group_id_role_mappings_realm_composite_get) | **GET** /admin/realms/{realm}/groups/{group-id}/role-mappings/realm/composite | Get effective realm-level role mappings This will recurse all composite roles to get the result.
[**admin_realms_realm_groups_group_id_role_mappings_realm_delete**](RoleMapperApi.md#admin_realms_realm_groups_group_id_role_mappings_realm_delete) | **DELETE** /admin/realms/{realm}/groups/{group-id}/role-mappings/realm | Delete realm-level role mappings
[**admin_realms_realm_groups_group_id_role_mappings_realm_get**](RoleMapperApi.md#admin_realms_realm_groups_group_id_role_mappings_realm_get) | **GET** /admin/realms/{realm}/groups/{group-id}/role-mappings/realm | Get realm-level role mappings
[**admin_realms_realm_groups_group_id_role_mappings_realm_post**](RoleMapperApi.md#admin_realms_realm_groups_group_id_role_mappings_realm_post) | **POST** /admin/realms/{realm}/groups/{group-id}/role-mappings/realm | Add realm-level role mappings to the user
[**admin_realms_realm_users_user_id_role_mappings_get**](RoleMapperApi.md#admin_realms_realm_users_user_id_role_mappings_get) | **GET** /admin/realms/{realm}/users/{user-id}/role-mappings | Get role mappings
[**admin_realms_realm_users_user_id_role_mappings_realm_available_get**](RoleMapperApi.md#admin_realms_realm_users_user_id_role_mappings_realm_available_get) | **GET** /admin/realms/{realm}/users/{user-id}/role-mappings/realm/available | Get realm-level roles that can be mapped
[**admin_realms_realm_users_user_id_role_mappings_realm_composite_get**](RoleMapperApi.md#admin_realms_realm_users_user_id_role_mappings_realm_composite_get) | **GET** /admin/realms/{realm}/users/{user-id}/role-mappings/realm/composite | Get effective realm-level role mappings This will recurse all composite roles to get the result.
[**admin_realms_realm_users_user_id_role_mappings_realm_delete**](RoleMapperApi.md#admin_realms_realm_users_user_id_role_mappings_realm_delete) | **DELETE** /admin/realms/{realm}/users/{user-id}/role-mappings/realm | Delete realm-level role mappings
[**admin_realms_realm_users_user_id_role_mappings_realm_get**](RoleMapperApi.md#admin_realms_realm_users_user_id_role_mappings_realm_get) | **GET** /admin/realms/{realm}/users/{user-id}/role-mappings/realm | Get realm-level role mappings
[**admin_realms_realm_users_user_id_role_mappings_realm_post**](RoleMapperApi.md#admin_realms_realm_users_user_id_role_mappings_realm_post) | **POST** /admin/realms/{realm}/users/{user-id}/role-mappings/realm | Add realm-level role mappings to the user


# **admin_realms_realm_groups_group_id_role_mappings_get**
> mappings_representation.MappingsRepresentation admin_realms_realm_groups_group_id_role_mappings_get(realm, group_id)

Get role mappings

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
    api_instance = openapi_client.RoleMapperApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get role mappings
        api_response = api_instance.admin_realms_realm_groups_group_id_role_mappings_get(realm, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_groups_group_id_role_mappings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |

### Return type

[**mappings_representation.MappingsRepresentation**](MappingsRepresentation.md)

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

# **admin_realms_realm_groups_group_id_role_mappings_realm_available_get**
> [role_representation.RoleRepresentation] admin_realms_realm_groups_group_id_role_mappings_realm_available_get(realm, group_id)

Get realm-level roles that can be mapped

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
    api_instance = openapi_client.RoleMapperApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles that can be mapped
        api_response = api_instance.admin_realms_realm_groups_group_id_role_mappings_realm_available_get(realm, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_groups_group_id_role_mappings_realm_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |

### Return type

[**[role_representation.RoleRepresentation]**](RoleRepresentation.md)

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

# **admin_realms_realm_groups_group_id_role_mappings_realm_composite_get**
> [role_representation.RoleRepresentation] admin_realms_realm_groups_group_id_role_mappings_realm_composite_get(realm, group_id)

Get effective realm-level role mappings This will recurse all composite roles to get the result.

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
    api_instance = openapi_client.RoleMapperApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    brief_representation = True # bool | if false, return roles with their attributes (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Get effective realm-level role mappings This will recurse all composite roles to get the result.
        api_response = api_instance.admin_realms_realm_groups_group_id_role_mappings_realm_composite_get(realm, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_groups_group_id_role_mappings_realm_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective realm-level role mappings This will recurse all composite roles to get the result.
        api_response = api_instance.admin_realms_realm_groups_group_id_role_mappings_realm_composite_get(realm, group_id, brief_representation=brief_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_groups_group_id_role_mappings_realm_composite_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |
 **brief_representation** | **bool**| if false, return roles with their attributes | [optional] if omitted the server will use the default value of True

### Return type

[**[role_representation.RoleRepresentation]**](RoleRepresentation.md)

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

# **admin_realms_realm_groups_group_id_role_mappings_realm_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_groups_group_id_role_mappings_realm_delete(realm, group_id)

Delete realm-level role mappings

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
    api_instance = openapi_client.RoleMapperApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete realm-level role mappings
        api_response = api_instance.admin_realms_realm_groups_group_id_role_mappings_realm_delete(realm, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_groups_group_id_role_mappings_realm_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete realm-level role mappings
        api_response = api_instance.admin_realms_realm_groups_group_id_role_mappings_realm_delete(realm, group_id, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_groups_group_id_role_mappings_realm_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |
 **role_representation_role_representation** | [**[role_representation.RoleRepresentation]**](RoleRepresentation.md)|  | [optional]

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

# **admin_realms_realm_groups_group_id_role_mappings_realm_get**
> [role_representation.RoleRepresentation] admin_realms_realm_groups_group_id_role_mappings_realm_get(realm, group_id)

Get realm-level role mappings

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
    api_instance = openapi_client.RoleMapperApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get realm-level role mappings
        api_response = api_instance.admin_realms_realm_groups_group_id_role_mappings_realm_get(realm, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_groups_group_id_role_mappings_realm_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |

### Return type

[**[role_representation.RoleRepresentation]**](RoleRepresentation.md)

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

# **admin_realms_realm_groups_group_id_role_mappings_realm_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_groups_group_id_role_mappings_realm_post(realm, group_id)

Add realm-level role mappings to the user

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
    api_instance = openapi_client.RoleMapperApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add realm-level role mappings to the user
        api_response = api_instance.admin_realms_realm_groups_group_id_role_mappings_realm_post(realm, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_groups_group_id_role_mappings_realm_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add realm-level role mappings to the user
        api_response = api_instance.admin_realms_realm_groups_group_id_role_mappings_realm_post(realm, group_id, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_groups_group_id_role_mappings_realm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |
 **role_representation_role_representation** | [**[role_representation.RoleRepresentation]**](RoleRepresentation.md)|  | [optional]

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

# **admin_realms_realm_users_user_id_role_mappings_get**
> mappings_representation.MappingsRepresentation admin_realms_realm_users_user_id_role_mappings_get(realm, user_id)

Get role mappings

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
    api_instance = openapi_client.RoleMapperApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get role mappings
        api_response = api_instance.admin_realms_realm_users_user_id_role_mappings_get(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_users_user_id_role_mappings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |

### Return type

[**mappings_representation.MappingsRepresentation**](MappingsRepresentation.md)

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

# **admin_realms_realm_users_user_id_role_mappings_realm_available_get**
> [role_representation.RoleRepresentation] admin_realms_realm_users_user_id_role_mappings_realm_available_get(realm, user_id)

Get realm-level roles that can be mapped

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
    api_instance = openapi_client.RoleMapperApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles that can be mapped
        api_response = api_instance.admin_realms_realm_users_user_id_role_mappings_realm_available_get(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_users_user_id_role_mappings_realm_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |

### Return type

[**[role_representation.RoleRepresentation]**](RoleRepresentation.md)

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

# **admin_realms_realm_users_user_id_role_mappings_realm_composite_get**
> [role_representation.RoleRepresentation] admin_realms_realm_users_user_id_role_mappings_realm_composite_get(realm, user_id)

Get effective realm-level role mappings This will recurse all composite roles to get the result.

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
    api_instance = openapi_client.RoleMapperApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    brief_representation = True # bool | if false, return roles with their attributes (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Get effective realm-level role mappings This will recurse all composite roles to get the result.
        api_response = api_instance.admin_realms_realm_users_user_id_role_mappings_realm_composite_get(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_users_user_id_role_mappings_realm_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective realm-level role mappings This will recurse all composite roles to get the result.
        api_response = api_instance.admin_realms_realm_users_user_id_role_mappings_realm_composite_get(realm, user_id, brief_representation=brief_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_users_user_id_role_mappings_realm_composite_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |
 **brief_representation** | **bool**| if false, return roles with their attributes | [optional] if omitted the server will use the default value of True

### Return type

[**[role_representation.RoleRepresentation]**](RoleRepresentation.md)

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

# **admin_realms_realm_users_user_id_role_mappings_realm_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_role_mappings_realm_delete(realm, user_id)

Delete realm-level role mappings

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
    api_instance = openapi_client.RoleMapperApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete realm-level role mappings
        api_response = api_instance.admin_realms_realm_users_user_id_role_mappings_realm_delete(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_users_user_id_role_mappings_realm_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete realm-level role mappings
        api_response = api_instance.admin_realms_realm_users_user_id_role_mappings_realm_delete(realm, user_id, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_users_user_id_role_mappings_realm_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |
 **role_representation_role_representation** | [**[role_representation.RoleRepresentation]**](RoleRepresentation.md)|  | [optional]

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

# **admin_realms_realm_users_user_id_role_mappings_realm_get**
> [role_representation.RoleRepresentation] admin_realms_realm_users_user_id_role_mappings_realm_get(realm, user_id)

Get realm-level role mappings

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
    api_instance = openapi_client.RoleMapperApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get realm-level role mappings
        api_response = api_instance.admin_realms_realm_users_user_id_role_mappings_realm_get(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_users_user_id_role_mappings_realm_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |

### Return type

[**[role_representation.RoleRepresentation]**](RoleRepresentation.md)

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

# **admin_realms_realm_users_user_id_role_mappings_realm_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_role_mappings_realm_post(realm, user_id)

Add realm-level role mappings to the user

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
    api_instance = openapi_client.RoleMapperApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add realm-level role mappings to the user
        api_response = api_instance.admin_realms_realm_users_user_id_role_mappings_realm_post(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_users_user_id_role_mappings_realm_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add realm-level role mappings to the user
        api_response = api_instance.admin_realms_realm_users_user_id_role_mappings_realm_post(realm, user_id, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RoleMapperApi->admin_realms_realm_users_user_id_role_mappings_realm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |
 **role_representation_role_representation** | [**[role_representation.RoleRepresentation]**](RoleRepresentation.md)|  | [optional]

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

