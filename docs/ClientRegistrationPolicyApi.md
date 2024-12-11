# openapi_client.ClientRegistrationPolicyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_realm_client_registration_policy_providers_get**](ClientRegistrationPolicyApi.md#admin_realms_realm_client_registration_policy_providers_get) | **GET** /admin/realms/{realm}/client-registration-policy/providers | Base path for retrieve providers with the configProperties properly filled


# **admin_realms_realm_client_registration_policy_providers_get**
> [component_type_representation.ComponentTypeRepresentation] admin_realms_realm_client_registration_policy_providers_get(realm)

Base path for retrieve providers with the configProperties properly filled

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
    api_instance = openapi_client.ClientRegistrationPolicyApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Base path for retrieve providers with the configProperties properly filled
        api_response = api_instance.admin_realms_realm_client_registration_policy_providers_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientRegistrationPolicyApi->admin_realms_realm_client_registration_policy_providers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

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

