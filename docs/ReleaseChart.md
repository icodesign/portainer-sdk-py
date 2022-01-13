# ReleaseChart

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**list[ReleaseFile]**](ReleaseFile.md) | Files are miscellaneous files in a chart archive, e.g. README, LICENSE, etc. | [optional] 
**lock** | [**ReleaseLock**](ReleaseLock.md) | Lock is the contents of Chart.lock. | [optional] 
**metadata** | [**ReleaseMetadata**](ReleaseMetadata.md) | Metadata is the contents of the Chartfile. | [optional] 
**schema** | **list[int]** | Schema is an optional JSON schema for imposing structure on Values | [optional] 
**templates** | [**list[ReleaseFile]**](ReleaseFile.md) | Templates for this chart. | [optional] 
**values** | **object** | Values are default config for this chart. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


