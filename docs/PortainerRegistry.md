# PortainerRegistry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Stores temporary access token | [optional] 
**access_token_expiry** | **int** |  | [optional] 
**authentication** | **bool** | Is authentication against this registry enabled | [optional] 
**authorized_teams** | **list[int]** | Deprecated in DBVersion &#x3D;&#x3D; 18 | [optional] 
**authorized_users** | **list[int]** | Deprecated in DBVersion &#x3D;&#x3D; 18 | [optional] 
**base_url** | **str** | Base URL, introduced for ProGet registry | [optional] 
**ecr** | [**PortainerEcrData**](PortainerEcrData.md) |  | [optional] 
**gitlab** | [**PortainerGitlabRegistryData**](PortainerGitlabRegistryData.md) |  | [optional] 
**id** | **int** | Registry Identifier | [optional] 
**management_configuration** | [**PortainerRegistryManagementConfiguration**](PortainerRegistryManagementConfiguration.md) |  | [optional] 
**name** | **str** | Registry Name | [optional] 
**password** | **str** | Password or SecretAccessKey used to authenticate against this registry | [optional] 
**quay** | [**PortainerQuayRegistryData**](PortainerQuayRegistryData.md) |  | [optional] 
**registry_accesses** | [**PortainerRegistryAccesses**](PortainerRegistryAccesses.md) |  | [optional] 
**team_access_policies** | [**PortainerTeamAccessPolicies**](PortainerTeamAccessPolicies.md) | Deprecated in DBVersion &#x3D;&#x3D; 31 | [optional] 
**type** | **int** | Registry Type (1 - Quay, 2 - Azure, 3 - Custom, 4 - Gitlab, 5 - ProGet, 6 - DockerHub, 7 - ECR) | [optional] 
**url** | **str** | URL or IP address of the Docker registry | [optional] 
**user_access_policies** | [**PortainerUserAccessPolicies**](PortainerUserAccessPolicies.md) | Deprecated fields Deprecated in DBVersion &#x3D;&#x3D; 31 | [optional] 
**username** | **str** | Username or AccessKeyID used to authenticate against this registry | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


