# portainer.SettingsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_inspect**](SettingsApi.md#settings_inspect) | **GET** /settings | Retrieve Portainer settings
[**settings_public**](SettingsApi.md#settings_public) | **GET** /settings/public | Retrieve Portainer public settings
[**settings_update**](SettingsApi.md#settings_update) | **PUT** /settings | Update Portainer settings


# **settings_inspect**
> PortainerSettings settings_inspect()

Retrieve Portainer settings

Retrieve Portainer settings. **Access policy**: administrator

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
api_instance = portainer.SettingsApi(portainer.ApiClient(configuration))

try:
    # Retrieve Portainer settings
    api_response = api_instance.settings_inspect()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_inspect: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PortainerSettings**](PortainerSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_public**
> SettingsPublicSettingsResponse settings_public()

Retrieve Portainer public settings

Retrieve public settings. Returns a small set of settings that are not reserved to administrators only. **Access policy**: public

### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = portainer.SettingsApi()

try:
    # Retrieve Portainer public settings
    api_response = api_instance.settings_public()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_public: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsPublicSettingsResponse**](SettingsPublicSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_update**
> PortainerSettings settings_update(body)

Update Portainer settings

Update Portainer settings. **Access policy**: administrator

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
api_instance = portainer.SettingsApi(portainer.ApiClient(configuration))
body = portainer.SettingsSettingsUpdatePayload() # SettingsSettingsUpdatePayload | New settings

try:
    # Update Portainer settings
    api_response = api_instance.settings_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsSettingsUpdatePayload**](SettingsSettingsUpdatePayload.md)| New settings | 

### Return type

[**PortainerSettings**](PortainerSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

