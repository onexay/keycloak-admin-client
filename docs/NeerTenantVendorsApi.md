# openapi_client.NeerTenantVendorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_vendor_to_tenant**](NeerTenantVendorsApi.md#add_vendor_to_tenant) | **PUT** /tenant/{tenant_id}/vendor/{vendor_id} | Add vendor to tenant
[**delete_vendor_from_tenant**](NeerTenantVendorsApi.md#delete_vendor_from_tenant) | **DELETE** /tenant/{tenant_id}/vendor/{vendor_id} | Delete vendor from tenant
[**get_vendor_count_from_tenant**](NeerTenantVendorsApi.md#get_vendor_count_from_tenant) | **GET** /tenant/{tenant_id}/vendor/stats/count | Get vendor count from tenant
[**get_vendor_from_tenant**](NeerTenantVendorsApi.md#get_vendor_from_tenant) | **GET** /tenant/{tenant_id}/vendor/{vendor_id} | Get vendor from tenant
[**list_vendors_from_tenant**](NeerTenantVendorsApi.md#list_vendors_from_tenant) | **GET** /tenant/{tenant_id}/vendor/list/{page}/limit/{limit} | List vendors from tenant
[**update_vendor_from_tenant**](NeerTenantVendorsApi.md#update_vendor_from_tenant) | **PATCH** /tenant/{tenant_id}/vendor/{vendor_id} | Update vendor from tenant


# **add_vendor_to_tenant**
> tenant_vendors_res_schema.TenantVendorsResSchema add_vendor_to_tenant(tenant_id, vendor_id)

Add vendor to tenant

Add vendor to tenant using provided ID and request body.

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
    api_instance = openapi_client.NeerTenantVendorsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    tenant_vendors_req_schema_tenant_vendors_req_schema = openapi_client.TenantVendorsReqSchema() # tenant_vendors_req_schema.TenantVendorsReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add vendor to tenant
        api_response = api_instance.add_vendor_to_tenant(tenant_id, vendor_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerTenantVendorsApi->add_vendor_to_tenant: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add vendor to tenant
        api_response = api_instance.add_vendor_to_tenant(tenant_id, vendor_id, tenant_vendors_req_schema_tenant_vendors_req_schema=tenant_vendors_req_schema_tenant_vendors_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerTenantVendorsApi->add_vendor_to_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **tenant_vendors_req_schema_tenant_vendors_req_schema** | [**tenant_vendors_req_schema.TenantVendorsReqSchema**](TenantVendorsReqSchema.md)|  | [optional]

### Return type

[**tenant_vendors_res_schema.TenantVendorsResSchema**](TenantVendorsResSchema.md)

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

# **delete_vendor_from_tenant**
> tenant_vendors_res_schema.TenantVendorsResSchema delete_vendor_from_tenant(tenant_id, vendor_id, user_id)

Delete vendor from tenant

Delete vendor from tenant using provided ID.

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
    api_instance = openapi_client.NeerTenantVendorsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete vendor from tenant
        api_response = api_instance.delete_vendor_from_tenant(tenant_id, vendor_id, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerTenantVendorsApi->delete_vendor_from_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **user_id** | **str**|  |

### Return type

[**tenant_vendors_res_schema.TenantVendorsResSchema**](TenantVendorsResSchema.md)

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

# **get_vendor_count_from_tenant**
> tenant_vendors_count_res_schema.TenantVendorsCountResSchema get_vendor_count_from_tenant(tenant_id)

Get vendor count from tenant

Get vendor count from tenant using provided ID.

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
    api_instance = openapi_client.NeerTenantVendorsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get vendor count from tenant
        api_response = api_instance.get_vendor_count_from_tenant(tenant_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerTenantVendorsApi->get_vendor_count_from_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |

### Return type

[**tenant_vendors_count_res_schema.TenantVendorsCountResSchema**](TenantVendorsCountResSchema.md)

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

# **get_vendor_from_tenant**
> tenant_vendors_ext_res_schema.TenantVendorsExtResSchema get_vendor_from_tenant(tenant_id, vendor_id)

Get vendor from tenant

Get vendor from tenant using provided ID.

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
    api_instance = openapi_client.NeerTenantVendorsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get vendor from tenant
        api_response = api_instance.get_vendor_from_tenant(tenant_id, vendor_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerTenantVendorsApi->get_vendor_from_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |

### Return type

[**tenant_vendors_ext_res_schema.TenantVendorsExtResSchema**](TenantVendorsExtResSchema.md)

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

# **list_vendors_from_tenant**
> tenant_vendors_list_res_schema.TenantVendorsListResSchema list_vendors_from_tenant(tenant_id, page, limit)

List vendors from tenant

List vendors from tenant using provided ID.

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
    api_instance = openapi_client.NeerTenantVendorsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    page = 0 # int | 
    limit = 0 # int | 
    
    # example passing only required values which don't have defaults set
    try:
        # List vendors from tenant
        api_response = api_instance.list_vendors_from_tenant(tenant_id, page, limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerTenantVendorsApi->list_vendors_from_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **page** | **int**|  |
 **limit** | **int**|  |

### Return type

[**tenant_vendors_list_res_schema.TenantVendorsListResSchema**](TenantVendorsListResSchema.md)

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

# **update_vendor_from_tenant**
> tenant_vendors_res_schema.TenantVendorsResSchema update_vendor_from_tenant(tenant_id, vendor_id)

Update vendor from tenant

Update vendor from tenant using provided ID and request body.

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
    api_instance = openapi_client.NeerTenantVendorsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    tenant_vendors_req_schema_tenant_vendors_req_schema = openapi_client.TenantVendorsReqSchema() # tenant_vendors_req_schema.TenantVendorsReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update vendor from tenant
        api_response = api_instance.update_vendor_from_tenant(tenant_id, vendor_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerTenantVendorsApi->update_vendor_from_tenant: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update vendor from tenant
        api_response = api_instance.update_vendor_from_tenant(tenant_id, vendor_id, tenant_vendors_req_schema_tenant_vendors_req_schema=tenant_vendors_req_schema_tenant_vendors_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerTenantVendorsApi->update_vendor_from_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **tenant_vendors_req_schema_tenant_vendors_req_schema** | [**tenant_vendors_req_schema.TenantVendorsReqSchema**](TenantVendorsReqSchema.md)|  | [optional]

### Return type

[**tenant_vendors_res_schema.TenantVendorsResSchema**](TenantVendorsResSchema.md)

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

