# portainer.RegistriesApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registry_configure**](RegistriesApi.md#registry_configure) | **POST** /registries/{id}/configure | Configures a registry
[**registry_create**](RegistriesApi.md#registry_create) | **POST** /registries | Create a new registry
[**registry_delete**](RegistriesApi.md#registry_delete) | **DELETE** /registries/{id} | Remove a registry
[**registry_inspect**](RegistriesApi.md#registry_inspect) | **GET** /registries/{id} | Inspect a registry
[**registry_list**](RegistriesApi.md#registry_list) | **GET** /registries | List Registries
[**registry_update**](RegistriesApi.md#registry_update) | **PUT** /registries/{id} | Update a registry


# **registry_configure**
> registry_configure(id, body)

Configures a registry

Configures a registry. **Access policy**: restricted

### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = portainer.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt
configuration = portainer.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = portainer.RegistriesApi(portainer.ApiClient(configuration))
id = 56 # int | Registry identifier
body = portainer.RegistriesRegistryConfigurePayload() # RegistriesRegistryConfigurePayload | Registry configuration

try:
    # Configures a registry
    api_instance.registry_configure(id, body)
except ApiException as e:
    print("Exception when calling RegistriesApi->registry_configure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Registry identifier | 
 **body** | [**RegistriesRegistryConfigurePayload**](RegistriesRegistryConfigurePayload.md)| Registry configuration | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registry_create**
> PortainerRegistry registry_create(body)

Create a new registry

Create a new registry. **Access policy**: restricted

### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = portainer.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt
configuration = portainer.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = portainer.RegistriesApi(portainer.ApiClient(configuration))
body = portainer.RegistriesRegistryCreatePayload() # RegistriesRegistryCreatePayload | Registry details

try:
    # Create a new registry
    api_response = api_instance.registry_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistriesApi->registry_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegistriesRegistryCreatePayload**](RegistriesRegistryCreatePayload.md)| Registry details | 

### Return type

[**PortainerRegistry**](PortainerRegistry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registry_delete**
> registry_delete(id)

Remove a registry

Remove a registry **Access policy**: restricted

### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = portainer.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt
configuration = portainer.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = portainer.RegistriesApi(portainer.ApiClient(configuration))
id = 56 # int | Registry identifier

try:
    # Remove a registry
    api_instance.registry_delete(id)
except ApiException as e:
    print("Exception when calling RegistriesApi->registry_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Registry identifier | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registry_inspect**
> PortainerRegistry registry_inspect(id)

Inspect a registry

Retrieve details about a registry. **Access policy**: restricted

### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = portainer.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt
configuration = portainer.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = portainer.RegistriesApi(portainer.ApiClient(configuration))
id = 56 # int | Registry identifier

try:
    # Inspect a registry
    api_response = api_instance.registry_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistriesApi->registry_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Registry identifier | 

### Return type

[**PortainerRegistry**](PortainerRegistry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registry_list**
> list[PortainerRegistry] registry_list()

List Registries

List all registries based on the current user authorizations. Will return all registries if using an administrator account otherwise it will only return authorized registries. **Access policy**: restricted

### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = portainer.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt
configuration = portainer.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = portainer.RegistriesApi(portainer.ApiClient(configuration))

try:
    # List Registries
    api_response = api_instance.registry_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistriesApi->registry_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PortainerRegistry]**](PortainerRegistry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registry_update**
> PortainerRegistry registry_update(id, body)

Update a registry

Update a registry **Access policy**: restricted

### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = portainer.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt
configuration = portainer.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = portainer.RegistriesApi(portainer.ApiClient(configuration))
id = 56 # int | Registry identifier
body = portainer.RegistriesRegistryUpdatePayload() # RegistriesRegistryUpdatePayload | Registry details

try:
    # Update a registry
    api_response = api_instance.registry_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistriesApi->registry_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Registry identifier | 
 **body** | [**RegistriesRegistryUpdatePayload**](RegistriesRegistryUpdatePayload.md)| Registry details | 

### Return type

[**PortainerRegistry**](PortainerRegistry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

