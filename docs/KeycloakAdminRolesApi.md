# openapi_client.KeycloakAdminRolesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_realm_clients_client_uuid_roles_get**](KeycloakAdminRolesApi.md#admin_realms_realm_clients_client_uuid_roles_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/roles | Get all roles for the realm or client
[**admin_realms_realm_clients_client_uuid_roles_post**](KeycloakAdminRolesApi.md#admin_realms_realm_clients_client_uuid_roles_post) | **POST** /admin/realms/{realm}/clients/{client-uuid}/roles | Create a new role for the realm or client
[**admin_realms_realm_clients_client_uuid_roles_role_name_composites_clients_client_uuid_get**](KeycloakAdminRolesApi.md#admin_realms_realm_clients_client_uuid_roles_role_name_composites_clients_client_uuid_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/roles/{role-name}/composites/clients/{client-uuid} | Get client-level roles for the client that are in the role&#39;s composite
[**admin_realms_realm_clients_client_uuid_roles_role_name_composites_delete**](KeycloakAdminRolesApi.md#admin_realms_realm_clients_client_uuid_roles_role_name_composites_delete) | **DELETE** /admin/realms/{realm}/clients/{client-uuid}/roles/{role-name}/composites | Remove roles from the role&#39;s composite
[**admin_realms_realm_clients_client_uuid_roles_role_name_composites_get**](KeycloakAdminRolesApi.md#admin_realms_realm_clients_client_uuid_roles_role_name_composites_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/roles/{role-name}/composites | Get composites of the role
[**admin_realms_realm_clients_client_uuid_roles_role_name_composites_post**](KeycloakAdminRolesApi.md#admin_realms_realm_clients_client_uuid_roles_role_name_composites_post) | **POST** /admin/realms/{realm}/clients/{client-uuid}/roles/{role-name}/composites | Add a composite to the role
[**admin_realms_realm_clients_client_uuid_roles_role_name_composites_realm_get**](KeycloakAdminRolesApi.md#admin_realms_realm_clients_client_uuid_roles_role_name_composites_realm_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/roles/{role-name}/composites/realm | Get realm-level roles of the role&#39;s composite
[**admin_realms_realm_clients_client_uuid_roles_role_name_delete**](KeycloakAdminRolesApi.md#admin_realms_realm_clients_client_uuid_roles_role_name_delete) | **DELETE** /admin/realms/{realm}/clients/{client-uuid}/roles/{role-name} | Delete a role by name
[**admin_realms_realm_clients_client_uuid_roles_role_name_get**](KeycloakAdminRolesApi.md#admin_realms_realm_clients_client_uuid_roles_role_name_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/roles/{role-name} | Get a role by name
[**admin_realms_realm_clients_client_uuid_roles_role_name_groups_get**](KeycloakAdminRolesApi.md#admin_realms_realm_clients_client_uuid_roles_role_name_groups_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/roles/{role-name}/groups | Returns a stream of groups that have the specified role name
[**admin_realms_realm_clients_client_uuid_roles_role_name_management_permissions_get**](KeycloakAdminRolesApi.md#admin_realms_realm_clients_client_uuid_roles_role_name_management_permissions_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/roles/{role-name}/management/permissions | Return object stating whether role Authorization permissions have been initialized or not and a reference
[**admin_realms_realm_clients_client_uuid_roles_role_name_management_permissions_put**](KeycloakAdminRolesApi.md#admin_realms_realm_clients_client_uuid_roles_role_name_management_permissions_put) | **PUT** /admin/realms/{realm}/clients/{client-uuid}/roles/{role-name}/management/permissions | Return object stating whether role Authorization permissions have been initialized or not and a reference
[**admin_realms_realm_clients_client_uuid_roles_role_name_put**](KeycloakAdminRolesApi.md#admin_realms_realm_clients_client_uuid_roles_role_name_put) | **PUT** /admin/realms/{realm}/clients/{client-uuid}/roles/{role-name} | Update a role by name
[**admin_realms_realm_clients_client_uuid_roles_role_name_users_get**](KeycloakAdminRolesApi.md#admin_realms_realm_clients_client_uuid_roles_role_name_users_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/roles/{role-name}/users | Returns a stream of users that have the specified role name.
[**admin_realms_realm_roles_get**](KeycloakAdminRolesApi.md#admin_realms_realm_roles_get) | **GET** /admin/realms/{realm}/roles | Get all roles for the realm or client
[**admin_realms_realm_roles_post**](KeycloakAdminRolesApi.md#admin_realms_realm_roles_post) | **POST** /admin/realms/{realm}/roles | Create a new role for the realm or client
[**admin_realms_realm_roles_role_name_composites_clients_client_uuid_get**](KeycloakAdminRolesApi.md#admin_realms_realm_roles_role_name_composites_clients_client_uuid_get) | **GET** /admin/realms/{realm}/roles/{role-name}/composites/clients/{client-uuid} | Get client-level roles for the client that are in the role&#39;s composite
[**admin_realms_realm_roles_role_name_composites_delete**](KeycloakAdminRolesApi.md#admin_realms_realm_roles_role_name_composites_delete) | **DELETE** /admin/realms/{realm}/roles/{role-name}/composites | Remove roles from the role&#39;s composite
[**admin_realms_realm_roles_role_name_composites_get**](KeycloakAdminRolesApi.md#admin_realms_realm_roles_role_name_composites_get) | **GET** /admin/realms/{realm}/roles/{role-name}/composites | Get composites of the role
[**admin_realms_realm_roles_role_name_composites_post**](KeycloakAdminRolesApi.md#admin_realms_realm_roles_role_name_composites_post) | **POST** /admin/realms/{realm}/roles/{role-name}/composites | Add a composite to the role
[**admin_realms_realm_roles_role_name_composites_realm_get**](KeycloakAdminRolesApi.md#admin_realms_realm_roles_role_name_composites_realm_get) | **GET** /admin/realms/{realm}/roles/{role-name}/composites/realm | Get realm-level roles of the role&#39;s composite
[**admin_realms_realm_roles_role_name_delete**](KeycloakAdminRolesApi.md#admin_realms_realm_roles_role_name_delete) | **DELETE** /admin/realms/{realm}/roles/{role-name} | Delete a role by name
[**admin_realms_realm_roles_role_name_get**](KeycloakAdminRolesApi.md#admin_realms_realm_roles_role_name_get) | **GET** /admin/realms/{realm}/roles/{role-name} | Get a role by name
[**admin_realms_realm_roles_role_name_groups_get**](KeycloakAdminRolesApi.md#admin_realms_realm_roles_role_name_groups_get) | **GET** /admin/realms/{realm}/roles/{role-name}/groups | Returns a stream of groups that have the specified role name
[**admin_realms_realm_roles_role_name_management_permissions_get**](KeycloakAdminRolesApi.md#admin_realms_realm_roles_role_name_management_permissions_get) | **GET** /admin/realms/{realm}/roles/{role-name}/management/permissions | Return object stating whether role Authorization permissions have been initialized or not and a reference
[**admin_realms_realm_roles_role_name_management_permissions_put**](KeycloakAdminRolesApi.md#admin_realms_realm_roles_role_name_management_permissions_put) | **PUT** /admin/realms/{realm}/roles/{role-name}/management/permissions | Return object stating whether role Authorization permissions have been initialized or not and a reference
[**admin_realms_realm_roles_role_name_put**](KeycloakAdminRolesApi.md#admin_realms_realm_roles_role_name_put) | **PUT** /admin/realms/{realm}/roles/{role-name} | Update a role by name
[**admin_realms_realm_roles_role_name_users_get**](KeycloakAdminRolesApi.md#admin_realms_realm_roles_role_name_users_get) | **GET** /admin/realms/{realm}/roles/{role-name}/users | Returns a stream of users that have the specified role name.


# **admin_realms_realm_clients_client_uuid_roles_get**
> [role_representation.RoleRepresentation] admin_realms_realm_clients_client_uuid_roles_get(realm, client_uuid)

Get all roles for the realm or client

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    brief_representation = True # bool |  (optional) if omitted the server will use the default value of True
first = 56 # int |  (optional)
max = 56 # int |  (optional)
search = '' # str |  (optional) if omitted the server will use the default value of ''

    # example passing only required values which don't have defaults set
    try:
        # Get all roles for the realm or client
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all roles for the realm or client
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_get(realm, client_uuid, brief_representation=brief_representation, first=first, max=max, search=search)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **brief_representation** | **bool**|  | [optional] if omitted the server will use the default value of True
 **first** | **int**|  | [optional]
 **max** | **int**|  | [optional]
 **search** | **str**|  | [optional] if omitted the server will use the default value of ''

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

# **admin_realms_realm_clients_client_uuid_roles_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_roles_post(realm, client_uuid)

Create a new role for the realm or client

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    role_representation_role_representation = openapi_client.RoleRepresentation() # role_representation.RoleRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new role for the realm or client
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_post(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new role for the realm or client
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_post(realm, client_uuid, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **role_representation_role_representation** | [**role_representation.RoleRepresentation**](RoleRepresentation.md)|  | [optional]

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

# **admin_realms_realm_clients_client_uuid_roles_role_name_composites_clients_client_uuid_get**
> [role_representation.RoleRepresentation] admin_realms_realm_clients_client_uuid_roles_role_name_composites_clients_client_uuid_get(client_uuid, role_name, realm)

Get client-level roles for the client that are in the role's composite

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    client_uuid = 'client_uuid_example' # str | 
    role_name = 'role_name_example' # str | role's name (not id!)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get client-level roles for the client that are in the role's composite
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_composites_clients_client_uuid_get(client_uuid, role_name, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_composites_clients_client_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_uuid** | **str**|  |
 **role_name** | **str**| role&#39;s name (not id!) |
 **realm** | **str**|  |

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

# **admin_realms_realm_clients_client_uuid_roles_role_name_composites_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_roles_role_name_composites_delete(role_name, realm, client_uuid)

Remove roles from the role's composite

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | role's name (not id!)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove roles from the role's composite
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_composites_delete(role_name, realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_composites_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove roles from the role's composite
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_composites_delete(role_name, realm, client_uuid, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_composites_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| role&#39;s name (not id!) |
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
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

# **admin_realms_realm_clients_client_uuid_roles_role_name_composites_get**
> [role_representation.RoleRepresentation] admin_realms_realm_clients_client_uuid_roles_role_name_composites_get(role_name, realm, client_uuid)

Get composites of the role

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | role's name (not id!)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get composites of the role
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_composites_get(role_name, realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_composites_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| role&#39;s name (not id!) |
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

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

# **admin_realms_realm_clients_client_uuid_roles_role_name_composites_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_roles_role_name_composites_post(role_name, realm, client_uuid)

Add a composite to the role

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | role's name (not id!)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a composite to the role
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_composites_post(role_name, realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_composites_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a composite to the role
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_composites_post(role_name, realm, client_uuid, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_composites_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| role&#39;s name (not id!) |
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
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

# **admin_realms_realm_clients_client_uuid_roles_role_name_composites_realm_get**
> [role_representation.RoleRepresentation] admin_realms_realm_clients_client_uuid_roles_role_name_composites_realm_get(role_name, realm, client_uuid)

Get realm-level roles of the role's composite

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | role's name (not id!)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles of the role's composite
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_composites_realm_get(role_name, realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_composites_realm_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| role&#39;s name (not id!) |
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

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

# **admin_realms_realm_clients_client_uuid_roles_role_name_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_roles_role_name_delete(role_name, realm, client_uuid)

Delete a role by name

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | role's name (not id!)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete a role by name
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_delete(role_name, realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| role&#39;s name (not id!) |
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

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

# **admin_realms_realm_clients_client_uuid_roles_role_name_get**
> role_representation.RoleRepresentation admin_realms_realm_clients_client_uuid_roles_role_name_get(role_name, realm, client_uuid)

Get a role by name

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | role's name (not id!)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get a role by name
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_get(role_name, realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| role&#39;s name (not id!) |
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

### Return type

[**role_representation.RoleRepresentation**](RoleRepresentation.md)

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

# **admin_realms_realm_clients_client_uuid_roles_role_name_groups_get**
> [group_representation.GroupRepresentation] admin_realms_realm_clients_client_uuid_roles_role_name_groups_get(role_name, realm, client_uuid)

Returns a stream of groups that have the specified role name

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | the role name.
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    brief_representation = True # bool | if false, return a full representation of the {@code GroupRepresentation} objects. (optional) if omitted the server will use the default value of True
first = 56 # int | first result to return. Ignored if negative or {@code null}. (optional)
max = 56 # int | maximum number of results to return. Ignored if negative or {@code null}. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a stream of groups that have the specified role name
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_groups_get(role_name, realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_groups_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a stream of groups that have the specified role name
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_groups_get(role_name, realm, client_uuid, brief_representation=brief_representation, first=first, max=max)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| the role name. |
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **brief_representation** | **bool**| if false, return a full representation of the {@code GroupRepresentation} objects. | [optional] if omitted the server will use the default value of True
 **first** | **int**| first result to return. Ignored if negative or {@code null}. | [optional]
 **max** | **int**| maximum number of results to return. Ignored if negative or {@code null}. | [optional]

### Return type

[**[group_representation.GroupRepresentation]**](GroupRepresentation.md)

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

# **admin_realms_realm_clients_client_uuid_roles_role_name_management_permissions_get**
> management_permission_reference.ManagementPermissionReference admin_realms_realm_clients_client_uuid_roles_role_name_management_permissions_get(role_name, realm, client_uuid)

Return object stating whether role Authorization permissions have been initialized or not and a reference

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | 
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether role Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_management_permissions_get(role_name, realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_management_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**|  |
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

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

# **admin_realms_realm_clients_client_uuid_roles_role_name_management_permissions_put**
> management_permission_reference.ManagementPermissionReference admin_realms_realm_clients_client_uuid_roles_role_name_management_permissions_put(role_name, realm, client_uuid)

Return object stating whether role Authorization permissions have been initialized or not and a reference

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | 
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    management_permission_reference_management_permission_reference = openapi_client.ManagementPermissionReference() # management_permission_reference.ManagementPermissionReference |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether role Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_management_permissions_put(role_name, realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_management_permissions_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return object stating whether role Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_management_permissions_put(role_name, realm, client_uuid, management_permission_reference_management_permission_reference=management_permission_reference_management_permission_reference)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_management_permissions_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**|  |
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
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

# **admin_realms_realm_clients_client_uuid_roles_role_name_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_roles_role_name_put(role_name, realm, client_uuid)

Update a role by name

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | role's name (not id!)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    role_representation_role_representation = openapi_client.RoleRepresentation() # role_representation.RoleRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a role by name
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_put(role_name, realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a role by name
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_put(role_name, realm, client_uuid, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| role&#39;s name (not id!) |
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **role_representation_role_representation** | [**role_representation.RoleRepresentation**](RoleRepresentation.md)|  | [optional]

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

# **admin_realms_realm_clients_client_uuid_roles_role_name_users_get**
> [user_representation.UserRepresentation] admin_realms_realm_clients_client_uuid_roles_role_name_users_get(role_name, realm, client_uuid)

Returns a stream of users that have the specified role name.

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | the role name.
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    brief_representation = True # bool | Boolean which defines whether brief representations are returned (default: false) (optional)
first = 56 # int | first result to return. Ignored if negative or {@code null}. (optional)
max = 56 # int | maximum number of results to return. Ignored if negative or {@code null}. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a stream of users that have the specified role name.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_users_get(role_name, realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_users_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a stream of users that have the specified role name.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_roles_role_name_users_get(role_name, realm, client_uuid, brief_representation=brief_representation, first=first, max=max)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_clients_client_uuid_roles_role_name_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| the role name. |
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **brief_representation** | **bool**| Boolean which defines whether brief representations are returned (default: false) | [optional]
 **first** | **int**| first result to return. Ignored if negative or {@code null}. | [optional]
 **max** | **int**| maximum number of results to return. Ignored if negative or {@code null}. | [optional]

### Return type

[**[user_representation.UserRepresentation]**](UserRepresentation.md)

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

# **admin_realms_realm_roles_get**
> [role_representation.RoleRepresentation] admin_realms_realm_roles_get(realm)

Get all roles for the realm or client

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    realm = 'realm_example' # str | 
    brief_representation = True # bool |  (optional) if omitted the server will use the default value of True
first = 56 # int |  (optional)
max = 56 # int |  (optional)
search = '' # str |  (optional) if omitted the server will use the default value of ''

    # example passing only required values which don't have defaults set
    try:
        # Get all roles for the realm or client
        api_response = api_instance.admin_realms_realm_roles_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all roles for the realm or client
        api_response = api_instance.admin_realms_realm_roles_get(realm, brief_representation=brief_representation, first=first, max=max, search=search)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **brief_representation** | **bool**|  | [optional] if omitted the server will use the default value of True
 **first** | **int**|  | [optional]
 **max** | **int**|  | [optional]
 **search** | **str**|  | [optional] if omitted the server will use the default value of ''

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

# **admin_realms_realm_roles_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_roles_post(realm)

Create a new role for the realm or client

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    realm = 'realm_example' # str | 
    role_representation_role_representation = openapi_client.RoleRepresentation() # role_representation.RoleRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new role for the realm or client
        api_response = api_instance.admin_realms_realm_roles_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new role for the realm or client
        api_response = api_instance.admin_realms_realm_roles_post(realm, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **role_representation_role_representation** | [**role_representation.RoleRepresentation**](RoleRepresentation.md)|  | [optional]

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

# **admin_realms_realm_roles_role_name_composites_clients_client_uuid_get**
> [role_representation.RoleRepresentation] admin_realms_realm_roles_role_name_composites_clients_client_uuid_get(client_uuid, role_name, realm)

Get client-level roles for the client that are in the role's composite

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    client_uuid = 'client_uuid_example' # str | 
    role_name = 'role_name_example' # str | role's name (not id!)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get client-level roles for the client that are in the role's composite
        api_response = api_instance.admin_realms_realm_roles_role_name_composites_clients_client_uuid_get(client_uuid, role_name, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_composites_clients_client_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_uuid** | **str**|  |
 **role_name** | **str**| role&#39;s name (not id!) |
 **realm** | **str**|  |

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

# **admin_realms_realm_roles_role_name_composites_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_roles_role_name_composites_delete(role_name, realm)

Remove roles from the role's composite

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | role's name (not id!)
    realm = 'realm_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove roles from the role's composite
        api_response = api_instance.admin_realms_realm_roles_role_name_composites_delete(role_name, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_composites_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove roles from the role's composite
        api_response = api_instance.admin_realms_realm_roles_role_name_composites_delete(role_name, realm, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_composites_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| role&#39;s name (not id!) |
 **realm** | **str**|  |
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

# **admin_realms_realm_roles_role_name_composites_get**
> [role_representation.RoleRepresentation] admin_realms_realm_roles_role_name_composites_get(role_name, realm)

Get composites of the role

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | role's name (not id!)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get composites of the role
        api_response = api_instance.admin_realms_realm_roles_role_name_composites_get(role_name, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_composites_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| role&#39;s name (not id!) |
 **realm** | **str**|  |

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

# **admin_realms_realm_roles_role_name_composites_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_roles_role_name_composites_post(role_name, realm)

Add a composite to the role

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | role's name (not id!)
    realm = 'realm_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a composite to the role
        api_response = api_instance.admin_realms_realm_roles_role_name_composites_post(role_name, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_composites_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a composite to the role
        api_response = api_instance.admin_realms_realm_roles_role_name_composites_post(role_name, realm, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_composites_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| role&#39;s name (not id!) |
 **realm** | **str**|  |
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

# **admin_realms_realm_roles_role_name_composites_realm_get**
> [role_representation.RoleRepresentation] admin_realms_realm_roles_role_name_composites_realm_get(role_name, realm)

Get realm-level roles of the role's composite

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | role's name (not id!)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles of the role's composite
        api_response = api_instance.admin_realms_realm_roles_role_name_composites_realm_get(role_name, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_composites_realm_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| role&#39;s name (not id!) |
 **realm** | **str**|  |

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

# **admin_realms_realm_roles_role_name_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_roles_role_name_delete(role_name, realm)

Delete a role by name

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | role's name (not id!)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete a role by name
        api_response = api_instance.admin_realms_realm_roles_role_name_delete(role_name, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| role&#39;s name (not id!) |
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_roles_role_name_get**
> role_representation.RoleRepresentation admin_realms_realm_roles_role_name_get(role_name, realm)

Get a role by name

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | role's name (not id!)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get a role by name
        api_response = api_instance.admin_realms_realm_roles_role_name_get(role_name, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| role&#39;s name (not id!) |
 **realm** | **str**|  |

### Return type

[**role_representation.RoleRepresentation**](RoleRepresentation.md)

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

# **admin_realms_realm_roles_role_name_groups_get**
> [group_representation.GroupRepresentation] admin_realms_realm_roles_role_name_groups_get(role_name, realm)

Returns a stream of groups that have the specified role name

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | the role name.
    realm = 'realm_example' # str | 
    brief_representation = True # bool | if false, return a full representation of the {@code GroupRepresentation} objects. (optional) if omitted the server will use the default value of True
first = 56 # int | first result to return. Ignored if negative or {@code null}. (optional)
max = 56 # int | maximum number of results to return. Ignored if negative or {@code null}. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a stream of groups that have the specified role name
        api_response = api_instance.admin_realms_realm_roles_role_name_groups_get(role_name, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_groups_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a stream of groups that have the specified role name
        api_response = api_instance.admin_realms_realm_roles_role_name_groups_get(role_name, realm, brief_representation=brief_representation, first=first, max=max)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| the role name. |
 **realm** | **str**|  |
 **brief_representation** | **bool**| if false, return a full representation of the {@code GroupRepresentation} objects. | [optional] if omitted the server will use the default value of True
 **first** | **int**| first result to return. Ignored if negative or {@code null}. | [optional]
 **max** | **int**| maximum number of results to return. Ignored if negative or {@code null}. | [optional]

### Return type

[**[group_representation.GroupRepresentation]**](GroupRepresentation.md)

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

# **admin_realms_realm_roles_role_name_management_permissions_get**
> management_permission_reference.ManagementPermissionReference admin_realms_realm_roles_role_name_management_permissions_get(role_name, realm)

Return object stating whether role Authorization permissions have been initialized or not and a reference

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether role Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_roles_role_name_management_permissions_get(role_name, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_management_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**|  |
 **realm** | **str**|  |

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

# **admin_realms_realm_roles_role_name_management_permissions_put**
> management_permission_reference.ManagementPermissionReference admin_realms_realm_roles_role_name_management_permissions_put(role_name, realm)

Return object stating whether role Authorization permissions have been initialized or not and a reference

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | 
    realm = 'realm_example' # str | 
    management_permission_reference_management_permission_reference = openapi_client.ManagementPermissionReference() # management_permission_reference.ManagementPermissionReference |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether role Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_roles_role_name_management_permissions_put(role_name, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_management_permissions_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return object stating whether role Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_roles_role_name_management_permissions_put(role_name, realm, management_permission_reference_management_permission_reference=management_permission_reference_management_permission_reference)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_management_permissions_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**|  |
 **realm** | **str**|  |
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

# **admin_realms_realm_roles_role_name_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_roles_role_name_put(role_name, realm)

Update a role by name

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | role's name (not id!)
    realm = 'realm_example' # str | 
    role_representation_role_representation = openapi_client.RoleRepresentation() # role_representation.RoleRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a role by name
        api_response = api_instance.admin_realms_realm_roles_role_name_put(role_name, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a role by name
        api_response = api_instance.admin_realms_realm_roles_role_name_put(role_name, realm, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| role&#39;s name (not id!) |
 **realm** | **str**|  |
 **role_representation_role_representation** | [**role_representation.RoleRepresentation**](RoleRepresentation.md)|  | [optional]

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

# **admin_realms_realm_roles_role_name_users_get**
> [user_representation.UserRepresentation] admin_realms_realm_roles_role_name_users_get(role_name, realm)

Returns a stream of users that have the specified role name.

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
    api_instance = openapi_client.KeycloakAdminRolesApi(api_client)
    role_name = 'role_name_example' # str | the role name.
    realm = 'realm_example' # str | 
    brief_representation = True # bool | Boolean which defines whether brief representations are returned (default: false) (optional)
first = 56 # int | first result to return. Ignored if negative or {@code null}. (optional)
max = 56 # int | maximum number of results to return. Ignored if negative or {@code null}. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a stream of users that have the specified role name.
        api_response = api_instance.admin_realms_realm_roles_role_name_users_get(role_name, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_users_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a stream of users that have the specified role name.
        api_response = api_instance.admin_realms_realm_roles_role_name_users_get(role_name, realm, brief_representation=brief_representation, first=first, max=max)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesApi->admin_realms_realm_roles_role_name_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| the role name. |
 **realm** | **str**|  |
 **brief_representation** | **bool**| Boolean which defines whether brief representations are returned (default: false) | [optional]
 **first** | **int**| first result to return. Ignored if negative or {@code null}. | [optional]
 **max** | **int**| maximum number of results to return. Ignored if negative or {@code null}. | [optional]

### Return type

[**[user_representation.UserRepresentation]**](UserRepresentation.md)

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

