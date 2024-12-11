# openapi_client.ClientInitialAccessApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_realm_clients_initial_access_get**](ClientInitialAccessApi.md#admin_realms_realm_clients_initial_access_get) | **GET** /admin/realms/{realm}/clients-initial-access | /admin/realms/{realm}/clients-initial-access
[**admin_realms_realm_clients_initial_access_id_delete**](ClientInitialAccessApi.md#admin_realms_realm_clients_initial_access_id_delete) | **DELETE** /admin/realms/{realm}/clients-initial-access/{id} | /admin/realms/{realm}/clients-initial-access/{id}
[**admin_realms_realm_clients_initial_access_post**](ClientInitialAccessApi.md#admin_realms_realm_clients_initial_access_post) | **POST** /admin/realms/{realm}/clients-initial-access | Create a new initial access token.


# **admin_realms_realm_clients_initial_access_get**
> [client_initial_access_presentation.ClientInitialAccessPresentation] admin_realms_realm_clients_initial_access_get(realm)

/admin/realms/{realm}/clients-initial-access

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
    api_instance = openapi_client.ClientInitialAccessApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/clients-initial-access
        api_response = api_instance.admin_realms_realm_clients_initial_access_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientInitialAccessApi->admin_realms_realm_clients_initial_access_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

[**[client_initial_access_presentation.ClientInitialAccessPresentation]**](ClientInitialAccessPresentation.md)

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

# **admin_realms_realm_clients_initial_access_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_initial_access_id_delete(id, realm)

/admin/realms/{realm}/clients-initial-access/{id}

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
    api_instance = openapi_client.ClientInitialAccessApi(api_client)
    id = 'id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/clients-initial-access/{id}
        api_response = api_instance.admin_realms_realm_clients_initial_access_id_delete(id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientInitialAccessApi->admin_realms_realm_clients_initial_access_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **admin_realms_realm_clients_initial_access_post**
> client_initial_access_create_presentation.ClientInitialAccessCreatePresentation admin_realms_realm_clients_initial_access_post(realm)

Create a new initial access token.

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
    api_instance = openapi_client.ClientInitialAccessApi(api_client)
    realm = 'realm_example' # str | 
    client_initial_access_create_presentation_client_initial_access_create_presentation = openapi_client.ClientInitialAccessCreatePresentation() # client_initial_access_create_presentation.ClientInitialAccessCreatePresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new initial access token.
        api_response = api_instance.admin_realms_realm_clients_initial_access_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientInitialAccessApi->admin_realms_realm_clients_initial_access_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new initial access token.
        api_response = api_instance.admin_realms_realm_clients_initial_access_post(realm, client_initial_access_create_presentation_client_initial_access_create_presentation=client_initial_access_create_presentation_client_initial_access_create_presentation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientInitialAccessApi->admin_realms_realm_clients_initial_access_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_initial_access_create_presentation_client_initial_access_create_presentation** | [**client_initial_access_create_presentation.ClientInitialAccessCreatePresentation**](ClientInitialAccessCreatePresentation.md)|  | [optional]

### Return type

[**client_initial_access_create_presentation.ClientInitialAccessCreatePresentation**](ClientInitialAccessCreatePresentation.md)

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

