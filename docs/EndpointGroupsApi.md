# portainer.EndpointGroupsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoint_group_add_endpoint**](EndpointGroupsApi.md#endpoint_group_add_endpoint) | **PUT** /endpoint_groups/{id}/endpoints/{endpointId} | Add an environment(endpoint) to an environment(endpoint) group
[**endpoint_group_delete**](EndpointGroupsApi.md#endpoint_group_delete) | **DELETE** /endpoint_groups/{id} | Remove an environment(endpoint) group
[**endpoint_group_delete_endpoint**](EndpointGroupsApi.md#endpoint_group_delete_endpoint) | **DELETE** /endpoint_groups/{id}/endpoints/{endpointId} | Removes environment(endpoint) from an environment(endpoint) group
[**endpoint_group_list**](EndpointGroupsApi.md#endpoint_group_list) | **GET** /endpoint_groups | List Environment(Endpoint) groups
[**endpoint_group_update**](EndpointGroupsApi.md#endpoint_group_update) | **PUT** /endpoint_groups/{id} | Update an environment(endpoint) group
[**endpoint_groups_id_get**](EndpointGroupsApi.md#endpoint_groups_id_get) | **GET** /endpoint_groups/{id} | Inspect an Environment(Endpoint) group
[**endpoint_groups_post**](EndpointGroupsApi.md#endpoint_groups_post) | **POST** /endpoint_groups | Create an Environment(Endpoint) Group


# **endpoint_group_add_endpoint**
> endpoint_group_add_endpoint(id, endpoint_id)

Add an environment(endpoint) to an environment(endpoint) group

Add an environment(endpoint) to an environment(endpoint) group **Access policy**: administrator

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
api_instance = portainer.EndpointGroupsApi(portainer.ApiClient(configuration))
id = 56 # int | EndpointGroup identifier
endpoint_id = 56 # int | Environment(Endpoint) identifier

try:
    # Add an environment(endpoint) to an environment(endpoint) group
    api_instance.endpoint_group_add_endpoint(id, endpoint_id)
except ApiException as e:
    print("Exception when calling EndpointGroupsApi->endpoint_group_add_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EndpointGroup identifier | 
 **endpoint_id** | **int**| Environment(Endpoint) identifier | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_group_delete**
> endpoint_group_delete(id)

Remove an environment(endpoint) group

Remove an environment(endpoint) group. **Access policy**: administrator

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
api_instance = portainer.EndpointGroupsApi(portainer.ApiClient(configuration))
id = 56 # int | EndpointGroup identifier

try:
    # Remove an environment(endpoint) group
    api_instance.endpoint_group_delete(id)
except ApiException as e:
    print("Exception when calling EndpointGroupsApi->endpoint_group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EndpointGroup identifier | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_group_delete_endpoint**
> endpoint_group_delete_endpoint(id, endpoint_id)

Removes environment(endpoint) from an environment(endpoint) group

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
api_instance = portainer.EndpointGroupsApi(portainer.ApiClient(configuration))
id = 56 # int | EndpointGroup identifier
endpoint_id = 56 # int | Environment(Endpoint) identifier

try:
    # Removes environment(endpoint) from an environment(endpoint) group
    api_instance.endpoint_group_delete_endpoint(id, endpoint_id)
except ApiException as e:
    print("Exception when calling EndpointGroupsApi->endpoint_group_delete_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EndpointGroup identifier | 
 **endpoint_id** | **int**| Environment(Endpoint) identifier | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_group_list**
> list[PortainerEndpointGroup] endpoint_group_list()

List Environment(Endpoint) groups

List all environment(endpoint) groups based on the current user authorizations. Will return all environment(endpoint) groups if using an administrator account otherwise it will only return authorized environment(endpoint) groups. **Access policy**: restricted

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
api_instance = portainer.EndpointGroupsApi(portainer.ApiClient(configuration))

try:
    # List Environment(Endpoint) groups
    api_response = api_instance.endpoint_group_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointGroupsApi->endpoint_group_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PortainerEndpointGroup]**](PortainerEndpointGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_group_update**
> PortainerEndpointGroup endpoint_group_update(id, body)

Update an environment(endpoint) group

Update an environment(endpoint) group. **Access policy**: administrator

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
api_instance = portainer.EndpointGroupsApi(portainer.ApiClient(configuration))
id = 56 # int | EndpointGroup identifier
body = portainer.EndpointgroupsEndpointGroupUpdatePayload() # EndpointgroupsEndpointGroupUpdatePayload | EndpointGroup details

try:
    # Update an environment(endpoint) group
    api_response = api_instance.endpoint_group_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointGroupsApi->endpoint_group_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EndpointGroup identifier | 
 **body** | [**EndpointgroupsEndpointGroupUpdatePayload**](EndpointgroupsEndpointGroupUpdatePayload.md)| EndpointGroup details | 

### Return type

[**PortainerEndpointGroup**](PortainerEndpointGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_groups_id_get**
> PortainerEndpointGroup endpoint_groups_id_get(id)

Inspect an Environment(Endpoint) group

Retrieve details abont an environment(endpoint) group. **Access policy**: administrator

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
api_instance = portainer.EndpointGroupsApi(portainer.ApiClient(configuration))
id = 56 # int | Environment(Endpoint) group identifier

try:
    # Inspect an Environment(Endpoint) group
    api_response = api_instance.endpoint_groups_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointGroupsApi->endpoint_groups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) group identifier | 

### Return type

[**PortainerEndpointGroup**](PortainerEndpointGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_groups_post**
> PortainerEndpointGroup endpoint_groups_post(body)

Create an Environment(Endpoint) Group

Create a new environment(endpoint) group. **Access policy**: administrator

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
api_instance = portainer.EndpointGroupsApi(portainer.ApiClient(configuration))
body = portainer.EndpointgroupsEndpointGroupCreatePayload() # EndpointgroupsEndpointGroupCreatePayload | Environment(Endpoint) Group details

try:
    # Create an Environment(Endpoint) Group
    api_response = api_instance.endpoint_groups_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointGroupsApi->endpoint_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EndpointgroupsEndpointGroupCreatePayload**](EndpointgroupsEndpointGroupCreatePayload.md)| Environment(Endpoint) Group details | 

### Return type

[**PortainerEndpointGroup**](PortainerEndpointGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

