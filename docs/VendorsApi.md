# openapi_client.VendorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_vendors**](VendorsApi.md#count_vendors) | **GET** /vendor/stats/count | Count vendors
[**create_vendor**](VendorsApi.md#create_vendor) | **PUT** /vendor/new | Create a new vendor
[**delete_vendor**](VendorsApi.md#delete_vendor) | **DELETE** /vendor/{vendor_id} | Delete a vendor
[**export_vendors**](VendorsApi.md#export_vendors) | **POST** /vendor/export | Export vendors
[**get_vendor**](VendorsApi.md#get_vendor) | **GET** /vendor/{vendor_id} | Get a vendor
[**import_vendors**](VendorsApi.md#import_vendors) | **POST** /vendor/import | Import vendors
[**list_vendors**](VendorsApi.md#list_vendors) | **GET** /vendor/list/{page}/limit/{limit} | List vendors
[**update_vendor**](VendorsApi.md#update_vendor) | **PATCH** /vendor/{vendor_id} | Update a vendor


# **count_vendors**
> vendor_count_res_schema.VendorCountResSchema count_vendors()

Count vendors

Count the number of vendors.

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
    api_instance = openapi_client.VendorsApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Count vendors
        api_response = api_instance.count_vendors()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VendorsApi->count_vendors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**vendor_count_res_schema.VendorCountResSchema**](VendorCountResSchema.md)

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

# **create_vendor**
> vendor_res_schema.VendorResSchema create_vendor()

Create a new vendor

Create a new vendor using request body.

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
    api_instance = openapi_client.VendorsApi(api_client)
    vendor_req_schema_vendor_req_schema = openapi_client.VendorReqSchema() # vendor_req_schema.VendorReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new vendor
        api_response = api_instance.create_vendor(vendor_req_schema_vendor_req_schema=vendor_req_schema_vendor_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VendorsApi->create_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_req_schema_vendor_req_schema** | [**vendor_req_schema.VendorReqSchema**](VendorReqSchema.md)|  | [optional]

### Return type

[**vendor_res_schema.VendorResSchema**](VendorResSchema.md)

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

# **delete_vendor**
> vendor_res_schema.VendorResSchema delete_vendor(vendor_id)

Delete a vendor

Delete a vendor using provided ID.

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
    api_instance = openapi_client.VendorsApi(api_client)
    vendor_id = 'vendor_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete a vendor
        api_response = api_instance.delete_vendor(vendor_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VendorsApi->delete_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **str**|  |

### Return type

[**vendor_res_schema.VendorResSchema**](VendorResSchema.md)

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

# **export_vendors**
> vendor_export_res_schema.VendorExportResSchema export_vendors()

Export vendors

Export vendors using provided pagination parameters.

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
    api_instance = openapi_client.VendorsApi(api_client)
    vendor_export_req_schema_vendor_export_req_schema = openapi_client.VendorExportReqSchema() # vendor_export_req_schema.VendorExportReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export vendors
        api_response = api_instance.export_vendors(vendor_export_req_schema_vendor_export_req_schema=vendor_export_req_schema_vendor_export_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VendorsApi->export_vendors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_export_req_schema_vendor_export_req_schema** | [**vendor_export_req_schema.VendorExportReqSchema**](VendorExportReqSchema.md)|  | [optional]

### Return type

[**vendor_export_res_schema.VendorExportResSchema**](VendorExportResSchema.md)

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

# **get_vendor**
> vendor_res_schema.VendorResSchema get_vendor(vendor_id)

Get a vendor

Get a vendor using provided ID.

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
    api_instance = openapi_client.VendorsApi(api_client)
    vendor_id = 'vendor_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get a vendor
        api_response = api_instance.get_vendor(vendor_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VendorsApi->get_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **str**|  |

### Return type

[**vendor_res_schema.VendorResSchema**](VendorResSchema.md)

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

# **import_vendors**
> vendor_import_res_schema.VendorImportResSchema import_vendors()

Import vendors

Import vendors using request body.

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
    api_instance = openapi_client.VendorsApi(api_client)
    vendor_import_req_schema_vendor_import_req_schema = openapi_client.VendorImportReqSchema() # vendor_import_req_schema.VendorImportReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import vendors
        api_response = api_instance.import_vendors(vendor_import_req_schema_vendor_import_req_schema=vendor_import_req_schema_vendor_import_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VendorsApi->import_vendors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_import_req_schema_vendor_import_req_schema** | [**vendor_import_req_schema.VendorImportReqSchema**](VendorImportReqSchema.md)|  | [optional]

### Return type

[**vendor_import_res_schema.VendorImportResSchema**](VendorImportResSchema.md)

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

# **list_vendors**
> vendor_list_res_schema.VendorListResSchema list_vendors(page, limit)

List vendors

List vendors using provided pagination parameters.

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
    api_instance = openapi_client.VendorsApi(api_client)
    page = 0 # int | 
    limit = 0 # int | 
    
    # example passing only required values which don't have defaults set
    try:
        # List vendors
        api_response = api_instance.list_vendors(page, limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VendorsApi->list_vendors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **limit** | **int**|  |

### Return type

[**vendor_list_res_schema.VendorListResSchema**](VendorListResSchema.md)

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

# **update_vendor**
> vendor_res_schema.VendorResSchema update_vendor(vendor_id)

Update a vendor

Update a vendor using provided ID and request body.

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
    api_instance = openapi_client.VendorsApi(api_client)
    vendor_id = 'vendor_id_example' # str | 
    vendor_req_schema_vendor_req_schema = openapi_client.VendorReqSchema() # vendor_req_schema.VendorReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a vendor
        api_response = api_instance.update_vendor(vendor_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VendorsApi->update_vendor: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a vendor
        api_response = api_instance.update_vendor(vendor_id, vendor_req_schema_vendor_req_schema=vendor_req_schema_vendor_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VendorsApi->update_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **str**|  |
 **vendor_req_schema_vendor_req_schema** | [**vendor_req_schema.VendorReqSchema**](VendorReqSchema.md)|  | [optional]

### Return type

[**vendor_res_schema.VendorResSchema**](VendorResSchema.md)

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

