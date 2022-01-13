# EndpointsEndpointStatusInspectResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkin** | **int** | The current value of CheckinInterval | [optional] 
**credentials** | **str** |  | [optional] 
**port** | **int** | The tunnel port | [optional] 
**schedules** | [**list[EndpointsEdgeJobResponse]**](EndpointsEdgeJobResponse.md) | List of requests for jobs to run on the environment(endpoint) | [optional] 
**stacks** | [**list[EndpointsStackStatusResponse]**](EndpointsStackStatusResponse.md) | List of stacks to be deployed on the environments(endpoints) | [optional] 
**status** | **str** | Status represents the environment(endpoint) status | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


