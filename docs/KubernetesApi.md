# portainer.KubernetesApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_kubernetes_config**](KubernetesApi.md#get_kubernetes_config) | **GET** /kubernetes/config | Generates kubeconfig file enabling client communication with k8s api server
[**get_kubernetes_nodes_limits**](KubernetesApi.md#get_kubernetes_nodes_limits) | **GET** /kubernetes/{id}/nodes_limits | Get CPU and memory limits of all nodes within k8s cluster
[**kubernetes_namespaces_toggle_system**](KubernetesApi.md#kubernetes_namespaces_toggle_system) | **PUT** /kubernetes/{id}/namespaces/{namespace}/system | Toggle the system state for a namespace


# **get_kubernetes_config**
> get_kubernetes_config(ids=ids, exclude_ids=exclude_ids)

Generates kubeconfig file enabling client communication with k8s api server

Generates kubeconfig file enabling client communication with k8s api server **Access policy**: authenticated

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
api_instance = portainer.KubernetesApi(portainer.ApiClient(configuration))
ids = [56] # list[int] | will include only these environments(endpoints) (optional)
exclude_ids = [56] # list[int] | will exclude these environments(endpoints) (optional)

try:
    # Generates kubeconfig file enabling client communication with k8s api server
    api_instance.get_kubernetes_config(ids=ids, exclude_ids=exclude_ids)
except ApiException as e:
    print("Exception when calling KubernetesApi->get_kubernetes_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| will include only these environments(endpoints) | [optional] 
 **exclude_ids** | [**list[int]**](int.md)| will exclude these environments(endpoints) | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_nodes_limits**
> PortainerK8sNodesLimits get_kubernetes_nodes_limits(id)

Get CPU and memory limits of all nodes within k8s cluster

Get CPU and memory limits of all nodes within k8s cluster **Access policy**: authenticated

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
api_instance = portainer.KubernetesApi(portainer.ApiClient(configuration))
id = 56 # int | Environment(Endpoint) identifier

try:
    # Get CPU and memory limits of all nodes within k8s cluster
    api_response = api_instance.get_kubernetes_nodes_limits(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KubernetesApi->get_kubernetes_nodes_limits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 

### Return type

[**PortainerK8sNodesLimits**](PortainerK8sNodesLimits.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_namespaces_toggle_system**
> kubernetes_namespaces_toggle_system(id, namespace, body)

Toggle the system state for a namespace

Toggle the system state for a namespace **Access policy**: administrator or environment(endpoint) admin

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
api_instance = portainer.KubernetesApi(portainer.ApiClient(configuration))
id = 56 # int | Environment(Endpoint) identifier
namespace = 'namespace_example' # str | Namespace name
body = portainer.KubernetesNamespacesToggleSystemPayload() # KubernetesNamespacesToggleSystemPayload | Update details

try:
    # Toggle the system state for a namespace
    api_instance.kubernetes_namespaces_toggle_system(id, namespace, body)
except ApiException as e:
    print("Exception when calling KubernetesApi->kubernetes_namespaces_toggle_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **namespace** | **str**| Namespace name | 
 **body** | [**KubernetesNamespacesToggleSystemPayload**](KubernetesNamespacesToggleSystemPayload.md)| Update details | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

