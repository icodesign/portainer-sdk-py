# PortainerCustomTemplate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by_user_id** | **int** | User identifier who created this template | [optional] 
**description** | **str** | Description of the template | [optional] 
**entry_point** | **str** | Path to the Stack file | [optional] 
**id** | **int** | CustomTemplate Identifier | [optional] 
**logo** | **str** | URL of the template&#39;s logo | [optional] 
**note** | **str** | A note that will be displayed in the UI. Supports HTML content | [optional] 
**platform** | **int** | Platform associated to the template. Valid values are: 1 - &#39;linux&#39;, 2 - &#39;windows&#39; | [optional] 
**project_path** | **str** | Path on disk to the repository hosting the Stack file | [optional] 
**resource_control** | [**PortainerResourceControl**](PortainerResourceControl.md) |  | [optional] 
**title** | **str** | Title of the template | [optional] 
**type** | **int** | Type of created stack (1 - swarm, 2 - compose) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


