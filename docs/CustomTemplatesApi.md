# portainer.CustomTemplatesApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_template_create**](CustomTemplatesApi.md#custom_template_create) | **POST** /custom_templates | Create a custom template
[**custom_template_delete**](CustomTemplatesApi.md#custom_template_delete) | **DELETE** /custom_templates/{id} | Remove a template
[**custom_template_file**](CustomTemplatesApi.md#custom_template_file) | **GET** /custom_templates/{id}/file | Get Template stack file content.
[**custom_template_inspect**](CustomTemplatesApi.md#custom_template_inspect) | **GET** /custom_templates/{id} | Inspect a custom template
[**custom_template_list**](CustomTemplatesApi.md#custom_template_list) | **GET** /custom_templates | List available custom templates
[**custom_template_update**](CustomTemplatesApi.md#custom_template_update) | **PUT** /custom_templates/{id} | Update a template


# **custom_template_create**
> PortainerCustomTemplate custom_template_create(method, body_string=body_string, body_repository=body_repository, title=title, description=description, note=note, platform=platform, type=type, file=file)

Create a custom template

Create a custom template. **Access policy**: authenticated

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
api_instance = portainer.CustomTemplatesApi(portainer.ApiClient(configuration))
method = 'method_example' # str | method for creating template
body_string = portainer.CustomtemplatesCustomTemplateFromFileContentPayload() # CustomtemplatesCustomTemplateFromFileContentPayload | Required when using method=string (optional)
body_repository = portainer.CustomtemplatesCustomTemplateFromGitRepositoryPayload() # CustomtemplatesCustomTemplateFromGitRepositoryPayload | Required when using method=repository (optional)
title = 'title_example' # str | Title of the template. required when method is file (optional)
description = 'description_example' # str | Description of the template. required when method is file (optional)
note = 'note_example' # str | A note that will be displayed in the UI. Supports HTML content (optional)
platform = 56 # int | Platform associated to the template (1 - 'linux', 2 - 'windows'). required when method is file (optional)
type = 56 # int | Type of created stack (1 - swarm, 2 - compose), required when method is file (optional)
file = '/path/to/file.txt' # file | required when method is file (optional)

try:
    # Create a custom template
    api_response = api_instance.custom_template_create(method, body_string=body_string, body_repository=body_repository, title=title, description=description, note=note, platform=platform, type=type, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomTemplatesApi->custom_template_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method** | **str**| method for creating template | 
 **body_string** | [**CustomtemplatesCustomTemplateFromFileContentPayload**](CustomtemplatesCustomTemplateFromFileContentPayload.md)| Required when using method&#x3D;string | [optional] 
 **body_repository** | [**CustomtemplatesCustomTemplateFromGitRepositoryPayload**](CustomtemplatesCustomTemplateFromGitRepositoryPayload.md)| Required when using method&#x3D;repository | [optional] 
 **title** | **str**| Title of the template. required when method is file | [optional] 
 **description** | **str**| Description of the template. required when method is file | [optional] 
 **note** | **str**| A note that will be displayed in the UI. Supports HTML content | [optional] 
 **platform** | **int**| Platform associated to the template (1 - &#39;linux&#39;, 2 - &#39;windows&#39;). required when method is file | [optional] 
 **type** | **int**| Type of created stack (1 - swarm, 2 - compose), required when method is file | [optional] 
 **file** | **file**| required when method is file | [optional] 

### Return type

[**PortainerCustomTemplate**](PortainerCustomTemplate.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_template_delete**
> custom_template_delete(id)

Remove a template

Remove a template. **Access policy**: authenticated

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
api_instance = portainer.CustomTemplatesApi(portainer.ApiClient(configuration))
id = 56 # int | Template identifier

try:
    # Remove a template
    api_instance.custom_template_delete(id)
except ApiException as e:
    print("Exception when calling CustomTemplatesApi->custom_template_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Template identifier | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_template_file**
> CustomtemplatesFileResponse custom_template_file(id)

Get Template stack file content.

Retrieve the content of the Stack file for the specified custom template **Access policy**: authenticated

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
api_instance = portainer.CustomTemplatesApi(portainer.ApiClient(configuration))
id = 56 # int | Template identifier

try:
    # Get Template stack file content.
    api_response = api_instance.custom_template_file(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomTemplatesApi->custom_template_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Template identifier | 

### Return type

[**CustomtemplatesFileResponse**](CustomtemplatesFileResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_template_inspect**
> PortainerCustomTemplate custom_template_inspect(id)

Inspect a custom template

Retrieve details about a template. **Access policy**: authenticated

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
api_instance = portainer.CustomTemplatesApi(portainer.ApiClient(configuration))
id = 56 # int | Template identifier

try:
    # Inspect a custom template
    api_response = api_instance.custom_template_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomTemplatesApi->custom_template_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Template identifier | 

### Return type

[**PortainerCustomTemplate**](PortainerCustomTemplate.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_template_list**
> list[PortainerCustomTemplate] custom_template_list(type)

List available custom templates

List available custom templates. **Access policy**: authenticated

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
api_instance = portainer.CustomTemplatesApi(portainer.ApiClient(configuration))
type = [56] # list[int] | Template types

try:
    # List available custom templates
    api_response = api_instance.custom_template_list(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomTemplatesApi->custom_template_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**list[int]**](int.md)| Template types | 

### Return type

[**list[PortainerCustomTemplate]**](PortainerCustomTemplate.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_template_update**
> PortainerCustomTemplate custom_template_update(id, body)

Update a template

Update a template. **Access policy**: authenticated

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
api_instance = portainer.CustomTemplatesApi(portainer.ApiClient(configuration))
id = 56 # int | Template identifier
body = portainer.CustomtemplatesCustomTemplateUpdatePayload() # CustomtemplatesCustomTemplateUpdatePayload | Template details

try:
    # Update a template
    api_response = api_instance.custom_template_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomTemplatesApi->custom_template_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Template identifier | 
 **body** | [**CustomtemplatesCustomTemplateUpdatePayload**](CustomtemplatesCustomTemplateUpdatePayload.md)| Template details | 

### Return type

[**PortainerCustomTemplate**](PortainerCustomTemplate.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

