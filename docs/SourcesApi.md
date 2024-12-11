# openapi_client.SourcesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_source**](SourcesApi.md#create_source) | **PUT** /tenant/{tenant_id}/vendor/{vendor_id}/source/new | Create a new source
[**delete_source**](SourcesApi.md#delete_source) | **DELETE** /tenant/{tenant_id}/vendor/{vendor_id}/source/{source_id} | Delete source
[**export_sources**](SourcesApi.md#export_sources) | **POST** /tenant/{tenant_id}/vendor/{vendor_id}/source/export | Export sources
[**get_source**](SourcesApi.md#get_source) | **GET** /tenant/{tenant_id}/vendor/{vendor_id}/source/{source_id} | Get source
[**import_sources**](SourcesApi.md#import_sources) | **POST** /tenant/{tenant_id}/vendor/{vendor_id}/source/import | Import sources
[**list_sources**](SourcesApi.md#list_sources) | **GET** /tenant/{tenant_id}/vendor/{vendor_id}/source/list/{page}/limit/{limit} | List sources
[**update_source**](SourcesApi.md#update_source) | **PATCH** /tenant/{tenant_id}/vendor/{vendor_id}/source/{source_id} | Update source


# **create_source**
> source_res_schema.SourceResSchema create_source(tenant_id, vendor_id)

Create a new source

Create a new source

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
    api_instance = openapi_client.SourcesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    source_req_schema_source_req_schema = openapi_client.SourceReqSchema() # source_req_schema.SourceReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new source
        api_response = api_instance.create_source(tenant_id, vendor_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SourcesApi->create_source: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new source
        api_response = api_instance.create_source(tenant_id, vendor_id, source_req_schema_source_req_schema=source_req_schema_source_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SourcesApi->create_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **source_req_schema_source_req_schema** | [**source_req_schema.SourceReqSchema**](SourceReqSchema.md)|  | [optional]

### Return type

[**source_res_schema.SourceResSchema**](SourceResSchema.md)

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

# **delete_source**
> any_of_source_res_schemanull.AnyOfSourceResSchemanull delete_source(tenant_id, vendor_id, source_id)

Delete source

Delete source

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
    api_instance = openapi_client.SourcesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    source_id = 'source_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete source
        api_response = api_instance.delete_source(tenant_id, vendor_id, source_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SourcesApi->delete_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **source_id** | **str**|  |

### Return type

[**any_of_source_res_schemanull.AnyOfSourceResSchemanull**](AnyOfSourceResSchemanull.md)

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

# **export_sources**
> source_export_res_schema.SourceExportResSchema export_sources(tenant_id, vendor_id)

Export sources

Export sources using provided pagination parameters.

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
    api_instance = openapi_client.SourcesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    source_export_req_schema_source_export_req_schema = openapi_client.SourceExportReqSchema() # source_export_req_schema.SourceExportReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export sources
        api_response = api_instance.export_sources(tenant_id, vendor_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SourcesApi->export_sources: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export sources
        api_response = api_instance.export_sources(tenant_id, vendor_id, source_export_req_schema_source_export_req_schema=source_export_req_schema_source_export_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SourcesApi->export_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **source_export_req_schema_source_export_req_schema** | [**source_export_req_schema.SourceExportReqSchema**](SourceExportReqSchema.md)|  | [optional]

### Return type

[**source_export_res_schema.SourceExportResSchema**](SourceExportResSchema.md)

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

# **get_source**
> any_of_source_res_schemanull.AnyOfSourceResSchemanull get_source(tenant_id, vendor_id, source_id)

Get source

Get source

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
    api_instance = openapi_client.SourcesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    source_id = 'source_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get source
        api_response = api_instance.get_source(tenant_id, vendor_id, source_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SourcesApi->get_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **source_id** | **str**|  |

### Return type

[**any_of_source_res_schemanull.AnyOfSourceResSchemanull**](AnyOfSourceResSchemanull.md)

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

# **import_sources**
> source_import_res_schema.SourceImportResSchema import_sources(tenant_id, vendor_id)

Import sources

Import sources using request body.

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
    api_instance = openapi_client.SourcesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    source_import_req_schema_source_import_req_schema = openapi_client.SourceImportReqSchema() # source_import_req_schema.SourceImportReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import sources
        api_response = api_instance.import_sources(tenant_id, vendor_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SourcesApi->import_sources: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import sources
        api_response = api_instance.import_sources(tenant_id, vendor_id, source_import_req_schema_source_import_req_schema=source_import_req_schema_source_import_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SourcesApi->import_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **source_import_req_schema_source_import_req_schema** | [**source_import_req_schema.SourceImportReqSchema**](SourceImportReqSchema.md)|  | [optional]

### Return type

[**source_import_res_schema.SourceImportResSchema**](SourceImportResSchema.md)

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

# **list_sources**
> source_list_res_schema.SourceListResSchema list_sources(tenant_id, vendor_id, page, limit)

List sources

List sources using provided pagination parameters.

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
    api_instance = openapi_client.SourcesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    page = 0 # int | 
    limit = 0 # int | 
    
    # example passing only required values which don't have defaults set
    try:
        # List sources
        api_response = api_instance.list_sources(tenant_id, vendor_id, page, limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SourcesApi->list_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **page** | **int**|  |
 **limit** | **int**|  |

### Return type

[**source_list_res_schema.SourceListResSchema**](SourceListResSchema.md)

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

# **update_source**
> source_res_schema.SourceResSchema update_source(tenant_id, vendor_id, source_id)

Update source

Update source

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
    api_instance = openapi_client.SourcesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    source_id = 'source_id_example' # str | 
    source_req_schema_source_req_schema = openapi_client.SourceReqSchema() # source_req_schema.SourceReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update source
        api_response = api_instance.update_source(tenant_id, vendor_id, source_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SourcesApi->update_source: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update source
        api_response = api_instance.update_source(tenant_id, vendor_id, source_id, source_req_schema_source_req_schema=source_req_schema_source_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SourcesApi->update_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **source_id** | **str**|  |
 **source_req_schema_source_req_schema** | [**source_req_schema.SourceReqSchema**](SourceReqSchema.md)|  | [optional]

### Return type

[**source_res_schema.SourceResSchema**](SourceResSchema.md)

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

