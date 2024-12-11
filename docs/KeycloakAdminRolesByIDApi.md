# openapi_client.KeycloakAdminRolesByIDApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_realm_roles_by_id_role_id_composites_clients_client_uuid_get**](KeycloakAdminRolesByIDApi.md#admin_realms_realm_roles_by_id_role_id_composites_clients_client_uuid_get) | **GET** /admin/realms/{realm}/roles-by-id/{role-id}/composites/clients/{clientUuid} | Get client-level roles for the client that are in the role&#39;s composite
[**admin_realms_realm_roles_by_id_role_id_composites_delete**](KeycloakAdminRolesByIDApi.md#admin_realms_realm_roles_by_id_role_id_composites_delete) | **DELETE** /admin/realms/{realm}/roles-by-id/{role-id}/composites | Remove a set of roles from the role&#39;s composite
[**admin_realms_realm_roles_by_id_role_id_composites_get**](KeycloakAdminRolesByIDApi.md#admin_realms_realm_roles_by_id_role_id_composites_get) | **GET** /admin/realms/{realm}/roles-by-id/{role-id}/composites | Get role&#39;s children Returns a set of role&#39;s children provided the role is a composite.
[**admin_realms_realm_roles_by_id_role_id_composites_post**](KeycloakAdminRolesByIDApi.md#admin_realms_realm_roles_by_id_role_id_composites_post) | **POST** /admin/realms/{realm}/roles-by-id/{role-id}/composites | Make the role a composite role by associating some child roles
[**admin_realms_realm_roles_by_id_role_id_composites_realm_get**](KeycloakAdminRolesByIDApi.md#admin_realms_realm_roles_by_id_role_id_composites_realm_get) | **GET** /admin/realms/{realm}/roles-by-id/{role-id}/composites/realm | Get realm-level roles that are in the role&#39;s composite
[**admin_realms_realm_roles_by_id_role_id_delete**](KeycloakAdminRolesByIDApi.md#admin_realms_realm_roles_by_id_role_id_delete) | **DELETE** /admin/realms/{realm}/roles-by-id/{role-id} | Delete the role
[**admin_realms_realm_roles_by_id_role_id_get**](KeycloakAdminRolesByIDApi.md#admin_realms_realm_roles_by_id_role_id_get) | **GET** /admin/realms/{realm}/roles-by-id/{role-id} | Get a specific role&#39;s representation
[**admin_realms_realm_roles_by_id_role_id_management_permissions_get**](KeycloakAdminRolesByIDApi.md#admin_realms_realm_roles_by_id_role_id_management_permissions_get) | **GET** /admin/realms/{realm}/roles-by-id/{role-id}/management/permissions | Return object stating whether role Authorization permissions have been initialized or not and a reference
[**admin_realms_realm_roles_by_id_role_id_management_permissions_put**](KeycloakAdminRolesByIDApi.md#admin_realms_realm_roles_by_id_role_id_management_permissions_put) | **PUT** /admin/realms/{realm}/roles-by-id/{role-id}/management/permissions | Return object stating whether role Authorization permissions have been initialized or not and a reference
[**admin_realms_realm_roles_by_id_role_id_put**](KeycloakAdminRolesByIDApi.md#admin_realms_realm_roles_by_id_role_id_put) | **PUT** /admin/realms/{realm}/roles-by-id/{role-id} | Update the role


# **admin_realms_realm_roles_by_id_role_id_composites_clients_client_uuid_get**
> [role_representation.RoleRepresentation] admin_realms_realm_roles_by_id_role_id_composites_clients_client_uuid_get(client_uuid, role_id, realm)

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
    api_instance = openapi_client.KeycloakAdminRolesByIDApi(api_client)
    client_uuid = 'client_uuid_example' # str | 
    role_id = 'role_id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get client-level roles for the client that are in the role's composite
        api_response = api_instance.admin_realms_realm_roles_by_id_role_id_composites_clients_client_uuid_get(client_uuid, role_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesByIDApi->admin_realms_realm_roles_by_id_role_id_composites_clients_client_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_uuid** | **str**|  |
 **role_id** | **str**|  |
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

# **admin_realms_realm_roles_by_id_role_id_composites_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_roles_by_id_role_id_composites_delete(role_id, realm)

Remove a set of roles from the role's composite

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
    api_instance = openapi_client.KeycloakAdminRolesByIDApi(api_client)
    role_id = 'role_id_example' # str | Role id
    realm = 'realm_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove a set of roles from the role's composite
        api_response = api_instance.admin_realms_realm_roles_by_id_role_id_composites_delete(role_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesByIDApi->admin_realms_realm_roles_by_id_role_id_composites_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a set of roles from the role's composite
        api_response = api_instance.admin_realms_realm_roles_by_id_role_id_composites_delete(role_id, realm, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesByIDApi->admin_realms_realm_roles_by_id_role_id_composites_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Role id |
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

# **admin_realms_realm_roles_by_id_role_id_composites_get**
> [role_representation.RoleRepresentation] admin_realms_realm_roles_by_id_role_id_composites_get(role_id, realm)

Get role's children Returns a set of role's children provided the role is a composite.

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
    api_instance = openapi_client.KeycloakAdminRolesByIDApi(api_client)
    role_id = 'role_id_example' # str | 
    realm = 'realm_example' # str | 
    first = 56 # int |  (optional)
max = 56 # int |  (optional)
search = 'search_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get role's children Returns a set of role's children provided the role is a composite.
        api_response = api_instance.admin_realms_realm_roles_by_id_role_id_composites_get(role_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesByIDApi->admin_realms_realm_roles_by_id_role_id_composites_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get role's children Returns a set of role's children provided the role is a composite.
        api_response = api_instance.admin_realms_realm_roles_by_id_role_id_composites_get(role_id, realm, first=first, max=max, search=search)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesByIDApi->admin_realms_realm_roles_by_id_role_id_composites_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**|  |
 **realm** | **str**|  |
 **first** | **int**|  | [optional]
 **max** | **int**|  | [optional]
 **search** | **str**|  | [optional]

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

# **admin_realms_realm_roles_by_id_role_id_composites_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_roles_by_id_role_id_composites_post(role_id, realm)

Make the role a composite role by associating some child roles

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
    api_instance = openapi_client.KeycloakAdminRolesByIDApi(api_client)
    role_id = 'role_id_example' # str | 
    realm = 'realm_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Make the role a composite role by associating some child roles
        api_response = api_instance.admin_realms_realm_roles_by_id_role_id_composites_post(role_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesByIDApi->admin_realms_realm_roles_by_id_role_id_composites_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Make the role a composite role by associating some child roles
        api_response = api_instance.admin_realms_realm_roles_by_id_role_id_composites_post(role_id, realm, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesByIDApi->admin_realms_realm_roles_by_id_role_id_composites_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**|  |
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

# **admin_realms_realm_roles_by_id_role_id_composites_realm_get**
> [role_representation.RoleRepresentation] admin_realms_realm_roles_by_id_role_id_composites_realm_get(role_id, realm)

Get realm-level roles that are in the role's composite

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
    api_instance = openapi_client.KeycloakAdminRolesByIDApi(api_client)
    role_id = 'role_id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles that are in the role's composite
        api_response = api_instance.admin_realms_realm_roles_by_id_role_id_composites_realm_get(role_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesByIDApi->admin_realms_realm_roles_by_id_role_id_composites_realm_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**|  |
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

# **admin_realms_realm_roles_by_id_role_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_roles_by_id_role_id_delete(role_id, realm)

Delete the role

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
    api_instance = openapi_client.KeycloakAdminRolesByIDApi(api_client)
    role_id = 'role_id_example' # str | id of role
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete the role
        api_response = api_instance.admin_realms_realm_roles_by_id_role_id_delete(role_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesByIDApi->admin_realms_realm_roles_by_id_role_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| id of role |
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

# **admin_realms_realm_roles_by_id_role_id_get**
> role_representation.RoleRepresentation admin_realms_realm_roles_by_id_role_id_get(role_id, realm)

Get a specific role's representation

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
    api_instance = openapi_client.KeycloakAdminRolesByIDApi(api_client)
    role_id = 'role_id_example' # str | id of role
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get a specific role's representation
        api_response = api_instance.admin_realms_realm_roles_by_id_role_id_get(role_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesByIDApi->admin_realms_realm_roles_by_id_role_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| id of role |
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

# **admin_realms_realm_roles_by_id_role_id_management_permissions_get**
> management_permission_reference.ManagementPermissionReference admin_realms_realm_roles_by_id_role_id_management_permissions_get(role_id, realm)

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
    api_instance = openapi_client.KeycloakAdminRolesByIDApi(api_client)
    role_id = 'role_id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether role Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_roles_by_id_role_id_management_permissions_get(role_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesByIDApi->admin_realms_realm_roles_by_id_role_id_management_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**|  |
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

# **admin_realms_realm_roles_by_id_role_id_management_permissions_put**
> management_permission_reference.ManagementPermissionReference admin_realms_realm_roles_by_id_role_id_management_permissions_put(role_id, realm)

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
    api_instance = openapi_client.KeycloakAdminRolesByIDApi(api_client)
    role_id = 'role_id_example' # str | 
    realm = 'realm_example' # str | 
    management_permission_reference_management_permission_reference = openapi_client.ManagementPermissionReference() # management_permission_reference.ManagementPermissionReference |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether role Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_roles_by_id_role_id_management_permissions_put(role_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesByIDApi->admin_realms_realm_roles_by_id_role_id_management_permissions_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return object stating whether role Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_roles_by_id_role_id_management_permissions_put(role_id, realm, management_permission_reference_management_permission_reference=management_permission_reference_management_permission_reference)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesByIDApi->admin_realms_realm_roles_by_id_role_id_management_permissions_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**|  |
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

# **admin_realms_realm_roles_by_id_role_id_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_roles_by_id_role_id_put(role_id, realm)

Update the role

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
    api_instance = openapi_client.KeycloakAdminRolesByIDApi(api_client)
    role_id = 'role_id_example' # str | id of role
    realm = 'realm_example' # str | 
    role_representation_role_representation = openapi_client.RoleRepresentation() # role_representation.RoleRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the role
        api_response = api_instance.admin_realms_realm_roles_by_id_role_id_put(role_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesByIDApi->admin_realms_realm_roles_by_id_role_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the role
        api_response = api_instance.admin_realms_realm_roles_by_id_role_id_put(role_id, realm, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminRolesByIDApi->admin_realms_realm_roles_by_id_role_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| id of role |
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

