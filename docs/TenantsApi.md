# openapi_client.TenantsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_tenants**](TenantsApi.md#count_tenants) | **GET** /tenant/stats/count | Count tenants
[**create_tenant**](TenantsApi.md#create_tenant) | **PUT** /tenant/new | Create a new tenant
[**delete_tenant**](TenantsApi.md#delete_tenant) | **DELETE** /tenant/{tenant_id} | Delete a tenant
[**export_tenants**](TenantsApi.md#export_tenants) | **POST** /tenant/export | Export tenants
[**get_tenant**](TenantsApi.md#get_tenant) | **GET** /tenant/{tenant_id} | Get a tenant
[**import_tenants**](TenantsApi.md#import_tenants) | **POST** /tenant/import | Import tenants
[**list_tenants**](TenantsApi.md#list_tenants) | **GET** /tenant/list/{page}/limit/{limit} | List tenants
[**update_tenant**](TenantsApi.md#update_tenant) | **PATCH** /tenant/{tenant_id} | Update a tenant


# **count_tenants**
> tenant_stats_count_res_schema.TenantStatsCountResSchema count_tenants()

Count tenants

Count tenants.

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
    api_instance = openapi_client.TenantsApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Count tenants
        api_response = api_instance.count_tenants()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantsApi->count_tenants: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**tenant_stats_count_res_schema.TenantStatsCountResSchema**](TenantStatsCountResSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tenant**
> tenant_res_schema.TenantResSchema create_tenant()

Create a new tenant

Create a new tenant using request body.

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
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_req_schema_tenant_req_schema = openapi_client.TenantReqSchema() # tenant_req_schema.TenantReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new tenant
        api_response = api_instance.create_tenant(tenant_req_schema_tenant_req_schema=tenant_req_schema_tenant_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantsApi->create_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_req_schema_tenant_req_schema** | [**tenant_req_schema.TenantReqSchema**](TenantReqSchema.md)|  | [optional]

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

# **delete_tenant**
> tenant_res_schema.TenantResSchema delete_tenant(tenant_id)

Delete a tenant

Delete a tenant using provided ID.

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
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete a tenant
        api_response = api_instance.delete_tenant(tenant_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantsApi->delete_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |

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

# **export_tenants**
> tenant_export_res_schema.TenantExportResSchema export_tenants()

Export tenants

Export tenants using provided pagination parameters.

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
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_export_req_schema_tenant_export_req_schema = openapi_client.TenantExportReqSchema() # tenant_export_req_schema.TenantExportReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export tenants
        api_response = api_instance.export_tenants(tenant_export_req_schema_tenant_export_req_schema=tenant_export_req_schema_tenant_export_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantsApi->export_tenants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_export_req_schema_tenant_export_req_schema** | [**tenant_export_req_schema.TenantExportReqSchema**](TenantExportReqSchema.md)|  | [optional]

### Return type

[**tenant_export_res_schema.TenantExportResSchema**](TenantExportResSchema.md)

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

# **get_tenant**
> tenant_res_schema.TenantResSchema get_tenant(tenant_id)

Get a tenant

Get a tenant using provided ID.

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
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get a tenant
        api_response = api_instance.get_tenant(tenant_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantsApi->get_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |

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

# **import_tenants**
> tenant_import_res_schema.TenantImportResSchema import_tenants()

Import tenants

Import tenants using request body.

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
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_import_req_schema_tenant_import_req_schema = openapi_client.TenantImportReqSchema() # tenant_import_req_schema.TenantImportReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import tenants
        api_response = api_instance.import_tenants(tenant_import_req_schema_tenant_import_req_schema=tenant_import_req_schema_tenant_import_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantsApi->import_tenants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_import_req_schema_tenant_import_req_schema** | [**tenant_import_req_schema.TenantImportReqSchema**](TenantImportReqSchema.md)|  | [optional]

### Return type

[**tenant_import_res_schema.TenantImportResSchema**](TenantImportResSchema.md)

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

# **list_tenants**
> tenant_list_res_schema.TenantListResSchema list_tenants(page, limit)

List tenants

List tenants using provided pagination parameters.

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
    api_instance = openapi_client.TenantsApi(api_client)
    page = 0 # int | 
    limit = 0 # int | 
    
    # example passing only required values which don't have defaults set
    try:
        # List tenants
        api_response = api_instance.list_tenants(page, limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantsApi->list_tenants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **limit** | **int**|  |

### Return type

[**tenant_list_res_schema.TenantListResSchema**](TenantListResSchema.md)

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

# **update_tenant**
> tenant_res_schema.TenantResSchema update_tenant(tenant_id)

Update a tenant

Update a tenant using provided ID and request body.

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
    api_instance = openapi_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_req_schema_tenant_req_schema = openapi_client.TenantReqSchema() # tenant_req_schema.TenantReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a tenant
        api_response = api_instance.update_tenant(tenant_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantsApi->update_tenant: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a tenant
        api_response = api_instance.update_tenant(tenant_id, tenant_req_schema_tenant_req_schema=tenant_req_schema_tenant_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TenantsApi->update_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **tenant_req_schema_tenant_req_schema** | [**tenant_req_schema.TenantReqSchema**](TenantReqSchema.md)|  | [optional]

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

