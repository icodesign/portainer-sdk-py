# portainer.UsersApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_admin_check**](UsersApi.md#user_admin_check) | **GET** /users/admin/check | Check administrator account existence
[**user_admin_init**](UsersApi.md#user_admin_init) | **POST** /users/admin/init | Initialize administrator account
[**user_create**](UsersApi.md#user_create) | **POST** /users | Create a new user
[**user_delete**](UsersApi.md#user_delete) | **DELETE** /users/{id} | Remove a user
[**user_generate_api_key**](UsersApi.md#user_generate_api_key) | **POST** /users/{id}/tokens | Generate an API key for a user
[**user_get_api_keys**](UsersApi.md#user_get_api_keys) | **GET** /users/{id}/tokens | Get all API keys for a user
[**user_inspect**](UsersApi.md#user_inspect) | **GET** /users/{id} | Inspect a user
[**user_list**](UsersApi.md#user_list) | **GET** /users | List users
[**user_memberships_inspect**](UsersApi.md#user_memberships_inspect) | **GET** /users/{id}/memberships | Inspect a user memberships
[**user_remove_api_key**](UsersApi.md#user_remove_api_key) | **DELETE** /users/{id}/tokens/{keyID} | Remove an api-key associated to a user
[**user_update**](UsersApi.md#user_update) | **PUT** /users/{id} | Update a user
[**user_update_password**](UsersApi.md#user_update_password) | **PUT** /users/{id}/passwd | Update password for a user


# **user_admin_check**
> user_admin_check()

Check administrator account existence

Check if an administrator account exists in the database. **Access policy**: public

### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = portainer.UsersApi()

try:
    # Check administrator account existence
    api_instance.user_admin_check()
except ApiException as e:
    print("Exception when calling UsersApi->user_admin_check: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_admin_init**
> PortainerUser user_admin_init(body)

Initialize administrator account

Initialize the 'admin' user account. **Access policy**: public

### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = portainer.UsersApi()
body = portainer.UsersAdminInitPayload() # UsersAdminInitPayload | User details

try:
    # Initialize administrator account
    api_response = api_instance.user_admin_init(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_admin_init: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersAdminInitPayload**](UsersAdminInitPayload.md)| User details | 

### Return type

[**PortainerUser**](PortainerUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_create**
> PortainerUser user_create(body)

Create a new user

Create a new Portainer user. Only team leaders and administrators can create users. Only administrators can create an administrator user account. **Access policy**: restricted

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
api_instance = portainer.UsersApi(portainer.ApiClient(configuration))
body = portainer.UsersUserCreatePayload() # UsersUserCreatePayload | User details

try:
    # Create a new user
    api_response = api_instance.user_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersUserCreatePayload**](UsersUserCreatePayload.md)| User details | 

### Return type

[**PortainerUser**](PortainerUser.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_delete**
> user_delete(id)

Remove a user

Remove a user. **Access policy**: administrator

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
api_instance = portainer.UsersApi(portainer.ApiClient(configuration))
id = 56 # int | User identifier

try:
    # Remove a user
    api_instance.user_delete(id)
except ApiException as e:
    print("Exception when calling UsersApi->user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User identifier | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_generate_api_key**
> UsersAccessTokenResponse user_generate_api_key(id, body)

Generate an API key for a user

Generates an API key for a user. Only the calling user can generate a token for themselves. **Access policy**: restricted

### Example
```python
from __future__ import print_function
import time
import portainer
from portainer.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
configuration = portainer.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = portainer.UsersApi(portainer.ApiClient(configuration))
id = 56 # int | User identifier
body = portainer.UsersUserAccessTokenCreatePayload() # UsersUserAccessTokenCreatePayload | details

try:
    # Generate an API key for a user
    api_response = api_instance.user_generate_api_key(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_generate_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User identifier | 
 **body** | [**UsersUserAccessTokenCreatePayload**](UsersUserAccessTokenCreatePayload.md)| details | 

### Return type

[**UsersAccessTokenResponse**](UsersAccessTokenResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_api_keys**
> list[PortainerAPIKey] user_get_api_keys(id)

Get all API keys for a user

Gets all API keys for a user. Only the calling user or admin can retrieve api-keys. **Access policy**: authenticated

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
api_instance = portainer.UsersApi(portainer.ApiClient(configuration))
id = 56 # int | User identifier

try:
    # Get all API keys for a user
    api_response = api_instance.user_get_api_keys(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_get_api_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User identifier | 

### Return type

[**list[PortainerAPIKey]**](PortainerAPIKey.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_inspect**
> PortainerUser user_inspect(id)

Inspect a user

Retrieve details about a user. User passwords are filtered out, and should never be accessible. **Access policy**: authenticated

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
api_instance = portainer.UsersApi(portainer.ApiClient(configuration))
id = 56 # int | User identifier

try:
    # Inspect a user
    api_response = api_instance.user_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User identifier | 

### Return type

[**PortainerUser**](PortainerUser.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_list**
> list[PortainerUser] user_list()

List users

List Portainer users. Non-administrator users will only be able to list other non-administrator user accounts. User passwords are filtered out, and should never be accessible. **Access policy**: restricted

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
api_instance = portainer.UsersApi(portainer.ApiClient(configuration))

try:
    # List users
    api_response = api_instance.user_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PortainerUser]**](PortainerUser.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_memberships_inspect**
> PortainerTeamMembership user_memberships_inspect(id)

Inspect a user memberships

Inspect a user memberships. **Access policy**: restricted

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
api_instance = portainer.UsersApi(portainer.ApiClient(configuration))
id = 56 # int | User identifier

try:
    # Inspect a user memberships
    api_response = api_instance.user_memberships_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_memberships_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User identifier | 

### Return type

[**PortainerTeamMembership**](PortainerTeamMembership.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_remove_api_key**
> user_remove_api_key(id, key_id)

Remove an api-key associated to a user

Remove an api-key associated to a user.. Only the calling user or admin can remove api-key. **Access policy**: authenticated

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
api_instance = portainer.UsersApi(portainer.ApiClient(configuration))
id = 56 # int | User identifier
key_id = 56 # int | Api Key identifier

try:
    # Remove an api-key associated to a user
    api_instance.user_remove_api_key(id, key_id)
except ApiException as e:
    print("Exception when calling UsersApi->user_remove_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User identifier | 
 **key_id** | **int**| Api Key identifier | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_update**
> PortainerUser user_update(id, body)

Update a user

Update user details. A regular user account can only update his details. **Access policy**: authenticated

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
api_instance = portainer.UsersApi(portainer.ApiClient(configuration))
id = 56 # int | User identifier
body = portainer.UsersUserUpdatePayload() # UsersUserUpdatePayload | User details

try:
    # Update a user
    api_response = api_instance.user_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User identifier | 
 **body** | [**UsersUserUpdatePayload**](UsersUserUpdatePayload.md)| User details | 

### Return type

[**PortainerUser**](PortainerUser.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_update_password**
> user_update_password(id, body)

Update password for a user

Update password for the specified user. **Access policy**: authenticated

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
api_instance = portainer.UsersApi(portainer.ApiClient(configuration))
id = 56 # int | identifier
body = portainer.UsersUserUpdatePasswordPayload() # UsersUserUpdatePasswordPayload | details

try:
    # Update password for a user
    api_instance.user_update_password(id, body)
except ApiException as e:
    print("Exception when calling UsersApi->user_update_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| identifier | 
 **body** | [**UsersUserUpdatePasswordPayload**](UsersUserUpdatePasswordPayload.md)| details | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

