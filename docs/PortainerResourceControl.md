# PortainerResourceControl

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | **int** |  | [optional] 
**administrators_only** | **bool** | Permit access to resource only to admins | [optional] 
**id** | **int** | ResourceControl Identifier | [optional] 
**owner_id** | **int** | Deprecated fields Deprecated in DBVersion &#x3D;&#x3D; 2 | [optional] 
**public** | **bool** | Permit access to the associated resource to any user | [optional] 
**resource_id** | **str** | Docker resource identifier on which access control will be applied.\\ In the case of a resource control applied to a stack, use the stack name as identifier | [optional] 
**sub_resource_ids** | **list[str]** | List of Docker resources that will inherit this access control | [optional] 
**system** | **bool** |  | [optional] 
**team_accesses** | [**list[PortainerTeamResourceAccess]**](PortainerTeamResourceAccess.md) |  | [optional] 
**type** | **int** | Type of Docker resource. Valid values are: 1- container, 2 -service 3 - volume, 4 - secret, 5 - stack, 6 - config or 7 - custom template | [optional] 
**user_accesses** | [**list[PortainerUserResourceAccess]**](PortainerUserResourceAccess.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


