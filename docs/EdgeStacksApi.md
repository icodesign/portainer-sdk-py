# portainer.EdgeStacksApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_stack_create**](EdgeStacksApi.md#edge_stack_create) | **POST** /edge_stacks | Create an EdgeStack
[**edge_stack_delete**](EdgeStacksApi.md#edge_stack_delete) | **DELETE** /edge_stacks/{id} | Delete an EdgeStack
[**edge_stack_file**](EdgeStacksApi.md#edge_stack_file) | **GET** /edge_stacks/{id}/file | Fetches the stack file for an EdgeStack
[**edge_stack_inspect**](EdgeStacksApi.md#edge_stack_inspect) | **GET** /edge_stacks/{id} | Inspect an EdgeStack
[**edge_stack_list**](EdgeStacksApi.md#edge_stack_list) | **GET** /edge_stacks | Fetches the list of EdgeStacks
[**edge_stack_status_update**](EdgeStacksApi.md#edge_stack_status_update) | **PUT** /edge_stacks/{id}/status | Update an EdgeStack status
[**edge_stack_update**](EdgeStacksApi.md#edge_stack_update) | **PUT** /edge_stacks/{id} | Update an EdgeStack
[**endpoints_id_edge_stacks_stack_id_get**](EdgeStacksApi.md#endpoints_id_edge_stacks_stack_id_get) | **GET** /endpoints/{id}/edge/stacks/{stackId} | Inspect an Edge Stack for an Environment(Endpoint)


# **edge_stack_create**
> PortainerEdgeStack edge_stack_create(method, body_string, body_file, body_repository)

Create an EdgeStack

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
api_instance = portainer.EdgeStacksApi(portainer.ApiClient(configuration))
method = 'method_example' # str | Creation Method
body_string = portainer.EdgestacksSwarmStackFromFileContentPayload() # EdgestacksSwarmStackFromFileContentPayload | Required when using method=string
body_file = portainer.EdgestacksSwarmStackFromFileUploadPayload() # EdgestacksSwarmStackFromFileUploadPayload | Required when using method=file
body_repository = portainer.EdgestacksSwarmStackFromGitRepositoryPayload() # EdgestacksSwarmStackFromGitRepositoryPayload | Required when using method=repository

try:
    # Create an EdgeStack
    api_response = api_instance.edge_stack_create(method, body_string, body_file, body_repository)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeStacksApi->edge_stack_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method** | **str**| Creation Method | 
 **body_string** | [**EdgestacksSwarmStackFromFileContentPayload**](EdgestacksSwarmStackFromFileContentPayload.md)| Required when using method&#x3D;string | 
 **body_file** | [**EdgestacksSwarmStackFromFileUploadPayload**](EdgestacksSwarmStackFromFileUploadPayload.md)| Required when using method&#x3D;file | 
 **body_repository** | [**EdgestacksSwarmStackFromGitRepositoryPayload**](EdgestacksSwarmStackFromGitRepositoryPayload.md)| Required when using method&#x3D;repository | 

### Return type

[**PortainerEdgeStack**](PortainerEdgeStack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_stack_delete**
> edge_stack_delete(id)

Delete an EdgeStack

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
api_instance = portainer.EdgeStacksApi(portainer.ApiClient(configuration))
id = 'id_example' # str | EdgeStack Id

try:
    # Delete an EdgeStack
    api_instance.edge_stack_delete(id)
except ApiException as e:
    print("Exception when calling EdgeStacksApi->edge_stack_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EdgeStack Id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_stack_file**
> EdgestacksStackFileResponse edge_stack_file(id)

Fetches the stack file for an EdgeStack

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
api_instance = portainer.EdgeStacksApi(portainer.ApiClient(configuration))
id = 'id_example' # str | EdgeStack Id

try:
    # Fetches the stack file for an EdgeStack
    api_response = api_instance.edge_stack_file(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeStacksApi->edge_stack_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EdgeStack Id | 

### Return type

[**EdgestacksStackFileResponse**](EdgestacksStackFileResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_stack_inspect**
> PortainerEdgeStack edge_stack_inspect(id)

Inspect an EdgeStack

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
api_instance = portainer.EdgeStacksApi(portainer.ApiClient(configuration))
id = 'id_example' # str | EdgeStack Id

try:
    # Inspect an EdgeStack
    api_response = api_instance.edge_stack_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeStacksApi->edge_stack_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EdgeStack Id | 

### Return type

[**PortainerEdgeStack**](PortainerEdgeStack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_stack_list**
> list[PortainerEdgeStack] edge_stack_list()

Fetches the list of EdgeStacks

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
api_instance = portainer.EdgeStacksApi(portainer.ApiClient(configuration))

try:
    # Fetches the list of EdgeStacks
    api_response = api_instance.edge_stack_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeStacksApi->edge_stack_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PortainerEdgeStack]**](PortainerEdgeStack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_stack_status_update**
> PortainerEdgeStack edge_stack_status_update(id)

Update an EdgeStack status

Authorized only if the request is done by an Edge Environment(Endpoint)

### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = portainer.EdgeStacksApi()
id = 'id_example' # str | EdgeStack Id

try:
    # Update an EdgeStack status
    api_response = api_instance.edge_stack_status_update(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeStacksApi->edge_stack_status_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EdgeStack Id | 

### Return type

[**PortainerEdgeStack**](PortainerEdgeStack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_stack_update**
> PortainerEdgeStack edge_stack_update(id, body)

Update an EdgeStack

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
api_instance = portainer.EdgeStacksApi(portainer.ApiClient(configuration))
id = 'id_example' # str | EdgeStack Id
body = portainer.EdgestacksUpdateEdgeStackPayload() # EdgestacksUpdateEdgeStackPayload | EdgeStack data

try:
    # Update an EdgeStack
    api_response = api_instance.edge_stack_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeStacksApi->edge_stack_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EdgeStack Id | 
 **body** | [**EdgestacksUpdateEdgeStackPayload**](EdgestacksUpdateEdgeStackPayload.md)| EdgeStack data | 

### Return type

[**PortainerEdgeStack**](PortainerEdgeStack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_id_edge_stacks_stack_id_get**
> EndpointedgeConfigResponse endpoints_id_edge_stacks_stack_id_get(id, stack_id)

Inspect an Edge Stack for an Environment(Endpoint)

**Access policy**: public

### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = portainer.EdgeStacksApi()
id = 'id_example' # str | environment(endpoint) Id
stack_id = 'stack_id_example' # str | EdgeStack Id

try:
    # Inspect an Edge Stack for an Environment(Endpoint)
    api_response = api_instance.endpoints_id_edge_stacks_stack_id_get(id, stack_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeStacksApi->endpoints_id_edge_stacks_stack_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| environment(endpoint) Id | 
 **stack_id** | **str**| EdgeStack Id | 

### Return type

[**EndpointedgeConfigResponse**](EndpointedgeConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

