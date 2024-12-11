# openapi_client.StatusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metrics**](StatusApi.md#get_metrics) | **GET** /status/metrics | Get the metrics of the service
[**get_status**](StatusApi.md#get_status) | **GET** /status/ | Get the status of the service


# **get_metrics**
> status_metrics_res_schema.StatusMetricsResSchema get_metrics()

Get the metrics of the service

Get the metrics of the service

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
    api_instance = openapi_client.StatusApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Get the metrics of the service
        api_response = api_instance.get_metrics()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StatusApi->get_metrics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**status_metrics_res_schema.StatusMetricsResSchema**](StatusMetricsResSchema.md)

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

# **get_status**
> status_version_res_schema.StatusVersionResSchema get_status()

Get the status of the service

Get the status of the service

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
    api_instance = openapi_client.StatusApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Get the status of the service
        api_response = api_instance.get_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StatusApi->get_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**status_version_res_schema.StatusVersionResSchema**](StatusVersionResSchema.md)

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

