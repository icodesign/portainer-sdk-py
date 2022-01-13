# ReleaseHook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_policies** | **list[str]** | DeletePolicies are the policies that indicate when to delete the hook | [optional] 
**events** | **list[str]** | Events are the events that this hook fires on. | [optional] 
**kind** | **str** | Kind is the Kubernetes kind. | [optional] 
**last_run** | [**ReleaseHookExecution**](ReleaseHookExecution.md) | LastRun indicates the date/time this was last run. | [optional] 
**manifest** | **str** | Manifest is the manifest contents. | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** | Path is the chart-relative path to the template. | [optional] 
**weight** | **int** | Weight indicates the sort order for execution among similar Hook type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


