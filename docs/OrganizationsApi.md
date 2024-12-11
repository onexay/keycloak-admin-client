# openapi_client.OrganizationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_realm_organizations_get**](OrganizationsApi.md#admin_realms_realm_organizations_get) | **GET** /admin/realms/{realm}/organizations | Returns a paginated list of organizations filtered according to the specified parameters
[**admin_realms_realm_organizations_id_delete**](OrganizationsApi.md#admin_realms_realm_organizations_id_delete) | **DELETE** /admin/realms/{realm}/organizations/{id} | Deletes the organization
[**admin_realms_realm_organizations_id_get**](OrganizationsApi.md#admin_realms_realm_organizations_id_get) | **GET** /admin/realms/{realm}/organizations/{id} | Returns the organization representation
[**admin_realms_realm_organizations_id_identity_providers_alias_delete**](OrganizationsApi.md#admin_realms_realm_organizations_id_identity_providers_alias_delete) | **DELETE** /admin/realms/{realm}/organizations/{id}/identity-providers/{alias} | Removes the identity provider with the specified alias from the organization
[**admin_realms_realm_organizations_id_identity_providers_alias_get**](OrganizationsApi.md#admin_realms_realm_organizations_id_identity_providers_alias_get) | **GET** /admin/realms/{realm}/organizations/{id}/identity-providers/{alias} | Returns the identity provider associated with the organization that has the specified alias
[**admin_realms_realm_organizations_id_identity_providers_get**](OrganizationsApi.md#admin_realms_realm_organizations_id_identity_providers_get) | **GET** /admin/realms/{realm}/organizations/{id}/identity-providers | Returns all identity providers associated with the organization
[**admin_realms_realm_organizations_id_identity_providers_post**](OrganizationsApi.md#admin_realms_realm_organizations_id_identity_providers_post) | **POST** /admin/realms/{realm}/organizations/{id}/identity-providers | Adds the identity provider with the specified id to the organization
[**admin_realms_realm_organizations_id_members_count_get**](OrganizationsApi.md#admin_realms_realm_organizations_id_members_count_get) | **GET** /admin/realms/{realm}/organizations/{id}/members/count | Returns number of members in the organization.
[**admin_realms_realm_organizations_id_members_get**](OrganizationsApi.md#admin_realms_realm_organizations_id_members_get) | **GET** /admin/realms/{realm}/organizations/{id}/members | Returns a paginated list of organization members filtered according to the specified parameters
[**admin_realms_realm_organizations_id_members_id_delete**](OrganizationsApi.md#admin_realms_realm_organizations_id_members_id_delete) | **DELETE** /admin/realms/{realm}/organizations/{id}/members/{id} | Removes the user with the specified id from the organization
[**admin_realms_realm_organizations_id_members_id_get**](OrganizationsApi.md#admin_realms_realm_organizations_id_members_id_get) | **GET** /admin/realms/{realm}/organizations/{id}/members/{id} | Returns the member of the organization with the specified id
[**admin_realms_realm_organizations_id_members_id_organizations_get**](OrganizationsApi.md#admin_realms_realm_organizations_id_members_id_organizations_get) | **GET** /admin/realms/{realm}/organizations/{id}/members/{id}/organizations | Returns the organizations associated with the user that has the specified id
[**admin_realms_realm_organizations_id_members_invite_existing_user_post**](OrganizationsApi.md#admin_realms_realm_organizations_id_members_invite_existing_user_post) | **POST** /admin/realms/{realm}/organizations/{id}/members/invite-existing-user | Invites an existing user to the organization, using the specified user id
[**admin_realms_realm_organizations_id_members_invite_user_post**](OrganizationsApi.md#admin_realms_realm_organizations_id_members_invite_user_post) | **POST** /admin/realms/{realm}/organizations/{id}/members/invite-user | Invites an existing user or sends a registration link to a new user, based on the provided e-mail address.
[**admin_realms_realm_organizations_id_members_post**](OrganizationsApi.md#admin_realms_realm_organizations_id_members_post) | **POST** /admin/realms/{realm}/organizations/{id}/members | Adds the user with the specified id as a member of the organization
[**admin_realms_realm_organizations_id_put**](OrganizationsApi.md#admin_realms_realm_organizations_id_put) | **PUT** /admin/realms/{realm}/organizations/{id} | Updates the organization
[**admin_realms_realm_organizations_members_id_organizations_get**](OrganizationsApi.md#admin_realms_realm_organizations_members_id_organizations_get) | **GET** /admin/realms/{realm}/organizations/members/{id}/organizations | Returns the organizations associated with the user that has the specified id
[**admin_realms_realm_organizations_post**](OrganizationsApi.md#admin_realms_realm_organizations_post) | **POST** /admin/realms/{realm}/organizations | Creates a new organization


# **admin_realms_realm_organizations_get**
> [organization_representation.OrganizationRepresentation] admin_realms_realm_organizations_get(realm)

Returns a paginated list of organizations filtered according to the specified parameters

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    realm = 'realm_example' # str | 
    brief_representation = False # bool | if true, return the full representation. Otherwise, only the basic fields are returned. (optional) if omitted the server will use the default value of False
exact = True # bool | Boolean which defines whether the param 'search' must match exactly or not (optional)
first = 56 # int | The position of the first result to be processed (pagination offset) (optional)
max = 56 # int | The maximum number of results to be returned - defaults to 10 (optional)
q = 'q_example' # str | A query to search for custom attributes, in the format 'key1:value2 key2:value2' (optional)
search = 'search_example' # str | A String representing either an organization name or domain (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a paginated list of organizations filtered according to the specified parameters
        api_response = api_instance.admin_realms_realm_organizations_get(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a paginated list of organizations filtered according to the specified parameters
        api_response = api_instance.admin_realms_realm_organizations_get(realm, brief_representation=brief_representation, exact=exact, first=first, max=max, q=q, search=search)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **brief_representation** | **bool**| if true, return the full representation. Otherwise, only the basic fields are returned. | [optional] if omitted the server will use the default value of False
 **exact** | **bool**| Boolean which defines whether the param &#39;search&#39; must match exactly or not | [optional]
 **first** | **int**| The position of the first result to be processed (pagination offset) | [optional]
 **max** | **int**| The maximum number of results to be returned - defaults to 10 | [optional]
 **q** | **str**| A query to search for custom attributes, in the format &#39;key1:value2 key2:value2&#39; | [optional]
 **search** | **str**| A String representing either an organization name or domain | [optional]

### Return type

[**[organization_representation.OrganizationRepresentation]**](OrganizationRepresentation.md)

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

# **admin_realms_realm_organizations_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_organizations_id_delete(realm, id)

Deletes the organization

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    realm = 'realm_example' # str | 
    id = 'id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Deletes the organization
        api_response = api_instance.admin_realms_realm_organizations_id_delete(realm, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **id** | **str**|  |

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

# **admin_realms_realm_organizations_id_get**
> organization_representation.OrganizationRepresentation admin_realms_realm_organizations_id_get(realm, id)

Returns the organization representation

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    realm = 'realm_example' # str | 
    id = 'id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Returns the organization representation
        api_response = api_instance.admin_realms_realm_organizations_id_get(realm, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **id** | **str**|  |

### Return type

[**organization_representation.OrganizationRepresentation**](OrganizationRepresentation.md)

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

# **admin_realms_realm_organizations_id_identity_providers_alias_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_organizations_id_identity_providers_alias_delete(alias, realm, id)

Removes the identity provider with the specified alias from the organization

Breaks the association between the identity provider and the organization. The provider itself is not deleted. If no provider is found, or if it is not currently associated with the org, an error response is returned

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    alias = 'alias_example' # str | 
    realm = 'realm_example' # str | 
    id = 'id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Removes the identity provider with the specified alias from the organization
        api_response = api_instance.admin_realms_realm_organizations_id_identity_providers_alias_delete(alias, realm, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_identity_providers_alias_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**|  |
 **realm** | **str**|  |
 **id** | **str**|  |

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

# **admin_realms_realm_organizations_id_identity_providers_alias_get**
> identity_provider_representation.IdentityProviderRepresentation admin_realms_realm_organizations_id_identity_providers_alias_get(alias, realm, id)

Returns the identity provider associated with the organization that has the specified alias

Searches for an identity provider with the given alias. If one is found and is associated with the organization, it is returned. Otherwise, an error response with status NOT_FOUND is returned

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    alias = 'alias_example' # str | 
    realm = 'realm_example' # str | 
    id = 'id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Returns the identity provider associated with the organization that has the specified alias
        api_response = api_instance.admin_realms_realm_organizations_id_identity_providers_alias_get(alias, realm, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_identity_providers_alias_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**|  |
 **realm** | **str**|  |
 **id** | **str**|  |

### Return type

[**identity_provider_representation.IdentityProviderRepresentation**](IdentityProviderRepresentation.md)

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

# **admin_realms_realm_organizations_id_identity_providers_get**
> [identity_provider_representation.IdentityProviderRepresentation] admin_realms_realm_organizations_id_identity_providers_get(realm, id)

Returns all identity providers associated with the organization

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    realm = 'realm_example' # str | 
    id = 'id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Returns all identity providers associated with the organization
        api_response = api_instance.admin_realms_realm_organizations_id_identity_providers_get(realm, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_identity_providers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **id** | **str**|  |

### Return type

[**[identity_provider_representation.IdentityProviderRepresentation]**](IdentityProviderRepresentation.md)

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

# **admin_realms_realm_organizations_id_identity_providers_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_organizations_id_identity_providers_post(realm, id)

Adds the identity provider with the specified id to the organization

Adds, or associates, an existing identity provider with the organization. If no identity provider is found, or if it is already associated with the organization, an error response is returned

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    realm = 'realm_example' # str | 
    id = 'id_example' # str | 
    body = 'body_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Adds the identity provider with the specified id to the organization
        api_response = api_instance.admin_realms_realm_organizations_id_identity_providers_post(realm, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_identity_providers_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds the identity provider with the specified id to the organization
        api_response = api_instance.admin_realms_realm_organizations_id_identity_providers_post(realm, id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_identity_providers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **id** | **str**|  |
 **body** | **str**|  | [optional]

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

# **admin_realms_realm_organizations_id_members_count_get**
> int admin_realms_realm_organizations_id_members_count_get(realm, id)

Returns number of members in the organization.

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    realm = 'realm_example' # str | 
    id = 'id_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Returns number of members in the organization.
        api_response = api_instance.admin_realms_realm_organizations_id_members_count_get(realm, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **id** | **str**|  |

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

# **admin_realms_realm_organizations_id_members_get**
> [member_representation.MemberRepresentation] admin_realms_realm_organizations_id_members_get(realm, id)

Returns a paginated list of organization members filtered according to the specified parameters

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    realm = 'realm_example' # str | 
    id = 'id_example' # str | 
    exact = True # bool | Boolean which defines whether the param 'search' must match exactly or not (optional)
first = 56 # int | The position of the first result to be processed (pagination offset) (optional)
max = 56 # int | The maximum number of results to be returned. Defaults to 10 (optional)
membership_type = 'membership_type_example' # str | The membership type (optional)
search = 'search_example' # str | A String representing either a member's username, e-mail, first name, or last name. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a paginated list of organization members filtered according to the specified parameters
        api_response = api_instance.admin_realms_realm_organizations_id_members_get(realm, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_members_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a paginated list of organization members filtered according to the specified parameters
        api_response = api_instance.admin_realms_realm_organizations_id_members_get(realm, id, exact=exact, first=first, max=max, membership_type=membership_type, search=search)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **id** | **str**|  |
 **exact** | **bool**| Boolean which defines whether the param &#39;search&#39; must match exactly or not | [optional]
 **first** | **int**| The position of the first result to be processed (pagination offset) | [optional]
 **max** | **int**| The maximum number of results to be returned. Defaults to 10 | [optional]
 **membership_type** | **str**| The membership type | [optional]
 **search** | **str**| A String representing either a member&#39;s username, e-mail, first name, or last name. | [optional]

### Return type

[**[member_representation.MemberRepresentation]**](MemberRepresentation.md)

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

# **admin_realms_realm_organizations_id_members_id_delete**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_organizations_id_members_id_delete(id, realm)

Removes the user with the specified id from the organization

Breaks the association between the user and organization. The user itself is deleted in case the membership is managed, otherwise the user is not deleted. If no user is found, or if they are not a member of the organization, an error response is returned

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    id = 'id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Removes the user with the specified id from the organization
        api_response = api_instance.admin_realms_realm_organizations_id_members_id_delete(id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_members_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_organizations_id_members_id_get**
> member_representation.MemberRepresentation admin_realms_realm_organizations_id_members_id_get(id, realm)

Returns the member of the organization with the specified id

Searches for auser with the given id. If one is found, and is currently a member of the organization, returns it. Otherwise,an error response with status NOT_FOUND is returned

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    id = 'id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Returns the member of the organization with the specified id
        api_response = api_instance.admin_realms_realm_organizations_id_members_id_get(id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_members_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **realm** | **str**|  |

### Return type

[**member_representation.MemberRepresentation**](MemberRepresentation.md)

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

# **admin_realms_realm_organizations_id_members_id_organizations_get**
> [organization_representation.OrganizationRepresentation] admin_realms_realm_organizations_id_members_id_organizations_get(id, realm)

Returns the organizations associated with the user that has the specified id

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    id = 'id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Returns the organizations associated with the user that has the specified id
        api_response = api_instance.admin_realms_realm_organizations_id_members_id_organizations_get(id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_members_id_organizations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **realm** | **str**|  |

### Return type

[**[organization_representation.OrganizationRepresentation]**](OrganizationRepresentation.md)

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

# **admin_realms_realm_organizations_id_members_invite_existing_user_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_organizations_id_members_invite_existing_user_post(realm, id)

Invites an existing user to the organization, using the specified user id

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    realm = 'realm_example' # str | 
    id = 'id_example' # str | 
    id = 'id_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Invites an existing user to the organization, using the specified user id
        api_response = api_instance.admin_realms_realm_organizations_id_members_invite_existing_user_post(realm, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_members_invite_existing_user_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Invites an existing user to the organization, using the specified user id
        api_response = api_instance.admin_realms_realm_organizations_id_members_invite_existing_user_post(realm, id, id=id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_members_invite_existing_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **id** | **str**|  |
 **id** | **str**|  | [optional]

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

# **admin_realms_realm_organizations_id_members_invite_user_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_organizations_id_members_invite_user_post(realm, id)

Invites an existing user or sends a registration link to a new user, based on the provided e-mail address.

If the user with the given e-mail address exists, it sends an invitation link, otherwise it sends a registration link.

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    realm = 'realm_example' # str | 
    id = 'id_example' # str | 
    email = 'email_example' # str |  (optional)
first_name = 'first_name_example' # str |  (optional)
last_name = 'last_name_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Invites an existing user or sends a registration link to a new user, based on the provided e-mail address.
        api_response = api_instance.admin_realms_realm_organizations_id_members_invite_user_post(realm, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_members_invite_user_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Invites an existing user or sends a registration link to a new user, based on the provided e-mail address.
        api_response = api_instance.admin_realms_realm_organizations_id_members_invite_user_post(realm, id, email=email, first_name=first_name, last_name=last_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_members_invite_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **id** | **str**|  |
 **email** | **str**|  | [optional]
 **first_name** | **str**|  | [optional]
 **last_name** | **str**|  | [optional]

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

# **admin_realms_realm_organizations_id_members_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_organizations_id_members_post(realm, id)

Adds the user with the specified id as a member of the organization

Adds, or associates, an existing user with the organization. If no user is found, or if it is already associated with the organization, an error response is returned

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    realm = 'realm_example' # str | 
    id = 'id_example' # str | 
    body = 'body_example' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Adds the user with the specified id as a member of the organization
        api_response = api_instance.admin_realms_realm_organizations_id_members_post(realm, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_members_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds the user with the specified id as a member of the organization
        api_response = api_instance.admin_realms_realm_organizations_id_members_post(realm, id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **id** | **str**|  |
 **body** | **str**|  | [optional]

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

# **admin_realms_realm_organizations_id_put**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_organizations_id_put(realm, id)

Updates the organization

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    realm = 'realm_example' # str | 
    id = 'id_example' # str | 
    organization_representation_organization_representation = openapi_client.OrganizationRepresentation() # organization_representation.OrganizationRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates the organization
        api_response = api_instance.admin_realms_realm_organizations_id_put(realm, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates the organization
        api_response = api_instance.admin_realms_realm_organizations_id_put(realm, id, organization_representation_organization_representation=organization_representation_organization_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **id** | **str**|  |
 **organization_representation_organization_representation** | [**organization_representation.OrganizationRepresentation**](OrganizationRepresentation.md)|  | [optional]

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

# **admin_realms_realm_organizations_members_id_organizations_get**
> [organization_representation.OrganizationRepresentation] admin_realms_realm_organizations_members_id_organizations_get(id, realm)

Returns the organizations associated with the user that has the specified id

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    id = 'id_example' # str | 
    realm = 'realm_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Returns the organizations associated with the user that has the specified id
        api_response = api_instance.admin_realms_realm_organizations_members_id_organizations_get(id, realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_members_id_organizations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **realm** | **str**|  |

### Return type

[**[organization_representation.OrganizationRepresentation]**](OrganizationRepresentation.md)

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

# **admin_realms_realm_organizations_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_organizations_post(realm)

Creates a new organization

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
    api_instance = openapi_client.OrganizationsApi(api_client)
    realm = 'realm_example' # str | 
    organization_representation_organization_representation = openapi_client.OrganizationRepresentation() # organization_representation.OrganizationRepresentation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates a new organization
        api_response = api_instance.admin_realms_realm_organizations_post(realm)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a new organization
        api_response = api_instance.admin_realms_realm_organizations_post(realm, organization_representation_organization_representation=organization_representation_organization_representation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->admin_realms_realm_organizations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **organization_representation_organization_representation** | [**organization_representation.OrganizationRepresentation**](OrganizationRepresentation.md)|  | [optional]

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

