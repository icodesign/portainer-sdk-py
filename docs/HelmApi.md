# portainer.HelmApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**helm_delete**](HelmApi.md#helm_delete) | **DELETE** /endpoints/{id}/kubernetes/helm/{release} | Delete Helm Release
[**helm_install**](HelmApi.md#helm_install) | **POST** /endpoints/{id}/kubernetes/helm | Install Helm Chart
[**helm_list**](HelmApi.md#helm_list) | **GET** /endpoints/{id}/kubernetes/helm | List Helm Releases
[**helm_repo_search**](HelmApi.md#helm_repo_search) | **GET** /templates/helm | Search Helm Charts
[**helm_show**](HelmApi.md#helm_show) | **GET** /templates/helm/{command} | Show Helm Chart Information
[**helm_user_repositories_list**](HelmApi.md#helm_user_repositories_list) | **GET** /endpoints/{id}/kubernetes/helm/repositories | List a users helm repositories
[**helm_user_repository_create**](HelmApi.md#helm_user_repository_create) | **POST** /endpoints/{id}/kubernetes/helm/repositories | Create a user helm repository


# **helm_delete**
> helm_delete(id, release, namespace)

Delete Helm Release

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
api_instance = portainer.HelmApi(portainer.ApiClient(configuration))
id = 56 # int | Environment(Endpoint) identifier
release = 'release_example' # str | The name of the release/application to uninstall
namespace = 'namespace_example' # str | An optional namespace

try:
    # Delete Helm Release
    api_instance.helm_delete(id, release, namespace)
except ApiException as e:
    print("Exception when calling HelmApi->helm_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **release** | **str**| The name of the release/application to uninstall | 
 **namespace** | **str**| An optional namespace | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_install**
> ReleaseRelease helm_install(id, payload)

Install Helm Chart

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
api_instance = portainer.HelmApi(portainer.ApiClient(configuration))
id = 56 # int | Environment(Endpoint) identifier
payload = portainer.HelmInstallChartPayload() # HelmInstallChartPayload | Chart details

try:
    # Install Helm Chart
    api_response = api_instance.helm_install(id, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmApi->helm_install: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **payload** | [**HelmInstallChartPayload**](HelmInstallChartPayload.md)| Chart details | 

### Return type

[**ReleaseRelease**](ReleaseRelease.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_list**
> list[ReleaseReleaseElement] helm_list(id, namespace, filter, selector)

List Helm Releases

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
api_instance = portainer.HelmApi(portainer.ApiClient(configuration))
id = 56 # int | Environment(Endpoint) identifier
namespace = 'namespace_example' # str | specify an optional namespace
filter = 'filter_example' # str | specify an optional filter
selector = 'selector_example' # str | specify an optional selector

try:
    # List Helm Releases
    api_response = api_instance.helm_list(id, namespace, filter, selector)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmApi->helm_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **namespace** | **str**| specify an optional namespace | 
 **filter** | **str**| specify an optional filter | 
 **selector** | **str**| specify an optional selector | 

### Return type

[**list[ReleaseReleaseElement]**](ReleaseReleaseElement.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_repo_search**
> str helm_repo_search(repo)

Search Helm Charts

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
api_instance = portainer.HelmApi(portainer.ApiClient(configuration))
repo = 'repo_example' # str | Helm repository URL

try:
    # Search Helm Charts
    api_response = api_instance.helm_repo_search(repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmApi->helm_repo_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Helm repository URL | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_show**
> str helm_show(repo, chart, command)

Show Helm Chart Information

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
api_instance = portainer.HelmApi(portainer.ApiClient(configuration))
repo = 'repo_example' # str | Helm repository URL
chart = 'chart_example' # str | Chart name
command = 'command_example' # str | chart/values/readme

try:
    # Show Helm Chart Information
    api_response = api_instance.helm_show(repo, chart, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmApi->helm_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Helm repository URL | 
 **chart** | **str**| Chart name | 
 **command** | **str**| chart/values/readme | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_user_repositories_list**
> HelmHelmUserRepositoryResponse helm_user_repositories_list(id)

List a users helm repositories

Inspect a user helm repositories. **Access policy**: authenticated

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
api_instance = portainer.HelmApi(portainer.ApiClient(configuration))
id = 56 # int | User identifier

try:
    # List a users helm repositories
    api_response = api_instance.helm_user_repositories_list(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmApi->helm_user_repositories_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User identifier | 

### Return type

[**HelmHelmUserRepositoryResponse**](HelmHelmUserRepositoryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_user_repository_create**
> PortainerHelmUserRepository helm_user_repository_create(id, payload)

Create a user helm repository

Create a user helm repository. **Access policy**: authenticated

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
api_instance = portainer.HelmApi(portainer.ApiClient(configuration))
id = 56 # int | Environment(Endpoint) identifier
payload = portainer.HelmAddHelmRepoUrlPayload() # HelmAddHelmRepoUrlPayload | Helm Repository

try:
    # Create a user helm repository
    api_response = api_instance.helm_user_repository_create(id, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmApi->helm_user_repository_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **payload** | [**HelmAddHelmRepoUrlPayload**](HelmAddHelmRepoUrlPayload.md)| Helm Repository | 

### Return type

[**PortainerHelmUserRepository**](PortainerHelmUserRepository.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

