# openapi_client.ReadingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reading**](ReadingsApi.md#create_reading) | **PUT** /tenant/{tenant_id}/vendor/{vendor_id}/meter/{meter_id}/user/{user_id}/reading/new | Create a reading
[**delete_reading**](ReadingsApi.md#delete_reading) | **DELETE** /tenant/{tenant_id}/vendor/{vendor_id}/meter/{meter_id}/user/{user_id}/reading/{reading_id} | Delete a meter reading
[**export_readings**](ReadingsApi.md#export_readings) | **POST** /tenant/{tenant_id}/vendor/{vendor_id}/meter/{meter_id}/user/{user_id}/reading/export | Export meter readings
[**get_reading**](ReadingsApi.md#get_reading) | **GET** /tenant/{tenant_id}/vendor/{vendor_id}/meter/{meter_id}/user/{user_id}/reading/{reading_id} | Get a meter reading
[**import_readings**](ReadingsApi.md#import_readings) | **POST** /tenant/{tenant_id}/vendor/{vendor_id}/meter/{meter_id}/user/{user_id}/reading/import | Import meter readings
[**list_readings**](ReadingsApi.md#list_readings) | **GET** /tenant/{tenant_id}/vendor/{vendor_id}/meter/{meter_id}/user/{user_id}/reading/list/{page}/limit/{limit} | List meter readings
[**update_reading**](ReadingsApi.md#update_reading) | **PATCH** /tenant/{tenant_id}/vendor/{vendor_id}/meter/{meter_id}/user/{user_id}/reading/{reading_id} | Update a meter reading


# **create_reading**
> reading_res_schema.ReadingResSchema create_reading(tenant_id, vendor_id, meter_id, user_id)

Create a reading

Create a new meter reading using provided tenant ID, vendor ID, meter ID, user ID and request body.

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
    api_instance = openapi_client.ReadingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    meter_id = 'meter_id_example' # str | 
    user_id = 'user_id_example' # str | 
    reading_req_schema_reading_req_schema = openapi_client.ReadingReqSchema() # reading_req_schema.ReadingReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a reading
        api_response = api_instance.create_reading(tenant_id, vendor_id, meter_id, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReadingsApi->create_reading: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a reading
        api_response = api_instance.create_reading(tenant_id, vendor_id, meter_id, user_id, reading_req_schema_reading_req_schema=reading_req_schema_reading_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReadingsApi->create_reading: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **meter_id** | **str**|  |
 **user_id** | **str**|  |
 **reading_req_schema_reading_req_schema** | [**reading_req_schema.ReadingReqSchema**](ReadingReqSchema.md)|  | [optional]

### Return type

[**reading_res_schema.ReadingResSchema**](ReadingResSchema.md)

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

# **delete_reading**
> reading_res_schema.ReadingResSchema delete_reading(tenant_id, vendor_id, meter_id, user_id, reading_id)

Delete a meter reading

Delete a meter reading using provided tenant ID, vendor ID, meter ID, user ID and reading ID.

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
    api_instance = openapi_client.ReadingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    meter_id = 'meter_id_example' # str | 
    user_id = 'user_id_example' # str | 
    reading_id = 'reading_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete a meter reading
        api_response = api_instance.delete_reading(tenant_id, vendor_id, meter_id, user_id, reading_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReadingsApi->delete_reading: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **meter_id** | **str**|  |
 **user_id** | **str**|  |
 **reading_id** | **str**|  |

### Return type

[**reading_res_schema.ReadingResSchema**](ReadingResSchema.md)

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

# **export_readings**
> reading_export_res_schema.ReadingExportResSchema export_readings(tenant_id, vendor_id, meter_id, user_id)

Export meter readings

Export meter readings using provided tenant ID, vendor ID, meter ID, user ID and pagination parameters.

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
    api_instance = openapi_client.ReadingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    meter_id = 'meter_id_example' # str | 
    user_id = 'user_id_example' # str | 
    reading_export_req_schema_reading_export_req_schema = openapi_client.ReadingExportReqSchema() # reading_export_req_schema.ReadingExportReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export meter readings
        api_response = api_instance.export_readings(tenant_id, vendor_id, meter_id, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReadingsApi->export_readings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export meter readings
        api_response = api_instance.export_readings(tenant_id, vendor_id, meter_id, user_id, reading_export_req_schema_reading_export_req_schema=reading_export_req_schema_reading_export_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReadingsApi->export_readings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **meter_id** | **str**|  |
 **user_id** | **str**|  |
 **reading_export_req_schema_reading_export_req_schema** | [**reading_export_req_schema.ReadingExportReqSchema**](ReadingExportReqSchema.md)|  | [optional]

### Return type

[**reading_export_res_schema.ReadingExportResSchema**](ReadingExportResSchema.md)

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

# **get_reading**
> reading_res_schema.ReadingResSchema get_reading(tenant_id, vendor_id, meter_id, user_id, reading_id)

Get a meter reading

Get a meter reading using provided tenant ID, vendor ID, meter ID, user ID and reading ID.

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
    api_instance = openapi_client.ReadingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    meter_id = 'meter_id_example' # str | 
    user_id = 'user_id_example' # str | 
    reading_id = 'reading_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get a meter reading
        api_response = api_instance.get_reading(tenant_id, vendor_id, meter_id, user_id, reading_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReadingsApi->get_reading: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **meter_id** | **str**|  |
 **user_id** | **str**|  |
 **reading_id** | **str**|  |

### Return type

[**reading_res_schema.ReadingResSchema**](ReadingResSchema.md)

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

# **import_readings**
> reading_import_res_schema.ReadingImportResSchema import_readings(tenant_id, vendor_id, meter_id, user_id)

Import meter readings

Import meter readings using provided tenant ID, vendor ID, meter ID, user ID and reading data.

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
    api_instance = openapi_client.ReadingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    meter_id = 'meter_id_example' # str | 
    user_id = 'user_id_example' # str | 
    reading_import_req_schema_reading_import_req_schema = openapi_client.ReadingImportReqSchema() # reading_import_req_schema.ReadingImportReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import meter readings
        api_response = api_instance.import_readings(tenant_id, vendor_id, meter_id, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReadingsApi->import_readings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import meter readings
        api_response = api_instance.import_readings(tenant_id, vendor_id, meter_id, user_id, reading_import_req_schema_reading_import_req_schema=reading_import_req_schema_reading_import_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReadingsApi->import_readings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **meter_id** | **str**|  |
 **user_id** | **str**|  |
 **reading_import_req_schema_reading_import_req_schema** | [**reading_import_req_schema.ReadingImportReqSchema**](ReadingImportReqSchema.md)|  | [optional]

### Return type

[**reading_import_res_schema.ReadingImportResSchema**](ReadingImportResSchema.md)

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

# **list_readings**
> str list_readings(tenant_id, vendor_id, meter_id, user_id, page, limit)

List meter readings

List meter readings using provided tenant ID, vendor ID, meter ID, user ID and pagination parameters.

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
    api_instance = openapi_client.ReadingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    meter_id = 'meter_id_example' # str | 
    user_id = 'user_id_example' # str | 
    page = 0 # int | 
    limit = 0 # int | 
    
    # example passing only required values which don't have defaults set
    try:
        # List meter readings
        api_response = api_instance.list_readings(tenant_id, vendor_id, meter_id, user_id, page, limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReadingsApi->list_readings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **meter_id** | **str**|  |
 **user_id** | **str**|  |
 **page** | **int**|  |
 **limit** | **int**|  |

### Return type

**str**

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

# **update_reading**
> reading_res_schema.ReadingResSchema update_reading(tenant_id, vendor_id, meter_id, user_id, reading_id)

Update a meter reading

Update a meter reading using provided tenant ID, vendor ID, meter ID, user ID and reading ID.

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
    api_instance = openapi_client.ReadingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    vendor_id = 'vendor_id_example' # str | 
    meter_id = 'meter_id_example' # str | 
    user_id = 'user_id_example' # str | 
    reading_id = 'reading_id_example' # str | 
    reading_req_schema_reading_req_schema = openapi_client.ReadingReqSchema() # reading_req_schema.ReadingReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a meter reading
        api_response = api_instance.update_reading(tenant_id, vendor_id, meter_id, user_id, reading_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReadingsApi->update_reading: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a meter reading
        api_response = api_instance.update_reading(tenant_id, vendor_id, meter_id, user_id, reading_id, reading_req_schema_reading_req_schema=reading_req_schema_reading_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReadingsApi->update_reading: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **vendor_id** | **str**|  |
 **meter_id** | **str**|  |
 **user_id** | **str**|  |
 **reading_id** | **str**|  |
 **reading_req_schema_reading_req_schema** | [**reading_req_schema.ReadingReqSchema**](ReadingReqSchema.md)|  | [optional]

### Return type

[**reading_res_schema.ReadingResSchema**](ReadingResSchema.md)

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

