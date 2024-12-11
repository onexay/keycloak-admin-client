# openapi_client.RealmsAdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_get**](RealmsAdminApi.md#admin_realms_get) | **GET** /admin/realms | Get accessible realms Returns a list of accessible realms. The list is filtered based on what realms the caller is allowed to view.
[**admin_realms_post**](RealmsAdminApi.md#admin_realms_post) | **POST** /admin/realms | Import a realm. Imports a realm from a full representation of that realm.
[**admin_realms_realm_admin_events_delete**](RealmsAdminApi.md#admin_realms_realm_admin_events_delete) | **DELETE** /admin/realms/{realm}/admin-events | Delete all admin events
[**admin_realms_realm_admin_events_get**](RealmsAdminApi.md#admin_realms_realm_admin_events_get) | **GET** /admin/realms/{realm}/admin-events | Get admin events Returns all admin events, or filters events based on URL query parameters listed here
[**admin_realms_realm_client_description_converter_post**](RealmsAdminApi.md#admin_realms_realm_client_description_converter_post) | **POST** /admin/realms/{realm}/client-description-converter | Base path for importing clients under this realm.
[**admin_realms_realm_client_policies_policies_get**](RealmsAdminApi.md#admin_realms_realm_client_policies_policies_get) | **GET** /admin/realms/{realm}/client-policies/policies | /admin/realms/{realm}/client-policies/policies
[**admin_realms_realm_client_policies_policies_put**](RealmsAdminApi.md#admin_realms_realm_client_policies_policies_put) | **PUT** /admin/realms/{realm}/client-policies/policies | /admin/realms/{realm}/client-policies/policies
[**admin_realms_realm_client_policies_profiles_get**](RealmsAdminApi.md#admin_realms_realm_client_policies_profiles_get) | **GET** /admin/realms/{realm}/client-policies/profiles | /admin/realms/{realm}/client-policies/profiles
[**admin_realms_realm_client_policies_profiles_put**](RealmsAdminApi.md#admin_realms_realm_client_policies_profiles_put) | **PUT** /admin/realms/{realm}/client-policies/profiles | /admin/realms/{realm}/client-policies/profiles
[**admin_realms_realm_client_session_stats_get**](RealmsAdminApi.md#admin_realms_realm_client_session_stats_get) | **GET** /admin/realms/{realm}/client-session-stats | Get client session stats Returns a JSON map.
[**admin_realms_realm_client_types_get**](RealmsAdminApi.md#admin_realms_realm_client_types_get) | **GET** /admin/realms/{realm}/client-types | List all client types available in the current realm
[**admin_realms_realm_client_types_put**](RealmsAdminApi.md#admin_realms_realm_client_types_put) | **PUT** /admin/realms/{realm}/client-types | Update a client type
[**admin_realms_realm_credential_registrators_get**](RealmsAdminApi.md#admin_realms_realm_credential_registrators_get) | **GET** /admin/realms/{realm}/credential-registrators | /admin/realms/{realm}/credential-registrators
[**admin_realms_realm_default_default_client_scopes_client_scope_id_delete**](RealmsAdminApi.md#admin_realms_realm_default_default_client_scopes_client_scope_id_delete) | **DELETE** /admin/realms/{realm}/default-default-client-scopes/{clientScopeId} | /admin/realms/{realm}/default-default-client-scopes/{clientScopeId}
[**admin_realms_realm_default_default_client_scopes_client_scope_id_put**](RealmsAdminApi.md#admin_realms_realm_default_default_client_scopes_client_scope_id_put) | **PUT** /admin/realms/{realm}/default-default-client-scopes/{clientScopeId} | /admin/realms/{realm}/default-default-client-scopes/{clientScopeId}
[**admin_realms_realm_default_default_client_scopes_get**](RealmsAdminApi.md#admin_realms_realm_default_default_client_scopes_get) | **GET** /admin/realms/{realm}/default-default-client-scopes | Get realm default client scopes.  Only name and ids are returned.
[**admin_realms_realm_default_groups_get**](RealmsAdminApi.md#admin_realms_realm_default_groups_get) | **GET** /admin/realms/{realm}/default-groups | Get group hierarchy.  Only name and ids are returned.
[**admin_realms_realm_default_groups_group_id_delete**](RealmsAdminApi.md#admin_realms_realm_default_groups_group_id_delete) | **DELETE** /admin/realms/{realm}/default-groups/{groupId} | /admin/realms/{realm}/default-groups/{groupId}
[**admin_realms_realm_default_groups_group_id_put**](RealmsAdminApi.md#admin_realms_realm_default_groups_group_id_put) | **PUT** /admin/realms/{realm}/default-groups/{groupId} | /admin/realms/{realm}/default-groups/{groupId}
[**admin_realms_realm_default_optional_client_scopes_client_scope_id_delete**](RealmsAdminApi.md#admin_realms_realm_default_optional_client_scopes_client_scope_id_delete) | **DELETE** /admin/realms/{realm}/default-optional-client-scopes/{clientScopeId} | /admin/realms/{realm}/default-optional-client-scopes/{clientScopeId}
[**admin_realms_realm_default_optional_client_scopes_client_scope_id_put**](RealmsAdminApi.md#admin_realms_realm_default_optional_client_scopes_client_scope_id_put) | **PUT** /admin/realms/{realm}/default-optional-client-scopes/{clientScopeId} | /admin/realms/{realm}/default-optional-client-scopes/{clientScopeId}
[**admin_realms_realm_default_optional_client_scopes_get**](RealmsAdminApi.md#admin_realms_realm_default_optional_client_scopes_get) | **GET** /admin/realms/{realm}/default-optional-client-scopes | Get realm optional client scopes.  Only name and ids are returned.
[**admin_realms_realm_delete**](RealmsAdminApi.md#admin_realms_realm_delete) | **DELETE** /admin/realms/{realm} | Delete the realm
[**admin_realms_realm_events_config_get**](RealmsAdminApi.md#admin_realms_realm_events_config_get) | **GET** /admin/realms/{realm}/events/config | Get the events provider configuration Returns JSON object with events provider configuration
[**admin_realms_realm_events_config_put**](RealmsAdminApi.md#admin_realms_realm_events_config_put) | **PUT** /admin/realms/{realm}/events/config | /admin/realms/{realm}/events/config
[**admin_realms_realm_events_delete**](RealmsAdminApi.md#admin_realms_realm_events_delete) | **DELETE** /admin/realms/{realm}/events | Delete all events
[**admin_realms_realm_events_get**](RealmsAdminApi.md#admin_realms_realm_events_get) | **GET** /admin/realms/{realm}/events | Get events Returns all events, or filters them based on URL query parameters listed here
[**admin_realms_realm_get**](RealmsAdminApi.md#admin_realms_realm_get) | **GET** /admin/realms/{realm} | Get the top-level representation of the realm It will not include nested information like User and Client representations.
[**admin_realms_realm_group_by_path_path_get**](RealmsAdminApi.md#admin_realms_realm_group_by_path_path_get) | **GET** /admin/realms/{realm}/group-by-path/{path} | /admin/realms/{realm}/group-by-path/{path}
[**admin_realms_realm_localization_get**](RealmsAdminApi.md#admin_realms_realm_localization_get) | **GET** /admin/realms/{realm}/localization | /admin/realms/{realm}/localization
[**admin_realms_realm_localization_locale_delete**](RealmsAdminApi.md#admin_realms_realm_localization_locale_delete) | **DELETE** /admin/realms/{realm}/localization/{locale} | /admin/realms/{realm}/localization/{locale}
[**admin_realms_realm_localization_locale_get**](RealmsAdminApi.md#admin_realms_realm_localization_locale_get) | **GET** /admin/realms/{realm}/localization/{locale} | /admin/realms/{realm}/localization/{locale}
[**admin_realms_realm_localization_locale_key_delete**](RealmsAdminApi.md#admin_realms_realm_localization_locale_key_delete) | **DELETE** /admin/realms/{realm}/localization/{locale}/{key} | /admin/realms/{realm}/localization/{locale}/{key}
[**admin_realms_realm_localization_locale_key_get**](RealmsAdminApi.md#admin_realms_realm_localization_locale_key_get) | **GET** /admin/realms/{realm}/localization/{locale}/{key} | /admin/realms/{realm}/localization/{locale}/{key}
[**admin_realms_realm_localization_locale_key_put**](RealmsAdminApi.md#admin_realms_realm_localization_locale_key_put) | **PUT** /admin/realms/{realm}/localization/{locale}/{key} | /admin/realms/{realm}/localization/{locale}/{key}
[**admin_realms_realm_localization_locale_post**](RealmsAdminApi.md#admin_realms_realm_localization_locale_post) | **POST** /admin/realms/{realm}/localization/{locale} | Import localization from uploaded JSON file
[**admin_realms_realm_logout_all_post**](RealmsAdminApi.md#admin_realms_realm_logout_all_post) | **POST** /admin/realms/{realm}/logout-all | Removes all user sessions.
[**admin_realms_realm_partial_export_post**](RealmsAdminApi.md#admin_realms_realm_partial_export_post) | **POST** /admin/realms/{realm}/partial-export | Partial export of existing realm into a JSON file.
[**admin_realms_realm_partial_import_post**](RealmsAdminApi.md#admin_realms_realm_partial_import_post) | **POST** /admin/realms/{realm}/partialImport | Partial import from a JSON file to an existing realm.
[**admin_realms_realm_push_revocation_post**](RealmsAdminApi.md#admin_realms_realm_push_revocation_post) | **POST** /admin/realms/{realm}/push-revocation | Push the realm&#39;s revocation policy to any client that has an admin url associated with it.
[**admin_realms_realm_put**](RealmsAdminApi.md#admin_realms_realm_put) | **PUT** /admin/realms/{realm} | Update the top-level information of the realm Any user, roles or client information in the representation will be ignored.
[**admin_realms_realm_sessions_session_delete**](RealmsAdminApi.md#admin_realms_realm_sessions_session_delete) | **DELETE** /admin/realms/{realm}/sessions/{session} | Remove a specific user session.
[**admin_realms_realm_test_smtp_connection_post**](RealmsAdminApi.md#admin_realms_realm_test_smtp_connection_post) | **POST** /admin/realms/{realm}/testSMTPConnection | Test SMTP connection with current logged in user
[**admin_realms_realm_users_management_permissions_get**](RealmsAdminApi.md#admin_realms_realm_users_management_permissions_get) | **GET** /admin/realms/{realm}/users-management-permissions | /admin/realms/{realm}/users-management-permissions
[**admin_realms_realm_users_management_permissions_put**](RealmsAdminApi.md#admin_realms_realm_users_management_permissions_put) | **PUT** /admin/realms/{realm}/users-management-permissions | /admin/realms/{realm}/users-management-permissions


# **admin_realms_get**
> [realm_representation.RealmRepresentation] admin_realms_get()

Get accessible realms Returns a list of accessible realms. The list is filtered based on what realms the caller is allowed to view.

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    brief_representation = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get accessible realms Returns a list of accessible realms. The list is filtered based on what realms the caller is allowed to view.
        api_response = api_instance.admin_realms_get(brief_representation=brief_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brief_representation** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**[realm_representation.RealmRepresentation]**](RealmRepresentation.md)

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

# **admin_realms_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_post()

Import a realm. Imports a realm from a full representation of that realm.

Realm name must be unique.

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    body = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import a realm. Imports a realm from a full representation of that realm.
        api_response = api_instance.admin_realms_post(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **file_type**|  | [optional]

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_admin_events_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_admin_events_delete(realm)

Delete all admin events

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete all admin events
        api_response = api_instance.admin_realms_realm_admin_events_delete(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_admin_events_delete: %s\n" % e)
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

# **admin_realms_realm_admin_events_get**
> [admin_event_representation.AdminEventRepresentation] admin_realms_realm_admin_events_get(realm)

Get admin events Returns all admin events, or filters events based on URL query parameters listed here

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    auth_client = 'auth_client_example' # str |  (optional)
auth_ip_address = 'auth_ip_address_example' # str |  (optional)
auth_realm = 'auth_realm_example' # str |  (optional)
auth_user = 'auth_user_example' # str | user id (optional)
date_from = 'date_from_example' # str |  (optional)
date_to = 'date_to_example' # str |  (optional)
first = 56 # int |  (optional)
max = 56 # int | Maximum results size (defaults to 100) (optional)
operation_types = ['operation_types_example'] # [str] |  (optional)
_resource_path = '_resource_path_example' # str |  (optional)
resource_types = ['resource_types_example'] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get admin events Returns all admin events, or filters events based on URL query parameters listed here
        api_response = api_instance.admin_realms_realm_admin_events_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_admin_events_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get admin events Returns all admin events, or filters events based on URL query parameters listed here
        api_response = api_instance.admin_realms_realm_admin_events_get(realm, auth_client=auth_client, auth_ip_address=auth_ip_address, auth_realm=auth_realm, auth_user=auth_user, date_from=date_from, date_to=date_to, first=first, max=max, operation_types=operation_types, _resource_path=_resource_path, resource_types=resource_types)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_admin_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **auth_client** | **str**|  | [optional]
 **auth_ip_address** | **str**|  | [optional]
 **auth_realm** | **str**|  | [optional]
 **auth_user** | **str**| user id | [optional]
 **date_from** | **str**|  | [optional]
 **date_to** | **str**|  | [optional]
 **first** | **int**|  | [optional]
 **max** | **int**| Maximum results size (defaults to 100) | [optional]
 **operation_types** | **[str]**|  | [optional]
 **_resource_path** | **str**|  | [optional]
 **resource_types** | **[str]**|  | [optional]

### Return type

[**[admin_event_representation.AdminEventRepresentation]**](AdminEventRepresentation.md)

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

# **admin_realms_realm_client_description_converter_post**
> client_representation.ClientRepresentation admin_realms_realm_client_description_converter_post(realm)

Base path for importing clients under this realm.

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    body = 'body_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Base path for importing clients under this realm.
        api_response = api_instance.admin_realms_realm_client_description_converter_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_client_description_converter_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Base path for importing clients under this realm.
        api_response = api_instance.admin_realms_realm_client_description_converter_post(realm, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_client_description_converter_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **body** | **str**|  | [optional]

### Return type

[**client_representation.ClientRepresentation**](ClientRepresentation.md)

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

# **admin_realms_realm_client_policies_policies_get**
> client_policies_representation.ClientPoliciesRepresentation admin_realms_realm_client_policies_policies_get(realm)

/admin/realms/{realm}/client-policies/policies

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    include_global_policies = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/client-policies/policies
        api_response = api_instance.admin_realms_realm_client_policies_policies_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_client_policies_policies_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /admin/realms/{realm}/client-policies/policies
        api_response = api_instance.admin_realms_realm_client_policies_policies_get(realm, include_global_policies=include_global_policies)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_client_policies_policies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **include_global_policies** | **bool**|  | [optional]

### Return type

[**client_policies_representation.ClientPoliciesRepresentation**](ClientPoliciesRepresentation.md)

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

# **admin_realms_realm_client_policies_policies_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_client_policies_policies_put(realm)

/admin/realms/{realm}/client-policies/policies

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    client_policies_representation_client_policies_representation = openapi_client.ClientPoliciesRepresentation() # client_policies_representation.ClientPoliciesRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/client-policies/policies
        api_response = api_instance.admin_realms_realm_client_policies_policies_put(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_client_policies_policies_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /admin/realms/{realm}/client-policies/policies
        api_response = api_instance.admin_realms_realm_client_policies_policies_put(realm, client_policies_representation_client_policies_representation=client_policies_representation_client_policies_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_client_policies_policies_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_policies_representation_client_policies_representation** | [**client_policies_representation.ClientPoliciesRepresentation**](ClientPoliciesRepresentation.md)|  | [optional]

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

# **admin_realms_realm_client_policies_profiles_get**
> client_profiles_representation.ClientProfilesRepresentation admin_realms_realm_client_policies_profiles_get(realm)

/admin/realms/{realm}/client-policies/profiles

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    include_global_profiles = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/client-policies/profiles
        api_response = api_instance.admin_realms_realm_client_policies_profiles_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_client_policies_profiles_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /admin/realms/{realm}/client-policies/profiles
        api_response = api_instance.admin_realms_realm_client_policies_profiles_get(realm, include_global_profiles=include_global_profiles)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_client_policies_profiles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **include_global_profiles** | **bool**|  | [optional]

### Return type

[**client_profiles_representation.ClientProfilesRepresentation**](ClientProfilesRepresentation.md)

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

# **admin_realms_realm_client_policies_profiles_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_client_policies_profiles_put(realm)

/admin/realms/{realm}/client-policies/profiles

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    client_profiles_representation_client_profiles_representation = openapi_client.ClientProfilesRepresentation() # client_profiles_representation.ClientProfilesRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/client-policies/profiles
        api_response = api_instance.admin_realms_realm_client_policies_profiles_put(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_client_policies_profiles_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /admin/realms/{realm}/client-policies/profiles
        api_response = api_instance.admin_realms_realm_client_policies_profiles_put(realm, client_profiles_representation_client_profiles_representation=client_profiles_representation_client_profiles_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_client_policies_profiles_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_profiles_representation_client_profiles_representation** | [**client_profiles_representation.ClientProfilesRepresentation**](ClientProfilesRepresentation.md)|  | [optional]

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

# **admin_realms_realm_client_session_stats_get**
> [{str: (str,)}] admin_realms_realm_client_session_stats_get(realm)

Get client session stats Returns a JSON map.

The key is the client id, the value is the number of sessions that currently are active with that client. Only clients that actually have a session associated with them will be in this map.

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get client session stats Returns a JSON map.
        api_response = api_instance.admin_realms_realm_client_session_stats_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_client_session_stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

**[{str: (str,)}]**

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

# **admin_realms_realm_client_types_get**
> client_types_representation.ClientTypesRepresentation admin_realms_realm_client_types_get(realm)

List all client types available in the current realm

This endpoint returns a list of both global and realm level client types and the attributes they set

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # List all client types available in the current realm
        api_response = api_instance.admin_realms_realm_client_types_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_client_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

[**client_types_representation.ClientTypesRepresentation**](ClientTypesRepresentation.md)

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

# **admin_realms_realm_client_types_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_client_types_put(realm)

Update a client type

This endpoint allows you to update a realm level client type

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    client_types_representation_client_types_representation = openapi_client.ClientTypesRepresentation() # client_types_representation.ClientTypesRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a client type
        api_response = api_instance.admin_realms_realm_client_types_put(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_client_types_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a client type
        api_response = api_instance.admin_realms_realm_client_types_put(realm, client_types_representation_client_types_representation=client_types_representation_client_types_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_client_types_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_types_representation_client_types_representation** | [**client_types_representation.ClientTypesRepresentation**](ClientTypesRepresentation.md)|  | [optional]

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_credential_registrators_get**
> [str] admin_realms_realm_credential_registrators_get(realm)

/admin/realms/{realm}/credential-registrators

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/credential-registrators
        api_response = api_instance.admin_realms_realm_credential_registrators_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_credential_registrators_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

**[str]**

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

# **admin_realms_realm_default_default_client_scopes_client_scope_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_default_default_client_scopes_client_scope_id_delete(client_scope_id, realm)

/admin/realms/{realm}/default-default-client-scopes/{clientScopeId}

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    client_scope_id = 'client_scope_id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/default-default-client-scopes/{clientScopeId}
        api_response = api_instance.admin_realms_realm_default_default_client_scopes_client_scope_id_delete(client_scope_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_default_default_client_scopes_client_scope_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_scope_id** | **str**|  |
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

# **admin_realms_realm_default_default_client_scopes_client_scope_id_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_default_default_client_scopes_client_scope_id_put(client_scope_id, realm)

/admin/realms/{realm}/default-default-client-scopes/{clientScopeId}

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    client_scope_id = 'client_scope_id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/default-default-client-scopes/{clientScopeId}
        api_response = api_instance.admin_realms_realm_default_default_client_scopes_client_scope_id_put(client_scope_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_default_default_client_scopes_client_scope_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_scope_id** | **str**|  |
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

# **admin_realms_realm_default_default_client_scopes_get**
> [client_scope_representation.ClientScopeRepresentation] admin_realms_realm_default_default_client_scopes_get(realm)

Get realm default client scopes.  Only name and ids are returned.

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get realm default client scopes.  Only name and ids are returned.
        api_response = api_instance.admin_realms_realm_default_default_client_scopes_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_default_default_client_scopes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

[**[client_scope_representation.ClientScopeRepresentation]**](ClientScopeRepresentation.md)

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

# **admin_realms_realm_default_groups_get**
> [group_representation.GroupRepresentation] admin_realms_realm_default_groups_get(realm)

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get group hierarchy.  Only name and ids are returned.
        api_response = api_instance.admin_realms_realm_default_groups_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_default_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

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

# **admin_realms_realm_default_groups_group_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_default_groups_group_id_delete(group_id, realm)

/admin/realms/{realm}/default-groups/{groupId}

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    group_id = 'group_id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/default-groups/{groupId}
        api_response = api_instance.admin_realms_realm_default_groups_group_id_delete(group_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_default_groups_group_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  |
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

# **admin_realms_realm_default_groups_group_id_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_default_groups_group_id_put(group_id, realm)

/admin/realms/{realm}/default-groups/{groupId}

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    group_id = 'group_id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/default-groups/{groupId}
        api_response = api_instance.admin_realms_realm_default_groups_group_id_put(group_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_default_groups_group_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  |
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

# **admin_realms_realm_default_optional_client_scopes_client_scope_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_default_optional_client_scopes_client_scope_id_delete(client_scope_id, realm)

/admin/realms/{realm}/default-optional-client-scopes/{clientScopeId}

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    client_scope_id = 'client_scope_id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/default-optional-client-scopes/{clientScopeId}
        api_response = api_instance.admin_realms_realm_default_optional_client_scopes_client_scope_id_delete(client_scope_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_default_optional_client_scopes_client_scope_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_scope_id** | **str**|  |
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

# **admin_realms_realm_default_optional_client_scopes_client_scope_id_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_default_optional_client_scopes_client_scope_id_put(client_scope_id, realm)

/admin/realms/{realm}/default-optional-client-scopes/{clientScopeId}

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    client_scope_id = 'client_scope_id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/default-optional-client-scopes/{clientScopeId}
        api_response = api_instance.admin_realms_realm_default_optional_client_scopes_client_scope_id_put(client_scope_id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_default_optional_client_scopes_client_scope_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_scope_id** | **str**|  |
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

# **admin_realms_realm_default_optional_client_scopes_get**
> [client_scope_representation.ClientScopeRepresentation] admin_realms_realm_default_optional_client_scopes_get(realm)

Get realm optional client scopes.  Only name and ids are returned.

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get realm optional client scopes.  Only name and ids are returned.
        api_response = api_instance.admin_realms_realm_default_optional_client_scopes_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_default_optional_client_scopes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

[**[client_scope_representation.ClientScopeRepresentation]**](ClientScopeRepresentation.md)

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

# **admin_realms_realm_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_delete(realm)

Delete the realm

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete the realm
        api_response = api_instance.admin_realms_realm_delete(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_delete: %s\n" % e)
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

# **admin_realms_realm_events_config_get**
> realm_events_config_representation.RealmEventsConfigRepresentation admin_realms_realm_events_config_get(realm)

Get the events provider configuration Returns JSON object with events provider configuration

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get the events provider configuration Returns JSON object with events provider configuration
        api_response = api_instance.admin_realms_realm_events_config_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_events_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

[**realm_events_config_representation.RealmEventsConfigRepresentation**](RealmEventsConfigRepresentation.md)

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

# **admin_realms_realm_events_config_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_events_config_put(realm)

/admin/realms/{realm}/events/config

Update the events provider Change the events provider and/or its configuration

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    realm_events_config_representation_realm_events_config_representation = openapi_client.RealmEventsConfigRepresentation() # realm_events_config_representation.RealmEventsConfigRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/events/config
        api_response = api_instance.admin_realms_realm_events_config_put(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_events_config_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /admin/realms/{realm}/events/config
        api_response = api_instance.admin_realms_realm_events_config_put(realm, realm_events_config_representation_realm_events_config_representation=realm_events_config_representation_realm_events_config_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_events_config_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **realm_events_config_representation_realm_events_config_representation** | [**realm_events_config_representation.RealmEventsConfigRepresentation**](RealmEventsConfigRepresentation.md)|  | [optional]

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_events_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_events_delete(realm)

Delete all events

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete all events
        api_response = api_instance.admin_realms_realm_events_delete(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_events_delete: %s\n" % e)
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

# **admin_realms_realm_events_get**
> [event_representation.EventRepresentation] admin_realms_realm_events_get(realm)

Get events Returns all events, or filters them based on URL query parameters listed here

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    client = 'client_example' # str | App or oauth client name (optional)
date_from = 'date_from_example' # str | From date (optional)
date_to = 'date_to_example' # str | To date (optional)
first = 56 # int | Paging offset (optional)
ip_address = 'ip_address_example' # str | IP Address (optional)
max = 56 # int | Maximum results size (defaults to 100) (optional)
type = ['type_example'] # [str] | The types of events to return (optional)
user = 'user_example' # str | User id (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get events Returns all events, or filters them based on URL query parameters listed here
        api_response = api_instance.admin_realms_realm_events_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_events_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get events Returns all events, or filters them based on URL query parameters listed here
        api_response = api_instance.admin_realms_realm_events_get(realm, client=client, date_from=date_from, date_to=date_to, first=first, ip_address=ip_address, max=max, type=type, user=user)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client** | **str**| App or oauth client name | [optional]
 **date_from** | **str**| From date | [optional]
 **date_to** | **str**| To date | [optional]
 **first** | **int**| Paging offset | [optional]
 **ip_address** | **str**| IP Address | [optional]
 **max** | **int**| Maximum results size (defaults to 100) | [optional]
 **type** | **[str]**| The types of events to return | [optional]
 **user** | **str**| User id | [optional]

### Return type

[**[event_representation.EventRepresentation]**](EventRepresentation.md)

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

# **admin_realms_realm_get**
> realm_representation.RealmRepresentation admin_realms_realm_get(realm)

Get the top-level representation of the realm It will not include nested information like User and Client representations.

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get the top-level representation of the realm It will not include nested information like User and Client representations.
        api_response = api_instance.admin_realms_realm_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

[**realm_representation.RealmRepresentation**](RealmRepresentation.md)

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

# **admin_realms_realm_group_by_path_path_get**
> group_representation.GroupRepresentation admin_realms_realm_group_by_path_path_get(path, realm)

/admin/realms/{realm}/group-by-path/{path}

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    path = 'path_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/group-by-path/{path}
        api_response = api_instance.admin_realms_realm_group_by_path_path_get(path, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_group_by_path_path_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  |
 **realm** | **str**|  |

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

# **admin_realms_realm_localization_get**
> [str] admin_realms_realm_localization_get(realm)

/admin/realms/{realm}/localization

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/localization
        api_response = api_instance.admin_realms_realm_localization_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_localization_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

**[str]**

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

# **admin_realms_realm_localization_locale_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_localization_locale_delete(locale, realm)

/admin/realms/{realm}/localization/{locale}

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    locale = 'locale_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/localization/{locale}
        api_response = api_instance.admin_realms_realm_localization_locale_delete(locale, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_localization_locale_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**|  |
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

# **admin_realms_realm_localization_locale_get**
> {str: (str,)} admin_realms_realm_localization_locale_get(locale, realm)

/admin/realms/{realm}/localization/{locale}

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    locale = 'locale_example' # str | 
    realm = 'realm_example' # str | 
    use_realm_default_locale_fallback = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/localization/{locale}
        api_response = api_instance.admin_realms_realm_localization_locale_get(locale, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_localization_locale_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /admin/realms/{realm}/localization/{locale}
        api_response = api_instance.admin_realms_realm_localization_locale_get(locale, realm, use_realm_default_locale_fallback=use_realm_default_locale_fallback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_localization_locale_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**|  |
 **realm** | **str**|  |
 **use_realm_default_locale_fallback** | **bool**|  | [optional]

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

# **admin_realms_realm_localization_locale_key_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_localization_locale_key_delete(key, locale, realm)

/admin/realms/{realm}/localization/{locale}/{key}

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    key = 'key_example' # str | 
    locale = 'locale_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/localization/{locale}/{key}
        api_response = api_instance.admin_realms_realm_localization_locale_key_delete(key, locale, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_localization_locale_key_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  |
 **locale** | **str**|  |
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

# **admin_realms_realm_localization_locale_key_get**
> str admin_realms_realm_localization_locale_key_get(key, locale, realm)

/admin/realms/{realm}/localization/{locale}/{key}

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    key = 'key_example' # str | 
    locale = 'locale_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/localization/{locale}/{key}
        api_response = api_instance.admin_realms_realm_localization_locale_key_get(key, locale, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_localization_locale_key_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  |
 **locale** | **str**|  |
 **realm** | **str**|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_localization_locale_key_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_localization_locale_key_put(key, locale, realm)

/admin/realms/{realm}/localization/{locale}/{key}

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    key = 'key_example' # str | 
    locale = 'locale_example' # str | 
    realm = 'realm_example' # str | 
    body = 'body_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/localization/{locale}/{key}
        api_response = api_instance.admin_realms_realm_localization_locale_key_put(key, locale, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_localization_locale_key_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /admin/realms/{realm}/localization/{locale}/{key}
        api_response = api_instance.admin_realms_realm_localization_locale_key_put(key, locale, realm, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_localization_locale_key_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  |
 **locale** | **str**|  |
 **realm** | **str**|  |
 **body** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_localization_locale_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_localization_locale_post(locale, realm)

Import localization from uploaded JSON file

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    locale = 'locale_example' # str | 
    realm = 'realm_example' # str | 
    request_body = {'key': 'request_body_example'} # {str: (str,)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import localization from uploaded JSON file
        api_response = api_instance.admin_realms_realm_localization_locale_post(locale, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_localization_locale_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import localization from uploaded JSON file
        api_response = api_instance.admin_realms_realm_localization_locale_post(locale, realm, request_body=request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_localization_locale_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**|  |
 **realm** | **str**|  |
 **request_body** | **{str: (str,)}**|  | [optional]

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_logout_all_post**
> global_request_result.GlobalRequestResult admin_realms_realm_logout_all_post(realm)

Removes all user sessions.

Any client that has an admin url will also be told to invalidate any sessions they have.

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Removes all user sessions.
        api_response = api_instance.admin_realms_realm_logout_all_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_logout_all_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

[**global_request_result.GlobalRequestResult**](GlobalRequestResult.md)

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

# **admin_realms_realm_partial_export_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_partial_export_post(realm)

Partial export of existing realm into a JSON file.

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    export_clients = True # bool |  (optional)
export_groups_and_roles = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Partial export of existing realm into a JSON file.
        api_response = api_instance.admin_realms_realm_partial_export_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_partial_export_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Partial export of existing realm into a JSON file.
        api_response = api_instance.admin_realms_realm_partial_export_post(realm, export_clients=export_clients, export_groups_and_roles=export_groups_and_roles)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_partial_export_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **export_clients** | **bool**|  | [optional]
 **export_groups_and_roles** | **bool**|  | [optional]

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_partial_import_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_partial_import_post(realm)

Partial import from a JSON file to an existing realm.

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    body = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Partial import from a JSON file to an existing realm.
        api_response = api_instance.admin_realms_realm_partial_import_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_partial_import_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Partial import from a JSON file to an existing realm.
        api_response = api_instance.admin_realms_realm_partial_import_post(realm, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_partial_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **body** | **file_type**|  | [optional]

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

# **admin_realms_realm_push_revocation_post**
> global_request_result.GlobalRequestResult admin_realms_realm_push_revocation_post(realm)

Push the realm's revocation policy to any client that has an admin url associated with it.

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Push the realm's revocation policy to any client that has an admin url associated with it.
        api_response = api_instance.admin_realms_realm_push_revocation_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_push_revocation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

[**global_request_result.GlobalRequestResult**](GlobalRequestResult.md)

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

# **admin_realms_realm_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_put(realm)

Update the top-level information of the realm Any user, roles or client information in the representation will be ignored.

This will only update top-level attributes of the realm.

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    realm_representation_realm_representation = openapi_client.RealmRepresentation() # realm_representation.RealmRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the top-level information of the realm Any user, roles or client information in the representation will be ignored.
        api_response = api_instance.admin_realms_realm_put(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the top-level information of the realm Any user, roles or client information in the representation will be ignored.
        api_response = api_instance.admin_realms_realm_put(realm, realm_representation_realm_representation=realm_representation_realm_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **realm_representation_realm_representation** | [**realm_representation.RealmRepresentation**](RealmRepresentation.md)|  | [optional]

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

# **admin_realms_realm_sessions_session_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_sessions_session_delete(session, realm)

Remove a specific user session.

Any client that has an admin url will also be told to invalidate this particular session.

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    session = 'session_example' # str | 
    realm = 'realm_example' # str | 
    is_offline = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Remove a specific user session.
        api_response = api_instance.admin_realms_realm_sessions_session_delete(session, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_sessions_session_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove a specific user session.
        api_response = api_instance.admin_realms_realm_sessions_session_delete(session, realm, is_offline=is_offline)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_sessions_session_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session** | **str**|  |
 **realm** | **str**|  |
 **is_offline** | **bool**|  | [optional] if omitted the server will use the default value of False

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

# **admin_realms_realm_test_smtp_connection_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_test_smtp_connection_post(realm)

Test SMTP connection with current logged in user

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    config = 'config_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Test SMTP connection with current logged in user
        api_response = api_instance.admin_realms_realm_test_smtp_connection_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_test_smtp_connection_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Test SMTP connection with current logged in user
        api_response = api_instance.admin_realms_realm_test_smtp_connection_post(realm, config=config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_test_smtp_connection_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **config** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_users_management_permissions_get**
> management_permission_reference.ManagementPermissionReference admin_realms_realm_users_management_permissions_get(realm)

/admin/realms/{realm}/users-management-permissions

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/users-management-permissions
        api_response = api_instance.admin_realms_realm_users_management_permissions_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_users_management_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

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

# **admin_realms_realm_users_management_permissions_put**
> management_permission_reference.ManagementPermissionReference admin_realms_realm_users_management_permissions_put(realm)

/admin/realms/{realm}/users-management-permissions

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
    api_instance = openapi_client.RealmsAdminApi(api_client)
    realm = 'realm_example' # str | 
    management_permission_reference_management_permission_reference = openapi_client.ManagementPermissionReference() # management_permission_reference.ManagementPermissionReference |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/users-management-permissions
        api_response = api_instance.admin_realms_realm_users_management_permissions_put(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_users_management_permissions_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /admin/realms/{realm}/users-management-permissions
        api_response = api_instance.admin_realms_realm_users_management_permissions_put(realm, management_permission_reference_management_permission_reference=management_permission_reference_management_permission_reference)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_realm_users_management_permissions_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
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

