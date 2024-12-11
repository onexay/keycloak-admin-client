# openapi_client.GroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_realm_groups_count_get**](GroupsApi.md#admin_realms_realm_groups_count_get) | **GET** /admin/realms/{realm}/groups/count | Returns the groups counts.
[**admin_realms_realm_groups_get**](GroupsApi.md#admin_realms_realm_groups_get) | **GET** /admin/realms/{realm}/groups | Get group hierarchy.  Only name and ids are returned.
[**admin_realms_realm_groups_group_id_children_get**](GroupsApi.md#admin_realms_realm_groups_group_id_children_get) | **GET** /admin/realms/{realm}/groups/{group-id}/children | Return a paginated list of subgroups that have a parent group corresponding to the group on the URL
[**admin_realms_realm_groups_group_id_children_post**](GroupsApi.md#admin_realms_realm_groups_group_id_children_post) | **POST** /admin/realms/{realm}/groups/{group-id}/children | Set or create child.
[**admin_realms_realm_groups_group_id_delete**](GroupsApi.md#admin_realms_realm_groups_group_id_delete) | **DELETE** /admin/realms/{realm}/groups/{group-id} | /admin/realms/{realm}/groups/{group-id}
[**admin_realms_realm_groups_group_id_get**](GroupsApi.md#admin_realms_realm_groups_group_id_get) | **GET** /admin/realms/{realm}/groups/{group-id} | /admin/realms/{realm}/groups/{group-id}
[**admin_realms_realm_groups_group_id_management_permissions_get**](GroupsApi.md#admin_realms_realm_groups_group_id_management_permissions_get) | **GET** /admin/realms/{realm}/groups/{group-id}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**admin_realms_realm_groups_group_id_management_permissions_put**](GroupsApi.md#admin_realms_realm_groups_group_id_management_permissions_put) | **PUT** /admin/realms/{realm}/groups/{group-id}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**admin_realms_realm_groups_group_id_members_get**](GroupsApi.md#admin_realms_realm_groups_group_id_members_get) | **GET** /admin/realms/{realm}/groups/{group-id}/members | Get users Returns a stream of users, filtered according to query parameters
[**admin_realms_realm_groups_group_id_put**](GroupsApi.md#admin_realms_realm_groups_group_id_put) | **PUT** /admin/realms/{realm}/groups/{group-id} | Update group, ignores subgroups.
[**admin_realms_realm_groups_post**](GroupsApi.md#admin_realms_realm_groups_post) | **POST** /admin/realms/{realm}/groups | create or add a top level realm groupSet or create child.


# **admin_realms_realm_groups_count_get**
> {str: (int,)} admin_realms_realm_groups_count_get(realm)

Returns the groups counts.

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
    api_instance = openapi_client.GroupsApi(api_client)
    realm = 'realm_example' # str | 
    search = 'search_example' # str |  (optional)
top = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Returns the groups counts.
        api_response = api_instance.admin_realms_realm_groups_count_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_count_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the groups counts.
        api_response = api_instance.admin_realms_realm_groups_count_get(realm, search=search, top=top)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **search** | **str**|  | [optional]
 **top** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

**{str: (int,)}**

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

# **admin_realms_realm_groups_get**
> [group_representation.GroupRepresentation] admin_realms_realm_groups_get(realm)

Get group hierarchy.  Only name and ids are returned.

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
    api_instance = openapi_client.GroupsApi(api_client)
    realm = 'realm_example' # str | 
    brief_representation = True # bool |  (optional) if omitted the server will use the default value of True
exact = False # bool |  (optional) if omitted the server will use the default value of False
first = 56 # int |  (optional)
max = 56 # int |  (optional)
populate_hierarchy = True # bool |  (optional) if omitted the server will use the default value of True
q = 'q_example' # str |  (optional)
search = 'search_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get group hierarchy.  Only name and ids are returned.
        api_response = api_instance.admin_realms_realm_groups_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get group hierarchy.  Only name and ids are returned.
        api_response = api_instance.admin_realms_realm_groups_get(realm, brief_representation=brief_representation, exact=exact, first=first, max=max, populate_hierarchy=populate_hierarchy, q=q, search=search)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **brief_representation** | **bool**|  | [optional] if omitted the server will use the default value of True
 **exact** | **bool**|  | [optional] if omitted the server will use the default value of False
 **first** | **int**|  | [optional]
 **max** | **int**|  | [optional]
 **populate_hierarchy** | **bool**|  | [optional] if omitted the server will use the default value of True
 **q** | **str**|  | [optional]
 **search** | **str**|  | [optional]

### Return type

[**[group_representation.GroupRepresentation]**](GroupRepresentation.md)

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

# **admin_realms_realm_groups_group_id_children_get**
> [group_representation.GroupRepresentation] admin_realms_realm_groups_group_id_children_get(realm, group_id)

Return a paginated list of subgroups that have a parent group corresponding to the group on the URL

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
    api_instance = openapi_client.GroupsApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    brief_representation = False # bool | Boolean which defines whether brief groups representations are returned or not (default: false) (optional) if omitted the server will use the default value of False
exact = True # bool | Boolean which defines whether the params \"search\" must match exactly or not (optional)
first = 56 # int | The position of the first result to be returned (pagination offset). (optional)
max = 56 # int | The maximum number of results that are to be returned. Defaults to 10 (optional)
search = 'search_example' # str | A String representing either an exact group name or a partial name (optional)

    # example passing only required values which don't have defaults set
    try:
        # Return a paginated list of subgroups that have a parent group corresponding to the group on the URL
        api_response = api_instance.admin_realms_realm_groups_group_id_children_get(realm, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_group_id_children_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return a paginated list of subgroups that have a parent group corresponding to the group on the URL
        api_response = api_instance.admin_realms_realm_groups_group_id_children_get(realm, group_id, brief_representation=brief_representation, exact=exact, first=first, max=max, search=search)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_group_id_children_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |
 **brief_representation** | **bool**| Boolean which defines whether brief groups representations are returned or not (default: false) | [optional] if omitted the server will use the default value of False
 **exact** | **bool**| Boolean which defines whether the params \&quot;search\&quot; must match exactly or not | [optional]
 **first** | **int**| The position of the first result to be returned (pagination offset). | [optional]
 **max** | **int**| The maximum number of results that are to be returned. Defaults to 10 | [optional]
 **search** | **str**| A String representing either an exact group name or a partial name | [optional]

### Return type

[**[group_representation.GroupRepresentation]**](GroupRepresentation.md)

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

# **admin_realms_realm_groups_group_id_children_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_groups_group_id_children_post(realm, group_id)

Set or create child.

This will just set the parent if it exists. Create it and set the parent if the group doesn’t exist.

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
    api_instance = openapi_client.GroupsApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    group_representation_group_representation = openapi_client.GroupRepresentation() # group_representation.GroupRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set or create child.
        api_response = api_instance.admin_realms_realm_groups_group_id_children_post(realm, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_group_id_children_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set or create child.
        api_response = api_instance.admin_realms_realm_groups_group_id_children_post(realm, group_id, group_representation_group_representation=group_representation_group_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_group_id_children_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |
 **group_representation_group_representation** | [**group_representation.GroupRepresentation**](GroupRepresentation.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_groups_group_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_groups_group_id_delete(realm, group_id)

/admin/realms/{realm}/groups/{group-id}

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
    api_instance = openapi_client.GroupsApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/groups/{group-id}
        api_response = api_instance.admin_realms_realm_groups_group_id_delete(realm, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_group_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |

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

# **admin_realms_realm_groups_group_id_get**
> group_representation.GroupRepresentation admin_realms_realm_groups_group_id_get(realm, group_id)

/admin/realms/{realm}/groups/{group-id}

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
    api_instance = openapi_client.GroupsApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/groups/{group-id}
        api_response = api_instance.admin_realms_realm_groups_group_id_get(realm, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |

### Return type

[**group_representation.GroupRepresentation**](GroupRepresentation.md)

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

# **admin_realms_realm_groups_group_id_management_permissions_get**
> management_permission_reference.ManagementPermissionReference admin_realms_realm_groups_group_id_management_permissions_get(realm, group_id)

Return object stating whether client Authorization permissions have been initialized or not and a reference

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
    api_instance = openapi_client.GroupsApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether client Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_groups_group_id_management_permissions_get(realm, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_group_id_management_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |

### Return type

[**management_permission_reference.ManagementPermissionReference**](ManagementPermissionReference.md)

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

# **admin_realms_realm_groups_group_id_management_permissions_put**
> management_permission_reference.ManagementPermissionReference admin_realms_realm_groups_group_id_management_permissions_put(realm, group_id)

Return object stating whether client Authorization permissions have been initialized or not and a reference

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
    api_instance = openapi_client.GroupsApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    management_permission_reference_management_permission_reference = openapi_client.ManagementPermissionReference() # management_permission_reference.ManagementPermissionReference |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether client Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_groups_group_id_management_permissions_put(realm, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_group_id_management_permissions_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return object stating whether client Authorization permissions have been initialized or not and a reference
        api_response = api_instance.admin_realms_realm_groups_group_id_management_permissions_put(realm, group_id, management_permission_reference_management_permission_reference=management_permission_reference_management_permission_reference)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_group_id_management_permissions_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |
 **management_permission_reference_management_permission_reference** | [**management_permission_reference.ManagementPermissionReference**](ManagementPermissionReference.md)|  | [optional]

### Return type

[**management_permission_reference.ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_groups_group_id_members_get**
> [user_representation.UserRepresentation] admin_realms_realm_groups_group_id_members_get(realm, group_id)

Get users Returns a stream of users, filtered according to query parameters

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
    api_instance = openapi_client.GroupsApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    brief_representation = True # bool | Only return basic information (only guaranteed to return id, username, created, first and last name, email, enabled state, email verification state, federation link, and access. Note that it means that namely user attributes, required actions, and not before are not returned.) (optional)
first = 56 # int | Pagination offset (optional)
max = 56 # int | Maximum results size (defaults to 100) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get users Returns a stream of users, filtered according to query parameters
        api_response = api_instance.admin_realms_realm_groups_group_id_members_get(realm, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_group_id_members_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get users Returns a stream of users, filtered according to query parameters
        api_response = api_instance.admin_realms_realm_groups_group_id_members_get(realm, group_id, brief_representation=brief_representation, first=first, max=max)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_group_id_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |
 **brief_representation** | **bool**| Only return basic information (only guaranteed to return id, username, created, first and last name, email, enabled state, email verification state, federation link, and access. Note that it means that namely user attributes, required actions, and not before are not returned.) | [optional]
 **first** | **int**| Pagination offset | [optional]
 **max** | **int**| Maximum results size (defaults to 100) | [optional]

### Return type

[**[user_representation.UserRepresentation]**](UserRepresentation.md)

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

# **admin_realms_realm_groups_group_id_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_groups_group_id_put(realm, group_id)

Update group, ignores subgroups.

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
    api_instance = openapi_client.GroupsApi(api_client)
    realm = 'realm_example' # str | 
    group_id = 'group_id_example' # str | 
    group_representation_group_representation = openapi_client.GroupRepresentation() # group_representation.GroupRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update group, ignores subgroups.
        api_response = api_instance.admin_realms_realm_groups_group_id_put(realm, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_group_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update group, ignores subgroups.
        api_response = api_instance.admin_realms_realm_groups_group_id_put(realm, group_id, group_representation_group_representation=group_representation_group_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_group_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_id** | **str**|  |
 **group_representation_group_representation** | [**group_representation.GroupRepresentation**](GroupRepresentation.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_groups_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_groups_post(realm)

create or add a top level realm groupSet or create child.

This will update the group and set the parent if it exists. Create it and set the parent if the group doesn’t exist.

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
    api_instance = openapi_client.GroupsApi(api_client)
    realm = 'realm_example' # str | 
    group_representation_group_representation = openapi_client.GroupRepresentation() # group_representation.GroupRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # create or add a top level realm groupSet or create child.
        api_response = api_instance.admin_realms_realm_groups_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # create or add a top level realm groupSet or create child.
        api_response = api_instance.admin_realms_realm_groups_post(realm, group_representation_group_representation=group_representation_group_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->admin_realms_realm_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **group_representation_group_representation** | [**group_representation.GroupRepresentation**](GroupRepresentation.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

