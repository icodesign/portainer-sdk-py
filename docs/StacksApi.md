# portainer.StacksApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stack_associate**](StacksApi.md#stack_associate) | **PUT** /stacks/{id}/associate | Associate an orphaned stack to a new environment(endpoint)
[**stack_create**](StacksApi.md#stack_create) | **POST** /stacks | Deploy a new stack
[**stack_delete**](StacksApi.md#stack_delete) | **DELETE** /stacks/{id} | Remove a stack
[**stack_file_inspect**](StacksApi.md#stack_file_inspect) | **GET** /stacks/{id}/file | Retrieve the content of the Stack file for the specified stack
[**stack_git_redeploy**](StacksApi.md#stack_git_redeploy) | **PUT** /stacks/{id}/git/redeploy | Redeploy a stack
[**stack_inspect**](StacksApi.md#stack_inspect) | **GET** /stacks/{id} | Inspect a stack
[**stack_list**](StacksApi.md#stack_list) | **GET** /stacks | List stacks
[**stack_migrate**](StacksApi.md#stack_migrate) | **POST** /stacks/{id}/migrate | Migrate a stack to another environment(endpoint)
[**stack_start**](StacksApi.md#stack_start) | **POST** /stacks/{id}/start | Starts a stopped Stack
[**stack_stop**](StacksApi.md#stack_stop) | **POST** /stacks/{id}/stop | Stops a stopped Stack
[**stack_update**](StacksApi.md#stack_update) | **PUT** /stacks/{id} | Update a stack
[**stack_update_git**](StacksApi.md#stack_update_git) | **PUT** /stacks/{id}/git | Update a stack&#39;s Git configs
[**webhook_invoke**](StacksApi.md#webhook_invoke) | **POST** /stacks/webhooks/{webhookID} | Webhook for triggering stack updates from git


# **stack_associate**
> PortainerStack stack_associate(id, endpoint_id, swarm_id, orphaned_running)

Associate an orphaned stack to a new environment(endpoint)

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
api_instance = portainer.StacksApi(portainer.ApiClient(configuration))
id = 56 # int | Stack identifier
endpoint_id = 56 # int | Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack.
swarm_id = 56 # int | Swarm identifier
orphaned_running = true # bool | Indicates whether the stack is orphaned

try:
    # Associate an orphaned stack to a new environment(endpoint)
    api_response = api_instance.stack_associate(id, endpoint_id, swarm_id, orphaned_running)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->stack_associate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 
 **endpoint_id** | **int**| Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack. | 
 **swarm_id** | **int**| Swarm identifier | 
 **orphaned_running** | **bool**| Indicates whether the stack is orphaned | 

### Return type

[**PortainerStack**](PortainerStack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_create**
> PortainerCustomTemplate stack_create(type, method, endpoint_id, body_swarm_string=body_swarm_string, body_swarm_repository=body_swarm_repository, body_compose_string=body_compose_string, body_compose_repository=body_compose_repository, name=name, swarm_id=swarm_id, env=env, file=file)

Deploy a new stack

Deploy a new stack into a Docker environment(endpoint) specified via the environment(endpoint) identifier. **Access policy**: authenticated

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
api_instance = portainer.StacksApi(portainer.ApiClient(configuration))
type = 56 # int | Stack deployment type. Possible values: 1 (Swarm stack) or 2 (Compose stack).
method = 'method_example' # str | Stack deployment method. Possible values: file, string or repository.
endpoint_id = 56 # int | Identifier of the environment(endpoint) that will be used to deploy the stack
body_swarm_string = portainer.StacksSwarmStackFromFileContentPayload() # StacksSwarmStackFromFileContentPayload | Required when using method=string and type=1 (optional)
body_swarm_repository = portainer.StacksSwarmStackFromGitRepositoryPayload() # StacksSwarmStackFromGitRepositoryPayload | Required when using method=repository and type=1 (optional)
body_compose_string = portainer.StacksComposeStackFromFileContentPayload() # StacksComposeStackFromFileContentPayload | Required when using method=string and type=2 (optional)
body_compose_repository = portainer.StacksComposeStackFromGitRepositoryPayload() # StacksComposeStackFromGitRepositoryPayload | Required when using method=repository and type=2 (optional)
name = 'name_example' # str | Name of the stack. required when method is file (optional)
swarm_id = 'swarm_id_example' # str | Swarm cluster identifier. Required when method equals file and type equals 1. required when method is file (optional)
env = 'env_example' # str | Environment(Endpoint) variables passed during deployment, represented as a JSON array [{'name': 'name', 'value': 'value'}]. Optional, used when method equals file and type equals 1. (optional)
file = '/path/to/file.txt' # file | Stack file. required when method is file (optional)

try:
    # Deploy a new stack
    api_response = api_instance.stack_create(type, method, endpoint_id, body_swarm_string=body_swarm_string, body_swarm_repository=body_swarm_repository, body_compose_string=body_compose_string, body_compose_repository=body_compose_repository, name=name, swarm_id=swarm_id, env=env, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->stack_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **int**| Stack deployment type. Possible values: 1 (Swarm stack) or 2 (Compose stack). | 
 **method** | **str**| Stack deployment method. Possible values: file, string or repository. | 
 **endpoint_id** | **int**| Identifier of the environment(endpoint) that will be used to deploy the stack | 
 **body_swarm_string** | [**StacksSwarmStackFromFileContentPayload**](StacksSwarmStackFromFileContentPayload.md)| Required when using method&#x3D;string and type&#x3D;1 | [optional] 
 **body_swarm_repository** | [**StacksSwarmStackFromGitRepositoryPayload**](StacksSwarmStackFromGitRepositoryPayload.md)| Required when using method&#x3D;repository and type&#x3D;1 | [optional] 
 **body_compose_string** | [**StacksComposeStackFromFileContentPayload**](StacksComposeStackFromFileContentPayload.md)| Required when using method&#x3D;string and type&#x3D;2 | [optional] 
 **body_compose_repository** | [**StacksComposeStackFromGitRepositoryPayload**](StacksComposeStackFromGitRepositoryPayload.md)| Required when using method&#x3D;repository and type&#x3D;2 | [optional] 
 **name** | **str**| Name of the stack. required when method is file | [optional] 
 **swarm_id** | **str**| Swarm cluster identifier. Required when method equals file and type equals 1. required when method is file | [optional] 
 **env** | **str**| Environment(Endpoint) variables passed during deployment, represented as a JSON array [{&#39;name&#39;: &#39;name&#39;, &#39;value&#39;: &#39;value&#39;}]. Optional, used when method equals file and type equals 1. | [optional] 
 **file** | **file**| Stack file. required when method is file | [optional] 

### Return type

[**PortainerCustomTemplate**](PortainerCustomTemplate.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_delete**
> stack_delete(id, external=external, endpoint_id=endpoint_id)

Remove a stack

Remove a stack. **Access policy**: restricted

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
api_instance = portainer.StacksApi(portainer.ApiClient(configuration))
id = 56 # int | Stack identifier
external = true # bool | Set to true to delete an external stack. Only external Swarm stacks are supported (optional)
endpoint_id = 56 # int | Environment(Endpoint) identifier used to remove an external stack (required when external is set to true) (optional)

try:
    # Remove a stack
    api_instance.stack_delete(id, external=external, endpoint_id=endpoint_id)
except ApiException as e:
    print("Exception when calling StacksApi->stack_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 
 **external** | **bool**| Set to true to delete an external stack. Only external Swarm stacks are supported | [optional] 
 **endpoint_id** | **int**| Environment(Endpoint) identifier used to remove an external stack (required when external is set to true) | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_file_inspect**
> StacksStackFileResponse stack_file_inspect(id)

Retrieve the content of the Stack file for the specified stack

Get Stack file content. **Access policy**: restricted

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
api_instance = portainer.StacksApi(portainer.ApiClient(configuration))
id = 56 # int | Stack identifier

try:
    # Retrieve the content of the Stack file for the specified stack
    api_response = api_instance.stack_file_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->stack_file_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 

### Return type

[**StacksStackFileResponse**](StacksStackFileResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_git_redeploy**
> PortainerStack stack_git_redeploy(id, body, endpoint_id=endpoint_id)

Redeploy a stack

Pull and redeploy a stack via Git **Access policy**: authenticated

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
api_instance = portainer.StacksApi(portainer.ApiClient(configuration))
id = 56 # int | Stack identifier
body = portainer.StacksStackGitRedployPayload() # StacksStackGitRedployPayload | Git configs for pull and redeploy a stack
endpoint_id = 56 # int | Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack. (optional)

try:
    # Redeploy a stack
    api_response = api_instance.stack_git_redeploy(id, body, endpoint_id=endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->stack_git_redeploy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 
 **body** | [**StacksStackGitRedployPayload**](StacksStackGitRedployPayload.md)| Git configs for pull and redeploy a stack | 
 **endpoint_id** | **int**| Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack. | [optional] 

### Return type

[**PortainerStack**](PortainerStack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_inspect**
> PortainerStack stack_inspect(id)

Inspect a stack

Retrieve details about a stack. **Access policy**: restricted

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
api_instance = portainer.StacksApi(portainer.ApiClient(configuration))
id = 56 # int | Stack identifier

try:
    # Inspect a stack
    api_response = api_instance.stack_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->stack_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 

### Return type

[**PortainerStack**](PortainerStack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_list**
> list[PortainerStack] stack_list(filters=filters)

List stacks

List all stacks based on the current user authorizations. Will return all stacks if using an administrator account otherwise it will only return the list of stacks the user have access to. **Access policy**: authenticated

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
api_instance = portainer.StacksApi(portainer.ApiClient(configuration))
filters = 'filters_example' # str | Filters to process on the stack list. Encoded as JSON (a map[string]string). For example, {'SwarmID': 'jpofkc0i9uo9wtx1zesuk649w'} will only return stacks that are part of the specified Swarm cluster. Available filters: EndpointID, SwarmID. (optional)

try:
    # List stacks
    api_response = api_instance.stack_list(filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->stack_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filters to process on the stack list. Encoded as JSON (a map[string]string). For example, {&#39;SwarmID&#39;: &#39;jpofkc0i9uo9wtx1zesuk649w&#39;} will only return stacks that are part of the specified Swarm cluster. Available filters: EndpointID, SwarmID. | [optional] 

### Return type

[**list[PortainerStack]**](PortainerStack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_migrate**
> PortainerStack stack_migrate(id, body, endpoint_id=endpoint_id)

Migrate a stack to another environment(endpoint)

Migrate a stack from an environment(endpoint) to another environment(endpoint). It will re-create the stack inside the target environment(endpoint) before removing the original stack. **Access policy**: authenticated

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
api_instance = portainer.StacksApi(portainer.ApiClient(configuration))
id = 56 # int | Stack identifier
body = portainer.StacksStackMigratePayload() # StacksStackMigratePayload | Stack migration details
endpoint_id = 56 # int | Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack. (optional)

try:
    # Migrate a stack to another environment(endpoint)
    api_response = api_instance.stack_migrate(id, body, endpoint_id=endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->stack_migrate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 
 **body** | [**StacksStackMigratePayload**](StacksStackMigratePayload.md)| Stack migration details | 
 **endpoint_id** | **int**| Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack. | [optional] 

### Return type

[**PortainerStack**](PortainerStack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_start**
> PortainerStack stack_start(id)

Starts a stopped Stack

Starts a stopped Stack. **Access policy**: authenticated

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
api_instance = portainer.StacksApi(portainer.ApiClient(configuration))
id = 56 # int | Stack identifier

try:
    # Starts a stopped Stack
    api_response = api_instance.stack_start(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->stack_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 

### Return type

[**PortainerStack**](PortainerStack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_stop**
> PortainerStack stack_stop(id)

Stops a stopped Stack

Stops a stopped Stack. **Access policy**: authenticated

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
api_instance = portainer.StacksApi(portainer.ApiClient(configuration))
id = 56 # int | Stack identifier

try:
    # Stops a stopped Stack
    api_response = api_instance.stack_stop(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->stack_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 

### Return type

[**PortainerStack**](PortainerStack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_update**
> PortainerStack stack_update(id, body, endpoint_id=endpoint_id)

Update a stack

Update a stack. **Access policy**: authenticated

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
api_instance = portainer.StacksApi(portainer.ApiClient(configuration))
id = 56 # int | Stack identifier
body = portainer.StacksUpdateSwarmStackPayload() # StacksUpdateSwarmStackPayload | Stack details
endpoint_id = 56 # int | Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack. (optional)

try:
    # Update a stack
    api_response = api_instance.stack_update(id, body, endpoint_id=endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->stack_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 
 **body** | [**StacksUpdateSwarmStackPayload**](StacksUpdateSwarmStackPayload.md)| Stack details | 
 **endpoint_id** | **int**| Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack. | [optional] 

### Return type

[**PortainerStack**](PortainerStack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_update_git**
> PortainerStack stack_update_git(id, body, endpoint_id=endpoint_id)

Update a stack's Git configs

Update the Git settings in a stack, e.g., RepositoryReferenceName and AutoUpdate **Access policy**: authenticated

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
api_instance = portainer.StacksApi(portainer.ApiClient(configuration))
id = 56 # int | Stack identifier
body = portainer.StacksStackGitUpdatePayload() # StacksStackGitUpdatePayload | Git configs for pull and redeploy a stack
endpoint_id = 56 # int | Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack. (optional)

try:
    # Update a stack's Git configs
    api_response = api_instance.stack_update_git(id, body, endpoint_id=endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->stack_update_git: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 
 **body** | [**StacksStackGitUpdatePayload**](StacksStackGitUpdatePayload.md)| Git configs for pull and redeploy a stack | 
 **endpoint_id** | **int**| Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack. | [optional] 

### Return type

[**PortainerStack**](PortainerStack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_invoke**
> webhook_invoke(webhook_id)

Webhook for triggering stack updates from git

**Access policy**: public

### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = portainer.StacksApi()
webhook_id = 'webhook_id_example' # str | Stack identifier

try:
    # Webhook for triggering stack updates from git
    api_instance.webhook_invoke(webhook_id)
except ApiException as e:
    print("Exception when calling StacksApi->webhook_invoke: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Stack identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

