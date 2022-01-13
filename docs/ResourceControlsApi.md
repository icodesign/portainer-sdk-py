# portainer.ResourceControlsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_control_create**](ResourceControlsApi.md#resource_control_create) | **POST** /resource_controls | Create a new resource control
[**resource_control_delete**](ResourceControlsApi.md#resource_control_delete) | **DELETE** /resource_controls/{id} | Remove a resource control
[**resource_control_update**](ResourceControlsApi.md#resource_control_update) | **PUT** /resource_controls/{id} | Update a resource control


# **resource_control_create**
> PortainerResourceControl resource_control_create(body)

Create a new resource control

Create a new resource control to restrict access to a Docker resource. **Access policy**: administrator

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
api_instance = portainer.ResourceControlsApi(portainer.ApiClient(configuration))
body = portainer.ResourcecontrolsResourceControlCreatePayload() # ResourcecontrolsResourceControlCreatePayload | Resource control details

try:
    # Create a new resource control
    api_response = api_instance.resource_control_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceControlsApi->resource_control_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourcecontrolsResourceControlCreatePayload**](ResourcecontrolsResourceControlCreatePayload.md)| Resource control details | 

### Return type

[**PortainerResourceControl**](PortainerResourceControl.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_control_delete**
> resource_control_delete(id)

Remove a resource control

Remove a resource control. **Access policy**: administrator

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
api_instance = portainer.ResourceControlsApi(portainer.ApiClient(configuration))
id = 56 # int | Resource control identifier

try:
    # Remove a resource control
    api_instance.resource_control_delete(id)
except ApiException as e:
    print("Exception when calling ResourceControlsApi->resource_control_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Resource control identifier | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_control_update**
> PortainerResourceControl resource_control_update(id, body)

Update a resource control

Update a resource control **Access policy**: authenticated

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
api_instance = portainer.ResourceControlsApi(portainer.ApiClient(configuration))
id = 56 # int | Resource control identifier
body = portainer.ResourcecontrolsResourceControlUpdatePayload() # ResourcecontrolsResourceControlUpdatePayload | Resource control details

try:
    # Update a resource control
    api_response = api_instance.resource_control_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceControlsApi->resource_control_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Resource control identifier | 
 **body** | [**ResourcecontrolsResourceControlUpdatePayload**](ResourcecontrolsResourceControlUpdatePayload.md)| Resource control details | 

### Return type

[**PortainerResourceControl**](PortainerResourceControl.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

