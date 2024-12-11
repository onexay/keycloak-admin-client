# openapi_client.TenantUsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_to_tenant**](TenantUsersApi.md#add_user_to_tenant) | **PUT** /tenant/{tenant_id}/user/{user_id} | Add user to tenant
[**delete_user_from_tenant**](TenantUsersApi.md#delete_user_from_tenant) | **DELETE** /tenant/{tenant_id}/user/{user_id} | Delete user from tenant
[**get_user_count_from_tenant**](TenantUsersApi.md#get_user_count_from_tenant) | **GET** /tenant/{tenant_id}/user/stats/count | Get user count from tenant
[**get_user_from_tenant**](TenantUsersApi.md#get_user_from_tenant) | **GET** /tenant/{tenant_id}/user/{user_id} | Get user from tenant
[**list_users_from_tenant**](TenantUsersApi.md#list_users_from_tenant) | **GET** /tenant/{tenant_id}/user/list/{page}/limit/{limit} | List users from tenant
[**update_user_from_tenant**](TenantUsersApi.md#update_user_from_tenant) | **PATCH** /tenant/{tenant_id}/user/{user_id} | Update user from tenant


# **add_user_to_tenant**
> tenant_users_res_schema.TenantUsersResSchema add_user_to_tenant(tenant_id, user_id)

Add user to tenant

Add user to tenant using provided ID and request body.

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
    api_instance = openapi_client.TenantUsersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    user_id = 'user_id_example' # str | 
    tenant_users_req_schema_tenant_users_req_schema = openapi_client.TenantUsersReqSchema() # tenant_users_req_schema.TenantUsersReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add user to tenant
        api_response = api_instance.add_user_to_tenant(tenant_id, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantUsersApi->add_user_to_tenant: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add user to tenant
        api_response = api_instance.add_user_to_tenant(tenant_id, user_id, tenant_users_req_schema_tenant_users_req_schema=tenant_users_req_schema_tenant_users_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantUsersApi->add_user_to_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **user_id** | **str**|  |
 **tenant_users_req_schema_tenant_users_req_schema** | [**tenant_users_req_schema.TenantUsersReqSchema**](TenantUsersReqSchema.md)|  | [optional]

### Return type

[**tenant_users_res_schema.TenantUsersResSchema**](TenantUsersResSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_from_tenant**
> tenant_res_schema.TenantResSchema delete_user_from_tenant(tenant_id, user_id)

Delete user from tenant

Delete user from tenant using provided ID.

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
    api_instance = openapi_client.TenantUsersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete user from tenant
        api_response = api_instance.delete_user_from_tenant(tenant_id, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantUsersApi->delete_user_from_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **user_id** | **str**|  |

### Return type

[**tenant_res_schema.TenantResSchema**](TenantResSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_count_from_tenant**
> tenant_users_count_res_schema.TenantUsersCountResSchema get_user_count_from_tenant(tenant_id)

Get user count from tenant

Get user count from tenant using provided ID.

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
    api_instance = openapi_client.TenantUsersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get user count from tenant
        api_response = api_instance.get_user_count_from_tenant(tenant_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantUsersApi->get_user_count_from_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |

### Return type

[**tenant_users_count_res_schema.TenantUsersCountResSchema**](TenantUsersCountResSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_from_tenant**
> tenant_users_ext_res_schema.TenantUsersExtResSchema get_user_from_tenant(tenant_id, user_id)

Get user from tenant

Get user from tenant using provided ID.

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
    api_instance = openapi_client.TenantUsersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get user from tenant
        api_response = api_instance.get_user_from_tenant(tenant_id, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantUsersApi->get_user_from_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **user_id** | **str**|  |

### Return type

[**tenant_users_ext_res_schema.TenantUsersExtResSchema**](TenantUsersExtResSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users_from_tenant**
> tenant_users_list_res_schema.TenantUsersListResSchema list_users_from_tenant(tenant_id, page, limit)

List users from tenant

List users from tenant using provided ID.

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
    api_instance = openapi_client.TenantUsersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    page = 0 # int | 
    limit = 0 # int | 
    
    # example passing only required values which don't have defaults set
    try:
        # List users from tenant
        api_response = api_instance.list_users_from_tenant(tenant_id, page, limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantUsersApi->list_users_from_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **page** | **int**|  |
 **limit** | **int**|  |

### Return type

[**tenant_users_list_res_schema.TenantUsersListResSchema**](TenantUsersListResSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_from_tenant**
> tenant_res_schema.TenantResSchema update_user_from_tenant(tenant_id, user_id)

Update user from tenant

Update user from tenant using provided ID and request body.

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
    api_instance = openapi_client.TenantUsersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    user_id = 'user_id_example' # str | 
    body = None # bool, date, datetime, dict, float, int, list, str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update user from tenant
        api_response = api_instance.update_user_from_tenant(tenant_id, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantUsersApi->update_user_from_tenant: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update user from tenant
        api_response = api_instance.update_user_from_tenant(tenant_id, user_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantUsersApi->update_user_from_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **user_id** | **str**|  |
 **body** | **bool, date, datetime, dict, float, int, list, str**|  | [optional]

### Return type

[**tenant_res_schema.TenantResSchema**](TenantResSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

