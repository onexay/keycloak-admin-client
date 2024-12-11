# openapi_client.AttackDetectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_realm_attack_detection_brute_force_users_delete**](AttackDetectionApi.md#admin_realms_realm_attack_detection_brute_force_users_delete) | **DELETE** /admin/realms/{realm}/attack-detection/brute-force/users | Clear any user login failures for all users This can release temporary disabled users
[**admin_realms_realm_attack_detection_brute_force_users_user_id_delete**](AttackDetectionApi.md#admin_realms_realm_attack_detection_brute_force_users_user_id_delete) | **DELETE** /admin/realms/{realm}/attack-detection/brute-force/users/{userId} | Clear any user login failures for the user This can release temporary disabled user
[**admin_realms_realm_attack_detection_brute_force_users_user_id_get**](AttackDetectionApi.md#admin_realms_realm_attack_detection_brute_force_users_user_id_get) | **GET** /admin/realms/{realm}/attack-detection/brute-force/users/{userId} | Get status of a username in brute force detection


# **admin_realms_realm_attack_detection_brute_force_users_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_attack_detection_brute_force_users_delete(realm)

Clear any user login failures for all users This can release temporary disabled users

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
    api_instance = openapi_client.AttackDetectionApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Clear any user login failures for all users This can release temporary disabled users
        api_response = api_instance.admin_realms_realm_attack_detection_brute_force_users_delete(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AttackDetectionApi->admin_realms_realm_attack_detection_brute_force_users_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_attack_detection_brute_force_users_user_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_attack_detection_brute_force_users_user_id_delete(user_id, realm)

Clear any user login failures for the user This can release temporary disabled user

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
    api_instance = openapi_client.AttackDetectionApi(api_client)
    user_id = 'user_id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Clear any user login failures for the user This can release temporary disabled user
        api_response = api_instance.admin_realms_realm_attack_detection_brute_force_users_user_id_delete(user_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AttackDetectionApi->admin_realms_realm_attack_detection_brute_force_users_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **realm** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_attack_detection_brute_force_users_user_id_get**
> {str: (str,)} admin_realms_realm_attack_detection_brute_force_users_user_id_get(user_id, realm)

Get status of a username in brute force detection

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
    api_instance = openapi_client.AttackDetectionApi(api_client)
    user_id = 'user_id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get status of a username in brute force detection
        api_response = api_instance.admin_realms_realm_attack_detection_brute_force_users_user_id_get(user_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AttackDetectionApi->admin_realms_realm_attack_detection_brute_force_users_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **realm** | **str**|  |

### Return type

**{str: (str,)}**

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

