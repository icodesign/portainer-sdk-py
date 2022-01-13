# portainer.TemplatesApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**template_file**](TemplatesApi.md#template_file) | **POST** /templates/file | Get a template&#39;s file
[**template_list**](TemplatesApi.md#template_list) | **GET** /templates | List available templates


# **template_file**
> TemplatesFileResponse template_file(body)

Get a template's file

Get a template's file **Access policy**: authenticated

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
api_instance = portainer.TemplatesApi(portainer.ApiClient(configuration))
body = portainer.TemplatesFilePayload() # TemplatesFilePayload | File details

try:
    # Get a template's file
    api_response = api_instance.template_file(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplatesFilePayload**](TemplatesFilePayload.md)| File details | 

### Return type

[**TemplatesFileResponse**](TemplatesFileResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_list**
> TemplatesListResponse template_list()

List available templates

List available templates. **Access policy**: authenticated

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
api_instance = portainer.TemplatesApi(portainer.ApiClient(configuration))

try:
    # List available templates
    api_response = api_instance.template_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TemplatesListResponse**](TemplatesListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

