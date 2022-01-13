# ResourcecontrolsResourceControlCreatePayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrators_only** | **bool** | Permit access to resource only to admins | [optional] 
**public** | **bool** | Permit access to the associated resource to any user | [optional] 
**resource_id** | **str** |  | 
**sub_resource_i_ds** | **list[str]** | List of Docker resources that will inherit this access control | [optional] 
**teams** | **list[int]** | List of team identifiers with access to the associated resource | [optional] 
**type** | **str** | Type of Docker resource. Valid values are: container, volume\\ service, secret, config or stack | 
**users** | **list[int]** | List of user identifiers with access to the associated resource | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


