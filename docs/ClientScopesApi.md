# openapi_client.ClientScopesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_realm_client_scopes_client_scope_id_delete**](ClientScopesApi.md#admin_realms_realm_client_scopes_client_scope_id_delete) | **DELETE** /admin/realms/{realm}/client-scopes/{client-scope-id} | Delete the client scope
[**admin_realms_realm_client_scopes_client_scope_id_get**](ClientScopesApi.md#admin_realms_realm_client_scopes_client_scope_id_get) | **GET** /admin/realms/{realm}/client-scopes/{client-scope-id} | Get representation of the client scope
[**admin_realms_realm_client_scopes_client_scope_id_put**](ClientScopesApi.md#admin_realms_realm_client_scopes_client_scope_id_put) | **PUT** /admin/realms/{realm}/client-scopes/{client-scope-id} | Update the client scope
[**admin_realms_realm_client_scopes_get**](ClientScopesApi.md#admin_realms_realm_client_scopes_get) | **GET** /admin/realms/{realm}/client-scopes | Get client scopes belonging to the realm Returns a list of client scopes belonging to the realm
[**admin_realms_realm_client_scopes_post**](ClientScopesApi.md#admin_realms_realm_client_scopes_post) | **POST** /admin/realms/{realm}/client-scopes | Create a new client scope Client Scope’s name must be unique!
[**admin_realms_realm_client_templates_client_scope_id_delete**](ClientScopesApi.md#admin_realms_realm_client_templates_client_scope_id_delete) | **DELETE** /admin/realms/{realm}/client-templates/{client-scope-id} | Delete the client scope
[**admin_realms_realm_client_templates_client_scope_id_get**](ClientScopesApi.md#admin_realms_realm_client_templates_client_scope_id_get) | **GET** /admin/realms/{realm}/client-templates/{client-scope-id} | Get representation of the client scope
[**admin_realms_realm_client_templates_client_scope_id_put**](ClientScopesApi.md#admin_realms_realm_client_templates_client_scope_id_put) | **PUT** /admin/realms/{realm}/client-templates/{client-scope-id} | Update the client scope
[**admin_realms_realm_client_templates_get**](ClientScopesApi.md#admin_realms_realm_client_templates_get) | **GET** /admin/realms/{realm}/client-templates | Get client scopes belonging to the realm Returns a list of client scopes belonging to the realm
[**admin_realms_realm_client_templates_post**](ClientScopesApi.md#admin_realms_realm_client_templates_post) | **POST** /admin/realms/{realm}/client-templates | Create a new client scope Client Scope’s name must be unique!


# **admin_realms_realm_client_scopes_client_scope_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_client_scopes_client_scope_id_delete(realm, client_scope_id)

Delete the client scope

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
    api_instance = openapi_client.ClientScopesApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete the client scope
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_delete(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientScopesApi->admin_realms_realm_client_scopes_client_scope_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |

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

# **admin_realms_realm_client_scopes_client_scope_id_get**
> client_scope_representation.ClientScopeRepresentation admin_realms_realm_client_scopes_client_scope_id_get(realm, client_scope_id)

Get representation of the client scope

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
    api_instance = openapi_client.ClientScopesApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get representation of the client scope
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_get(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientScopesApi->admin_realms_realm_client_scopes_client_scope_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |

### Return type

[**client_scope_representation.ClientScopeRepresentation**](ClientScopeRepresentation.md)

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

# **admin_realms_realm_client_scopes_client_scope_id_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_client_scopes_client_scope_id_put(realm, client_scope_id)

Update the client scope

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
    api_instance = openapi_client.ClientScopesApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    client_scope_representation_client_scope_representation = openapi_client.ClientScopeRepresentation() # client_scope_representation.ClientScopeRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the client scope
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_put(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientScopesApi->admin_realms_realm_client_scopes_client_scope_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the client scope
        api_response = api_instance.admin_realms_realm_client_scopes_client_scope_id_put(realm, client_scope_id, client_scope_representation_client_scope_representation=client_scope_representation_client_scope_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientScopesApi->admin_realms_realm_client_scopes_client_scope_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
 **client_scope_representation_client_scope_representation** | [**client_scope_representation.ClientScopeRepresentation**](ClientScopeRepresentation.md)|  | [optional]

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

# **admin_realms_realm_client_scopes_get**
> [client_scope_representation.ClientScopeRepresentation] admin_realms_realm_client_scopes_get(realm)

Get client scopes belonging to the realm Returns a list of client scopes belonging to the realm

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
    api_instance = openapi_client.ClientScopesApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get client scopes belonging to the realm Returns a list of client scopes belonging to the realm
        api_response = api_instance.admin_realms_realm_client_scopes_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientScopesApi->admin_realms_realm_client_scopes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

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

# **admin_realms_realm_client_scopes_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_client_scopes_post(realm)

Create a new client scope Client Scope’s name must be unique!

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
    api_instance = openapi_client.ClientScopesApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_representation_client_scope_representation = openapi_client.ClientScopeRepresentation() # client_scope_representation.ClientScopeRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new client scope Client Scope’s name must be unique!
        api_response = api_instance.admin_realms_realm_client_scopes_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientScopesApi->admin_realms_realm_client_scopes_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new client scope Client Scope’s name must be unique!
        api_response = api_instance.admin_realms_realm_client_scopes_post(realm, client_scope_representation_client_scope_representation=client_scope_representation_client_scope_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientScopesApi->admin_realms_realm_client_scopes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_representation_client_scope_representation** | [**client_scope_representation.ClientScopeRepresentation**](ClientScopeRepresentation.md)|  | [optional]

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

# **admin_realms_realm_client_templates_client_scope_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_client_templates_client_scope_id_delete(realm, client_scope_id)

Delete the client scope

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
    api_instance = openapi_client.ClientScopesApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete the client scope
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_delete(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientScopesApi->admin_realms_realm_client_templates_client_scope_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |

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

# **admin_realms_realm_client_templates_client_scope_id_get**
> client_scope_representation.ClientScopeRepresentation admin_realms_realm_client_templates_client_scope_id_get(realm, client_scope_id)

Get representation of the client scope

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
    api_instance = openapi_client.ClientScopesApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get representation of the client scope
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_get(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientScopesApi->admin_realms_realm_client_templates_client_scope_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |

### Return type

[**client_scope_representation.ClientScopeRepresentation**](ClientScopeRepresentation.md)

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

# **admin_realms_realm_client_templates_client_scope_id_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_client_templates_client_scope_id_put(realm, client_scope_id)

Update the client scope

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
    api_instance = openapi_client.ClientScopesApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_id = 'client_scope_id_example' # str | 
    client_scope_representation_client_scope_representation = openapi_client.ClientScopeRepresentation() # client_scope_representation.ClientScopeRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the client scope
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_put(realm, client_scope_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientScopesApi->admin_realms_realm_client_templates_client_scope_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the client scope
        api_response = api_instance.admin_realms_realm_client_templates_client_scope_id_put(realm, client_scope_id, client_scope_representation_client_scope_representation=client_scope_representation_client_scope_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientScopesApi->admin_realms_realm_client_templates_client_scope_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_id** | **str**|  |
 **client_scope_representation_client_scope_representation** | [**client_scope_representation.ClientScopeRepresentation**](ClientScopeRepresentation.md)|  | [optional]

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

# **admin_realms_realm_client_templates_get**
> [client_scope_representation.ClientScopeRepresentation] admin_realms_realm_client_templates_get(realm)

Get client scopes belonging to the realm Returns a list of client scopes belonging to the realm

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
    api_instance = openapi_client.ClientScopesApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get client scopes belonging to the realm Returns a list of client scopes belonging to the realm
        api_response = api_instance.admin_realms_realm_client_templates_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientScopesApi->admin_realms_realm_client_templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

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

# **admin_realms_realm_client_templates_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_client_templates_post(realm)

Create a new client scope Client Scope’s name must be unique!

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
    api_instance = openapi_client.ClientScopesApi(api_client)
    realm = 'realm_example' # str | 
    client_scope_representation_client_scope_representation = openapi_client.ClientScopeRepresentation() # client_scope_representation.ClientScopeRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new client scope Client Scope’s name must be unique!
        api_response = api_instance.admin_realms_realm_client_templates_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientScopesApi->admin_realms_realm_client_templates_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new client scope Client Scope’s name must be unique!
        api_response = api_instance.admin_realms_realm_client_templates_post(realm, client_scope_representation_client_scope_representation=client_scope_representation_client_scope_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientScopesApi->admin_realms_realm_client_templates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_scope_representation_client_scope_representation** | [**client_scope_representation.ClientScopeRepresentation**](ClientScopeRepresentation.md)|  | [optional]

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

