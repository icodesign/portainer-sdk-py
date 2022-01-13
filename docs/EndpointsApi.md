# portainer.EndpointsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoint_association_delete**](EndpointsApi.md#endpoint_association_delete) | **PUT** /endpoints/{id}/association | De-association an edge environment(endpoint)
[**endpoint_create**](EndpointsApi.md#endpoint_create) | **POST** /endpoints | Create a new environment(endpoint)
[**endpoint_delete**](EndpointsApi.md#endpoint_delete) | **DELETE** /endpoints/{id} | Remove an environment(endpoint)
[**endpoint_dockerhub_status**](EndpointsApi.md#endpoint_dockerhub_status) | **GET** /endpoints/{id}/dockerhub/{registryId} | fetch docker pull limits
[**endpoint_extension_add**](EndpointsApi.md#endpoint_extension_add) | **POST** /endpoints/{id}/extensions | 
[**endpoint_extension_remove**](EndpointsApi.md#endpoint_extension_remove) | **DELETE** /endpoints/{id}/extensions/{extensionType} | 
[**endpoint_inspect**](EndpointsApi.md#endpoint_inspect) | **GET** /endpoints/{id} | Inspect an environment(endpoint)
[**endpoint_list**](EndpointsApi.md#endpoint_list) | **GET** /endpoints | List environments(endpoints)
[**endpoint_registries_list**](EndpointsApi.md#endpoint_registries_list) | **GET** /endpoints/{id}/registries | List Registries on environment
[**endpoint_registry_access**](EndpointsApi.md#endpoint_registry_access) | **PUT** /endpoints/{id}/registries/{registryId} | update registry access for environment
[**endpoint_registry_inspect**](EndpointsApi.md#endpoint_registry_inspect) | **GET** /endpoints/{id}/registries/{registryId} | get registry for environment
[**endpoint_settings_update**](EndpointsApi.md#endpoint_settings_update) | **PUT** /endpoints/{id}/settings | Update settings for an environment(endpoint)
[**endpoint_snapshot**](EndpointsApi.md#endpoint_snapshot) | **POST** /endpoints/{id}/snapshot | Snapshots an environment(endpoint)
[**endpoint_snapshots**](EndpointsApi.md#endpoint_snapshots) | **POST** /endpoints/snapshot | Snapshot all environments(endpoints)
[**endpoint_status_inspect**](EndpointsApi.md#endpoint_status_inspect) | **GET** /endpoints/{id}/status | Get environment(endpoint) status
[**endpoint_update**](EndpointsApi.md#endpoint_update) | **PUT** /endpoints/{id} | Update an environment(endpoint)
[**endpoints_id_edge_jobs_job_id_logs_post**](EndpointsApi.md#endpoints_id_edge_jobs_job_id_logs_post) | **POST** /endpoints/{id}/edge/jobs/{jobID}/logs | Inspect an EdgeJob Log
[**endpoints_id_edge_stacks_stack_id_get**](EndpointsApi.md#endpoints_id_edge_stacks_stack_id_get) | **GET** /endpoints/{id}/edge/stacks/{stackId} | Inspect an Edge Stack for an Environment(Endpoint)


# **endpoint_association_delete**
> PortainerEndpoint endpoint_association_delete(id)

De-association an edge environment(endpoint)

De-association an edge environment(endpoint). **Access policy**: administrator

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
api_instance = portainer.EndpointsApi(portainer.ApiClient(configuration))
id = 56 # int | Environment(Endpoint) identifier

try:
    # De-association an edge environment(endpoint)
    api_response = api_instance.endpoint_association_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_association_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 

### Return type

[**PortainerEndpoint**](PortainerEndpoint.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_create**
> PortainerEndpoint endpoint_create(name, endpoint_creation_type, url=url, public_url=public_url, group_id=group_id, tls=tls, tls_skip_verify=tls_skip_verify, tls_skip_client_verify=tls_skip_client_verify, tlsca_cert_file=tlsca_cert_file, tls_cert_file=tls_cert_file, tls_key_file=tls_key_file, azure_application_id=azure_application_id, azure_tenant_id=azure_tenant_id, azure_authentication_key=azure_authentication_key, tag_i_ds=tag_i_ds, edge_checkin_interval=edge_checkin_interval)

Create a new environment(endpoint)

Create a new environment(endpoint) that will be used to manage an environment(endpoint). **Access policy**: administrator

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
api_instance = portainer.EndpointsApi(portainer.ApiClient(configuration))
name = 'name_example' # str | Name that will be used to identify this environment(endpoint) (example: my-environment)
endpoint_creation_type = 56 # int | Environment(Endpoint) type. Value must be one of: 1 (Local Docker environment), 2 (Agent environment), 3 (Azure environment), 4 (Edge agent environment) or 5 (Local Kubernetes Environment
url = 'url_example' # str | URL or IP address of a Docker host (example: docker.mydomain.tld:2375). Defaults to local if not specified (Linux: /var/run/docker.sock, Windows: //./pipe/docker_engine) (optional)
public_url = 'public_url_example' # str | URL or IP address where exposed containers will be reachable. Defaults to URL if not specified (example: docker.mydomain.tld:2375) (optional)
group_id = 56 # int | Environment(Endpoint) group identifier. If not specified will default to 1 (unassigned). (optional)
tls = true # bool | Require TLS to connect against this environment(endpoint) (optional)
tls_skip_verify = true # bool | Skip server verification when using TLS (optional)
tls_skip_client_verify = true # bool | Skip client verification when using TLS (optional)
tlsca_cert_file = '/path/to/file.txt' # file | TLS CA certificate file (optional)
tls_cert_file = '/path/to/file.txt' # file | TLS client certificate file (optional)
tls_key_file = '/path/to/file.txt' # file | TLS client key file (optional)
azure_application_id = 'azure_application_id_example' # str | Azure application ID. Required if environment(endpoint) type is set to 3 (optional)
azure_tenant_id = 'azure_tenant_id_example' # str | Azure tenant ID. Required if environment(endpoint) type is set to 3 (optional)
azure_authentication_key = 'azure_authentication_key_example' # str | Azure authentication key. Required if environment(endpoint) type is set to 3 (optional)
tag_i_ds = [56] # list[int] | List of tag identifiers to which this environment(endpoint) is associated (optional)
edge_checkin_interval = 56 # int | The check in interval for edge agent (in seconds) (optional)

try:
    # Create a new environment(endpoint)
    api_response = api_instance.endpoint_create(name, endpoint_creation_type, url=url, public_url=public_url, group_id=group_id, tls=tls, tls_skip_verify=tls_skip_verify, tls_skip_client_verify=tls_skip_client_verify, tlsca_cert_file=tlsca_cert_file, tls_cert_file=tls_cert_file, tls_key_file=tls_key_file, azure_application_id=azure_application_id, azure_tenant_id=azure_tenant_id, azure_authentication_key=azure_authentication_key, tag_i_ds=tag_i_ds, edge_checkin_interval=edge_checkin_interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name that will be used to identify this environment(endpoint) (example: my-environment) | 
 **endpoint_creation_type** | **int**| Environment(Endpoint) type. Value must be one of: 1 (Local Docker environment), 2 (Agent environment), 3 (Azure environment), 4 (Edge agent environment) or 5 (Local Kubernetes Environment | 
 **url** | **str**| URL or IP address of a Docker host (example: docker.mydomain.tld:2375). Defaults to local if not specified (Linux: /var/run/docker.sock, Windows: //./pipe/docker_engine) | [optional] 
 **public_url** | **str**| URL or IP address where exposed containers will be reachable. Defaults to URL if not specified (example: docker.mydomain.tld:2375) | [optional] 
 **group_id** | **int**| Environment(Endpoint) group identifier. If not specified will default to 1 (unassigned). | [optional] 
 **tls** | **bool**| Require TLS to connect against this environment(endpoint) | [optional] 
 **tls_skip_verify** | **bool**| Skip server verification when using TLS | [optional] 
 **tls_skip_client_verify** | **bool**| Skip client verification when using TLS | [optional] 
 **tlsca_cert_file** | **file**| TLS CA certificate file | [optional] 
 **tls_cert_file** | **file**| TLS client certificate file | [optional] 
 **tls_key_file** | **file**| TLS client key file | [optional] 
 **azure_application_id** | **str**| Azure application ID. Required if environment(endpoint) type is set to 3 | [optional] 
 **azure_tenant_id** | **str**| Azure tenant ID. Required if environment(endpoint) type is set to 3 | [optional] 
 **azure_authentication_key** | **str**| Azure authentication key. Required if environment(endpoint) type is set to 3 | [optional] 
 **tag_i_ds** | [**list[int]**](int.md)| List of tag identifiers to which this environment(endpoint) is associated | [optional] 
 **edge_checkin_interval** | **int**| The check in interval for edge agent (in seconds) | [optional] 

### Return type

[**PortainerEndpoint**](PortainerEndpoint.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_delete**
> endpoint_delete(id)

Remove an environment(endpoint)

Remove an environment(endpoint). **Access policy**: administrator

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
api_instance = portainer.EndpointsApi(portainer.ApiClient(configuration))
id = 56 # int | Environment(Endpoint) identifier

try:
    # Remove an environment(endpoint)
    api_instance.endpoint_delete(id)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_dockerhub_status**
> EndpointsDockerhubStatusResponse endpoint_dockerhub_status(id, registry_id)

fetch docker pull limits

get docker pull limits for a docker hub registry in the environment **Access policy**:

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
api_instance = portainer.EndpointsApi(portainer.ApiClient(configuration))
id = 56 # int | endpoint ID
registry_id = 56 # int | registry ID

try:
    # fetch docker pull limits
    api_response = api_instance.endpoint_dockerhub_status(id, registry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_dockerhub_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| endpoint ID | 
 **registry_id** | **int**| registry ID | 

### Return type

[**EndpointsDockerhubStatusResponse**](EndpointsDockerhubStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_extension_add**
> endpoint_extension_add(id)



### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = portainer.EndpointsApi()
id = 56 # int | Environment(Endpoint) identifier

try:
    api_instance.endpoint_extension_add(id)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_extension_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_extension_remove**
> endpoint_extension_remove(id, extension_type)



### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = portainer.EndpointsApi()
id = 56 # int | Environment(Endpoint) identifier
extension_type = 'extension_type_example' # str | Extension Type

try:
    api_instance.endpoint_extension_remove(id, extension_type)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_extension_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **extension_type** | **str**| Extension Type | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_inspect**
> PortainerEndpoint endpoint_inspect(id)

Inspect an environment(endpoint)

Retrieve details about an environment(endpoint). **Access policy**: restricted

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
api_instance = portainer.EndpointsApi(portainer.ApiClient(configuration))
id = 56 # int | Environment(Endpoint) identifier

try:
    # Inspect an environment(endpoint)
    api_response = api_instance.endpoint_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 

### Return type

[**PortainerEndpoint**](PortainerEndpoint.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_list**
> list[PortainerEndpoint] endpoint_list(start=start, search=search, group_id=group_id, limit=limit, types=types, tag_ids=tag_ids, tags_partial_match=tags_partial_match, endpoint_ids=endpoint_ids)

List environments(endpoints)

List all environments(endpoints) based on the current user authorizations. Will return all environments(endpoints) if using an administrator account otherwise it will only return authorized environments(endpoints). **Access policy**: restricted

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
api_instance = portainer.EndpointsApi(portainer.ApiClient(configuration))
start = 56 # int | Start searching from (optional)
search = 'search_example' # str | Search query (optional)
group_id = 56 # int | List environments(endpoints) of this group (optional)
limit = 56 # int | Limit results to this value (optional)
types = [56] # list[int] | List environments(endpoints) of this type (optional)
tag_ids = [56] # list[int] | search environments(endpoints) with these tags (depends on tagsPartialMatch) (optional)
tags_partial_match = true # bool | If true, will return environment(endpoint) which has one of tagIds, if false (or missing) will return only environments(endpoints) that has all the tags (optional)
endpoint_ids = [56] # list[int] | will return only these environments(endpoints) (optional)

try:
    # List environments(endpoints)
    api_response = api_instance.endpoint_list(start=start, search=search, group_id=group_id, limit=limit, types=types, tag_ids=tag_ids, tags_partial_match=tags_partial_match, endpoint_ids=endpoint_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Start searching from | [optional] 
 **search** | **str**| Search query | [optional] 
 **group_id** | **int**| List environments(endpoints) of this group | [optional] 
 **limit** | **int**| Limit results to this value | [optional] 
 **types** | [**list[int]**](int.md)| List environments(endpoints) of this type | [optional] 
 **tag_ids** | [**list[int]**](int.md)| search environments(endpoints) with these tags (depends on tagsPartialMatch) | [optional] 
 **tags_partial_match** | **bool**| If true, will return environment(endpoint) which has one of tagIds, if false (or missing) will return only environments(endpoints) that has all the tags | [optional] 
 **endpoint_ids** | [**list[int]**](int.md)| will return only these environments(endpoints) | [optional] 

### Return type

[**list[PortainerEndpoint]**](PortainerEndpoint.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_registries_list**
> list[PortainerRegistry] endpoint_registries_list(id, namespace=namespace)

List Registries on environment

List all registries based on the current user authorizations in current environment. **Access policy**: authenticated

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
api_instance = portainer.EndpointsApi(portainer.ApiClient(configuration))
id = 56 # int | Environment(Endpoint) identifier
namespace = 'namespace_example' # str | required if kubernetes environment, will show registries by namespace (optional)

try:
    # List Registries on environment
    api_response = api_instance.endpoint_registries_list(id, namespace=namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_registries_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **namespace** | **str**| required if kubernetes environment, will show registries by namespace | [optional] 

### Return type

[**list[PortainerRegistry]**](PortainerRegistry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_registry_access**
> endpoint_registry_access(id, registry_id, body)

update registry access for environment

**Access policy**: authenticated

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
api_instance = portainer.EndpointsApi(portainer.ApiClient(configuration))
id = 56 # int | Environment(Endpoint) identifier
registry_id = 56 # int | Registry identifier
body = portainer.EndpointsRegistryAccessPayload() # EndpointsRegistryAccessPayload | details

try:
    # update registry access for environment
    api_instance.endpoint_registry_access(id, registry_id, body)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_registry_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **registry_id** | **int**| Registry identifier | 
 **body** | [**EndpointsRegistryAccessPayload**](EndpointsRegistryAccessPayload.md)| details | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_registry_inspect**
> PortainerRegistry endpoint_registry_inspect(id, registry_id)

get registry for environment

**Access policy**: authenticated

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
api_instance = portainer.EndpointsApi(portainer.ApiClient(configuration))
id = 56 # int | identifier
registry_id = 56 # int | Registry identifier

try:
    # get registry for environment
    api_response = api_instance.endpoint_registry_inspect(id, registry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_registry_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifier | 
 **registry_id** | **int**| Registry identifier | 

### Return type

[**PortainerRegistry**](PortainerRegistry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_settings_update**
> PortainerEndpoint endpoint_settings_update(id, body)

Update settings for an environment(endpoint)

Update settings for an environment(endpoint). **Access policy**: authenticated

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
api_instance = portainer.EndpointsApi(portainer.ApiClient(configuration))
id = 56 # int | Environment(Endpoint) identifier
body = portainer.EndpointsEndpointSettingsUpdatePayload() # EndpointsEndpointSettingsUpdatePayload | Environment(Endpoint) details

try:
    # Update settings for an environment(endpoint)
    api_response = api_instance.endpoint_settings_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **body** | [**EndpointsEndpointSettingsUpdatePayload**](EndpointsEndpointSettingsUpdatePayload.md)| Environment(Endpoint) details | 

### Return type

[**PortainerEndpoint**](PortainerEndpoint.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_snapshot**
> endpoint_snapshot(id)

Snapshots an environment(endpoint)

Snapshots an environment(endpoint) **Access policy**: administrator

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
api_instance = portainer.EndpointsApi(portainer.ApiClient(configuration))
id = 56 # int | Environment(Endpoint) identifier

try:
    # Snapshots an environment(endpoint)
    api_instance.endpoint_snapshot(id)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_snapshots**
> endpoint_snapshots()

Snapshot all environments(endpoints)

Snapshot all environments(endpoints) **Access policy**: administrator

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
api_instance = portainer.EndpointsApi(portainer.ApiClient(configuration))

try:
    # Snapshot all environments(endpoints)
    api_instance.endpoint_snapshots()
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_snapshots: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_status_inspect**
> EndpointsEndpointStatusInspectResponse endpoint_status_inspect(id)

Get environment(endpoint) status

Environment(Endpoint) for edge agent to check status of environment(endpoint) **Access policy**: restricted only to Edge environments(endpoints)

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
api_instance = portainer.EndpointsApi(portainer.ApiClient(configuration))
id = 56 # int | Environment(Endpoint) identifier

try:
    # Get environment(endpoint) status
    api_response = api_instance.endpoint_status_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_status_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 

### Return type

[**EndpointsEndpointStatusInspectResponse**](EndpointsEndpointStatusInspectResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_update**
> PortainerEndpoint endpoint_update(id, body)

Update an environment(endpoint)

Update an environment(endpoint). **Access policy**: authenticated

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
api_instance = portainer.EndpointsApi(portainer.ApiClient(configuration))
id = 56 # int | Environment(Endpoint) identifier
body = portainer.EndpointsEndpointUpdatePayload() # EndpointsEndpointUpdatePayload | Environment(Endpoint) details

try:
    # Update an environment(endpoint)
    api_response = api_instance.endpoint_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **body** | [**EndpointsEndpointUpdatePayload**](EndpointsEndpointUpdatePayload.md)| Environment(Endpoint) details | 

### Return type

[**PortainerEndpoint**](PortainerEndpoint.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = portainer.EndpointsApi()
id = 'id_example' # str | environment(endpoint) Id
job_id = 'job_id_example' # str | Job Id

try:
    # Inspect an EdgeJob Log
    api_instance.endpoints_id_edge_jobs_job_id_logs_post(id, job_id)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoints_id_edge_jobs_job_id_logs_post: %s\n" % e)
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
api_instance = portainer.EndpointsApi()
id = 'id_example' # str | environment(endpoint) Id
stack_id = 'stack_id_example' # str | EdgeStack Id

try:
    # Inspect an Edge Stack for an Environment(Endpoint)
    api_response = api_instance.endpoints_id_edge_stacks_stack_id_get(id, stack_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoints_id_edge_stacks_stack_id_get: %s\n" % e)
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

