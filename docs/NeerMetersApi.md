# openapi_client.NeerMetersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_meter**](NeerMetersApi.md#create_meter) | **PUT** /tenant/{tenant_id}/vendor/{vendor_id}/meter/new | Create a new meter
[**delete_meter**](NeerMetersApi.md#delete_meter) | **DELETE** /tenant/{tenant_id}/vendor/{vendor_id}/meter/{meter_id} | Delete a meter
[**export_meters**](NeerMetersApi.md#export_meters) | **POST** /tenant/{tenant_id}/vendor/{vendor_id}/meter/export | Export meters
[**get_meter**](NeerMetersApi.md#get_meter) | **GET** /tenant/{tenant_id}/vendor/{vendor_id}/meter/{meter_id} | Get a meter
[**import_meters**](NeerMetersApi.md#import_meters) | **POST** /tenant/{tenant_id}/vendor/{vendor_id}/meter/import | Import meters
[**list_meters**](NeerMetersApi.md#list_meters) | **GET** /tenant/{tenant_id}/vendor/{vendor_id}/meter/list/{page}/limit/{limit} | List meters
[**update_meter**](NeerMetersApi.md#update_meter) | **PATCH** /tenant/{tenant_id}/vendor/{vendor_id}/meter/{meter_id} | Update a meter


# **create_meter**
> meter_res_schema.MeterResSchema create_meter(tenant_id, vendor_id)

Create a new meter

Create a new meter using request body.

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
    api_instance = openapi_client.NeerMetersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    meter_req_schema_meter_req_schema = openapi_client.MeterReqSchema() # meter_req_schema.MeterReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new meter
        api_response = api_instance.create_meter(tenant_id, vendor_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerMetersApi->create_meter: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new meter
        api_response = api_instance.create_meter(tenant_id, vendor_id, meter_req_schema_meter_req_schema=meter_req_schema_meter_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerMetersApi->create_meter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **meter_req_schema_meter_req_schema** | [**meter_req_schema.MeterReqSchema**](MeterReqSchema.md)|  | [optional]

### Return type

[**meter_res_schema.MeterResSchema**](MeterResSchema.md)

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

# **delete_meter**
> meter_res_schema.MeterResSchema delete_meter(tenant_id, vendor_id, meter_id)

Delete a meter

Delete a meter using provided ID.

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
    api_instance = openapi_client.NeerMetersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    meter_id = 'meter_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete a meter
        api_response = api_instance.delete_meter(tenant_id, vendor_id, meter_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerMetersApi->delete_meter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **meter_id** | **str**|  |

### Return type

[**meter_res_schema.MeterResSchema**](MeterResSchema.md)

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

# **export_meters**
> meter_export_res_schema.MeterExportResSchema export_meters(tenant_id, vendor_id)

Export meters

Export meters using provided pagination parameters.

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
    api_instance = openapi_client.NeerMetersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    meter_export_req_schema_meter_export_req_schema = openapi_client.MeterExportReqSchema() # meter_export_req_schema.MeterExportReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export meters
        api_response = api_instance.export_meters(tenant_id, vendor_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerMetersApi->export_meters: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export meters
        api_response = api_instance.export_meters(tenant_id, vendor_id, meter_export_req_schema_meter_export_req_schema=meter_export_req_schema_meter_export_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerMetersApi->export_meters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **meter_export_req_schema_meter_export_req_schema** | [**meter_export_req_schema.MeterExportReqSchema**](MeterExportReqSchema.md)|  | [optional]

### Return type

[**meter_export_res_schema.MeterExportResSchema**](MeterExportResSchema.md)

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

# **get_meter**
> meter_res_schema.MeterResSchema get_meter(tenant_id, vendor_id, meter_id)

Get a meter

Get a meter using provided ID.

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
    api_instance = openapi_client.NeerMetersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    meter_id = 'meter_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get a meter
        api_response = api_instance.get_meter(tenant_id, vendor_id, meter_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerMetersApi->get_meter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **meter_id** | **str**|  |

### Return type

[**meter_res_schema.MeterResSchema**](MeterResSchema.md)

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

# **import_meters**
> meter_import_res_schema.MeterImportResSchema import_meters(tenant_id, vendor_id)

Import meters

Import meters using request body.

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
    api_instance = openapi_client.NeerMetersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    meter_import_req_schema_meter_import_req_schema = openapi_client.MeterImportReqSchema() # meter_import_req_schema.MeterImportReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import meters
        api_response = api_instance.import_meters(tenant_id, vendor_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerMetersApi->import_meters: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import meters
        api_response = api_instance.import_meters(tenant_id, vendor_id, meter_import_req_schema_meter_import_req_schema=meter_import_req_schema_meter_import_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerMetersApi->import_meters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **meter_import_req_schema_meter_import_req_schema** | [**meter_import_req_schema.MeterImportReqSchema**](MeterImportReqSchema.md)|  | [optional]

### Return type

[**meter_import_res_schema.MeterImportResSchema**](MeterImportResSchema.md)

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

# **list_meters**
> meter_list_res_schema.MeterListResSchema list_meters(tenant_id, vendor_id, page, limit)

List meters

List meters using provided pagination parameters.

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
    api_instance = openapi_client.NeerMetersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    page = 0 # int | 
    limit = 0 # int | 
    
    # example passing only required values which don't have defaults set
    try:
        # List meters
        api_response = api_instance.list_meters(tenant_id, vendor_id, page, limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerMetersApi->list_meters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **page** | **int**|  |
 **limit** | **int**|  |

### Return type

[**meter_list_res_schema.MeterListResSchema**](MeterListResSchema.md)

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

# **update_meter**
> meter_res_schema.MeterResSchema update_meter(tenant_id, vendor_id, meter_id)

Update a meter

Update a meter using provided ID and request body.

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
    api_instance = openapi_client.NeerMetersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    meter_id = 'meter_id_example' # str | 
    meter_req_schema_meter_req_schema = openapi_client.MeterReqSchema() # meter_req_schema.MeterReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a meter
        api_response = api_instance.update_meter(tenant_id, vendor_id, meter_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerMetersApi->update_meter: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a meter
        api_response = api_instance.update_meter(tenant_id, vendor_id, meter_id, meter_req_schema_meter_req_schema=meter_req_schema_meter_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerMetersApi->update_meter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **meter_id** | **str**|  |
 **meter_req_schema_meter_req_schema** | [**meter_req_schema.MeterReqSchema**](MeterReqSchema.md)|  | [optional]

### Return type

[**meter_res_schema.MeterResSchema**](MeterResSchema.md)

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

