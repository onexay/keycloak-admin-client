# openapi_client.KeycloakAdminAuthenticationManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_realm_authentication_authenticator_providers_get**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_authenticator_providers_get) | **GET** /admin/realms/{realm}/authentication/authenticator-providers | Get authenticator providers Returns a stream of authenticator providers.
[**admin_realms_realm_authentication_client_authenticator_providers_get**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_client_authenticator_providers_get) | **GET** /admin/realms/{realm}/authentication/client-authenticator-providers | Get client authenticator providers Returns a stream of client authenticator providers.
[**admin_realms_realm_authentication_config_description_provider_id_get**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_config_description_provider_id_get) | **GET** /admin/realms/{realm}/authentication/config-description/{providerId} | Get authenticator provider&#39;s configuration description
[**admin_realms_realm_authentication_config_id_delete**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_config_id_delete) | **DELETE** /admin/realms/{realm}/authentication/config/{id} | Delete authenticator configuration
[**admin_realms_realm_authentication_config_id_get**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_config_id_get) | **GET** /admin/realms/{realm}/authentication/config/{id} | Get authenticator configuration
[**admin_realms_realm_authentication_config_id_put**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_config_id_put) | **PUT** /admin/realms/{realm}/authentication/config/{id} | Update authenticator configuration
[**admin_realms_realm_authentication_config_post**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_config_post) | **POST** /admin/realms/{realm}/authentication/config | Create new authenticator configuration
[**admin_realms_realm_authentication_executions_execution_id_config_id_get**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_executions_execution_id_config_id_get) | **GET** /admin/realms/{realm}/authentication/executions/{executionId}/config/{id} | Get execution&#39;s configuration
[**admin_realms_realm_authentication_executions_execution_id_config_post**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_executions_execution_id_config_post) | **POST** /admin/realms/{realm}/authentication/executions/{executionId}/config | Update execution with new configuration
[**admin_realms_realm_authentication_executions_execution_id_delete**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_executions_execution_id_delete) | **DELETE** /admin/realms/{realm}/authentication/executions/{executionId} | Delete execution
[**admin_realms_realm_authentication_executions_execution_id_get**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_executions_execution_id_get) | **GET** /admin/realms/{realm}/authentication/executions/{executionId} | Get Single Execution
[**admin_realms_realm_authentication_executions_execution_id_lower_priority_post**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_executions_execution_id_lower_priority_post) | **POST** /admin/realms/{realm}/authentication/executions/{executionId}/lower-priority | Lower execution&#39;s priority
[**admin_realms_realm_authentication_executions_execution_id_raise_priority_post**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_executions_execution_id_raise_priority_post) | **POST** /admin/realms/{realm}/authentication/executions/{executionId}/raise-priority | Raise execution&#39;s priority
[**admin_realms_realm_authentication_executions_post**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_executions_post) | **POST** /admin/realms/{realm}/authentication/executions | Add new authentication execution
[**admin_realms_realm_authentication_flows_flow_alias_copy_post**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_flows_flow_alias_copy_post) | **POST** /admin/realms/{realm}/authentication/flows/{flowAlias}/copy | Copy existing authentication flow under a new name The new name is given as &#39;newName&#39; attribute of the passed JSON object
[**admin_realms_realm_authentication_flows_flow_alias_executions_execution_post**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_flows_flow_alias_executions_execution_post) | **POST** /admin/realms/{realm}/authentication/flows/{flowAlias}/executions/execution | Add new authentication execution to a flow
[**admin_realms_realm_authentication_flows_flow_alias_executions_flow_post**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_flows_flow_alias_executions_flow_post) | **POST** /admin/realms/{realm}/authentication/flows/{flowAlias}/executions/flow | Add new flow with new execution to existing flow
[**admin_realms_realm_authentication_flows_flow_alias_executions_get**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_flows_flow_alias_executions_get) | **GET** /admin/realms/{realm}/authentication/flows/{flowAlias}/executions | Get authentication executions for a flow
[**admin_realms_realm_authentication_flows_flow_alias_executions_put**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_flows_flow_alias_executions_put) | **PUT** /admin/realms/{realm}/authentication/flows/{flowAlias}/executions | Update authentication executions of a Flow
[**admin_realms_realm_authentication_flows_get**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_flows_get) | **GET** /admin/realms/{realm}/authentication/flows | Get authentication flows Returns a stream of authentication flows.
[**admin_realms_realm_authentication_flows_id_delete**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_flows_id_delete) | **DELETE** /admin/realms/{realm}/authentication/flows/{id} | Delete an authentication flow
[**admin_realms_realm_authentication_flows_id_get**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_flows_id_get) | **GET** /admin/realms/{realm}/authentication/flows/{id} | Get authentication flow for id
[**admin_realms_realm_authentication_flows_id_put**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_flows_id_put) | **PUT** /admin/realms/{realm}/authentication/flows/{id} | Update an authentication flow
[**admin_realms_realm_authentication_flows_post**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_flows_post) | **POST** /admin/realms/{realm}/authentication/flows | Create a new authentication flow
[**admin_realms_realm_authentication_form_action_providers_get**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_form_action_providers_get) | **GET** /admin/realms/{realm}/authentication/form-action-providers | Get form action providers Returns a stream of form action providers.
[**admin_realms_realm_authentication_form_providers_get**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_form_providers_get) | **GET** /admin/realms/{realm}/authentication/form-providers | Get form providers Returns a stream of form providers.
[**admin_realms_realm_authentication_per_client_config_description_get**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_per_client_config_description_get) | **GET** /admin/realms/{realm}/authentication/per-client-config-description | Get configuration descriptions for all clients
[**admin_realms_realm_authentication_register_required_action_post**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_register_required_action_post) | **POST** /admin/realms/{realm}/authentication/register-required-action | Register a new required actions
[**admin_realms_realm_authentication_required_actions_alias_config_delete**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_required_actions_alias_config_delete) | **DELETE** /admin/realms/{realm}/authentication/required-actions/{alias}/config | Delete RequiredAction configuration
[**admin_realms_realm_authentication_required_actions_alias_config_description_get**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_required_actions_alias_config_description_get) | **GET** /admin/realms/{realm}/authentication/required-actions/{alias}/config-description | Get RequiredAction provider configuration description
[**admin_realms_realm_authentication_required_actions_alias_config_get**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_required_actions_alias_config_get) | **GET** /admin/realms/{realm}/authentication/required-actions/{alias}/config | Get RequiredAction configuration
[**admin_realms_realm_authentication_required_actions_alias_config_put**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_required_actions_alias_config_put) | **PUT** /admin/realms/{realm}/authentication/required-actions/{alias}/config | Update RequiredAction configuration
[**admin_realms_realm_authentication_required_actions_alias_delete**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_required_actions_alias_delete) | **DELETE** /admin/realms/{realm}/authentication/required-actions/{alias} | Delete required action
[**admin_realms_realm_authentication_required_actions_alias_get**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_required_actions_alias_get) | **GET** /admin/realms/{realm}/authentication/required-actions/{alias} | Get required action for alias
[**admin_realms_realm_authentication_required_actions_alias_lower_priority_post**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_required_actions_alias_lower_priority_post) | **POST** /admin/realms/{realm}/authentication/required-actions/{alias}/lower-priority | Lower required action&#39;s priority
[**admin_realms_realm_authentication_required_actions_alias_put**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_required_actions_alias_put) | **PUT** /admin/realms/{realm}/authentication/required-actions/{alias} | Update required action
[**admin_realms_realm_authentication_required_actions_alias_raise_priority_post**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_required_actions_alias_raise_priority_post) | **POST** /admin/realms/{realm}/authentication/required-actions/{alias}/raise-priority | Raise required action&#39;s priority
[**admin_realms_realm_authentication_required_actions_get**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_required_actions_get) | **GET** /admin/realms/{realm}/authentication/required-actions | Get required actions Returns a stream of required actions.
[**admin_realms_realm_authentication_unregistered_required_actions_get**](KeycloakAdminAuthenticationManagementApi.md#admin_realms_realm_authentication_unregistered_required_actions_get) | **GET** /admin/realms/{realm}/authentication/unregistered-required-actions | Get unregistered required actions Returns a stream of unregistered required actions.


# **admin_realms_realm_authentication_authenticator_providers_get**
> [{str: (str,)}] admin_realms_realm_authentication_authenticator_providers_get(realm)

Get authenticator providers Returns a stream of authenticator providers.

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get authenticator providers Returns a stream of authenticator providers.
        api_response = api_instance.admin_realms_realm_authentication_authenticator_providers_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_authenticator_providers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

**[{str: (str,)}]**

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

# **admin_realms_realm_authentication_client_authenticator_providers_get**
> [{str: (str,)}] admin_realms_realm_authentication_client_authenticator_providers_get(realm)

Get client authenticator providers Returns a stream of client authenticator providers.

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get client authenticator providers Returns a stream of client authenticator providers.
        api_response = api_instance.admin_realms_realm_authentication_client_authenticator_providers_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_client_authenticator_providers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

**[{str: (str,)}]**

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

# **admin_realms_realm_authentication_config_description_provider_id_get**
> authenticator_config_info_representation.AuthenticatorConfigInfoRepresentation admin_realms_realm_authentication_config_description_provider_id_get(provider_id, realm)

Get authenticator provider's configuration description

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    provider_id = 'provider_id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get authenticator provider's configuration description
        api_response = api_instance.admin_realms_realm_authentication_config_description_provider_id_get(provider_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_config_description_provider_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  |
 **realm** | **str**|  |

### Return type

[**authenticator_config_info_representation.AuthenticatorConfigInfoRepresentation**](AuthenticatorConfigInfoRepresentation.md)

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

# **admin_realms_realm_authentication_config_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_config_id_delete(id, realm)

Delete authenticator configuration

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    id = 'id_example' # str | Configuration id
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete authenticator configuration
        api_response = api_instance.admin_realms_realm_authentication_config_id_delete(id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_config_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Configuration id |
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

# **admin_realms_realm_authentication_config_id_get**
> authenticator_config_representation.AuthenticatorConfigRepresentation admin_realms_realm_authentication_config_id_get(id, realm)

Get authenticator configuration

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    id = 'id_example' # str | Configuration id
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get authenticator configuration
        api_response = api_instance.admin_realms_realm_authentication_config_id_get(id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_config_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Configuration id |
 **realm** | **str**|  |

### Return type

[**authenticator_config_representation.AuthenticatorConfigRepresentation**](AuthenticatorConfigRepresentation.md)

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

# **admin_realms_realm_authentication_config_id_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_config_id_put(id, realm)

Update authenticator configuration

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    id = 'id_example' # str | Configuration id
    realm = 'realm_example' # str | 
    authenticator_config_representation_authenticator_config_representation = openapi_client.AuthenticatorConfigRepresentation() # authenticator_config_representation.AuthenticatorConfigRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update authenticator configuration
        api_response = api_instance.admin_realms_realm_authentication_config_id_put(id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_config_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update authenticator configuration
        api_response = api_instance.admin_realms_realm_authentication_config_id_put(id, realm, authenticator_config_representation_authenticator_config_representation=authenticator_config_representation_authenticator_config_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_config_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Configuration id |
 **realm** | **str**|  |
 **authenticator_config_representation_authenticator_config_representation** | [**authenticator_config_representation.AuthenticatorConfigRepresentation**](AuthenticatorConfigRepresentation.md)|  | [optional]

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

# **admin_realms_realm_authentication_config_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_config_post(realm)

Create new authenticator configuration

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    realm = 'realm_example' # str | 
    authenticator_config_representation_authenticator_config_representation = openapi_client.AuthenticatorConfigRepresentation() # authenticator_config_representation.AuthenticatorConfigRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create new authenticator configuration
        api_response = api_instance.admin_realms_realm_authentication_config_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_config_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create new authenticator configuration
        api_response = api_instance.admin_realms_realm_authentication_config_post(realm, authenticator_config_representation_authenticator_config_representation=authenticator_config_representation_authenticator_config_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_config_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **authenticator_config_representation_authenticator_config_representation** | [**authenticator_config_representation.AuthenticatorConfigRepresentation**](AuthenticatorConfigRepresentation.md)|  | [optional]

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

# **admin_realms_realm_authentication_executions_execution_id_config_id_get**
> authenticator_config_representation.AuthenticatorConfigRepresentation admin_realms_realm_authentication_executions_execution_id_config_id_get(execution_id, id, realm)

Get execution's configuration

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    execution_id = 'execution_id_example' # str | Execution id
    id = 'id_example' # str | Configuration id
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get execution's configuration
        api_response = api_instance.admin_realms_realm_authentication_executions_execution_id_config_id_get(execution_id, id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_executions_execution_id_config_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| Execution id |
 **id** | **str**| Configuration id |
 **realm** | **str**|  |

### Return type

[**authenticator_config_representation.AuthenticatorConfigRepresentation**](AuthenticatorConfigRepresentation.md)

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

# **admin_realms_realm_authentication_executions_execution_id_config_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_executions_execution_id_config_post(execution_id, realm)

Update execution with new configuration

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    execution_id = 'execution_id_example' # str | Execution id
    realm = 'realm_example' # str | 
    authenticator_config_representation_authenticator_config_representation = openapi_client.AuthenticatorConfigRepresentation() # authenticator_config_representation.AuthenticatorConfigRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update execution with new configuration
        api_response = api_instance.admin_realms_realm_authentication_executions_execution_id_config_post(execution_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_executions_execution_id_config_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update execution with new configuration
        api_response = api_instance.admin_realms_realm_authentication_executions_execution_id_config_post(execution_id, realm, authenticator_config_representation_authenticator_config_representation=authenticator_config_representation_authenticator_config_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_executions_execution_id_config_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| Execution id |
 **realm** | **str**|  |
 **authenticator_config_representation_authenticator_config_representation** | [**authenticator_config_representation.AuthenticatorConfigRepresentation**](AuthenticatorConfigRepresentation.md)|  | [optional]

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

# **admin_realms_realm_authentication_executions_execution_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_executions_execution_id_delete(execution_id, realm)

Delete execution

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    execution_id = 'execution_id_example' # str | Execution id
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete execution
        api_response = api_instance.admin_realms_realm_authentication_executions_execution_id_delete(execution_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_executions_execution_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| Execution id |
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

# **admin_realms_realm_authentication_executions_execution_id_get**
> authentication_execution_representation.AuthenticationExecutionRepresentation admin_realms_realm_authentication_executions_execution_id_get(execution_id, realm)

Get Single Execution

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    execution_id = 'execution_id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get Single Execution
        api_response = api_instance.admin_realms_realm_authentication_executions_execution_id_get(execution_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_executions_execution_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**|  |
 **realm** | **str**|  |

### Return type

[**authentication_execution_representation.AuthenticationExecutionRepresentation**](AuthenticationExecutionRepresentation.md)

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

# **admin_realms_realm_authentication_executions_execution_id_lower_priority_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_executions_execution_id_lower_priority_post(execution_id, realm)

Lower execution's priority

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    execution_id = 'execution_id_example' # str | Execution id
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Lower execution's priority
        api_response = api_instance.admin_realms_realm_authentication_executions_execution_id_lower_priority_post(execution_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_executions_execution_id_lower_priority_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| Execution id |
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

# **admin_realms_realm_authentication_executions_execution_id_raise_priority_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_executions_execution_id_raise_priority_post(execution_id, realm)

Raise execution's priority

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    execution_id = 'execution_id_example' # str | Execution id
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Raise execution's priority
        api_response = api_instance.admin_realms_realm_authentication_executions_execution_id_raise_priority_post(execution_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_executions_execution_id_raise_priority_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| Execution id |
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

# **admin_realms_realm_authentication_executions_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_executions_post(realm)

Add new authentication execution

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    realm = 'realm_example' # str | 
    authentication_execution_representation_authentication_execution_representation = openapi_client.AuthenticationExecutionRepresentation() # authentication_execution_representation.AuthenticationExecutionRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add new authentication execution
        api_response = api_instance.admin_realms_realm_authentication_executions_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_executions_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add new authentication execution
        api_response = api_instance.admin_realms_realm_authentication_executions_post(realm, authentication_execution_representation_authentication_execution_representation=authentication_execution_representation_authentication_execution_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_executions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **authentication_execution_representation_authentication_execution_representation** | [**authentication_execution_representation.AuthenticationExecutionRepresentation**](AuthenticationExecutionRepresentation.md)|  | [optional]

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

# **admin_realms_realm_authentication_flows_flow_alias_copy_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_flows_flow_alias_copy_post(flow_alias, realm)

Copy existing authentication flow under a new name The new name is given as 'newName' attribute of the passed JSON object

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    flow_alias = 'flow_alias_example' # str | name of the existing authentication flow
    realm = 'realm_example' # str | 
    request_body = {'key': 'request_body_example'} # {str: (str,)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Copy existing authentication flow under a new name The new name is given as 'newName' attribute of the passed JSON object
        api_response = api_instance.admin_realms_realm_authentication_flows_flow_alias_copy_post(flow_alias, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_flows_flow_alias_copy_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Copy existing authentication flow under a new name The new name is given as 'newName' attribute of the passed JSON object
        api_response = api_instance.admin_realms_realm_authentication_flows_flow_alias_copy_post(flow_alias, realm, request_body=request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_flows_flow_alias_copy_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_alias** | **str**| name of the existing authentication flow |
 **realm** | **str**|  |
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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_authentication_flows_flow_alias_executions_execution_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_flows_flow_alias_executions_execution_post(flow_alias, realm)

Add new authentication execution to a flow

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    flow_alias = 'flow_alias_example' # str | Alias of parent flow
    realm = 'realm_example' # str | 
    request_body = {'key': 'request_body_example'} # {str: (str,)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add new authentication execution to a flow
        api_response = api_instance.admin_realms_realm_authentication_flows_flow_alias_executions_execution_post(flow_alias, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_flows_flow_alias_executions_execution_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add new authentication execution to a flow
        api_response = api_instance.admin_realms_realm_authentication_flows_flow_alias_executions_execution_post(flow_alias, realm, request_body=request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_flows_flow_alias_executions_execution_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_alias** | **str**| Alias of parent flow |
 **realm** | **str**|  |
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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_authentication_flows_flow_alias_executions_flow_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_flows_flow_alias_executions_flow_post(flow_alias, realm)

Add new flow with new execution to existing flow

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    flow_alias = 'flow_alias_example' # str | Alias of parent authentication flow
    realm = 'realm_example' # str | 
    request_body = {'key': 'request_body_example'} # {str: (str,)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add new flow with new execution to existing flow
        api_response = api_instance.admin_realms_realm_authentication_flows_flow_alias_executions_flow_post(flow_alias, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_flows_flow_alias_executions_flow_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add new flow with new execution to existing flow
        api_response = api_instance.admin_realms_realm_authentication_flows_flow_alias_executions_flow_post(flow_alias, realm, request_body=request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_flows_flow_alias_executions_flow_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_alias** | **str**| Alias of parent authentication flow |
 **realm** | **str**|  |
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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_authentication_flows_flow_alias_executions_get**
> [authentication_execution_info_representation.AuthenticationExecutionInfoRepresentation] admin_realms_realm_authentication_flows_flow_alias_executions_get(flow_alias, realm)

Get authentication executions for a flow

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    flow_alias = 'flow_alias_example' # str | Flow alias
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get authentication executions for a flow
        api_response = api_instance.admin_realms_realm_authentication_flows_flow_alias_executions_get(flow_alias, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_flows_flow_alias_executions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_alias** | **str**| Flow alias |
 **realm** | **str**|  |

### Return type

[**[authentication_execution_info_representation.AuthenticationExecutionInfoRepresentation]**](AuthenticationExecutionInfoRepresentation.md)

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

# **admin_realms_realm_authentication_flows_flow_alias_executions_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_flows_flow_alias_executions_put(flow_alias, realm)

Update authentication executions of a Flow

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    flow_alias = 'flow_alias_example' # str | Flow alias
    realm = 'realm_example' # str | 
    authentication_execution_info_representation_authentication_execution_info_representation = openapi_client.AuthenticationExecutionInfoRepresentation() # authentication_execution_info_representation.AuthenticationExecutionInfoRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update authentication executions of a Flow
        api_response = api_instance.admin_realms_realm_authentication_flows_flow_alias_executions_put(flow_alias, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_flows_flow_alias_executions_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update authentication executions of a Flow
        api_response = api_instance.admin_realms_realm_authentication_flows_flow_alias_executions_put(flow_alias, realm, authentication_execution_info_representation_authentication_execution_info_representation=authentication_execution_info_representation_authentication_execution_info_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_flows_flow_alias_executions_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_alias** | **str**| Flow alias |
 **realm** | **str**|  |
 **authentication_execution_info_representation_authentication_execution_info_representation** | [**authentication_execution_info_representation.AuthenticationExecutionInfoRepresentation**](AuthenticationExecutionInfoRepresentation.md)|  | [optional]

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

# **admin_realms_realm_authentication_flows_get**
> [authentication_flow_representation.AuthenticationFlowRepresentation] admin_realms_realm_authentication_flows_get(realm)

Get authentication flows Returns a stream of authentication flows.

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get authentication flows Returns a stream of authentication flows.
        api_response = api_instance.admin_realms_realm_authentication_flows_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_flows_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

[**[authentication_flow_representation.AuthenticationFlowRepresentation]**](AuthenticationFlowRepresentation.md)

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

# **admin_realms_realm_authentication_flows_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_flows_id_delete(id, realm)

Delete an authentication flow

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    id = 'id_example' # str | Flow id
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete an authentication flow
        api_response = api_instance.admin_realms_realm_authentication_flows_id_delete(id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_flows_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Flow id |
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

# **admin_realms_realm_authentication_flows_id_get**
> authentication_flow_representation.AuthenticationFlowRepresentation admin_realms_realm_authentication_flows_id_get(id, realm)

Get authentication flow for id

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    id = 'id_example' # str | Flow id
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get authentication flow for id
        api_response = api_instance.admin_realms_realm_authentication_flows_id_get(id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_flows_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Flow id |
 **realm** | **str**|  |

### Return type

[**authentication_flow_representation.AuthenticationFlowRepresentation**](AuthenticationFlowRepresentation.md)

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

# **admin_realms_realm_authentication_flows_id_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_flows_id_put(id, realm)

Update an authentication flow

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    id = 'id_example' # str | 
    realm = 'realm_example' # str | 
    authentication_flow_representation_authentication_flow_representation = openapi_client.AuthenticationFlowRepresentation() # authentication_flow_representation.AuthenticationFlowRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an authentication flow
        api_response = api_instance.admin_realms_realm_authentication_flows_id_put(id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_flows_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an authentication flow
        api_response = api_instance.admin_realms_realm_authentication_flows_id_put(id, realm, authentication_flow_representation_authentication_flow_representation=authentication_flow_representation_authentication_flow_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_flows_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **realm** | **str**|  |
 **authentication_flow_representation_authentication_flow_representation** | [**authentication_flow_representation.AuthenticationFlowRepresentation**](AuthenticationFlowRepresentation.md)|  | [optional]

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

# **admin_realms_realm_authentication_flows_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_flows_post(realm)

Create a new authentication flow

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    realm = 'realm_example' # str | 
    authentication_flow_representation_authentication_flow_representation = openapi_client.AuthenticationFlowRepresentation() # authentication_flow_representation.AuthenticationFlowRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new authentication flow
        api_response = api_instance.admin_realms_realm_authentication_flows_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_flows_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new authentication flow
        api_response = api_instance.admin_realms_realm_authentication_flows_post(realm, authentication_flow_representation_authentication_flow_representation=authentication_flow_representation_authentication_flow_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_flows_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **authentication_flow_representation_authentication_flow_representation** | [**authentication_flow_representation.AuthenticationFlowRepresentation**](AuthenticationFlowRepresentation.md)|  | [optional]

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

# **admin_realms_realm_authentication_form_action_providers_get**
> [{str: (str,)}] admin_realms_realm_authentication_form_action_providers_get(realm)

Get form action providers Returns a stream of form action providers.

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get form action providers Returns a stream of form action providers.
        api_response = api_instance.admin_realms_realm_authentication_form_action_providers_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_form_action_providers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

**[{str: (str,)}]**

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

# **admin_realms_realm_authentication_form_providers_get**
> [{str: (str,)}] admin_realms_realm_authentication_form_providers_get(realm)

Get form providers Returns a stream of form providers.

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get form providers Returns a stream of form providers.
        api_response = api_instance.admin_realms_realm_authentication_form_providers_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_form_providers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

**[{str: (str,)}]**

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

# **admin_realms_realm_authentication_per_client_config_description_get**
> {str: ([config_property_representation.ConfigPropertyRepresentation],)} admin_realms_realm_authentication_per_client_config_description_get(realm)

Get configuration descriptions for all clients

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get configuration descriptions for all clients
        api_response = api_instance.admin_realms_realm_authentication_per_client_config_description_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_per_client_config_description_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

**{str: ([config_property_representation.ConfigPropertyRepresentation],)}**

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

# **admin_realms_realm_authentication_register_required_action_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_register_required_action_post(realm)

Register a new required actions

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    realm = 'realm_example' # str | 
    request_body = {'key': 'request_body_example'} # {str: (str,)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Register a new required actions
        api_response = api_instance.admin_realms_realm_authentication_register_required_action_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_register_required_action_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Register a new required actions
        api_response = api_instance.admin_realms_realm_authentication_register_required_action_post(realm, request_body=request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_register_required_action_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
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

# **admin_realms_realm_authentication_required_actions_alias_config_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_required_actions_alias_config_delete(alias, realm)

Delete RequiredAction configuration

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    alias = 'alias_example' # str | Alias of required action
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete RequiredAction configuration
        api_response = api_instance.admin_realms_realm_authentication_required_actions_alias_config_delete(alias, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_required_actions_alias_config_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias of required action |
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

# **admin_realms_realm_authentication_required_actions_alias_config_description_get**
> required_action_config_info_representation.RequiredActionConfigInfoRepresentation admin_realms_realm_authentication_required_actions_alias_config_description_get(alias, realm)

Get RequiredAction provider configuration description

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    alias = 'alias_example' # str | Alias of required action
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get RequiredAction provider configuration description
        api_response = api_instance.admin_realms_realm_authentication_required_actions_alias_config_description_get(alias, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_required_actions_alias_config_description_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias of required action |
 **realm** | **str**|  |

### Return type

[**required_action_config_info_representation.RequiredActionConfigInfoRepresentation**](RequiredActionConfigInfoRepresentation.md)

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

# **admin_realms_realm_authentication_required_actions_alias_config_get**
> required_action_config_representation.RequiredActionConfigRepresentation admin_realms_realm_authentication_required_actions_alias_config_get(alias, realm)

Get RequiredAction configuration

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    alias = 'alias_example' # str | Alias of required action
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get RequiredAction configuration
        api_response = api_instance.admin_realms_realm_authentication_required_actions_alias_config_get(alias, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_required_actions_alias_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias of required action |
 **realm** | **str**|  |

### Return type

[**required_action_config_representation.RequiredActionConfigRepresentation**](RequiredActionConfigRepresentation.md)

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

# **admin_realms_realm_authentication_required_actions_alias_config_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_required_actions_alias_config_put(alias, realm)

Update RequiredAction configuration

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    alias = 'alias_example' # str | Alias of required action
    realm = 'realm_example' # str | 
    required_action_config_representation_required_action_config_representation = openapi_client.RequiredActionConfigRepresentation() # required_action_config_representation.RequiredActionConfigRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update RequiredAction configuration
        api_response = api_instance.admin_realms_realm_authentication_required_actions_alias_config_put(alias, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_required_actions_alias_config_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update RequiredAction configuration
        api_response = api_instance.admin_realms_realm_authentication_required_actions_alias_config_put(alias, realm, required_action_config_representation_required_action_config_representation=required_action_config_representation_required_action_config_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_required_actions_alias_config_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias of required action |
 **realm** | **str**|  |
 **required_action_config_representation_required_action_config_representation** | [**required_action_config_representation.RequiredActionConfigRepresentation**](RequiredActionConfigRepresentation.md)|  | [optional]

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

# **admin_realms_realm_authentication_required_actions_alias_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_required_actions_alias_delete(alias, realm)

Delete required action

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    alias = 'alias_example' # str | Alias of required action
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete required action
        api_response = api_instance.admin_realms_realm_authentication_required_actions_alias_delete(alias, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_required_actions_alias_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias of required action |
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

# **admin_realms_realm_authentication_required_actions_alias_get**
> required_action_provider_representation.RequiredActionProviderRepresentation admin_realms_realm_authentication_required_actions_alias_get(alias, realm)

Get required action for alias

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    alias = 'alias_example' # str | Alias of required action
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get required action for alias
        api_response = api_instance.admin_realms_realm_authentication_required_actions_alias_get(alias, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_required_actions_alias_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias of required action |
 **realm** | **str**|  |

### Return type

[**required_action_provider_representation.RequiredActionProviderRepresentation**](RequiredActionProviderRepresentation.md)

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

# **admin_realms_realm_authentication_required_actions_alias_lower_priority_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_required_actions_alias_lower_priority_post(alias, realm)

Lower required action's priority

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    alias = 'alias_example' # str | Alias of required action
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Lower required action's priority
        api_response = api_instance.admin_realms_realm_authentication_required_actions_alias_lower_priority_post(alias, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_required_actions_alias_lower_priority_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias of required action |
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

# **admin_realms_realm_authentication_required_actions_alias_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_required_actions_alias_put(alias, realm)

Update required action

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    alias = 'alias_example' # str | Alias of required action
    realm = 'realm_example' # str | 
    required_action_provider_representation_required_action_provider_representation = openapi_client.RequiredActionProviderRepresentation() # required_action_provider_representation.RequiredActionProviderRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update required action
        api_response = api_instance.admin_realms_realm_authentication_required_actions_alias_put(alias, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_required_actions_alias_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update required action
        api_response = api_instance.admin_realms_realm_authentication_required_actions_alias_put(alias, realm, required_action_provider_representation_required_action_provider_representation=required_action_provider_representation_required_action_provider_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_required_actions_alias_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias of required action |
 **realm** | **str**|  |
 **required_action_provider_representation_required_action_provider_representation** | [**required_action_provider_representation.RequiredActionProviderRepresentation**](RequiredActionProviderRepresentation.md)|  | [optional]

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

# **admin_realms_realm_authentication_required_actions_alias_raise_priority_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_authentication_required_actions_alias_raise_priority_post(alias, realm)

Raise required action's priority

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    alias = 'alias_example' # str | Alias of required action
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Raise required action's priority
        api_response = api_instance.admin_realms_realm_authentication_required_actions_alias_raise_priority_post(alias, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_required_actions_alias_raise_priority_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias of required action |
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

# **admin_realms_realm_authentication_required_actions_get**
> [required_action_provider_representation.RequiredActionProviderRepresentation] admin_realms_realm_authentication_required_actions_get(realm)

Get required actions Returns a stream of required actions.

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get required actions Returns a stream of required actions.
        api_response = api_instance.admin_realms_realm_authentication_required_actions_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_required_actions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

[**[required_action_provider_representation.RequiredActionProviderRepresentation]**](RequiredActionProviderRepresentation.md)

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

# **admin_realms_realm_authentication_unregistered_required_actions_get**
> [{str: (str,)}] admin_realms_realm_authentication_unregistered_required_actions_get(realm)

Get unregistered required actions Returns a stream of unregistered required actions.

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
    api_instance = openapi_client.KeycloakAdminAuthenticationManagementApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get unregistered required actions Returns a stream of unregistered required actions.
        api_response = api_instance.admin_realms_realm_authentication_unregistered_required_actions_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminAuthenticationManagementApi->admin_realms_realm_authentication_unregistered_required_actions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

**[{str: (str,)}]**

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

