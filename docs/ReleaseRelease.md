# ReleaseRelease

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart** | [**ReleaseChart**](ReleaseChart.md) | Info provides information about a release Info *Info &#x60;json:\&quot;info,omitempty\&quot;&#x60; Chart is the chart that was released. | [optional] 
**config** | **object** | Config is the set of extra Values added to the chart. These values override the default values inside of the chart. | [optional] 
**hooks** | [**list[ReleaseHook]**](ReleaseHook.md) | Hooks are all of the hooks declared for this release. | [optional] 
**manifest** | **str** | Manifest is the string representation of the rendered template. | [optional] 
**name** | **str** | Name is the name of the release | [optional] 
**namespace** | **str** | Namespace is the kubernetes namespace of the release. | [optional] 
**version** | **int** | Version is an int which represents the revision of the release. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


