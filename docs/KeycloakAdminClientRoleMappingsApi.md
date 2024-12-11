# openapi_client.KeycloakAdminClientRoleMappingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_realm_groups_group_id_role_mappings_clients_client_id_available_get**](KeycloakAdminClientRoleMappingsApi.md#admin_realms_realm_groups_group_id_role_mappings_clients_client_id_available_get) | **GET** /admin/realms/{realm}/groups/{group-id}/role-mappings/clients/{client-id}/available | Get available client-level roles that can be mapped to the user or group
[**admin_realms_realm_groups_group_id_role_mappings_clients_client_id_composite_get**](KeycloakAdminClientRoleMappingsApi.md#admin_realms_realm_groups_group_id_role_mappings_clients_client_id_composite_get) | **GET** /admin/realms/{realm}/groups/{group-id}/role-mappings/clients/{client-id}/composite | Get effective client-level role mappings This recurses any composite roles
[**admin_realms_realm_groups_group_id_role_mappings_clients_client_id_delete**](KeycloakAdminClientRoleMappingsApi.md#admin_realms_realm_groups_group_id_role_mappings_clients_client_id_delete) | **DELETE** /admin/realms/{realm}/groups/{group-id}/role-mappings/clients/{client-id} | Delete client-level roles from user or group role mapping
[**admin_realms_realm_groups_group_id_role_mappings_clients_client_id_get**](KeycloakAdminClientRoleMappingsApi.md#admin_realms_realm_groups_group_id_role_mappings_clients_client_id_get) | **GET** /admin/realms/{realm}/groups/{group-id}/role-mappings/clients/{client-id} | Get client-level role mappings for the user or group, and the app
[**admin_realms_realm_groups_group_id_role_mappings_clients_client_id_post**](KeycloakAdminClientRoleMappingsApi.md#admin_realms_realm_groups_group_id_role_mappings_clients_client_id_post) | **POST** /admin/realms/{realm}/groups/{group-id}/role-mappings/clients/{client-id} | Add client-level roles to the user or group role mapping
[**admin_realms_realm_users_user_id_role_mappings_clients_client_id_available_get**](KeycloakAdminClientRoleMappingsApi.md#admin_realms_realm_users_user_id_role_mappings_clients_client_id_available_get) | **GET** /admin/realms/{realm}/users/{user-id}/role-mappings/clients/{client-id}/available | Get available client-level roles that can be mapped to the user or group
[**admin_realms_realm_users_user_id_role_mappings_clients_client_id_composite_get**](KeycloakAdminClientRoleMappingsApi.md#admin_realms_realm_users_user_id_role_mappings_clients_client_id_composite_get) | **GET** /admin/realms/{realm}/users/{user-id}/role-mappings/clients/{client-id}/composite | Get effective client-level role mappings This recurses any composite roles
[**admin_realms_realm_users_user_id_role_mappings_clients_client_id_delete**](KeycloakAdminClientRoleMappingsApi.md#admin_realms_realm_users_user_id_role_mappings_clients_client_id_delete) | **DELETE** /admin/realms/{realm}/users/{user-id}/role-mappings/clients/{client-id} | Delete client-level roles from user or group role mapping
[**admin_realms_realm_users_user_id_role_mappings_clients_client_id_get**](KeycloakAdminClientRoleMappingsApi.md#admin_realms_realm_users_user_id_role_mappings_clients_client_id_get) | **GET** /admin/realms/{realm}/users/{user-id}/role-mappings/clients/{client-id} | Get client-level role mappings for the user or group, and the app
[**admin_realms_realm_users_user_id_role_mappings_clients_client_id_post**](KeycloakAdminClientRoleMappingsApi.md#admin_realms_realm_users_user_id_role_mappings_clients_client_id_post) | **POST** /admin/realms/{realm}/users/{user-id}/role-mappings/clients/{client-id} | Add client-level roles to the user or group role mapping


# **admin_realms_realm_groups_group_id_role_mappings_clients_client_id_available_get**
> [role_representation.RoleRepresentation] admin_realms_realm_groups_group_id_role_mappings_clients_client_id_available_get(realm, group_id, client_id)

Get available client-level roles that can be mapped to the user or group

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
    api_instance = openapi_client.KeycloakAdminClientRoleMappingsApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    client_id = 'client_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get available client-level roles that can be mapped to the user or group
        api_response = api_instance.admin_realms_realm_groups_group_id_role_mappings_clients_client_id_available_get(realm, group_id, client_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientRoleMappingsApi->admin_realms_realm_groups_group_id_role_mappings_clients_client_id_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |
 **client_id** | **str**|  |

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

# **admin_realms_realm_groups_group_id_role_mappings_clients_client_id_composite_get**
> [role_representation.RoleRepresentation] admin_realms_realm_groups_group_id_role_mappings_clients_client_id_composite_get(realm, group_id, client_id)

Get effective client-level role mappings This recurses any composite roles

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
    api_instance = openapi_client.KeycloakAdminClientRoleMappingsApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    client_id = 'client_id_example' # str | 
    brief_representation = True # bool | if false, return roles with their attributes (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Get effective client-level role mappings This recurses any composite roles
        api_response = api_instance.admin_realms_realm_groups_group_id_role_mappings_clients_client_id_composite_get(realm, group_id, client_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientRoleMappingsApi->admin_realms_realm_groups_group_id_role_mappings_clients_client_id_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective client-level role mappings This recurses any composite roles
        api_response = api_instance.admin_realms_realm_groups_group_id_role_mappings_clients_client_id_composite_get(realm, group_id, client_id, brief_representation=brief_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientRoleMappingsApi->admin_realms_realm_groups_group_id_role_mappings_clients_client_id_composite_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |
 **client_id** | **str**|  |
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

# **admin_realms_realm_groups_group_id_role_mappings_clients_client_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_groups_group_id_role_mappings_clients_client_id_delete(realm, group_id, client_id)

Delete client-level roles from user or group role mapping

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
    api_instance = openapi_client.KeycloakAdminClientRoleMappingsApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    client_id = 'client_id_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete client-level roles from user or group role mapping
        api_response = api_instance.admin_realms_realm_groups_group_id_role_mappings_clients_client_id_delete(realm, group_id, client_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientRoleMappingsApi->admin_realms_realm_groups_group_id_role_mappings_clients_client_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete client-level roles from user or group role mapping
        api_response = api_instance.admin_realms_realm_groups_group_id_role_mappings_clients_client_id_delete(realm, group_id, client_id, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientRoleMappingsApi->admin_realms_realm_groups_group_id_role_mappings_clients_client_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |
 **client_id** | **str**|  |
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

# **admin_realms_realm_groups_group_id_role_mappings_clients_client_id_get**
> [role_representation.RoleRepresentation] admin_realms_realm_groups_group_id_role_mappings_clients_client_id_get(realm, group_id, client_id)

Get client-level role mappings for the user or group, and the app

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
    api_instance = openapi_client.KeycloakAdminClientRoleMappingsApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    client_id = 'client_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get client-level role mappings for the user or group, and the app
        api_response = api_instance.admin_realms_realm_groups_group_id_role_mappings_clients_client_id_get(realm, group_id, client_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientRoleMappingsApi->admin_realms_realm_groups_group_id_role_mappings_clients_client_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |
 **client_id** | **str**|  |

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

# **admin_realms_realm_groups_group_id_role_mappings_clients_client_id_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_groups_group_id_role_mappings_clients_client_id_post(realm, group_id, client_id)

Add client-level roles to the user or group role mapping

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
    api_instance = openapi_client.KeycloakAdminClientRoleMappingsApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    client_id = 'client_id_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add client-level roles to the user or group role mapping
        api_response = api_instance.admin_realms_realm_groups_group_id_role_mappings_clients_client_id_post(realm, group_id, client_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientRoleMappingsApi->admin_realms_realm_groups_group_id_role_mappings_clients_client_id_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add client-level roles to the user or group role mapping
        api_response = api_instance.admin_realms_realm_groups_group_id_role_mappings_clients_client_id_post(realm, group_id, client_id, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientRoleMappingsApi->admin_realms_realm_groups_group_id_role_mappings_clients_client_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |
 **client_id** | **str**|  |
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

# **admin_realms_realm_users_user_id_role_mappings_clients_client_id_available_get**
> [role_representation.RoleRepresentation] admin_realms_realm_users_user_id_role_mappings_clients_client_id_available_get(realm, user_id, client_id)

Get available client-level roles that can be mapped to the user or group

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
    api_instance = openapi_client.KeycloakAdminClientRoleMappingsApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    client_id = 'client_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get available client-level roles that can be mapped to the user or group
        api_response = api_instance.admin_realms_realm_users_user_id_role_mappings_clients_client_id_available_get(realm, user_id, client_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientRoleMappingsApi->admin_realms_realm_users_user_id_role_mappings_clients_client_id_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |
 **client_id** | **str**|  |

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

# **admin_realms_realm_users_user_id_role_mappings_clients_client_id_composite_get**
> [role_representation.RoleRepresentation] admin_realms_realm_users_user_id_role_mappings_clients_client_id_composite_get(realm, user_id, client_id)

Get effective client-level role mappings This recurses any composite roles

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
    api_instance = openapi_client.KeycloakAdminClientRoleMappingsApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    client_id = 'client_id_example' # str | 
    brief_representation = True # bool | if false, return roles with their attributes (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Get effective client-level role mappings This recurses any composite roles
        api_response = api_instance.admin_realms_realm_users_user_id_role_mappings_clients_client_id_composite_get(realm, user_id, client_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientRoleMappingsApi->admin_realms_realm_users_user_id_role_mappings_clients_client_id_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective client-level role mappings This recurses any composite roles
        api_response = api_instance.admin_realms_realm_users_user_id_role_mappings_clients_client_id_composite_get(realm, user_id, client_id, brief_representation=brief_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientRoleMappingsApi->admin_realms_realm_users_user_id_role_mappings_clients_client_id_composite_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |
 **client_id** | **str**|  |
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

# **admin_realms_realm_users_user_id_role_mappings_clients_client_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_role_mappings_clients_client_id_delete(realm, user_id, client_id)

Delete client-level roles from user or group role mapping

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
    api_instance = openapi_client.KeycloakAdminClientRoleMappingsApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    client_id = 'client_id_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete client-level roles from user or group role mapping
        api_response = api_instance.admin_realms_realm_users_user_id_role_mappings_clients_client_id_delete(realm, user_id, client_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientRoleMappingsApi->admin_realms_realm_users_user_id_role_mappings_clients_client_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete client-level roles from user or group role mapping
        api_response = api_instance.admin_realms_realm_users_user_id_role_mappings_clients_client_id_delete(realm, user_id, client_id, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientRoleMappingsApi->admin_realms_realm_users_user_id_role_mappings_clients_client_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |
 **client_id** | **str**|  |
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

# **admin_realms_realm_users_user_id_role_mappings_clients_client_id_get**
> [role_representation.RoleRepresentation] admin_realms_realm_users_user_id_role_mappings_clients_client_id_get(realm, user_id, client_id)

Get client-level role mappings for the user or group, and the app

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
    api_instance = openapi_client.KeycloakAdminClientRoleMappingsApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    client_id = 'client_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get client-level role mappings for the user or group, and the app
        api_response = api_instance.admin_realms_realm_users_user_id_role_mappings_clients_client_id_get(realm, user_id, client_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientRoleMappingsApi->admin_realms_realm_users_user_id_role_mappings_clients_client_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |
 **client_id** | **str**|  |

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

# **admin_realms_realm_users_user_id_role_mappings_clients_client_id_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_role_mappings_clients_client_id_post(realm, user_id, client_id)

Add client-level roles to the user or group role mapping

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
    api_instance = openapi_client.KeycloakAdminClientRoleMappingsApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    client_id = 'client_id_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add client-level roles to the user or group role mapping
        api_response = api_instance.admin_realms_realm_users_user_id_role_mappings_clients_client_id_post(realm, user_id, client_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientRoleMappingsApi->admin_realms_realm_users_user_id_role_mappings_clients_client_id_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add client-level roles to the user or group role mapping
        api_response = api_instance.admin_realms_realm_users_user_id_role_mappings_clients_client_id_post(realm, user_id, client_id, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientRoleMappingsApi->admin_realms_realm_users_user_id_role_mappings_clients_client_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |
 **client_id** | **str**|  |
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

