# ReleaseDependency

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Alias usable alias to be used for the chart | [optional] 
**condition** | **str** | A yaml path that resolves to a boolean, used for enabling/disabling charts (e.g. subchart1.enabled ) | [optional] 
**enabled** | **bool** | Enabled bool determines if chart should be loaded | [optional] 
**import_values** | **list[object]** | ImportValues holds the mapping of source values to parent key to be imported. Each item can be a string or pair of child/parent sublist items. | [optional] 
**name** | **str** | Name is the name of the dependency.  This must mach the name in the dependency&#39;s Chart.yaml. | [optional] 
**repository** | **str** | The URL to the repository.  Appending &#x60;index.yaml&#x60; to this string should result in a URL that can be used to fetch the repository index. | [optional] 
**tags** | **list[str]** | Tags can be used to group charts for enabling/disabling together | [optional] 
**version** | **str** | Version is the version (range) of this chart.  A lock file will always produce a single version, while a dependency may contain a semantic version range. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


