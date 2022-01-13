# portainer.UploadApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_tls**](UploadApi.md#upload_tls) | **POST** /upload/tls/{certificate} | Upload TLS files


# **upload_tls**
> upload_tls(certificate, folder, file)

Upload TLS files

Use this environment(endpoint) to upload TLS files. **Access policy**: administrator

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
api_instance = portainer.UploadApi(portainer.ApiClient(configuration))
certificate = 'certificate_example' # str | TLS file type. Valid values are 'ca', 'cert' or 'key'.
folder = 'folder_example' # str | Folder where the TLS file will be stored. Will be created if not existing
file = '/path/to/file.txt' # file | The file to upload

try:
    # Upload TLS files
    api_instance.upload_tls(certificate, folder, file)
except ApiException as e:
    print("Exception when calling UploadApi->upload_tls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate** | **str**| TLS file type. Valid values are &#39;ca&#39;, &#39;cert&#39; or &#39;key&#39;. | 
 **folder** | **str**| Folder where the TLS file will be stored. Will be created if not existing | 
 **file** | **file**| The file to upload | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

