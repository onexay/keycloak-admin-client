# openapi_client.KeycloakAdminUsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_realm_users_count_get**](KeycloakAdminUsersApi.md#admin_realms_realm_users_count_get) | **GET** /admin/realms/{realm}/users/count | Returns the number of users that match the given criteria.
[**admin_realms_realm_users_get**](KeycloakAdminUsersApi.md#admin_realms_realm_users_get) | **GET** /admin/realms/{realm}/users | Get users Returns a stream of users, filtered according to query parameters.
[**admin_realms_realm_users_post**](KeycloakAdminUsersApi.md#admin_realms_realm_users_post) | **POST** /admin/realms/{realm}/users | Create a new user Username must be unique.
[**admin_realms_realm_users_profile_get**](KeycloakAdminUsersApi.md#admin_realms_realm_users_profile_get) | **GET** /admin/realms/{realm}/users/profile | /admin/realms/{realm}/users/profile
[**admin_realms_realm_users_profile_metadata_get**](KeycloakAdminUsersApi.md#admin_realms_realm_users_profile_metadata_get) | **GET** /admin/realms/{realm}/users/profile/metadata | /admin/realms/{realm}/users/profile/metadata
[**admin_realms_realm_users_profile_put**](KeycloakAdminUsersApi.md#admin_realms_realm_users_profile_put) | **PUT** /admin/realms/{realm}/users/profile | /admin/realms/{realm}/users/profile
[**admin_realms_realm_users_user_id_configured_user_storage_credential_types_get**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_configured_user_storage_credential_types_get) | **GET** /admin/realms/{realm}/users/{user-id}/configured-user-storage-credential-types | Return credential types, which are provided by the user storage where user is stored.
[**admin_realms_realm_users_user_id_consents_client_delete**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_consents_client_delete) | **DELETE** /admin/realms/{realm}/users/{user-id}/consents/{client} | Revoke consent and offline tokens for particular client from user
[**admin_realms_realm_users_user_id_consents_get**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_consents_get) | **GET** /admin/realms/{realm}/users/{user-id}/consents | Get consents granted by the user
[**admin_realms_realm_users_user_id_credentials_credential_id_delete**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_credentials_credential_id_delete) | **DELETE** /admin/realms/{realm}/users/{user-id}/credentials/{credentialId} | Remove a credential for a user
[**admin_realms_realm_users_user_id_credentials_credential_id_move_after_new_previous_credential_id_post**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_credentials_credential_id_move_after_new_previous_credential_id_post) | **POST** /admin/realms/{realm}/users/{user-id}/credentials/{credentialId}/moveAfter/{newPreviousCredentialId} | Move a credential to a position behind another credential
[**admin_realms_realm_users_user_id_credentials_credential_id_move_to_first_post**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_credentials_credential_id_move_to_first_post) | **POST** /admin/realms/{realm}/users/{user-id}/credentials/{credentialId}/moveToFirst | Move a credential to a first position in the credentials list of the user
[**admin_realms_realm_users_user_id_credentials_credential_id_user_label_put**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_credentials_credential_id_user_label_put) | **PUT** /admin/realms/{realm}/users/{user-id}/credentials/{credentialId}/userLabel | Update a credential label for a user
[**admin_realms_realm_users_user_id_credentials_get**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_credentials_get) | **GET** /admin/realms/{realm}/users/{user-id}/credentials | /admin/realms/{realm}/users/{user-id}/credentials
[**admin_realms_realm_users_user_id_delete**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_delete) | **DELETE** /admin/realms/{realm}/users/{user-id} | Delete the user
[**admin_realms_realm_users_user_id_disable_credential_types_put**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_disable_credential_types_put) | **PUT** /admin/realms/{realm}/users/{user-id}/disable-credential-types | Disable all credentials for a user of a specific type
[**admin_realms_realm_users_user_id_execute_actions_email_put**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_execute_actions_email_put) | **PUT** /admin/realms/{realm}/users/{user-id}/execute-actions-email | Send an email to the user with a link they can click to execute particular actions.
[**admin_realms_realm_users_user_id_federated_identity_get**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_federated_identity_get) | **GET** /admin/realms/{realm}/users/{user-id}/federated-identity | Get social logins associated with the user
[**admin_realms_realm_users_user_id_federated_identity_provider_delete**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_federated_identity_provider_delete) | **DELETE** /admin/realms/{realm}/users/{user-id}/federated-identity/{provider} | Remove a social login provider from user
[**admin_realms_realm_users_user_id_federated_identity_provider_post**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_federated_identity_provider_post) | **POST** /admin/realms/{realm}/users/{user-id}/federated-identity/{provider} | Add a social login provider to the user
[**admin_realms_realm_users_user_id_get**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_get) | **GET** /admin/realms/{realm}/users/{user-id} | Get representation of the user
[**admin_realms_realm_users_user_id_groups_count_get**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_groups_count_get) | **GET** /admin/realms/{realm}/users/{user-id}/groups/count | /admin/realms/{realm}/users/{user-id}/groups/count
[**admin_realms_realm_users_user_id_groups_get**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_groups_get) | **GET** /admin/realms/{realm}/users/{user-id}/groups | /admin/realms/{realm}/users/{user-id}/groups
[**admin_realms_realm_users_user_id_groups_group_id_delete**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_groups_group_id_delete) | **DELETE** /admin/realms/{realm}/users/{user-id}/groups/{groupId} | /admin/realms/{realm}/users/{user-id}/groups/{groupId}
[**admin_realms_realm_users_user_id_groups_group_id_put**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_groups_group_id_put) | **PUT** /admin/realms/{realm}/users/{user-id}/groups/{groupId} | /admin/realms/{realm}/users/{user-id}/groups/{groupId}
[**admin_realms_realm_users_user_id_impersonation_post**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_impersonation_post) | **POST** /admin/realms/{realm}/users/{user-id}/impersonation | Impersonate the user
[**admin_realms_realm_users_user_id_logout_post**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_logout_post) | **POST** /admin/realms/{realm}/users/{user-id}/logout | Remove all user sessions associated with the user Also send notification to all clients that have an admin URL to invalidate the sessions for the particular user.
[**admin_realms_realm_users_user_id_offline_sessions_client_uuid_get**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_offline_sessions_client_uuid_get) | **GET** /admin/realms/{realm}/users/{user-id}/offline-sessions/{clientUuid} | Get offline sessions associated with the user and client
[**admin_realms_realm_users_user_id_put**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_put) | **PUT** /admin/realms/{realm}/users/{user-id} | Update the user
[**admin_realms_realm_users_user_id_reset_password_email_put**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_reset_password_email_put) | **PUT** /admin/realms/{realm}/users/{user-id}/reset-password-email | Send an email to the user with a link they can click to reset their password.
[**admin_realms_realm_users_user_id_reset_password_put**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_reset_password_put) | **PUT** /admin/realms/{realm}/users/{user-id}/reset-password | Set up a new password for the user.
[**admin_realms_realm_users_user_id_send_verify_email_put**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_send_verify_email_put) | **PUT** /admin/realms/{realm}/users/{user-id}/send-verify-email | Send an email-verification email to the user An email contains a link the user can click to verify their email address.
[**admin_realms_realm_users_user_id_sessions_get**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_sessions_get) | **GET** /admin/realms/{realm}/users/{user-id}/sessions | Get sessions associated with the user
[**admin_realms_realm_users_user_id_unmanaged_attributes_get**](KeycloakAdminUsersApi.md#admin_realms_realm_users_user_id_unmanaged_attributes_get) | **GET** /admin/realms/{realm}/users/{user-id}/unmanagedAttributes | /admin/realms/{realm}/users/{user-id}/unmanagedAttributes


# **admin_realms_realm_users_count_get**
> int admin_realms_realm_users_count_get(realm)

Returns the number of users that match the given criteria.

It can be called in three different ways. 1. Don’t specify any criteria and pass {@code null}. The number of all users within that realm will be returned. <p> 2. If {@code search} is specified other criteria such as {@code last} will be ignored even though you set them. The {@code search} string will be matched against the first and last name, the username and the email of a user. <p> 3. If {@code search} is unspecified but any of {@code last}, {@code first}, {@code email} or {@code username} those criteria are matched against their respective fields on a user entity. Combined with a logical and.

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    email = 'email_example' # str | email filter (optional)
email_verified = True # bool |  (optional)
enabled = True # bool | Boolean representing if user is enabled or not (optional)
first_name = 'first_name_example' # str | first name filter (optional)
last_name = 'last_name_example' # str | last name filter (optional)
q = 'q_example' # str |  (optional)
search = 'search_example' # str | arbitrary search string for all the fields below. Default search behavior is prefix-based (e.g., foo or foo*). Use *foo* for infix search and \"foo\" for exact search. (optional)
username = 'username_example' # str | username filter (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns the number of users that match the given criteria.
        api_response = api_instance.admin_realms_realm_users_count_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_count_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the number of users that match the given criteria.
        api_response = api_instance.admin_realms_realm_users_count_get(realm, email=email, email_verified=email_verified, enabled=enabled, first_name=first_name, last_name=last_name, q=q, search=search, username=username)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **email** | **str**| email filter | [optional]
 **email_verified** | **bool**|  | [optional]
 **enabled** | **bool**| Boolean representing if user is enabled or not | [optional]
 **first_name** | **str**| first name filter | [optional]
 **last_name** | **str**| last name filter | [optional]
 **q** | **str**|  | [optional]
 **search** | **str**| arbitrary search string for all the fields below. Default search behavior is prefix-based (e.g., foo or foo*). Use *foo* for infix search and \&quot;foo\&quot; for exact search. | [optional]
 **username** | **str**| username filter | [optional]

### Return type

**int**

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

# **admin_realms_realm_users_get**
> [user_representation.UserRepresentation] admin_realms_realm_users_get(realm)

Get users Returns a stream of users, filtered according to query parameters.

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    brief_representation = True # bool | Boolean which defines whether brief representations are returned (default: false) (optional)
email = 'email_example' # str | A String contained in email, or the complete email, if param \"exact\" is true (optional)
email_verified = True # bool | whether the email has been verified (optional)
enabled = True # bool | Boolean representing if user is enabled or not (optional)
exact = True # bool | Boolean which defines whether the params \"last\", \"first\", \"email\" and \"username\" must match exactly (optional)
first = 56 # int | Pagination offset (optional)
first_name = 'first_name_example' # str | A String contained in firstName, or the complete firstName, if param \"exact\" is true (optional)
idp_alias = 'idp_alias_example' # str | The alias of an Identity Provider linked to the user (optional)
idp_user_id = 'idp_user_id_example' # str | The userId at an Identity Provider linked to the user (optional)
last_name = 'last_name_example' # str | A String contained in lastName, or the complete lastName, if param \"exact\" is true (optional)
max = 56 # int | Maximum results size (defaults to 100) (optional)
q = 'q_example' # str | A query to search for custom attributes, in the format 'key1:value2 key2:value2' (optional)
search = 'search_example' # str | A String contained in username, first or last name, or email. Default search behavior is prefix-based (e.g., foo or foo*). Use *foo* for infix search and \"foo\" for exact search. (optional)
username = 'username_example' # str | A String contained in username, or the complete username, if param \"exact\" is true (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get users Returns a stream of users, filtered according to query parameters.
        api_response = api_instance.admin_realms_realm_users_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get users Returns a stream of users, filtered according to query parameters.
        api_response = api_instance.admin_realms_realm_users_get(realm, brief_representation=brief_representation, email=email, email_verified=email_verified, enabled=enabled, exact=exact, first=first, first_name=first_name, idp_alias=idp_alias, idp_user_id=idp_user_id, last_name=last_name, max=max, q=q, search=search, username=username)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **brief_representation** | **bool**| Boolean which defines whether brief representations are returned (default: false) | [optional]
 **email** | **str**| A String contained in email, or the complete email, if param \&quot;exact\&quot; is true | [optional]
 **email_verified** | **bool**| whether the email has been verified | [optional]
 **enabled** | **bool**| Boolean representing if user is enabled or not | [optional]
 **exact** | **bool**| Boolean which defines whether the params \&quot;last\&quot;, \&quot;first\&quot;, \&quot;email\&quot; and \&quot;username\&quot; must match exactly | [optional]
 **first** | **int**| Pagination offset | [optional]
 **first_name** | **str**| A String contained in firstName, or the complete firstName, if param \&quot;exact\&quot; is true | [optional]
 **idp_alias** | **str**| The alias of an Identity Provider linked to the user | [optional]
 **idp_user_id** | **str**| The userId at an Identity Provider linked to the user | [optional]
 **last_name** | **str**| A String contained in lastName, or the complete lastName, if param \&quot;exact\&quot; is true | [optional]
 **max** | **int**| Maximum results size (defaults to 100) | [optional]
 **q** | **str**| A query to search for custom attributes, in the format &#39;key1:value2 key2:value2&#39; | [optional]
 **search** | **str**| A String contained in username, first or last name, or email. Default search behavior is prefix-based (e.g., foo or foo*). Use *foo* for infix search and \&quot;foo\&quot; for exact search. | [optional]
 **username** | **str**| A String contained in username, or the complete username, if param \&quot;exact\&quot; is true | [optional]

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

# **admin_realms_realm_users_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_post(realm)

Create a new user Username must be unique.

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_representation_user_representation = openapi_client.UserRepresentation() # user_representation.UserRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new user Username must be unique.
        api_response = api_instance.admin_realms_realm_users_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new user Username must be unique.
        api_response = api_instance.admin_realms_realm_users_post(realm, user_representation_user_representation=user_representation_user_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_representation_user_representation** | [**user_representation.UserRepresentation**](UserRepresentation.md)|  | [optional]

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

# **admin_realms_realm_users_profile_get**
> up_config.UpConfig admin_realms_realm_users_profile_get(realm)

/admin/realms/{realm}/users/profile

Get the configuration for the user profile

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/users/profile
        api_response = api_instance.admin_realms_realm_users_profile_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_profile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

[**up_config.UpConfig**](UpConfig.md)

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

# **admin_realms_realm_users_profile_metadata_get**
> user_profile_metadata.UserProfileMetadata admin_realms_realm_users_profile_metadata_get(realm)

/admin/realms/{realm}/users/profile/metadata

Get the UserProfileMetadata from the configuration

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/users/profile/metadata
        api_response = api_instance.admin_realms_realm_users_profile_metadata_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_profile_metadata_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |

### Return type

[**user_profile_metadata.UserProfileMetadata**](UserProfileMetadata.md)

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

# **admin_realms_realm_users_profile_put**
> up_config.UpConfig admin_realms_realm_users_profile_put(realm)

/admin/realms/{realm}/users/profile

Set the configuration for the user profile

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    up_config_up_config = openapi_client.UpConfig() # up_config.UpConfig |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/users/profile
        api_response = api_instance.admin_realms_realm_users_profile_put(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_profile_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /admin/realms/{realm}/users/profile
        api_response = api_instance.admin_realms_realm_users_profile_put(realm, up_config_up_config=up_config_up_config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_profile_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **up_config_up_config** | [**up_config.UpConfig**](UpConfig.md)|  | [optional]

### Return type

[**up_config.UpConfig**](UpConfig.md)

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

# **admin_realms_realm_users_user_id_configured_user_storage_credential_types_get**
> [str] admin_realms_realm_users_user_id_configured_user_storage_credential_types_get(realm, user_id)

Return credential types, which are provided by the user storage where user is stored.

Returned values can contain for example \"password\", \"otp\" etc. This will always return empty list for \"local\" users, which are not backed by any user storage

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Return credential types, which are provided by the user storage where user is stored.
        api_response = api_instance.admin_realms_realm_users_user_id_configured_user_storage_credential_types_get(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_configured_user_storage_credential_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |

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

# **admin_realms_realm_users_user_id_consents_client_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_consents_client_delete(client, realm, user_id)

Revoke consent and offline tokens for particular client from user

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    client = 'client_example' # str | Client id
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Revoke consent and offline tokens for particular client from user
        api_response = api_instance.admin_realms_realm_users_user_id_consents_client_delete(client, realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_consents_client_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | **str**| Client id |
 **realm** | **str**|  |
 **user_id** | **str**|  |

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

# **admin_realms_realm_users_user_id_consents_get**
> [{str: (str,)}] admin_realms_realm_users_user_id_consents_get(realm, user_id)

Get consents granted by the user

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get consents granted by the user
        api_response = api_instance.admin_realms_realm_users_user_id_consents_get(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_consents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |

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

# **admin_realms_realm_users_user_id_credentials_credential_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_credentials_credential_id_delete(credential_id, realm, user_id)

Remove a credential for a user

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    credential_id = 'credential_id_example' # str | 
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Remove a credential for a user
        api_response = api_instance.admin_realms_realm_users_user_id_credentials_credential_id_delete(credential_id, realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_credentials_credential_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  |
 **realm** | **str**|  |
 **user_id** | **str**|  |

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

# **admin_realms_realm_users_user_id_credentials_credential_id_move_after_new_previous_credential_id_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_credentials_credential_id_move_after_new_previous_credential_id_post(credential_id, new_previous_credential_id, realm, user_id)

Move a credential to a position behind another credential

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    credential_id = 'credential_id_example' # str | The credential to move
    new_previous_credential_id = 'new_previous_credential_id_example' # str | The credential that will be the previous element in the list. If set to null, the moved credential will be the first element in the list.
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Move a credential to a position behind another credential
        api_response = api_instance.admin_realms_realm_users_user_id_credentials_credential_id_move_after_new_previous_credential_id_post(credential_id, new_previous_credential_id, realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_credentials_credential_id_move_after_new_previous_credential_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**| The credential to move |
 **new_previous_credential_id** | **str**| The credential that will be the previous element in the list. If set to null, the moved credential will be the first element in the list. |
 **realm** | **str**|  |
 **user_id** | **str**|  |

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

# **admin_realms_realm_users_user_id_credentials_credential_id_move_to_first_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_credentials_credential_id_move_to_first_post(credential_id, realm, user_id)

Move a credential to a first position in the credentials list of the user

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    credential_id = 'credential_id_example' # str | The credential to move
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Move a credential to a first position in the credentials list of the user
        api_response = api_instance.admin_realms_realm_users_user_id_credentials_credential_id_move_to_first_post(credential_id, realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_credentials_credential_id_move_to_first_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**| The credential to move |
 **realm** | **str**|  |
 **user_id** | **str**|  |

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

# **admin_realms_realm_users_user_id_credentials_credential_id_user_label_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_credentials_credential_id_user_label_put(credential_id, realm, user_id)

Update a credential label for a user

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    credential_id = 'credential_id_example' # str | 
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    body = 'body_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a credential label for a user
        api_response = api_instance.admin_realms_realm_users_user_id_credentials_credential_id_user_label_put(credential_id, realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_credentials_credential_id_user_label_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a credential label for a user
        api_response = api_instance.admin_realms_realm_users_user_id_credentials_credential_id_user_label_put(credential_id, realm, user_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_credentials_credential_id_user_label_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  |
 **realm** | **str**|  |
 **user_id** | **str**|  |
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

# **admin_realms_realm_users_user_id_credentials_get**
> [credential_representation.CredentialRepresentation] admin_realms_realm_users_user_id_credentials_get(realm, user_id)

/admin/realms/{realm}/users/{user-id}/credentials

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/users/{user-id}/credentials
        api_response = api_instance.admin_realms_realm_users_user_id_credentials_get(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_credentials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |

### Return type

[**[credential_representation.CredentialRepresentation]**](CredentialRepresentation.md)

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

# **admin_realms_realm_users_user_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_delete(realm, user_id)

Delete the user

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Delete the user
        api_response = api_instance.admin_realms_realm_users_user_id_delete(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |

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

# **admin_realms_realm_users_user_id_disable_credential_types_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_disable_credential_types_put(realm, user_id)

Disable all credentials for a user of a specific type

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    request_body = ['request_body_example'] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Disable all credentials for a user of a specific type
        api_response = api_instance.admin_realms_realm_users_user_id_disable_credential_types_put(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_disable_credential_types_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Disable all credentials for a user of a specific type
        api_response = api_instance.admin_realms_realm_users_user_id_disable_credential_types_put(realm, user_id, request_body=request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_disable_credential_types_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |
 **request_body** | **[str]**|  | [optional]

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

# **admin_realms_realm_users_user_id_execute_actions_email_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_execute_actions_email_put(realm, user_id)

Send an email to the user with a link they can click to execute particular actions.

An email contains a link the user can click to perform a set of required actions. The redirectUri and clientId parameters are optional. If no redirect is given, then there will be no link back to click after actions have completed. Redirect uri must be a valid uri for the particular clientId.

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    client_id = 'client_id_example' # str | Client id (optional)
lifespan = 56 # int | Number of seconds after which the generated token expires (optional)
redirect_uri = 'redirect_uri_example' # str | Redirect uri (optional)
request_body = ['request_body_example'] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send an email to the user with a link they can click to execute particular actions.
        api_response = api_instance.admin_realms_realm_users_user_id_execute_actions_email_put(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_execute_actions_email_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an email to the user with a link they can click to execute particular actions.
        api_response = api_instance.admin_realms_realm_users_user_id_execute_actions_email_put(realm, user_id, client_id=client_id, lifespan=lifespan, redirect_uri=redirect_uri, request_body=request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_execute_actions_email_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |
 **client_id** | **str**| Client id | [optional]
 **lifespan** | **int**| Number of seconds after which the generated token expires | [optional]
 **redirect_uri** | **str**| Redirect uri | [optional]
 **request_body** | **[str]**|  | [optional]

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

# **admin_realms_realm_users_user_id_federated_identity_get**
> [federated_identity_representation.FederatedIdentityRepresentation] admin_realms_realm_users_user_id_federated_identity_get(realm, user_id)

Get social logins associated with the user

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get social logins associated with the user
        api_response = api_instance.admin_realms_realm_users_user_id_federated_identity_get(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_federated_identity_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |

### Return type

[**[federated_identity_representation.FederatedIdentityRepresentation]**](FederatedIdentityRepresentation.md)

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

# **admin_realms_realm_users_user_id_federated_identity_provider_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_federated_identity_provider_delete(provider, realm, user_id)

Remove a social login provider from user

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    provider = 'provider_example' # str | Social login provider id
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Remove a social login provider from user
        api_response = api_instance.admin_realms_realm_users_user_id_federated_identity_provider_delete(provider, realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_federated_identity_provider_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| Social login provider id |
 **realm** | **str**|  |
 **user_id** | **str**|  |

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

# **admin_realms_realm_users_user_id_federated_identity_provider_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_federated_identity_provider_post(provider, realm, user_id)

Add a social login provider to the user

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    provider = 'provider_example' # str | Social login provider id
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Add a social login provider to the user
        api_response = api_instance.admin_realms_realm_users_user_id_federated_identity_provider_post(provider, realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_federated_identity_provider_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| Social login provider id |
 **realm** | **str**|  |
 **user_id** | **str**|  |

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

# **admin_realms_realm_users_user_id_get**
> user_representation.UserRepresentation admin_realms_realm_users_user_id_get(realm, user_id)

Get representation of the user

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    user_profile_metadata = True # bool | Indicates if the user profile metadata should be added to the response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get representation of the user
        api_response = api_instance.admin_realms_realm_users_user_id_get(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get representation of the user
        api_response = api_instance.admin_realms_realm_users_user_id_get(realm, user_id, user_profile_metadata=user_profile_metadata)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |
 **user_profile_metadata** | **bool**| Indicates if the user profile metadata should be added to the response | [optional]

### Return type

[**user_representation.UserRepresentation**](UserRepresentation.md)

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

# **admin_realms_realm_users_user_id_groups_count_get**
> {str: (int,)} admin_realms_realm_users_user_id_groups_count_get(realm, user_id)

/admin/realms/{realm}/users/{user-id}/groups/count

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    search = 'search_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/users/{user-id}/groups/count
        api_response = api_instance.admin_realms_realm_users_user_id_groups_count_get(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_groups_count_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /admin/realms/{realm}/users/{user-id}/groups/count
        api_response = api_instance.admin_realms_realm_users_user_id_groups_count_get(realm, user_id, search=search)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_groups_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |
 **search** | **str**|  | [optional]

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

# **admin_realms_realm_users_user_id_groups_get**
> [group_representation.GroupRepresentation] admin_realms_realm_users_user_id_groups_get(realm, user_id)

/admin/realms/{realm}/users/{user-id}/groups

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    brief_representation = True # bool |  (optional) if omitted the server will use the default value of True
first = 56 # int |  (optional)
max = 56 # int |  (optional)
search = 'search_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/users/{user-id}/groups
        api_response = api_instance.admin_realms_realm_users_user_id_groups_get(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_groups_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /admin/realms/{realm}/users/{user-id}/groups
        api_response = api_instance.admin_realms_realm_users_user_id_groups_get(realm, user_id, brief_representation=brief_representation, first=first, max=max, search=search)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |
 **brief_representation** | **bool**|  | [optional] if omitted the server will use the default value of True
 **first** | **int**|  | [optional]
 **max** | **int**|  | [optional]
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

# **admin_realms_realm_users_user_id_groups_group_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_groups_group_id_delete(group_id, realm, user_id)

/admin/realms/{realm}/users/{user-id}/groups/{groupId}

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    group_id = 'group_id_example' # str | 
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/users/{user-id}/groups/{groupId}
        api_response = api_instance.admin_realms_realm_users_user_id_groups_group_id_delete(group_id, realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_groups_group_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  |
 **realm** | **str**|  |
 **user_id** | **str**|  |

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

# **admin_realms_realm_users_user_id_groups_group_id_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_groups_group_id_put(group_id, realm, user_id)

/admin/realms/{realm}/users/{user-id}/groups/{groupId}

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    group_id = 'group_id_example' # str | 
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/users/{user-id}/groups/{groupId}
        api_response = api_instance.admin_realms_realm_users_user_id_groups_group_id_put(group_id, realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_groups_group_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  |
 **realm** | **str**|  |
 **user_id** | **str**|  |

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

# **admin_realms_realm_users_user_id_impersonation_post**
> {str: (str,)} admin_realms_realm_users_user_id_impersonation_post(realm, user_id)

Impersonate the user

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Impersonate the user
        api_response = api_instance.admin_realms_realm_users_user_id_impersonation_post(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_impersonation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |

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

# **admin_realms_realm_users_user_id_logout_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_logout_post(realm, user_id)

Remove all user sessions associated with the user Also send notification to all clients that have an admin URL to invalidate the sessions for the particular user.

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Remove all user sessions associated with the user Also send notification to all clients that have an admin URL to invalidate the sessions for the particular user.
        api_response = api_instance.admin_realms_realm_users_user_id_logout_post(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_logout_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |

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

# **admin_realms_realm_users_user_id_offline_sessions_client_uuid_get**
> [user_session_representation.UserSessionRepresentation] admin_realms_realm_users_user_id_offline_sessions_client_uuid_get(client_uuid, realm, user_id)

Get offline sessions associated with the user and client

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    client_uuid = 'client_uuid_example' # str | 
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get offline sessions associated with the user and client
        api_response = api_instance.admin_realms_realm_users_user_id_offline_sessions_client_uuid_get(client_uuid, realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_offline_sessions_client_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_uuid** | **str**|  |
 **realm** | **str**|  |
 **user_id** | **str**|  |

### Return type

[**[user_session_representation.UserSessionRepresentation]**](UserSessionRepresentation.md)

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

# **admin_realms_realm_users_user_id_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_put(realm, user_id)

Update the user

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    user_representation_user_representation = openapi_client.UserRepresentation() # user_representation.UserRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the user
        api_response = api_instance.admin_realms_realm_users_user_id_put(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the user
        api_response = api_instance.admin_realms_realm_users_user_id_put(realm, user_id, user_representation_user_representation=user_representation_user_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |
 **user_representation_user_representation** | [**user_representation.UserRepresentation**](UserRepresentation.md)|  | [optional]

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

# **admin_realms_realm_users_user_id_reset_password_email_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_reset_password_email_put(realm, user_id)

Send an email to the user with a link they can click to reset their password.

The redirectUri and clientId parameters are optional. The default for the redirect is the account client. This endpoint has been deprecated.  Please use the execute-actions-email passing a list with UPDATE_PASSWORD within it.

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    client_id = 'client_id_example' # str | client id (optional)
redirect_uri = 'redirect_uri_example' # str | redirect uri (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send an email to the user with a link they can click to reset their password.
        api_response = api_instance.admin_realms_realm_users_user_id_reset_password_email_put(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_reset_password_email_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an email to the user with a link they can click to reset their password.
        api_response = api_instance.admin_realms_realm_users_user_id_reset_password_email_put(realm, user_id, client_id=client_id, redirect_uri=redirect_uri)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_reset_password_email_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |
 **client_id** | **str**| client id | [optional]
 **redirect_uri** | **str**| redirect uri | [optional]

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

# **admin_realms_realm_users_user_id_reset_password_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_reset_password_put(realm, user_id)

Set up a new password for the user.

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    credential_representation_credential_representation = openapi_client.CredentialRepresentation() # credential_representation.CredentialRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set up a new password for the user.
        api_response = api_instance.admin_realms_realm_users_user_id_reset_password_put(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_reset_password_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set up a new password for the user.
        api_response = api_instance.admin_realms_realm_users_user_id_reset_password_put(realm, user_id, credential_representation_credential_representation=credential_representation_credential_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_reset_password_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |
 **credential_representation_credential_representation** | [**credential_representation.CredentialRepresentation**](CredentialRepresentation.md)|  | [optional]

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

# **admin_realms_realm_users_user_id_send_verify_email_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_users_user_id_send_verify_email_put(realm, user_id)

Send an email-verification email to the user An email contains a link the user can click to verify their email address.

The redirectUri, clientId and lifespan parameters are optional. The default for the redirect is the account client. The default for the lifespan is 12 hours

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    client_id = 'client_id_example' # str | Client id (optional)
lifespan = 56 # int | Number of seconds after which the generated token expires (optional)
redirect_uri = 'redirect_uri_example' # str | Redirect uri (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send an email-verification email to the user An email contains a link the user can click to verify their email address.
        api_response = api_instance.admin_realms_realm_users_user_id_send_verify_email_put(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_send_verify_email_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an email-verification email to the user An email contains a link the user can click to verify their email address.
        api_response = api_instance.admin_realms_realm_users_user_id_send_verify_email_put(realm, user_id, client_id=client_id, lifespan=lifespan, redirect_uri=redirect_uri)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_send_verify_email_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |
 **client_id** | **str**| Client id | [optional]
 **lifespan** | **int**| Number of seconds after which the generated token expires | [optional]
 **redirect_uri** | **str**| Redirect uri | [optional]

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

# **admin_realms_realm_users_user_id_sessions_get**
> [user_session_representation.UserSessionRepresentation] admin_realms_realm_users_user_id_sessions_get(realm, user_id)

Get sessions associated with the user

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get sessions associated with the user
        api_response = api_instance.admin_realms_realm_users_user_id_sessions_get(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_sessions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |

### Return type

[**[user_session_representation.UserSessionRepresentation]**](UserSessionRepresentation.md)

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

# **admin_realms_realm_users_user_id_unmanaged_attributes_get**
> {str: ([str],)} admin_realms_realm_users_user_id_unmanaged_attributes_get(realm, user_id)

/admin/realms/{realm}/users/{user-id}/unmanagedAttributes

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
    api_instance = openapi_client.KeycloakAdminUsersApi(api_client)
    realm = 'realm_example' # str | 
    user_id = 'user_id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # /admin/realms/{realm}/users/{user-id}/unmanagedAttributes
        api_response = api_instance.admin_realms_realm_users_user_id_unmanaged_attributes_get(realm, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KeycloakAdminUsersApi->admin_realms_realm_users_user_id_unmanaged_attributes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **user_id** | **str**|  |

### Return type

**{str: ([str],)}**

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

