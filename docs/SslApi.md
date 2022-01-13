# portainer.SslApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**s_sl_inspect**](SslApi.md#s_sl_inspect) | **GET** /ssl | Inspect the ssl settings
[**s_sl_update**](SslApi.md#s_sl_update) | **PUT** /ssl | Update the ssl settings


# **s_sl_inspect**
> PortainerSSLSettings s_sl_inspect()

Inspect the ssl settings

Retrieve the ssl settings. **Access policy**: administrator

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
api_instance = portainer.SslApi(portainer.ApiClient(configuration))

try:
    # Inspect the ssl settings
    api_response = api_instance.s_sl_inspect()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SslApi->s_sl_inspect: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PortainerSSLSettings**](PortainerSSLSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_sl_update**
> s_sl_update(body)

Update the ssl settings

Update the ssl settings. **Access policy**: administrator

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
api_instance = portainer.SslApi(portainer.ApiClient(configuration))
body = portainer.SslSslUpdatePayload() # SslSslUpdatePayload | SSL Settings

try:
    # Update the ssl settings
    api_instance.s_sl_update(body)
except ApiException as e:
    print("Exception when calling SslApi->s_sl_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SslSslUpdatePayload**](SslSslUpdatePayload.md)| SSL Settings | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

