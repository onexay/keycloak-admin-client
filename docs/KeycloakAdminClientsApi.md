# openapi_client.KeycloakAdminClientsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_realm_clients_client_uuid_client_secret_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_client_secret_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/client-secret | Get the client secret
[**admin_realms_realm_clients_client_uuid_client_secret_post**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_client_secret_post) | **POST** /admin/realms/{realm}/clients/{client-uuid}/client-secret | Generate a new secret for the client
[**admin_realms_realm_clients_client_uuid_client_secret_rotated_delete**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_client_secret_rotated_delete) | **DELETE** /admin/realms/{realm}/clients/{client-uuid}/client-secret/rotated | Invalidate the rotated secret for the client
[**admin_realms_realm_clients_client_uuid_client_secret_rotated_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_client_secret_rotated_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/client-secret/rotated | Get the rotated client secret
[**admin_realms_realm_clients_client_uuid_default_client_scopes_client_scope_id_delete**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_default_client_scopes_client_scope_id_delete) | **DELETE** /admin/realms/{realm}/clients/{client-uuid}/default-client-scopes/{clientScopeId} | /admin/realms/{realm}/clients/{client-uuid}/default-client-scopes/{clientScopeId}
[**admin_realms_realm_clients_client_uuid_default_client_scopes_client_scope_id_put**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_default_client_scopes_client_scope_id_put) | **PUT** /admin/realms/{realm}/clients/{client-uuid}/default-client-scopes/{clientScopeId} | /admin/realms/{realm}/clients/{client-uuid}/default-client-scopes/{clientScopeId}
[**admin_realms_realm_clients_client_uuid_default_client_scopes_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_default_client_scopes_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/default-client-scopes | Get default client scopes.  Only name and ids are returned.
[**admin_realms_realm_clients_client_uuid_delete**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_delete) | **DELETE** /admin/realms/{realm}/clients/{client-uuid} | Delete the client
[**admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_access_token_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_access_token_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/evaluate-scopes/generate-example-access-token | Create JSON with payload of example access token
[**admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_id_token_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_id_token_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/evaluate-scopes/generate-example-id-token | Create JSON with payload of example id token
[**admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_userinfo_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_userinfo_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/evaluate-scopes/generate-example-userinfo | Create JSON with payload of example user info
[**admin_realms_realm_clients_client_uuid_evaluate_scopes_protocol_mappers_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_evaluate_scopes_protocol_mappers_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/evaluate-scopes/protocol-mappers | Return list of all protocol mappers, which will be used when generating tokens issued for particular client.
[**admin_realms_realm_clients_client_uuid_evaluate_scopes_scope_mappings_role_container_id_granted_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_evaluate_scopes_scope_mappings_role_container_id_granted_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/evaluate-scopes/scope-mappings/{roleContainerId}/granted | Get effective scope mapping of all roles of particular role container, which this client is defacto allowed to have in the accessToken issued for him.
[**admin_realms_realm_clients_client_uuid_evaluate_scopes_scope_mappings_role_container_id_not_granted_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_evaluate_scopes_scope_mappings_role_container_id_not_granted_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/evaluate-scopes/scope-mappings/{roleContainerId}/not-granted | Get roles, which this client doesn&#39;t have scope for and can&#39;t have them in the accessToken issued for him.
[**admin_realms_realm_clients_client_uuid_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_get) | **GET** /admin/realms/{realm}/clients/{client-uuid} | Get representation of the client
[**admin_realms_realm_clients_client_uuid_installation_providers_provider_id_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_installation_providers_provider_id_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/installation/providers/{providerId} | /admin/realms/{realm}/clients/{client-uuid}/installation/providers/{providerId}
[**admin_realms_realm_clients_client_uuid_management_permissions_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_management_permissions_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**admin_realms_realm_clients_client_uuid_management_permissions_put**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_management_permissions_put) | **PUT** /admin/realms/{realm}/clients/{client-uuid}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**admin_realms_realm_clients_client_uuid_nodes_node_delete**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_nodes_node_delete) | **DELETE** /admin/realms/{realm}/clients/{client-uuid}/nodes/{node} | Unregister a cluster node from the client
[**admin_realms_realm_clients_client_uuid_nodes_post**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_nodes_post) | **POST** /admin/realms/{realm}/clients/{client-uuid}/nodes | Register a cluster node with the client Manually register cluster node to this client - usually it’s not needed to call this directly as adapter should handle by sending registration request to Keycloak
[**admin_realms_realm_clients_client_uuid_offline_session_count_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_offline_session_count_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/offline-session-count | Get application offline session count Returns a number of offline user sessions associated with this client { \&quot;count\&quot;: number }
[**admin_realms_realm_clients_client_uuid_offline_sessions_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_offline_sessions_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/offline-sessions | Get offline sessions for client Returns a list of offline user sessions associated with this client
[**admin_realms_realm_clients_client_uuid_optional_client_scopes_client_scope_id_delete**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_optional_client_scopes_client_scope_id_delete) | **DELETE** /admin/realms/{realm}/clients/{client-uuid}/optional-client-scopes/{clientScopeId} | /admin/realms/{realm}/clients/{client-uuid}/optional-client-scopes/{clientScopeId}
[**admin_realms_realm_clients_client_uuid_optional_client_scopes_client_scope_id_put**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_optional_client_scopes_client_scope_id_put) | **PUT** /admin/realms/{realm}/clients/{client-uuid}/optional-client-scopes/{clientScopeId} | /admin/realms/{realm}/clients/{client-uuid}/optional-client-scopes/{clientScopeId}
[**admin_realms_realm_clients_client_uuid_optional_client_scopes_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_optional_client_scopes_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/optional-client-scopes | Get optional client scopes.  Only name and ids are returned.
[**admin_realms_realm_clients_client_uuid_push_revocation_post**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_push_revocation_post) | **POST** /admin/realms/{realm}/clients/{client-uuid}/push-revocation | Push the client&#39;s revocation policy to its admin URL If the client has an admin URL, push revocation policy to it.
[**admin_realms_realm_clients_client_uuid_put**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_put) | **PUT** /admin/realms/{realm}/clients/{client-uuid} | Update the client
[**admin_realms_realm_clients_client_uuid_registration_access_token_post**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_registration_access_token_post) | **POST** /admin/realms/{realm}/clients/{client-uuid}/registration-access-token | Generate a new registration access token for the client
[**admin_realms_realm_clients_client_uuid_service_account_user_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_service_account_user_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/service-account-user | Get a user dedicated to the service account
[**admin_realms_realm_clients_client_uuid_session_count_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_session_count_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/session-count | Get application session count Returns a number of user sessions associated with this client { \&quot;count\&quot;: number }
[**admin_realms_realm_clients_client_uuid_test_nodes_available_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_test_nodes_available_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/test-nodes-available | Test if registered cluster nodes are available Tests availability by sending &#39;ping&#39; request to all cluster nodes.
[**admin_realms_realm_clients_client_uuid_user_sessions_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_client_uuid_user_sessions_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/user-sessions | Get user sessions for client Returns a list of user sessions associated with this client 
[**admin_realms_realm_clients_get**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_get) | **GET** /admin/realms/{realm}/clients | Get clients belonging to the realm.
[**admin_realms_realm_clients_post**](KeycloakAdminClientsApi.md#admin_realms_realm_clients_post) | **POST** /admin/realms/{realm}/clients | Create a new client Client’s client_id must be unique!


# **admin_realms_realm_clients_client_uuid_client_secret_get**
> credential_representation.CredentialRepresentation admin_realms_realm_clients_client_uuid_client_secret_get(realm, client_uuid)

Get the client secret

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get the client secret
        api_response = api_instance.admin_realms_realm_clients_client_uuid_client_secret_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_client_secret_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

### Return type

[**credential_representation.CredentialRepresentation**](CredentialRepresentation.md)

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

# **admin_realms_realm_clients_client_uuid_client_secret_post**
> credential_representation.CredentialRepresentation admin_realms_realm_clients_client_uuid_client_secret_post(realm, client_uuid)

Generate a new secret for the client

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Generate a new secret for the client
        api_response = api_instance.admin_realms_realm_clients_client_uuid_client_secret_post(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_client_secret_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

### Return type

[**credential_representation.CredentialRepresentation**](CredentialRepresentation.md)

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

# **admin_realms_realm_clients_client_uuid_client_secret_rotated_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_client_secret_rotated_delete(realm, client_uuid)

Invalidate the rotated secret for the client

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Invalidate the rotated secret for the client
        api_response = api_instance.admin_realms_realm_clients_client_uuid_client_secret_rotated_delete(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_client_secret_rotated_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_clients_client_uuid_client_secret_rotated_get**
> credential_representation.CredentialRepresentation admin_realms_realm_clients_client_uuid_client_secret_rotated_get(realm, client_uuid)

Get the rotated client secret

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get the rotated client secret
        api_response = api_instance.admin_realms_realm_clients_client_uuid_client_secret_rotated_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_client_secret_rotated_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

### Return type

[**credential_representation.CredentialRepresentation**](CredentialRepresentation.md)

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

# **admin_realms_realm_clients_client_uuid_default_client_scopes_client_scope_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_default_client_scopes_client_scope_id_delete(client_scope_id, realm, client_uuid)

/admin/realms/{realm}/clients/{client-uuid}/default-client-scopes/{clientScopeId}

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    client_scope_id = 'client_scope_id_example' # str | 
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/clients/{client-uuid}/default-client-scopes/{clientScopeId}
        api_response = api_instance.admin_realms_realm_clients_client_uuid_default_client_scopes_client_scope_id_delete(client_scope_id, realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_default_client_scopes_client_scope_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_scope_id** | **str**|  |
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

# **admin_realms_realm_clients_client_uuid_default_client_scopes_client_scope_id_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_default_client_scopes_client_scope_id_put(client_scope_id, realm, client_uuid)

/admin/realms/{realm}/clients/{client-uuid}/default-client-scopes/{clientScopeId}

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    client_scope_id = 'client_scope_id_example' # str | 
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/clients/{client-uuid}/default-client-scopes/{clientScopeId}
        api_response = api_instance.admin_realms_realm_clients_client_uuid_default_client_scopes_client_scope_id_put(client_scope_id, realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_default_client_scopes_client_scope_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_scope_id** | **str**|  |
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

# **admin_realms_realm_clients_client_uuid_default_client_scopes_get**
> [client_scope_representation.ClientScopeRepresentation] admin_realms_realm_clients_client_uuid_default_client_scopes_get(realm, client_uuid)

Get default client scopes.  Only name and ids are returned.

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get default client scopes.  Only name and ids are returned.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_default_client_scopes_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_default_client_scopes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

### Return type

[**[client_scope_representation.ClientScopeRepresentation]**](ClientScopeRepresentation.md)

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

# **admin_realms_realm_clients_client_uuid_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_delete(realm, client_uuid)

Delete the client

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete the client
        api_response = api_instance.admin_realms_realm_clients_client_uuid_delete(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_access_token_get**
> access_token.AccessToken admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_access_token_get(realm, client_uuid)

Create JSON with payload of example access token

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    scope = 'scope_example' # str |  (optional)
user_id = 'user_id_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create JSON with payload of example access token
        api_response = api_instance.admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_access_token_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_access_token_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create JSON with payload of example access token
        api_response = api_instance.admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_access_token_get(realm, client_uuid, scope=scope, user_id=user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_access_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **scope** | **str**|  | [optional]
 **user_id** | **str**|  | [optional]

### Return type

[**access_token.AccessToken**](AccessToken.md)

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

# **admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_id_token_get**
> id_token.IdToken admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_id_token_get(realm, client_uuid)

Create JSON with payload of example id token

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    scope = 'scope_example' # str |  (optional)
user_id = 'user_id_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create JSON with payload of example id token
        api_response = api_instance.admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_id_token_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_id_token_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create JSON with payload of example id token
        api_response = api_instance.admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_id_token_get(realm, client_uuid, scope=scope, user_id=user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_id_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **scope** | **str**|  | [optional]
 **user_id** | **str**|  | [optional]

### Return type

[**id_token.IdToken**](IdToken.md)

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

# **admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_userinfo_get**
> {str: (str,)} admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_userinfo_get(realm, client_uuid)

Create JSON with payload of example user info

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    scope = 'scope_example' # str |  (optional)
user_id = 'user_id_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create JSON with payload of example user info
        api_response = api_instance.admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_userinfo_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_userinfo_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create JSON with payload of example user info
        api_response = api_instance.admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_userinfo_get(realm, client_uuid, scope=scope, user_id=user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_evaluate_scopes_generate_example_userinfo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **scope** | **str**|  | [optional]
 **user_id** | **str**|  | [optional]

### Return type

**{str: (str,)}**

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

# **admin_realms_realm_clients_client_uuid_evaluate_scopes_protocol_mappers_get**
> [protocol_mapper_evaluation_representation.ProtocolMapperEvaluationRepresentation] admin_realms_realm_clients_client_uuid_evaluate_scopes_protocol_mappers_get(realm, client_uuid)

Return list of all protocol mappers, which will be used when generating tokens issued for particular client.

This means protocol mappers assigned to this client directly and protocol mappers assigned to all client scopes of this client.

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    scope = 'scope_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Return list of all protocol mappers, which will be used when generating tokens issued for particular client.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_evaluate_scopes_protocol_mappers_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_evaluate_scopes_protocol_mappers_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return list of all protocol mappers, which will be used when generating tokens issued for particular client.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_evaluate_scopes_protocol_mappers_get(realm, client_uuid, scope=scope)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_evaluate_scopes_protocol_mappers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **scope** | **str**|  | [optional]

### Return type

[**[protocol_mapper_evaluation_representation.ProtocolMapperEvaluationRepresentation]**](ProtocolMapperEvaluationRepresentation.md)

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

# **admin_realms_realm_clients_client_uuid_evaluate_scopes_scope_mappings_role_container_id_granted_get**
> [role_representation.RoleRepresentation] admin_realms_realm_clients_client_uuid_evaluate_scopes_scope_mappings_role_container_id_granted_get(realm, client_uuid, role_container_id)

Get effective scope mapping of all roles of particular role container, which this client is defacto allowed to have in the accessToken issued for him.

This contains scope mappings, which this client has directly, as well as scope mappings, which are granted to all client scopes, which are linked with this client.

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    role_container_id = 'role_container_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get effective scope mapping of all roles of particular role container, which this client is defacto allowed to have in the accessToken issued for him.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_evaluate_scopes_scope_mappings_role_container_id_granted_get(realm, client_uuid, role_container_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_evaluate_scopes_scope_mappings_role_container_id_granted_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **role_container_id** | **str**|  |

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

# **admin_realms_realm_clients_client_uuid_evaluate_scopes_scope_mappings_role_container_id_not_granted_get**
> [role_representation.RoleRepresentation] admin_realms_realm_clients_client_uuid_evaluate_scopes_scope_mappings_role_container_id_not_granted_get(realm, client_uuid, role_container_id)

Get roles, which this client doesn't have scope for and can't have them in the accessToken issued for him.

Defacto all the other roles of particular role container, which are not in {@link #getGrantedScopeMappings()}

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    role_container_id = 'role_container_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get roles, which this client doesn't have scope for and can't have them in the accessToken issued for him.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_evaluate_scopes_scope_mappings_role_container_id_not_granted_get(realm, client_uuid, role_container_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_evaluate_scopes_scope_mappings_role_container_id_not_granted_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **role_container_id** | **str**|  |

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

# **admin_realms_realm_clients_client_uuid_get**
> client_representation.ClientRepresentation admin_realms_realm_clients_client_uuid_get(realm, client_uuid)

Get representation of the client

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get representation of the client
        api_response = api_instance.admin_realms_realm_clients_client_uuid_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

### Return type

[**client_representation.ClientRepresentation**](ClientRepresentation.md)

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

# **admin_realms_realm_clients_client_uuid_installation_providers_provider_id_get**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_installation_providers_provider_id_get(provider_id, realm, client_uuid)

/admin/realms/{realm}/clients/{client-uuid}/installation/providers/{providerId}

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    provider_id = 'provider_id_example' # str | 
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/clients/{client-uuid}/installation/providers/{providerId}
        api_response = api_instance.admin_realms_realm_clients_client_uuid_installation_providers_provider_id_get(provider_id, realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_installation_providers_provider_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  |
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_clients_client_uuid_management_permissions_get**
> management_permission_reference.ManagementPermissionReference admin_realms_realm_clients_client_uuid_management_permissions_get(realm, client_uuid)

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether client Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_clients_client_uuid_management_permissions_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_management_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **admin_realms_realm_clients_client_uuid_management_permissions_put**
> management_permission_reference.ManagementPermissionReference admin_realms_realm_clients_client_uuid_management_permissions_put(realm, client_uuid)

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    management_permission_reference_management_permission_reference = openapi_client.ManagementPermissionReference() # management_permission_reference.ManagementPermissionReference |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether client Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_clients_client_uuid_management_permissions_put(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_management_permissions_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return object stating whether client Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_clients_client_uuid_management_permissions_put(realm, client_uuid, management_permission_reference_management_permission_reference=management_permission_reference_management_permission_reference)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_management_permissions_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **admin_realms_realm_clients_client_uuid_nodes_node_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_nodes_node_delete(node, realm, client_uuid)

Unregister a cluster node from the client

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    node = 'node_example' # str | 
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Unregister a cluster node from the client
        api_response = api_instance.admin_realms_realm_clients_client_uuid_nodes_node_delete(node, realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_nodes_node_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | **str**|  |
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

# **admin_realms_realm_clients_client_uuid_nodes_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_nodes_post(realm, client_uuid)

Register a cluster node with the client Manually register cluster node to this client - usually it’s not needed to call this directly as adapter should handle by sending registration request to Keycloak

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    request_body = {'key': 'request_body_example'} # {str: (str,)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Register a cluster node with the client Manually register cluster node to this client - usually it’s not needed to call this directly as adapter should handle by sending registration request to Keycloak
        api_response = api_instance.admin_realms_realm_clients_client_uuid_nodes_post(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_nodes_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Register a cluster node with the client Manually register cluster node to this client - usually it’s not needed to call this directly as adapter should handle by sending registration request to Keycloak
        api_response = api_instance.admin_realms_realm_clients_client_uuid_nodes_post(realm, client_uuid, request_body=request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_nodes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **request_body** | **{str: (str,)}**|  | [optional]

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

# **admin_realms_realm_clients_client_uuid_offline_session_count_get**
> {str: (int,)} admin_realms_realm_clients_client_uuid_offline_session_count_get(realm, client_uuid)

Get application offline session count Returns a number of offline user sessions associated with this client { \"count\": number }

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get application offline session count Returns a number of offline user sessions associated with this client { \"count\": number }
        api_response = api_instance.admin_realms_realm_clients_client_uuid_offline_session_count_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_offline_session_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

### Return type

**{str: (int,)}**

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

# **admin_realms_realm_clients_client_uuid_offline_sessions_get**
> [user_session_representation.UserSessionRepresentation] admin_realms_realm_clients_client_uuid_offline_sessions_get(realm, client_uuid)

Get offline sessions for client Returns a list of offline user sessions associated with this client

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    first = 56 # int | Paging offset (optional)
max = 56 # int | Maximum results size (defaults to 100) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get offline sessions for client Returns a list of offline user sessions associated with this client
        api_response = api_instance.admin_realms_realm_clients_client_uuid_offline_sessions_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_offline_sessions_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get offline sessions for client Returns a list of offline user sessions associated with this client
        api_response = api_instance.admin_realms_realm_clients_client_uuid_offline_sessions_get(realm, client_uuid, first=first, max=max)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_offline_sessions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **first** | **int**| Paging offset | [optional]
 **max** | **int**| Maximum results size (defaults to 100) | [optional]

### Return type

[**[user_session_representation.UserSessionRepresentation]**](UserSessionRepresentation.md)

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

# **admin_realms_realm_clients_client_uuid_optional_client_scopes_client_scope_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_optional_client_scopes_client_scope_id_delete(client_scope_id, realm, client_uuid)

/admin/realms/{realm}/clients/{client-uuid}/optional-client-scopes/{clientScopeId}

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    client_scope_id = 'client_scope_id_example' # str | 
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/clients/{client-uuid}/optional-client-scopes/{clientScopeId}
        api_response = api_instance.admin_realms_realm_clients_client_uuid_optional_client_scopes_client_scope_id_delete(client_scope_id, realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_optional_client_scopes_client_scope_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_scope_id** | **str**|  |
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

# **admin_realms_realm_clients_client_uuid_optional_client_scopes_client_scope_id_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_optional_client_scopes_client_scope_id_put(client_scope_id, realm, client_uuid)

/admin/realms/{realm}/clients/{client-uuid}/optional-client-scopes/{clientScopeId}

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    client_scope_id = 'client_scope_id_example' # str | 
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/clients/{client-uuid}/optional-client-scopes/{clientScopeId}
        api_response = api_instance.admin_realms_realm_clients_client_uuid_optional_client_scopes_client_scope_id_put(client_scope_id, realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_optional_client_scopes_client_scope_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_scope_id** | **str**|  |
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

# **admin_realms_realm_clients_client_uuid_optional_client_scopes_get**
> [client_scope_representation.ClientScopeRepresentation] admin_realms_realm_clients_client_uuid_optional_client_scopes_get(realm, client_uuid)

Get optional client scopes.  Only name and ids are returned.

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get optional client scopes.  Only name and ids are returned.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_optional_client_scopes_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_optional_client_scopes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

### Return type

[**[client_scope_representation.ClientScopeRepresentation]**](ClientScopeRepresentation.md)

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

# **admin_realms_realm_clients_client_uuid_push_revocation_post**
> global_request_result.GlobalRequestResult admin_realms_realm_clients_client_uuid_push_revocation_post(realm, client_uuid)

Push the client's revocation policy to its admin URL If the client has an admin URL, push revocation policy to it.

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Push the client's revocation policy to its admin URL If the client has an admin URL, push revocation policy to it.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_push_revocation_post(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_push_revocation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

### Return type

[**global_request_result.GlobalRequestResult**](GlobalRequestResult.md)

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

# **admin_realms_realm_clients_client_uuid_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_put(realm, client_uuid)

Update the client

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    client_representation_client_representation = openapi_client.ClientRepresentation() # client_representation.ClientRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the client
        api_response = api_instance.admin_realms_realm_clients_client_uuid_put(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the client
        api_response = api_instance.admin_realms_realm_clients_client_uuid_put(realm, client_uuid, client_representation_client_representation=client_representation_client_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **client_representation_client_representation** | [**client_representation.ClientRepresentation**](ClientRepresentation.md)|  | [optional]

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

# **admin_realms_realm_clients_client_uuid_registration_access_token_post**
> client_representation.ClientRepresentation admin_realms_realm_clients_client_uuid_registration_access_token_post(realm, client_uuid)

Generate a new registration access token for the client

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Generate a new registration access token for the client
        api_response = api_instance.admin_realms_realm_clients_client_uuid_registration_access_token_post(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_registration_access_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

### Return type

[**client_representation.ClientRepresentation**](ClientRepresentation.md)

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

# **admin_realms_realm_clients_client_uuid_service_account_user_get**
> user_representation.UserRepresentation admin_realms_realm_clients_client_uuid_service_account_user_get(realm, client_uuid)

Get a user dedicated to the service account

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get a user dedicated to the service account
        api_response = api_instance.admin_realms_realm_clients_client_uuid_service_account_user_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_service_account_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

### Return type

[**user_representation.UserRepresentation**](UserRepresentation.md)

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

# **admin_realms_realm_clients_client_uuid_session_count_get**
> {str: (int,)} admin_realms_realm_clients_client_uuid_session_count_get(realm, client_uuid)

Get application session count Returns a number of user sessions associated with this client { \"count\": number }

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get application session count Returns a number of user sessions associated with this client { \"count\": number }
        api_response = api_instance.admin_realms_realm_clients_client_uuid_session_count_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_session_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

### Return type

**{str: (int,)}**

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

# **admin_realms_realm_clients_client_uuid_test_nodes_available_get**
> global_request_result.GlobalRequestResult admin_realms_realm_clients_client_uuid_test_nodes_available_get(realm, client_uuid)

Test if registered cluster nodes are available Tests availability by sending 'ping' request to all cluster nodes.

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Test if registered cluster nodes are available Tests availability by sending 'ping' request to all cluster nodes.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_test_nodes_available_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_test_nodes_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |

### Return type

[**global_request_result.GlobalRequestResult**](GlobalRequestResult.md)

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

# **admin_realms_realm_clients_client_uuid_user_sessions_get**
> [user_session_representation.UserSessionRepresentation] admin_realms_realm_clients_client_uuid_user_sessions_get(realm, client_uuid)

Get user sessions for client Returns a list of user sessions associated with this client 

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    first = 56 # int | Paging offset (optional)
max = 56 # int | Maximum results size (defaults to 100) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get user sessions for client Returns a list of user sessions associated with this client 
        api_response = api_instance.admin_realms_realm_clients_client_uuid_user_sessions_get(realm, client_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_user_sessions_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get user sessions for client Returns a list of user sessions associated with this client 
        api_response = api_instance.admin_realms_realm_clients_client_uuid_user_sessions_get(realm, client_uuid, first=first, max=max)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_client_uuid_user_sessions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **first** | **int**| Paging offset | [optional]
 **max** | **int**| Maximum results size (defaults to 100) | [optional]

### Return type

[**[user_session_representation.UserSessionRepresentation]**](UserSessionRepresentation.md)

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

# **admin_realms_realm_clients_get**
> [client_representation.ClientRepresentation] admin_realms_realm_clients_get(realm)

Get clients belonging to the realm.

If a client can’t be retrieved from the storage due to a problem with the underlying storage, it is silently removed from the returned list. This ensures that concurrent modifications to the list don’t prevent callers from retrieving this list.

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_id = 'client_id_example' # str | filter by clientId (optional)
first = 56 # int | the first result (optional)
max = 56 # int | the max results to return (optional)
q = 'q_example' # str |  (optional)
search = False # bool | whether this is a search query or a getClientById query (optional) if omitted the server will use the default value of False
viewable_only = False # bool | filter clients that cannot be viewed in full by admin (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get clients belonging to the realm.
        api_response = api_instance.admin_realms_realm_clients_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get clients belonging to the realm.
        api_response = api_instance.admin_realms_realm_clients_get(realm, client_id=client_id, first=first, max=max, q=q, search=search, viewable_only=viewable_only)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_id** | **str**| filter by clientId | [optional]
 **first** | **int**| the first result | [optional]
 **max** | **int**| the max results to return | [optional]
 **q** | **str**|  | [optional]
 **search** | **bool**| whether this is a search query or a getClientById query | [optional] if omitted the server will use the default value of False
 **viewable_only** | **bool**| filter clients that cannot be viewed in full by admin | [optional] if omitted the server will use the default value of False

### Return type

[**[client_representation.ClientRepresentation]**](ClientRepresentation.md)

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

# **admin_realms_realm_clients_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_post(realm)

Create a new client Client’s client_id must be unique!

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
    api_instance = openapi_client.KeycloakAdminClientsApi(api_client)
    realm = 'realm_example' # str | 
    client_representation_client_representation = openapi_client.ClientRepresentation() # client_representation.ClientRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new client Client’s client_id must be unique!
        api_response = api_instance.admin_realms_realm_clients_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new client Client’s client_id must be unique!
        api_response = api_instance.admin_realms_realm_clients_post(realm, client_representation_client_representation=client_representation_client_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminClientsApi->admin_realms_realm_clients_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_representation_client_representation** | [**client_representation.ClientRepresentation**](ClientRepresentation.md)|  | [optional]

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

