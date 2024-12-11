# openapi_client.ClientAttributeCertificateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_realm_clients_client_uuid_certificates_attr_download_post**](ClientAttributeCertificateApi.md#admin_realms_realm_clients_client_uuid_certificates_attr_download_post) | **POST** /admin/realms/{realm}/clients/{client-uuid}/certificates/{attr}/download | Get a keystore file for the client, containing private key and public certificate
[**admin_realms_realm_clients_client_uuid_certificates_attr_generate_and_download_post**](ClientAttributeCertificateApi.md#admin_realms_realm_clients_client_uuid_certificates_attr_generate_and_download_post) | **POST** /admin/realms/{realm}/clients/{client-uuid}/certificates/{attr}/generate-and-download | Generate a new keypair and certificate, and get the private key file  Generates a keypair and certificate and serves the private key in a specified keystore format. Only generated public certificate is saved in Keycloak DB - the private key is not.
[**admin_realms_realm_clients_client_uuid_certificates_attr_generate_post**](ClientAttributeCertificateApi.md#admin_realms_realm_clients_client_uuid_certificates_attr_generate_post) | **POST** /admin/realms/{realm}/clients/{client-uuid}/certificates/{attr}/generate | Generate a new certificate with new key pair
[**admin_realms_realm_clients_client_uuid_certificates_attr_get**](ClientAttributeCertificateApi.md#admin_realms_realm_clients_client_uuid_certificates_attr_get) | **GET** /admin/realms/{realm}/clients/{client-uuid}/certificates/{attr} | Get key info
[**admin_realms_realm_clients_client_uuid_certificates_attr_upload_certificate_post**](ClientAttributeCertificateApi.md#admin_realms_realm_clients_client_uuid_certificates_attr_upload_certificate_post) | **POST** /admin/realms/{realm}/clients/{client-uuid}/certificates/{attr}/upload-certificate | Upload only certificate, not private key
[**admin_realms_realm_clients_client_uuid_certificates_attr_upload_post**](ClientAttributeCertificateApi.md#admin_realms_realm_clients_client_uuid_certificates_attr_upload_post) | **POST** /admin/realms/{realm}/clients/{client-uuid}/certificates/{attr}/upload | Upload certificate and eventually private key


# **admin_realms_realm_clients_client_uuid_certificates_attr_download_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_certificates_attr_download_post(realm, client_uuid, attr)

Get a keystore file for the client, containing private key and public certificate

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
    api_instance = openapi_client.ClientAttributeCertificateApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    attr = 'attr_example' # str | 
    key_store_config_key_store_config = openapi_client.KeyStoreConfig() # key_store_config.KeyStoreConfig |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a keystore file for the client, containing private key and public certificate
        api_response = api_instance.admin_realms_realm_clients_client_uuid_certificates_attr_download_post(realm, client_uuid, attr)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientAttributeCertificateApi->admin_realms_realm_clients_client_uuid_certificates_attr_download_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a keystore file for the client, containing private key and public certificate
        api_response = api_instance.admin_realms_realm_clients_client_uuid_certificates_attr_download_post(realm, client_uuid, attr, key_store_config_key_store_config=key_store_config_key_store_config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientAttributeCertificateApi->admin_realms_realm_clients_client_uuid_certificates_attr_download_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **attr** | **str**|  |
 **key_store_config_key_store_config** | [**key_store_config.KeyStoreConfig**](KeyStoreConfig.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_clients_client_uuid_certificates_attr_generate_and_download_post**
> bool, date, datetime, dict, float, int, list, str admin_realms_realm_clients_client_uuid_certificates_attr_generate_and_download_post(realm, client_uuid, attr)

Generate a new keypair and certificate, and get the private key file  Generates a keypair and certificate and serves the private key in a specified keystore format. Only generated public certificate is saved in Keycloak DB - the private key is not.

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
    api_instance = openapi_client.ClientAttributeCertificateApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    attr = 'attr_example' # str | 
    key_store_config_key_store_config = openapi_client.KeyStoreConfig() # key_store_config.KeyStoreConfig |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generate a new keypair and certificate, and get the private key file  Generates a keypair and certificate and serves the private key in a specified keystore format. Only generated public certificate is saved in Keycloak DB - the private key is not.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_certificates_attr_generate_and_download_post(realm, client_uuid, attr)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientAttributeCertificateApi->admin_realms_realm_clients_client_uuid_certificates_attr_generate_and_download_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate a new keypair and certificate, and get the private key file  Generates a keypair and certificate and serves the private key in a specified keystore format. Only generated public certificate is saved in Keycloak DB - the private key is not.
        api_response = api_instance.admin_realms_realm_clients_client_uuid_certificates_attr_generate_and_download_post(realm, client_uuid, attr, key_store_config_key_store_config=key_store_config_key_store_config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientAttributeCertificateApi->admin_realms_realm_clients_client_uuid_certificates_attr_generate_and_download_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **attr** | **str**|  |
 **key_store_config_key_store_config** | [**key_store_config.KeyStoreConfig**](KeyStoreConfig.md)|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_realms_realm_clients_client_uuid_certificates_attr_generate_post**
> certificate_representation.CertificateRepresentation admin_realms_realm_clients_client_uuid_certificates_attr_generate_post(realm, client_uuid, attr)

Generate a new certificate with new key pair

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
    api_instance = openapi_client.ClientAttributeCertificateApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    attr = 'attr_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Generate a new certificate with new key pair
        api_response = api_instance.admin_realms_realm_clients_client_uuid_certificates_attr_generate_post(realm, client_uuid, attr)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientAttributeCertificateApi->admin_realms_realm_clients_client_uuid_certificates_attr_generate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **attr** | **str**|  |

### Return type

[**certificate_representation.CertificateRepresentation**](CertificateRepresentation.md)

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

# **admin_realms_realm_clients_client_uuid_certificates_attr_get**
> certificate_representation.CertificateRepresentation admin_realms_realm_clients_client_uuid_certificates_attr_get(realm, client_uuid, attr)

Get key info

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
    api_instance = openapi_client.ClientAttributeCertificateApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    attr = 'attr_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Get key info
        api_response = api_instance.admin_realms_realm_clients_client_uuid_certificates_attr_get(realm, client_uuid, attr)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientAttributeCertificateApi->admin_realms_realm_clients_client_uuid_certificates_attr_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **attr** | **str**|  |

### Return type

[**certificate_representation.CertificateRepresentation**](CertificateRepresentation.md)

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

# **admin_realms_realm_clients_client_uuid_certificates_attr_upload_certificate_post**
> certificate_representation.CertificateRepresentation admin_realms_realm_clients_client_uuid_certificates_attr_upload_certificate_post(realm, client_uuid, attr)

Upload only certificate, not private key

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
    api_instance = openapi_client.ClientAttributeCertificateApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    attr = 'attr_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Upload only certificate, not private key
        api_response = api_instance.admin_realms_realm_clients_client_uuid_certificates_attr_upload_certificate_post(realm, client_uuid, attr)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientAttributeCertificateApi->admin_realms_realm_clients_client_uuid_certificates_attr_upload_certificate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **attr** | **str**|  |

### Return type

[**certificate_representation.CertificateRepresentation**](CertificateRepresentation.md)

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

# **admin_realms_realm_clients_client_uuid_certificates_attr_upload_post**
> certificate_representation.CertificateRepresentation admin_realms_realm_clients_client_uuid_certificates_attr_upload_post(realm, client_uuid, attr)

Upload certificate and eventually private key

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
    api_instance = openapi_client.ClientAttributeCertificateApi(api_client)
    realm = 'realm_example' # str | 
    client_uuid = 'client_uuid_example' # str | 
    attr = 'attr_example' # str | 
    
    # example passing only required values which don't have defaults set
    try:
        # Upload certificate and eventually private key
        api_response = api_instance.admin_realms_realm_clients_client_uuid_certificates_attr_upload_post(realm, client_uuid, attr)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientAttributeCertificateApi->admin_realms_realm_clients_client_uuid_certificates_attr_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**|  |
 **client_uuid** | **str**|  |
 **attr** | **str**|  |

### Return type

[**certificate_representation.CertificateRepresentation**](CertificateRepresentation.md)

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

