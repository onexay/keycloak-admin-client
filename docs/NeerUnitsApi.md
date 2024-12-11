# openapi_client.NeerUnitsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_units**](NeerUnitsApi.md#count_units) | **GET** /tenant/{tenant_id}/unit/stats/count | Count units
[**create_unit**](NeerUnitsApi.md#create_unit) | **PUT** /tenant/{tenant_id}/unit/new | Create a new unit
[**delete_unit**](NeerUnitsApi.md#delete_unit) | **DELETE** /tenant/{tenant_id}/unit/{unit_id} | Delete a unit
[**export_units**](NeerUnitsApi.md#export_units) | **POST** /tenant/{tenant_id}/unit/export | Export units
[**get_unit**](NeerUnitsApi.md#get_unit) | **GET** /tenant/{tenant_id}/unit/{unit_id} | Get a unit
[**import_units**](NeerUnitsApi.md#import_units) | **POST** /tenant/{tenant_id}/unit/import | Import units
[**list_units**](NeerUnitsApi.md#list_units) | **GET** /tenant/{tenant_id}/unit/list/{page}/limit/{limit} | List units
[**update_unit**](NeerUnitsApi.md#update_unit) | **PATCH** /tenant/{tenant_id}/unit/{unit_id} | Update a unit


# **count_units**
> unit_count_res_schema.UnitCountResSchema count_units(tenant_id)

Count units

Count number of Units in a tenant.

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
    api_instance = openapi_client.NeerUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Count units
        api_response = api_instance.count_units(tenant_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerUnitsApi->count_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |

### Return type

[**unit_count_res_schema.UnitCountResSchema**](UnitCountResSchema.md)

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

# **create_unit**
> unit_res_schema.UnitResSchema create_unit(tenant_id)

Create a new unit

Create a new unit with provided tenant ID and request body.

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
    api_instance = openapi_client.NeerUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    unit_req_schema_unit_req_schema = openapi_client.UnitReqSchema() # unit_req_schema.UnitReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new unit
        api_response = api_instance.create_unit(tenant_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerUnitsApi->create_unit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new unit
        api_response = api_instance.create_unit(tenant_id, unit_req_schema_unit_req_schema=unit_req_schema_unit_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerUnitsApi->create_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **unit_req_schema_unit_req_schema** | [**unit_req_schema.UnitReqSchema**](UnitReqSchema.md)|  | [optional]

### Return type

[**unit_res_schema.UnitResSchema**](UnitResSchema.md)

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

# **delete_unit**
> unit_res_schema.UnitResSchema delete_unit(tenant_id, unit_id)

Delete a unit

Delete a unit using provided ID.

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
    api_instance = openapi_client.NeerUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    unit_id = 'unit_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete a unit
        api_response = api_instance.delete_unit(tenant_id, unit_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerUnitsApi->delete_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **unit_id** | **str**|  |

### Return type

[**unit_res_schema.UnitResSchema**](UnitResSchema.md)

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

# **export_units**
> unit_export_res_schema.UnitExportResSchema export_units(tenant_id)

Export units

Export units using provided pagination parameters.

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
    api_instance = openapi_client.NeerUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    unit_export_req_schema_unit_export_req_schema = openapi_client.UnitExportReqSchema() # unit_export_req_schema.UnitExportReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export units
        api_response = api_instance.export_units(tenant_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerUnitsApi->export_units: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export units
        api_response = api_instance.export_units(tenant_id, unit_export_req_schema_unit_export_req_schema=unit_export_req_schema_unit_export_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerUnitsApi->export_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **unit_export_req_schema_unit_export_req_schema** | [**unit_export_req_schema.UnitExportReqSchema**](UnitExportReqSchema.md)|  | [optional]

### Return type

[**unit_export_res_schema.UnitExportResSchema**](UnitExportResSchema.md)

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

# **get_unit**
> unit_res_schema.UnitResSchema get_unit(tenant_id, unit_id)

Get a unit

Get a unit with provided tenant ID, provided ID.

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
    api_instance = openapi_client.NeerUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    unit_id = 'unit_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get a unit
        api_response = api_instance.get_unit(tenant_id, unit_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerUnitsApi->get_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **unit_id** | **str**|  |

### Return type

[**unit_res_schema.UnitResSchema**](UnitResSchema.md)

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

# **import_units**
> unit_import_res_schema.UnitImportResSchema import_units(tenant_id)

Import units

Import units using provided pagination parameters.

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
    api_instance = openapi_client.NeerUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    unit_import_req_schema_unit_import_req_schema = openapi_client.UnitImportReqSchema() # unit_import_req_schema.UnitImportReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import units
        api_response = api_instance.import_units(tenant_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerUnitsApi->import_units: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import units
        api_response = api_instance.import_units(tenant_id, unit_import_req_schema_unit_import_req_schema=unit_import_req_schema_unit_import_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerUnitsApi->import_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **unit_import_req_schema_unit_import_req_schema** | [**unit_import_req_schema.UnitImportReqSchema**](UnitImportReqSchema.md)|  | [optional]

### Return type

[**unit_import_res_schema.UnitImportResSchema**](UnitImportResSchema.md)

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

# **list_units**
> unit_list_res_schema.UnitListResSchema list_units(tenant_id, page, limit)

List units

List units with provided tenant ID, pagination and limit.

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
    api_instance = openapi_client.NeerUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    page = 0 # int | 
    limit = 0 # int | 
    
    # example passing only required values which don't have defaults set
    try:
        # List units
        api_response = api_instance.list_units(tenant_id, page, limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerUnitsApi->list_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **page** | **int**|  |
 **limit** | **int**|  |

### Return type

[**unit_list_res_schema.UnitListResSchema**](UnitListResSchema.md)

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

# **update_unit**
> unit_res_schema.UnitResSchema update_unit(tenant_id, unit_id)

Update a unit

Update a unit using provided ID and request body.

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
    api_instance = openapi_client.NeerUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    unit_id = 'unit_id_example' # str | 
    unit_req_schema_unit_req_schema = openapi_client.UnitReqSchema() # unit_req_schema.UnitReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a unit
        api_response = api_instance.update_unit(tenant_id, unit_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerUnitsApi->update_unit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a unit
        api_response = api_instance.update_unit(tenant_id, unit_id, unit_req_schema_unit_req_schema=unit_req_schema_unit_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NeerUnitsApi->update_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **unit_id** | **str**|  |
 **unit_req_schema_unit_req_schema** | [**unit_req_schema.UnitReqSchema**](UnitReqSchema.md)|  | [optional]

### Return type

[**unit_res_schema.UnitResSchema**](UnitResSchema.md)

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

