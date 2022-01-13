# portainer.TeamMembershipsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**team_membership_create**](TeamMembershipsApi.md#team_membership_create) | **POST** /team_memberships | Create a new team membership
[**team_membership_delete**](TeamMembershipsApi.md#team_membership_delete) | **DELETE** /team_memberships/{id} | Remove a team membership
[**team_membership_list**](TeamMembershipsApi.md#team_membership_list) | **GET** /team_memberships | List team memberships
[**team_membership_update**](TeamMembershipsApi.md#team_membership_update) | **PUT** /team_memberships/{id} | Update a team membership
[**team_memberships**](TeamMembershipsApi.md#team_memberships) | **GET** /teams/{id}/memberships | List team memberships


# **team_membership_create**
> PortainerTeamMembership team_membership_create(body)

Create a new team membership

Create a new team memberships. Access is only available to administrators leaders of the associated team. **Access policy**: administrator

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
api_instance = portainer.TeamMembershipsApi(portainer.ApiClient(configuration))
body = portainer.TeammembershipsTeamMembershipCreatePayload() # TeammembershipsTeamMembershipCreatePayload | Team membership details

try:
    # Create a new team membership
    api_response = api_instance.team_membership_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMembershipsApi->team_membership_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TeammembershipsTeamMembershipCreatePayload**](TeammembershipsTeamMembershipCreatePayload.md)| Team membership details | 

### Return type

[**PortainerTeamMembership**](PortainerTeamMembership.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_membership_delete**
> team_membership_delete(id)

Remove a team membership

Remove a team membership. Access is only available to administrators leaders of the associated team. **Access policy**: administrator

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
api_instance = portainer.TeamMembershipsApi(portainer.ApiClient(configuration))
id = 56 # int | TeamMembership identifier

try:
    # Remove a team membership
    api_instance.team_membership_delete(id)
except ApiException as e:
    print("Exception when calling TeamMembershipsApi->team_membership_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| TeamMembership identifier | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_membership_list**
> list[PortainerTeamMembership] team_membership_list()

List team memberships

List team memberships. Access is only available to administrators and team leaders. **Access policy**: administrator

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
api_instance = portainer.TeamMembershipsApi(portainer.ApiClient(configuration))

try:
    # List team memberships
    api_response = api_instance.team_membership_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMembershipsApi->team_membership_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PortainerTeamMembership]**](PortainerTeamMembership.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_membership_update**
> PortainerTeamMembership team_membership_update(id, body)

Update a team membership

Update a team membership. Access is only available to administrators leaders of the associated team. **Access policy**: administrator

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
api_instance = portainer.TeamMembershipsApi(portainer.ApiClient(configuration))
id = 56 # int | Team membership identifier
body = portainer.TeammembershipsTeamMembershipUpdatePayload() # TeammembershipsTeamMembershipUpdatePayload | Team membership details

try:
    # Update a team membership
    api_response = api_instance.team_membership_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMembershipsApi->team_membership_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Team membership identifier | 
 **body** | [**TeammembershipsTeamMembershipUpdatePayload**](TeammembershipsTeamMembershipUpdatePayload.md)| Team membership details | 

### Return type

[**PortainerTeamMembership**](PortainerTeamMembership.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_memberships**
> list[PortainerTeamMembership] team_memberships(id)

List team memberships

List team memberships. Access is only available to administrators and team leaders. **Access policy**: restricted

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
api_instance = portainer.TeamMembershipsApi(portainer.ApiClient(configuration))
id = 'id_example' # str | Team Id

try:
    # List team memberships
    api_response = api_instance.team_memberships(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMembershipsApi->team_memberships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team Id | 

### Return type

[**list[PortainerTeamMembership]**](PortainerTeamMembership.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

