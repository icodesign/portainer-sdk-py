# portainer.WebhooksApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooks_get**](WebhooksApi.md#webhooks_get) | **GET** /webhooks | List webhooks
[**webhooks_id_delete**](WebhooksApi.md#webhooks_id_delete) | **DELETE** /webhooks/{id} | Delete a webhook
[**webhooks_id_put**](WebhooksApi.md#webhooks_id_put) | **PUT** /webhooks/{id} | Update a webhook
[**webhooks_post**](WebhooksApi.md#webhooks_post) | **POST** /webhooks | Create a webhook
[**webhooks_token_post**](WebhooksApi.md#webhooks_token_post) | **POST** /webhooks/{token} | Execute a webhook


# **webhooks_get**
> list[PortainerWebhook] webhooks_get(endpoint_id=endpoint_id, resource_id=resource_id)

List webhooks

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
api_instance = portainer.WebhooksApi(portainer.ApiClient(configuration))
endpoint_id = 56 # int |  (optional)
resource_id = 'resource_id_example' # str |  (optional)

try:
    # List webhooks
    api_response = api_instance.webhooks_get(endpoint_id=endpoint_id, resource_id=resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**|  | [optional] 
 **resource_id** | **str**|  | [optional] 

### Return type

[**list[PortainerWebhook]**](PortainerWebhook.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_id_delete**
> webhooks_id_delete(id)

Delete a webhook

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
api_instance = portainer.WebhooksApi(portainer.ApiClient(configuration))
id = 56 # int | Webhook id

try:
    # Delete a webhook
    api_instance.webhooks_id_delete(id)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Webhook id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_id_put**
> PortainerWebhook webhooks_id_put(body)

Update a webhook

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
api_instance = portainer.WebhooksApi(portainer.ApiClient(configuration))
body = portainer.WebhooksWebhookUpdatePayload() # WebhooksWebhookUpdatePayload | Webhook data

try:
    # Update a webhook
    api_response = api_instance.webhooks_id_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhooksWebhookUpdatePayload**](WebhooksWebhookUpdatePayload.md)| Webhook data | 

### Return type

[**PortainerWebhook**](PortainerWebhook.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_post**
> PortainerWebhook webhooks_post(body)

Create a webhook

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
api_instance = portainer.WebhooksApi(portainer.ApiClient(configuration))
body = portainer.WebhooksWebhookCreatePayload() # WebhooksWebhookCreatePayload | Webhook data

try:
    # Create a webhook
    api_response = api_instance.webhooks_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhooksWebhookCreatePayload**](WebhooksWebhookCreatePayload.md)| Webhook data | 

### Return type

[**PortainerWebhook**](PortainerWebhook.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_token_post**
> webhooks_token_post(token)

Execute a webhook

Acts on a passed in token UUID to restart the docker service **Access policy**: public

### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = portainer.WebhooksApi()
token = 'token_example' # str | Webhook token

try:
    # Execute a webhook
    api_instance.webhooks_token_post(token)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Webhook token | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

