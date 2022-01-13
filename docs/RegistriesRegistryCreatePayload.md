# RegistriesRegistryCreatePayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **bool** | Is authentication against this registry enabled | 
**base_url** | **str** | BaseURL required for ProGet registry | [optional] 
**ecr** | [**PortainerEcrData**](PortainerEcrData.md) | ECR specific details, required when type &#x3D; 7 | [optional] 
**gitlab** | [**PortainerGitlabRegistryData**](PortainerGitlabRegistryData.md) | Gitlab specific details, required when type &#x3D; 4 | [optional] 
**name** | **str** | Name that will be used to identify this registry | 
**password** | **str** | Password used to authenticate against this registry. required when Authentication is true | [optional] 
**quay** | [**PortainerQuayRegistryData**](PortainerQuayRegistryData.md) | Quay specific details, required when type &#x3D; 1 | [optional] 
**type** | **int** | Registry Type. Valid values are:  1 (Quay.io),  2 (Azure container registry),  3 (custom registry),  4 (Gitlab registry),  5 (ProGet registry),  6 (DockerHub)  7 (ECR) | 
**url** | **str** | URL or IP address of the Docker registry | 
**username** | **str** | Username used to authenticate against this registry. Required when Authentication is true | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


