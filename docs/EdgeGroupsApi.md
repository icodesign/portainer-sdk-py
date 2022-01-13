# portainer.EdgeGroupsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_group_create**](EdgeGroupsApi.md#edge_group_create) | **POST** /edge_groups | Create an EdgeGroup
[**edge_group_delete**](EdgeGroupsApi.md#edge_group_delete) | **DELETE** /edge_groups/{id} | Deletes an EdgeGroup
[**edge_group_inspect**](EdgeGroupsApi.md#edge_group_inspect) | **GET** /edge_groups/{id} | Inspects an EdgeGroup
[**edge_group_list**](EdgeGroupsApi.md#edge_group_list) | **GET** /edge_groups | list EdgeGroups
[**ege_group_update**](EdgeGroupsApi.md#ege_group_update) | **PUT** /edge_groups/{id} | Updates an EdgeGroup


# **edge_group_create**
> PortainerEdgeGroup edge_group_create(body)

Create an EdgeGroup

**Access policy**: administrator

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
api_instance = portainer.EdgeGroupsApi(portainer.ApiClient(configuration))
body = portainer.EdgegroupsEdgeGroupCreatePayload() # EdgegroupsEdgeGroupCreatePayload | EdgeGroup data

try:
    # Create an EdgeGroup
    api_response = api_instance.edge_group_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeGroupsApi->edge_group_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EdgegroupsEdgeGroupCreatePayload**](EdgegroupsEdgeGroupCreatePayload.md)| EdgeGroup data | 

### Return type

[**PortainerEdgeGroup**](PortainerEdgeGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_group_delete**
> edge_group_delete(id)

Deletes an EdgeGroup

**Access policy**: administrator

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
api_instance = portainer.EdgeGroupsApi(portainer.ApiClient(configuration))
id = 56 # int | EdgeGroup Id

try:
    # Deletes an EdgeGroup
    api_instance.edge_group_delete(id)
except ApiException as e:
    print("Exception when calling EdgeGroupsApi->edge_group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EdgeGroup Id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_group_inspect**
> PortainerEdgeGroup edge_group_inspect(id)

Inspects an EdgeGroup

**Access policy**: administrator

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
api_instance = portainer.EdgeGroupsApi(portainer.ApiClient(configuration))
id = 56 # int | EdgeGroup Id

try:
    # Inspects an EdgeGroup
    api_response = api_instance.edge_group_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeGroupsApi->edge_group_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EdgeGroup Id | 

### Return type

[**PortainerEdgeGroup**](PortainerEdgeGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_group_list**
> list[EdgegroupsDecoratedEdgeGroup] edge_group_list()

list EdgeGroups

**Access policy**: administrator

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
api_instance = portainer.EdgeGroupsApi(portainer.ApiClient(configuration))

try:
    # list EdgeGroups
    api_response = api_instance.edge_group_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeGroupsApi->edge_group_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EdgegroupsDecoratedEdgeGroup]**](EdgegroupsDecoratedEdgeGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ege_group_update**
> PortainerEdgeGroup ege_group_update(id, body)

Updates an EdgeGroup

**Access policy**: administrator

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
api_instance = portainer.EdgeGroupsApi(portainer.ApiClient(configuration))
id = 56 # int | EdgeGroup Id
body = portainer.EdgegroupsEdgeGroupUpdatePayload() # EdgegroupsEdgeGroupUpdatePayload | EdgeGroup data

try:
    # Updates an EdgeGroup
    api_response = api_instance.ege_group_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeGroupsApi->ege_group_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EdgeGroup Id | 
 **body** | [**EdgegroupsEdgeGroupUpdatePayload**](EdgegroupsEdgeGroupUpdatePayload.md)| EdgeGroup data | 

### Return type

[**PortainerEdgeGroup**](PortainerEdgeGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

