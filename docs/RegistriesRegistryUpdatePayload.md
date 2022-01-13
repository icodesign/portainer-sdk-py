# RegistriesRegistryUpdatePayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **bool** | Is authentication against this registry enabled | 
**base_url** | **str** | BaseURL is used for quay registry | [optional] 
**ecr** | [**PortainerEcrData**](PortainerEcrData.md) | ECR data | [optional] 
**name** | **str** | Name that will be used to identify this registry | 
**password** | **str** | Password used to authenticate against this registry. required when Authentication is true | [optional] 
**quay** | [**PortainerQuayRegistryData**](PortainerQuayRegistryData.md) | Quay data | [optional] 
**registry_accesses** | [**PortainerRegistryAccesses**](PortainerRegistryAccesses.md) | Registry access control | [optional] 
**url** | **str** | URL or IP address of the Docker registry | 
**username** | **str** | Username used to authenticate against this registry. Required when Authentication is true | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


