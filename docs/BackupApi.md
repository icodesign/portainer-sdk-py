# portainer.BackupApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backup**](BackupApi.md#backup) | **POST** /backup | Creates an archive with a system data snapshot that could be used to restore the system.
[**restore**](BackupApi.md#restore) | **POST** /restore | Triggers a system restore using provided backup file


# **backup**
> backup(body=body)

Creates an archive with a system data snapshot that could be used to restore the system.

Creates an archive with a system data snapshot that could be used to restore the system. **Access policy**: admin

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
api_instance = portainer.BackupApi(portainer.ApiClient(configuration))
body = portainer.BackupBackupPayload() # BackupBackupPayload | An object contains the password to encrypt the backup with (optional)

try:
    # Creates an archive with a system data snapshot that could be used to restore the system.
    api_instance.backup(body=body)
except ApiException as e:
    print("Exception when calling BackupApi->backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BackupBackupPayload**](BackupBackupPayload.md)| An object contains the password to encrypt the backup with | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore**
> restore(restore_payload)

Triggers a system restore using provided backup file

Triggers a system restore using provided backup file **Access policy**: public

### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = portainer.BackupApi()
restore_payload = portainer.BackupRestorePayload() # BackupRestorePayload | Restore request payload

try:
    # Triggers a system restore using provided backup file
    api_instance.restore(restore_payload)
except ApiException as e:
    print("Exception when calling BackupApi->restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restore_payload** | [**BackupRestorePayload**](BackupRestorePayload.md)| Restore request payload | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

