# openapi_client.KeycloakAdminScopeMappingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_available_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_available_get) | **GET** /admin/realms/{realm}/client-scopes/{client-scope-id}/scope-mappings/clients/{client}/available | The available client-level roles Returns the roles for the client that can be associated with the client&#39;s scope
[**admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_composite_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_composite_get) | **GET** /admin/realms/{realm}/client-scopes/{client-scope-id}/scope-mappings/clients/{client}/composite | Get effective client roles Returns the roles for the client that are associated with the client&#39;s scope.
[**admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_delete**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_delete) | **DELETE** /admin/realms/{realm}/client-scopes/{client-scope-id}/scope-mappings/clients/{client} | Remove client-level roles from the client&#39;s scope.
[**admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_get) | **GET** /admin/realms/{realm}/client-scopes/{client-scope-id}/scope-mappings/clients/{client} | Get the roles associated with a client&#39;s scope Returns roles for the client.
[**admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_post**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_post) | **POST** /admin/realms/{realm}/client-scopes/{client-scope-id}/scope-mappings/clients/{client} | Add client-level roles to the client&#39;s scope
[**admin_realms_realm_client_scopes_client_scope_id_scope_mappings_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_scopes_client_scope_id_scope_mappings_get) | **GET** /admin/realms/{realm}/client-scopes/{client-scope-id}/scope-mappings | Get all scope mappings for the client
[**admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_available_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_available_get) | **GET** /admin/realms/{realm}/client-scopes/{client-scope-id}/scope-mappings/realm/available | Get realm-level roles that are available to attach to this client&#39;s scope
[**admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_composite_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_composite_get) | **GET** /admin/realms/{realm}/client-scopes/{client-scope-id}/scope-mappings/realm/composite | Get effective realm-level roles associated with the client’s scope What this does is recurse any composite roles associated with the client’s scope and adds the roles to this lists.
[**admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_delete**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_delete) | **DELETE** /admin/realms/{realm}/client-scopes/{client-scope-id}/scope-mappings/realm | Remove a set of realm-level roles from the client&#39;s scope
[**admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_get) | **GET** /admin/realms/{realm}/client-scopes/{client-scope-id}/scope-mappings/realm | Get realm-level roles associated with the client&#39;s scope
[**admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_post**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_post) | **POST** /admin/realms/{realm}/client-scopes/{client-scope-id}/scope-mappings/realm | Add a set of realm-level roles to the client&#39;s scope
[**admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_available_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_available_get) | **GET** /admin/realms/{realm}/client-templates/{client-scope-id}/scope-mappings/clients/{client}/available | The available client-level roles Returns the roles for the client that can be associated with the client&#39;s scope
[**admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_composite_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_composite_get) | **GET** /admin/realms/{realm}/client-templates/{client-scope-id}/scope-mappings/clients/{client}/composite | Get effective client roles Returns the roles for the client that are associated with the client&#39;s scope.
[**admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_delete**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_delete) | **DELETE** /admin/realms/{realm}/client-templates/{client-scope-id}/scope-mappings/clients/{client} | Remove client-level roles from the client&#39;s scope.
[**admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_get) | **GET** /admin/realms/{realm}/client-templates/{client-scope-id}/scope-mappings/clients/{client} | Get the roles associated with a client&#39;s scope Returns roles for the client.
[**admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_post**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_post) | **POST** /admin/realms/{realm}/client-templates/{client-scope-id}/scope-mappings/clients/{client} | Add client-level roles to the client&#39;s scope
[**admin_realms_realm_client_templates_client_scope_id_scope_mappings_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_templates_client_scope_id_scope_mappings_get) | **GET** /admin/realms/{realm}/client-templates/{client-scope-id}/scope-mappings | Get all scope mappings for the client
[**admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_available_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_available_get) | **GET** /admin/realms/{realm}/client-templates/{client-scope-id}/scope-mappings/realm/available | Get realm-level roles that are available to attach to this client&#39;s scope
[**admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_composite_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_composite_get) | **GET** /admin/realms/{realm}/client-templates/{client-scope-id}/scope-mappings/realm/composite | Get effective realm-level roles associated with the client’s scope What this does is recurse any composite roles associated with the client’s scope and adds the roles to this lists.
[**admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_delete**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_delete) | **DELETE** /admin/realms/{realm}/client-templates/{client-scope-id}/scope-mappings/realm | Remove a set of realm-level roles from the client&#39;s scope
[**admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_get) | **GET** /admin/realms/{realm}/client-templates/{client-scope-id}/scope-mappings/realm | Get realm-level roles associated with the client&#39;s scope
[**admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_post**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_post) | **POST** /admin/realms/{realm}/client-templates/{client-scope-id}/scope-mappings/realm | Add a set of realm-level roles to the client&#39;s scope
[**admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_available_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_available_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/scope-mappings/clients/{client}/available | The available client-level roles Returns the roles for the client that can be associated with the client&#39;s scope
[**admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_composite_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_composite_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/scope-mappings/clients/{client}/composite | Get effective client roles Returns the roles for the client that are associated with the client&#39;s scope.
[**admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_delete**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_delete) | **DELETE** /admin/realms/{realm}/clients/{client-uuid}/scope-mappings/clients/{client} | Remove client-level roles from the client&#39;s scope.
[**admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/scope-mappings/clients/{client} | Get the roles associated with a client&#39;s scope Returns roles for the client.
[**admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_post**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_post) | **POST** /admin/realms/{realm}/clients/{client-uuid}/scope-mappings/clients/{client} | Add client-level roles to the client&#39;s scope
[**admin_realms_realm_clients_client_uuid_scope_mappings_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_clients_client_uuid_scope_mappings_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/scope-mappings | Get all scope mappings for the client
[**admin_realms_realm_clients_client_uuid_scope_mappings_realm_available_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_clients_client_uuid_scope_mappings_realm_available_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/scope-mappings/realm/available | Get realm-level roles that are available to attach to this client&#39;s scope
[**admin_realms_realm_clients_client_uuid_scope_mappings_realm_composite_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_clients_client_uuid_scope_mappings_realm_composite_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/scope-mappings/realm/composite | Get effective realm-level roles associated with the client’s scope What this does is recurse any composite roles associated with the client’s scope and adds the roles to this lists.
[**admin_realms_realm_clients_client_uuid_scope_mappings_realm_delete**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_clients_client_uuid_scope_mappings_realm_delete) | **DELETE** /admin/realms/{realm}/clients/{client-uuid}/scope-mappings/realm | Remove a set of realm-level roles from the client&#39;s scope
[**admin_realms_realm_clients_client_uuid_scope_mappings_realm_get**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_clients_client_uuid_scope_mappings_realm_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/scope-mappings/realm | Get realm-level roles associated with the client&#39;s scope
[**admin_realms_realm_clients_client_uuid_scope_mappings_realm_post**](KeycloakAdminScopeMappingsApi.md#admin_realms_realm_clients_client_uuid_scope_mappings_realm_post) | **POST** /admin/realms/{realm}/clients/{client-uuid}/scope-mappings/realm | Add a set of realm-level roles to the client&#39;s scope


# **admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_available_get**
> [role_representation.RoleRepresentation] admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_available_get(realm, client_scope_id, client)

The available client-level roles Returns the roles for the client that can be associated with the client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    client = 'client_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # The available client-level roles Returns the roles for the client that can be associated with the client's scope
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_available_get(realm, client_scope_id, client)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
 **client** | **str**|  |

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

# **admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_composite_get**
> [role_representation.RoleRepresentation] admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_composite_get(realm, client_scope_id, client)

Get effective client roles Returns the roles for the client that are associated with the client's scope.

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    client = 'client_example' # str | 
    brief_representation = True # bool | if false, return roles with their attributes (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Get effective client roles Returns the roles for the client that are associated with the client's scope.
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_composite_get(realm, client_scope_id, client)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective client roles Returns the roles for the client that are associated with the client's scope.
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_composite_get(realm, client_scope_id, client, brief_representation=brief_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_composite_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
 **client** | **str**|  |
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

# **admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_delete(realm, client_scope_id, client)

Remove client-level roles from the client's scope.

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    client = 'client_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove client-level roles from the client's scope.
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_delete(realm, client_scope_id, client)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove client-level roles from the client's scope.
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_delete(realm, client_scope_id, client, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
 **client** | **str**|  |
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

# **admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_get**
> [role_representation.RoleRepresentation] admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_get(realm, client_scope_id, client)

Get the roles associated with a client's scope Returns roles for the client.

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    client = 'client_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get the roles associated with a client's scope Returns roles for the client.
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_get(realm, client_scope_id, client)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
 **client** | **str**|  |

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

# **admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_post(realm, client_scope_id, client)

Add client-level roles to the client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    client = 'client_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add client-level roles to the client's scope
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_post(realm, client_scope_id, client)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add client-level roles to the client's scope
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_post(realm, client_scope_id, client, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_scopes_client_scope_id_scope_mappings_clients_client_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
 **client** | **str**|  |
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

# **admin_realms_realm_client_scopes_client_scope_id_scope_mappings_get**
> mappings_representation.MappingsRepresentation admin_realms_realm_client_scopes_client_scope_id_scope_mappings_get(realm, client_scope_id)

Get all scope mappings for the client

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get all scope mappings for the client
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_scope_mappings_get(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_scopes_client_scope_id_scope_mappings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |

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

# **admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_available_get**
> [role_representation.RoleRepresentation] admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_available_get(realm, client_scope_id)

Get realm-level roles that are available to attach to this client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles that are available to attach to this client's scope
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_available_get(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |

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

# **admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_composite_get**
> [role_representation.RoleRepresentation] admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_composite_get(realm, client_scope_id)

Get effective realm-level roles associated with the client’s scope What this does is recurse any composite roles associated with the client’s scope and adds the roles to this lists.

The method is really to show a comprehensive total view of realm-level roles associated with the client.

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    brief_representation = True # bool | if false, return roles with their attributes (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Get effective realm-level roles associated with the client’s scope What this does is recurse any composite roles associated with the client’s scope and adds the roles to this lists.
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_composite_get(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective realm-level roles associated with the client’s scope What this does is recurse any composite roles associated with the client’s scope and adds the roles to this lists.
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_composite_get(realm, client_scope_id, brief_representation=brief_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_composite_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
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

# **admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_delete(realm, client_scope_id)

Remove a set of realm-level roles from the client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove a set of realm-level roles from the client's scope
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_delete(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a set of realm-level roles from the client's scope
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_delete(realm, client_scope_id, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
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

# **admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_get**
> [role_representation.RoleRepresentation] admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_get(realm, client_scope_id)

Get realm-level roles associated with the client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles associated with the client's scope
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_get(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |

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

# **admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_post(realm, client_scope_id)

Add a set of realm-level roles to the client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a set of realm-level roles to the client's scope
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_post(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a set of realm-level roles to the client's scope
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_post(realm, client_scope_id, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_scopes_client_scope_id_scope_mappings_realm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
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

# **admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_available_get**
> [role_representation.RoleRepresentation] admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_available_get(realm, client_scope_id, client)

The available client-level roles Returns the roles for the client that can be associated with the client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    client = 'client_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # The available client-level roles Returns the roles for the client that can be associated with the client's scope
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_available_get(realm, client_scope_id, client)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
 **client** | **str**|  |

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

# **admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_composite_get**
> [role_representation.RoleRepresentation] admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_composite_get(realm, client_scope_id, client)

Get effective client roles Returns the roles for the client that are associated with the client's scope.

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    client = 'client_example' # str | 
    brief_representation = True # bool | if false, return roles with their attributes (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Get effective client roles Returns the roles for the client that are associated with the client's scope.
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_composite_get(realm, client_scope_id, client)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective client roles Returns the roles for the client that are associated with the client's scope.
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_composite_get(realm, client_scope_id, client, brief_representation=brief_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_composite_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
 **client** | **str**|  |
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

# **admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_delete(realm, client_scope_id, client)

Remove client-level roles from the client's scope.

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    client = 'client_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove client-level roles from the client's scope.
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_delete(realm, client_scope_id, client)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove client-level roles from the client's scope.
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_delete(realm, client_scope_id, client, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
 **client** | **str**|  |
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

# **admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_get**
> [role_representation.RoleRepresentation] admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_get(realm, client_scope_id, client)

Get the roles associated with a client's scope Returns roles for the client.

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    client = 'client_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get the roles associated with a client's scope Returns roles for the client.
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_get(realm, client_scope_id, client)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
 **client** | **str**|  |

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

# **admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_post(realm, client_scope_id, client)

Add client-level roles to the client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    client = 'client_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add client-level roles to the client's scope
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_post(realm, client_scope_id, client)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add client-level roles to the client's scope
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_post(realm, client_scope_id, client, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_templates_client_scope_id_scope_mappings_clients_client_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
 **client** | **str**|  |
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

# **admin_realms_realm_client_templates_client_scope_id_scope_mappings_get**
> mappings_representation.MappingsRepresentation admin_realms_realm_client_templates_client_scope_id_scope_mappings_get(realm, client_scope_id)

Get all scope mappings for the client

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get all scope mappings for the client
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_scope_mappings_get(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_templates_client_scope_id_scope_mappings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |

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

# **admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_available_get**
> [role_representation.RoleRepresentation] admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_available_get(realm, client_scope_id)

Get realm-level roles that are available to attach to this client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles that are available to attach to this client's scope
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_available_get(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |

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

# **admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_composite_get**
> [role_representation.RoleRepresentation] admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_composite_get(realm, client_scope_id)

Get effective realm-level roles associated with the client’s scope What this does is recurse any composite roles associated with the client’s scope and adds the roles to this lists.

The method is really to show a comprehensive total view of realm-level roles associated with the client.

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    brief_representation = True # bool | if false, return roles with their attributes (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Get effective realm-level roles associated with the client’s scope What this does is recurse any composite roles associated with the client’s scope and adds the roles to this lists.
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_composite_get(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective realm-level roles associated with the client’s scope What this does is recurse any composite roles associated with the client’s scope and adds the roles to this lists.
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_composite_get(realm, client_scope_id, brief_representation=brief_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_composite_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
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

# **admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_delete(realm, client_scope_id)

Remove a set of realm-level roles from the client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove a set of realm-level roles from the client's scope
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_delete(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a set of realm-level roles from the client's scope
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_delete(realm, client_scope_id, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
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

# **admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_get**
> [role_representation.RoleRepresentation] admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_get(realm, client_scope_id)

Get realm-level roles associated with the client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles associated with the client's scope
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_get(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |

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

# **admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_post(realm, client_scope_id)

Add a set of realm-level roles to the client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a set of realm-level roles to the client's scope
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_post(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a set of realm-level roles to the client's scope
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_post(realm, client_scope_id, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_client_templates_client_scope_id_scope_mappings_realm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
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

# **admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_available_get**
> [role_representation.RoleRepresentation] admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_available_get(realm, client_uuid, client)

The available client-level roles Returns the roles for the client that can be associated with the client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    client = 'client_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # The available client-level roles Returns the roles for the client that can be associated with the client's scope
        api_response = api_instance.admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_available_get(realm, client_uuid, client)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **client** | **str**|  |

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

# **admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_composite_get**
> [role_representation.RoleRepresentation] admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_composite_get(realm, client_uuid, client)

Get effective client roles Returns the roles for the client that are associated with the client's scope.

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    client = 'client_example' # str | 
    brief_representation = True # bool | if false, return roles with their attributes (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Get effective client roles Returns the roles for the client that are associated with the client's scope.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_composite_get(realm, client_uuid, client)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective client roles Returns the roles for the client that are associated with the client's scope.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_composite_get(realm, client_uuid, client, brief_representation=brief_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_composite_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **client** | **str**|  |
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

# **admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_delete(realm, client_uuid, client)

Remove client-level roles from the client's scope.

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    client = 'client_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove client-level roles from the client's scope.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_delete(realm, client_uuid, client)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove client-level roles from the client's scope.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_delete(realm, client_uuid, client, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **client** | **str**|  |
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

# **admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_get**
> [role_representation.RoleRepresentation] admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_get(realm, client_uuid, client)

Get the roles associated with a client's scope Returns roles for the client.

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    client = 'client_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get the roles associated with a client's scope Returns roles for the client.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_get(realm, client_uuid, client)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **client** | **str**|  |

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

# **admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_post(realm, client_uuid, client)

Add client-level roles to the client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    client = 'client_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add client-level roles to the client's scope
        api_response = api_instance.admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_post(realm, client_uuid, client)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add client-level roles to the client's scope
        api_response = api_instance.admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_post(realm, client_uuid, client, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_clients_client_uuid_scope_mappings_clients_client_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **client** | **str**|  |
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

# **admin_realms_realm_clients_client_uuid_scope_mappings_get**
> mappings_representation.MappingsRepresentation admin_realms_realm_clients_client_uuid_scope_mappings_get(realm, client_uuid)

Get all scope mappings for the client

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get all scope mappings for the client
        api_response = api_instance.admin_realms_realm_clients_client_uuid_scope_mappings_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_clients_client_uuid_scope_mappings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

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

# **admin_realms_realm_clients_client_uuid_scope_mappings_realm_available_get**
> [role_representation.RoleRepresentation] admin_realms_realm_clients_client_uuid_scope_mappings_realm_available_get(realm, client_uuid)

Get realm-level roles that are available to attach to this client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles that are available to attach to this client's scope
        api_response = api_instance.admin_realms_realm_clients_client_uuid_scope_mappings_realm_available_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_clients_client_uuid_scope_mappings_realm_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **admin_realms_realm_clients_client_uuid_scope_mappings_realm_composite_get**
> [role_representation.RoleRepresentation] admin_realms_realm_clients_client_uuid_scope_mappings_realm_composite_get(realm, client_uuid)

Get effective realm-level roles associated with the client’s scope What this does is recurse any composite roles associated with the client’s scope and adds the roles to this lists.

The method is really to show a comprehensive total view of realm-level roles associated with the client.

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    brief_representation = True # bool | if false, return roles with their attributes (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Get effective realm-level roles associated with the client’s scope What this does is recurse any composite roles associated with the client’s scope and adds the roles to this lists.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_scope_mappings_realm_composite_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_clients_client_uuid_scope_mappings_realm_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective realm-level roles associated with the client’s scope What this does is recurse any composite roles associated with the client’s scope and adds the roles to this lists.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_scope_mappings_realm_composite_get(realm, client_uuid, brief_representation=brief_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_clients_client_uuid_scope_mappings_realm_composite_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
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

# **admin_realms_realm_clients_client_uuid_scope_mappings_realm_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_scope_mappings_realm_delete(realm, client_uuid)

Remove a set of realm-level roles from the client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove a set of realm-level roles from the client's scope
        api_response = api_instance.admin_realms_realm_clients_client_uuid_scope_mappings_realm_delete(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_clients_client_uuid_scope_mappings_realm_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a set of realm-level roles from the client's scope
        api_response = api_instance.admin_realms_realm_clients_client_uuid_scope_mappings_realm_delete(realm, client_uuid, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_clients_client_uuid_scope_mappings_realm_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **admin_realms_realm_clients_client_uuid_scope_mappings_realm_get**
> [role_representation.RoleRepresentation] admin_realms_realm_clients_client_uuid_scope_mappings_realm_get(realm, client_uuid)

Get realm-level roles associated with the client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles associated with the client's scope
        api_response = api_instance.admin_realms_realm_clients_client_uuid_scope_mappings_realm_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_clients_client_uuid_scope_mappings_realm_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **admin_realms_realm_clients_client_uuid_scope_mappings_realm_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_scope_mappings_realm_post(realm, client_uuid)

Add a set of realm-level roles to the client's scope

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
    api_instance = openapi_client.KeycloakAdminScopeMappingsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    role_representation_role_representation = [openapi_client.RoleRepresentation()] # [role_representation.RoleRepresentation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a set of realm-level roles to the client's scope
        api_response = api_instance.admin_realms_realm_clients_client_uuid_scope_mappings_realm_post(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_clients_client_uuid_scope_mappings_realm_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a set of realm-level roles to the client's scope
        api_response = api_instance.admin_realms_realm_clients_client_uuid_scope_mappings_realm_post(realm, client_uuid, role_representation_role_representation=role_representation_role_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminScopeMappingsApi->admin_realms_realm_clients_client_uuid_scope_mappings_realm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

