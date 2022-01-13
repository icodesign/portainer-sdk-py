# portainer.EdgeApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoints_id_edge_jobs_job_id_logs_post**](EdgeApi.md#endpoints_id_edge_jobs_job_id_logs_post) | **POST** /endpoints/{id}/edge/jobs/{jobID}/logs | Inspect an EdgeJob Log
[**endpoints_id_edge_stacks_stack_id_get**](EdgeApi.md#endpoints_id_edge_stacks_stack_id_get) | **GET** /endpoints/{id}/edge/stacks/{stackId} | Inspect an Edge Stack for an Environment(Endpoint)


# **endpoints_id_edge_jobs_job_id_logs_post**
> endpoints_id_edge_jobs_job_id_logs_post(id, job_id)

Inspect an EdgeJob Log

**Access policy**: public

### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = portainer.EdgeApi()
id = 'id_example' # str | environment(endpoint) Id
job_id = 'job_id_example' # str | Job Id

try:
    # Inspect an EdgeJob Log
    api_instance.endpoints_id_edge_jobs_job_id_logs_post(id, job_id)
except ApiException as e:
    print("Exception when calling EdgeApi->endpoints_id_edge_jobs_job_id_logs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| environment(endpoint) Id | 
 **job_id** | **str**| Job Id | 

### Return type

void (empty response body)

### Authorization

No authorization required

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
api_instance = portainer.EdgeApi()
id = 'id_example' # str | environment(endpoint) Id
stack_id = 'stack_id_example' # str | EdgeStack Id

try:
    # Inspect an Edge Stack for an Environment(Endpoint)
    api_response = api_instance.endpoints_id_edge_stacks_stack_id_get(id, stack_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdgeApi->endpoints_id_edge_stacks_stack_id_get: %s\n" % e)
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

