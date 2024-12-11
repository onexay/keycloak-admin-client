# openapi_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_users**](UsersApi.md#count_users) | **GET** /user/stats/count | Count users
[**create_user**](UsersApi.md#create_user) | **PUT** /user/new | Create a new user
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /user/{user_id} | Delete a user
[**export_users**](UsersApi.md#export_users) | **POST** /user/export | Export users
[**get_user**](UsersApi.md#get_user) | **GET** /user/{user_id} | Get user details
[**import_users**](UsersApi.md#import_users) | **POST** /user/import | Import users
[**list_users**](UsersApi.md#list_users) | **GET** /user/list/{page}/limit/{limit} | List users
[**update_user**](UsersApi.md#update_user) | **PATCH** /user/{user_id} | Update a user


# **count_users**
> user_count_res_schema.UserCountResSchema count_users()

Count users

Count the number of users.

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
    api_instance = openapi_client.UsersApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Count users
        api_response = api_instance.count_users()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->count_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**user_count_res_schema.UserCountResSchema**](UserCountResSchema.md)

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

# **create_user**
> user_res_schema.UserResSchema create_user()

Create a new user

Create a new user using request body.

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
    api_instance = openapi_client.UsersApi(api_client)
    user_req_schema_user_req_schema = openapi_client.UserReqSchema() # user_req_schema.UserReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new user
        api_response = api_instance.create_user(user_req_schema_user_req_schema=user_req_schema_user_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_req_schema_user_req_schema** | [**user_req_schema.UserReqSchema**](UserReqSchema.md)|  | [optional]

### Return type

[**user_res_schema.UserResSchema**](UserResSchema.md)

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

# **delete_user**
> user_res_schema.UserResSchema delete_user(user_id)

Delete a user

Delete a user using provided ID.

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
    api_instance = openapi_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete a user
        api_response = api_instance.delete_user(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |

### Return type

[**user_res_schema.UserResSchema**](UserResSchema.md)

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

# **export_users**
> user_export_res_schema.UserExportResSchema export_users()

Export users

Export users using provided pagination parameters.

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
    api_instance = openapi_client.UsersApi(api_client)
    user_export_req_schema_user_export_req_schema = openapi_client.UserExportReqSchema() # user_export_req_schema.UserExportReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export users
        api_response = api_instance.export_users(user_export_req_schema_user_export_req_schema=user_export_req_schema_user_export_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->export_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_export_req_schema_user_export_req_schema** | [**user_export_req_schema.UserExportReqSchema**](UserExportReqSchema.md)|  | [optional]

### Return type

[**user_export_res_schema.UserExportResSchema**](UserExportResSchema.md)

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

# **get_user**
> user_res_schema.UserResSchema get_user(user_id)

Get user details

Get user details using user ID.

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
    api_instance = openapi_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get user details
        api_response = api_instance.get_user(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |

### Return type

[**user_res_schema.UserResSchema**](UserResSchema.md)

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

# **import_users**
> user_import_res_schema.UserImportResSchema import_users()

Import users

Import users using request body.

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
    api_instance = openapi_client.UsersApi(api_client)
    user_import_req_schema_user_import_req_schema = openapi_client.UserImportReqSchema() # user_import_req_schema.UserImportReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import users
        api_response = api_instance.import_users(user_import_req_schema_user_import_req_schema=user_import_req_schema_user_import_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->import_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_import_req_schema_user_import_req_schema** | [**user_import_req_schema.UserImportReqSchema**](UserImportReqSchema.md)|  | [optional]

### Return type

[**user_import_res_schema.UserImportResSchema**](UserImportResSchema.md)

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

# **list_users**
> user_list_res_schema.UserListResSchema list_users(page, limit)

List users

List users using provided tenant ID and pagination parameters.

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
    api_instance = openapi_client.UsersApi(api_client)
    page = 0 # int | 
    limit = 0 # int | 
    
    # example passing only required values which don't have defaults set
    try:
        # List users
        api_response = api_instance.list_users(page, limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **limit** | **int**|  |

### Return type

[**user_list_res_schema.UserListResSchema**](UserListResSchema.md)

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

# **update_user**
> user_res_schema.UserResSchema update_user(user_id)

Update a user

Update a user using provided ID and request body.

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
    api_instance = openapi_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    user_req_schema_user_req_schema = openapi_client.UserReqSchema() # user_req_schema.UserReqSchema |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a user
        api_response = api_instance.update_user(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a user
        api_response = api_instance.update_user(user_id, user_req_schema_user_req_schema=user_req_schema_user_req_schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **user_req_schema_user_req_schema** | [**user_req_schema.UserReqSchema**](UserReqSchema.md)|  | [optional]

### Return type

[**user_res_schema.UserResSchema**](UserResSchema.md)

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

