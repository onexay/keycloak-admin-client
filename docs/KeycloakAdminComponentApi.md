# openapi_client.KeycloakAdminComponentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_realm_components_get**](KeycloakAdminComponentApi.md#admin_realms_realm_components_get) | **GET** /admin/realms/{realm}/components | /admin/realms/{realm}/components
[**admin_realms_realm_components_id_delete**](KeycloakAdminComponentApi.md#admin_realms_realm_components_id_delete) | **DELETE** /admin/realms/{realm}/components/{id} | /admin/realms/{realm}/components/{id}
[**admin_realms_realm_components_id_get**](KeycloakAdminComponentApi.md#admin_realms_realm_components_id_get) | **GET** /admin/realms/{realm}/components/{id} | /admin/realms/{realm}/components/{id}
[**admin_realms_realm_components_id_put**](KeycloakAdminComponentApi.md#admin_realms_realm_components_id_put) | **PUT** /admin/realms/{realm}/components/{id} | /admin/realms/{realm}/components/{id}
[**admin_realms_realm_components_id_sub_component_types_get**](KeycloakAdminComponentApi.md#admin_realms_realm_components_id_sub_component_types_get) | **GET** /admin/realms/{realm}/components/{id}/sub-component-types | List of subcomponent types that are available to configure for a particular parent component.
[**admin_realms_realm_components_post**](KeycloakAdminComponentApi.md#admin_realms_realm_components_post) | **POST** /admin/realms/{realm}/components | /admin/realms/{realm}/components


# **admin_realms_realm_components_get**
> [component_representation.ComponentRepresentation] admin_realms_realm_components_get(realm)

/admin/realms/{realm}/components

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
    api_instance = openapi_client.KeycloakAdminComponentApi(api_client)
    realm = 'realm_example' # str | 
    name = 'name_example' # str |  (optional)
parent = 'parent_example' # str |  (optional)
type = 'type_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/components
        api_response = api_instance.admin_realms_realm_components_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminComponentApi->admin_realms_realm_components_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /admin/realms/{realm}/components
        api_response = api_instance.admin_realms_realm_components_get(realm, name=name, parent=parent, type=type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminComponentApi->admin_realms_realm_components_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **name** | **str**|  | [optional]
 **parent** | **str**|  | [optional]
 **type** | **str**|  | [optional]

### Return type

[**[component_representation.ComponentRepresentation]**](ComponentRepresentation.md)

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

# **admin_realms_realm_components_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_components_id_delete(id, realm)

/admin/realms/{realm}/components/{id}

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
    api_instance = openapi_client.KeycloakAdminComponentApi(api_client)
    id = 'id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/components/{id}
        api_response = api_instance.admin_realms_realm_components_id_delete(id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminComponentApi->admin_realms_realm_components_id_delete: %s\n" % e)
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

# **admin_realms_realm_components_id_get**
> component_representation.ComponentRepresentation admin_realms_realm_components_id_get(id, realm)

/admin/realms/{realm}/components/{id}

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
    api_instance = openapi_client.KeycloakAdminComponentApi(api_client)
    id = 'id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/components/{id}
        api_response = api_instance.admin_realms_realm_components_id_get(id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminComponentApi->admin_realms_realm_components_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **realm** | **str**|  |

### Return type

[**component_representation.ComponentRepresentation**](ComponentRepresentation.md)

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

# **admin_realms_realm_components_id_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_components_id_put(id, realm)

/admin/realms/{realm}/components/{id}

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
    api_instance = openapi_client.KeycloakAdminComponentApi(api_client)
    id = 'id_example' # str | 
    realm = 'realm_example' # str | 
    component_representation_component_representation = openapi_client.ComponentRepresentation() # component_representation.ComponentRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/components/{id}
        api_response = api_instance.admin_realms_realm_components_id_put(id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminComponentApi->admin_realms_realm_components_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /admin/realms/{realm}/components/{id}
        api_response = api_instance.admin_realms_realm_components_id_put(id, realm, component_representation_component_representation=component_representation_component_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminComponentApi->admin_realms_realm_components_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **realm** | **str**|  |
 **component_representation_component_representation** | [**component_representation.ComponentRepresentation**](ComponentRepresentation.md)|  | [optional]

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

# **admin_realms_realm_components_id_sub_component_types_get**
> [component_type_representation.ComponentTypeRepresentation] admin_realms_realm_components_id_sub_component_types_get(id, realm)

List of subcomponent types that are available to configure for a particular parent component.

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
    api_instance = openapi_client.KeycloakAdminComponentApi(api_client)
    id = 'id_example' # str | 
    realm = 'realm_example' # str | 
    type = 'type_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List of subcomponent types that are available to configure for a particular parent component.
        api_response = api_instance.admin_realms_realm_components_id_sub_component_types_get(id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminComponentApi->admin_realms_realm_components_id_sub_component_types_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List of subcomponent types that are available to configure for a particular parent component.
        api_response = api_instance.admin_realms_realm_components_id_sub_component_types_get(id, realm, type=type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminComponentApi->admin_realms_realm_components_id_sub_component_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **realm** | **str**|  |
 **type** | **str**|  | [optional]

### Return type

[**[component_type_representation.ComponentTypeRepresentation]**](ComponentTypeRepresentation.md)

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

# **admin_realms_realm_components_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_components_post(realm)

/admin/realms/{realm}/components

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
    api_instance = openapi_client.KeycloakAdminComponentApi(api_client)
    realm = 'realm_example' # str | 
    component_representation_component_representation = openapi_client.ComponentRepresentation() # component_representation.ComponentRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/components
        api_response = api_instance.admin_realms_realm_components_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminComponentApi->admin_realms_realm_components_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /admin/realms/{realm}/components
        api_response = api_instance.admin_realms_realm_components_post(realm, component_representation_component_representation=component_representation_component_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminComponentApi->admin_realms_realm_components_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **component_representation_component_representation** | [**component_representation.ComponentRepresentation**](ComponentRepresentation.md)|  | [optional]

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

