# portainer.EdgeJobsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_job_create**](EdgeJobsApi.md#edge_job_create) | **POST** /edge_jobs | Create an EdgeJob
[**edge_job_delete**](EdgeJobsApi.md#edge_job_delete) | **DELETE** /edge_jobs/{id} | Delete an EdgeJob
[**edge_job_file**](EdgeJobsApi.md#edge_job_file) | **GET** /edge_jobs/{id}/file | Fetch a file of an EdgeJob
[**edge_job_inspect**](EdgeJobsApi.md#edge_job_inspect) | **GET** /edge_jobs/{id} | Inspect an EdgeJob
[**edge_job_list**](EdgeJobsApi.md#edge_job_list) | **GET** /edge_jobs | Fetch EdgeJobs list
[**edge_job_task_logs_inspect**](EdgeJobsApi.md#edge_job_task_logs_inspect) | **GET** /edge_jobs/{id}/tasks/{taskID}/logs | Fetch the log for a specifc task on an EdgeJob
[**edge_job_tasks_clear**](EdgeJobsApi.md#edge_job_tasks_clear) | **DELETE** /edge_jobs/{id}/tasks/{taskID}/logs | Clear the log for a specifc task on an EdgeJob
[**edge_job_tasks_collect**](EdgeJobsApi.md#edge_job_tasks_collect) | **POST** /edge_jobs/{id}/tasks/{taskID}/logs | Collect the log for a specifc task on an EdgeJob
[**edge_job_tasks_list**](EdgeJobsApi.md#edge_job_tasks_list) | **GET** /edge_jobs/{id}/tasks | Fetch the list of tasks on an EdgeJob
[**edge_job_update**](EdgeJobsApi.md#edge_job_update) | **POST** /edge_jobs/{id} | Update an EdgeJob


# **edge_job_create**
> PortainerEdgeGroup edge_job_create(method, body_string, body_file)

Create an EdgeJob

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
api_instance = portainer.EdgeJobsApi(portainer.ApiClient(configuration))
method = 'method_example' # str | Creation Method
body_string = portainer.EdgejobsEdgeJobCreateFromFileContentPayload() # EdgejobsEdgeJobCreateFromFileContentPayload | EdgeGroup data when method is string
body_file = portainer.EdgejobsEdgeJobCreateFromFilePayload() # EdgejobsEdgeJobCreateFromFilePayload | EdgeGroup data when method is file

try:
    # Create an EdgeJob
    api_response = api_instance.edge_job_create(method, body_string, body_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeJobsApi->edge_job_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method** | **str**| Creation Method | 
 **body_string** | [**EdgejobsEdgeJobCreateFromFileContentPayload**](EdgejobsEdgeJobCreateFromFileContentPayload.md)| EdgeGroup data when method is string | 
 **body_file** | [**EdgejobsEdgeJobCreateFromFilePayload**](EdgejobsEdgeJobCreateFromFilePayload.md)| EdgeGroup data when method is file | 

### Return type

[**PortainerEdgeGroup**](PortainerEdgeGroup.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_job_delete**
> edge_job_delete(id)

Delete an EdgeJob

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
api_instance = portainer.EdgeJobsApi(portainer.ApiClient(configuration))
id = 'id_example' # str | EdgeJob Id

try:
    # Delete an EdgeJob
    api_instance.edge_job_delete(id)
except ApiException as e:
    print("Exception when calling EdgeJobsApi->edge_job_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EdgeJob Id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_job_file**
> EdgejobsEdgeJobFileResponse edge_job_file(id)

Fetch a file of an EdgeJob

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
api_instance = portainer.EdgeJobsApi(portainer.ApiClient(configuration))
id = 'id_example' # str | EdgeJob Id

try:
    # Fetch a file of an EdgeJob
    api_response = api_instance.edge_job_file(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeJobsApi->edge_job_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EdgeJob Id | 

### Return type

[**EdgejobsEdgeJobFileResponse**](EdgejobsEdgeJobFileResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_job_inspect**
> PortainerEdgeJob edge_job_inspect(id)

Inspect an EdgeJob

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
api_instance = portainer.EdgeJobsApi(portainer.ApiClient(configuration))
id = 'id_example' # str | EdgeJob Id

try:
    # Inspect an EdgeJob
    api_response = api_instance.edge_job_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeJobsApi->edge_job_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EdgeJob Id | 

### Return type

[**PortainerEdgeJob**](PortainerEdgeJob.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_job_list**
> list[PortainerEdgeJob] edge_job_list()

Fetch EdgeJobs list

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
api_instance = portainer.EdgeJobsApi(portainer.ApiClient(configuration))

try:
    # Fetch EdgeJobs list
    api_response = api_instance.edge_job_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeJobsApi->edge_job_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PortainerEdgeJob]**](PortainerEdgeJob.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_job_task_logs_inspect**
> EdgejobsFileResponse edge_job_task_logs_inspect(id, task_id)

Fetch the log for a specifc task on an EdgeJob

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
api_instance = portainer.EdgeJobsApi(portainer.ApiClient(configuration))
id = 'id_example' # str | EdgeJob Id
task_id = 'task_id_example' # str | Task Id

try:
    # Fetch the log for a specifc task on an EdgeJob
    api_response = api_instance.edge_job_task_logs_inspect(id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeJobsApi->edge_job_task_logs_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EdgeJob Id | 
 **task_id** | **str**| Task Id | 

### Return type

[**EdgejobsFileResponse**](EdgejobsFileResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_job_tasks_clear**
> edge_job_tasks_clear(id, task_id)

Clear the log for a specifc task on an EdgeJob

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
api_instance = portainer.EdgeJobsApi(portainer.ApiClient(configuration))
id = 'id_example' # str | EdgeJob Id
task_id = 'task_id_example' # str | Task Id

try:
    # Clear the log for a specifc task on an EdgeJob
    api_instance.edge_job_tasks_clear(id, task_id)
except ApiException as e:
    print("Exception when calling EdgeJobsApi->edge_job_tasks_clear: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EdgeJob Id | 
 **task_id** | **str**| Task Id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_job_tasks_collect**
> edge_job_tasks_collect(id, task_id)

Collect the log for a specifc task on an EdgeJob

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
api_instance = portainer.EdgeJobsApi(portainer.ApiClient(configuration))
id = 'id_example' # str | EdgeJob Id
task_id = 'task_id_example' # str | Task Id

try:
    # Collect the log for a specifc task on an EdgeJob
    api_instance.edge_job_tasks_collect(id, task_id)
except ApiException as e:
    print("Exception when calling EdgeJobsApi->edge_job_tasks_collect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EdgeJob Id | 
 **task_id** | **str**| Task Id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_job_tasks_list**
> list[EdgejobsTaskContainer] edge_job_tasks_list(id)

Fetch the list of tasks on an EdgeJob

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
api_instance = portainer.EdgeJobsApi(portainer.ApiClient(configuration))
id = 'id_example' # str | EdgeJob Id

try:
    # Fetch the list of tasks on an EdgeJob
    api_response = api_instance.edge_job_tasks_list(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeJobsApi->edge_job_tasks_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EdgeJob Id | 

### Return type

[**list[EdgejobsTaskContainer]**](EdgejobsTaskContainer.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_job_update**
> PortainerEdgeJob edge_job_update(id, body)

Update an EdgeJob

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
api_instance = portainer.EdgeJobsApi(portainer.ApiClient(configuration))
id = 'id_example' # str | EdgeJob Id
body = portainer.EdgejobsEdgeJobUpdatePayload() # EdgejobsEdgeJobUpdatePayload | EdgeGroup data

try:
    # Update an EdgeJob
    api_response = api_instance.edge_job_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeJobsApi->edge_job_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EdgeJob Id | 
 **body** | [**EdgejobsEdgeJobUpdatePayload**](EdgejobsEdgeJobUpdatePayload.md)| EdgeGroup data | 

### Return type

[**PortainerEdgeJob**](PortainerEdgeJob.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

