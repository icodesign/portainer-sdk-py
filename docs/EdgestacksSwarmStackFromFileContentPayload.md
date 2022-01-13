# EdgestacksSwarmStackFromFileContentPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_type** | **int** | Deployment type to deploy this stack Valid values are: 0 - &#39;compose&#39;, 1 - &#39;kubernetes&#39; for compose stacks will use kompose to convert to kubernetes manifest for kubernetes environments(endpoints) kubernetes deploytype is enabled only for kubernetes environments(endpoints) | [optional] 
**edge_groups** | **list[int]** | List of identifiers of EdgeGroups | [optional] 
**name** | **str** | Name of the stack | 
**stack_file_content** | **str** | Content of the Stack file | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


