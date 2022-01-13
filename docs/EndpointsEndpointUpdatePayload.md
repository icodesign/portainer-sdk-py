# EndpointsEndpointUpdatePayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_application_id** | **str** | Azure application ID | [optional] 
**azure_authentication_key** | **str** | Azure authentication key | [optional] 
**azure_tenant_id** | **str** | Azure tenant ID | [optional] 
**edge_checkin_interval** | **int** | The check in interval for edge agent (in seconds) | [optional] 
**group_id** | **int** | Group identifier | [optional] 
**kubernetes** | [**PortainerKubernetesData**](PortainerKubernetesData.md) | Associated Kubernetes data | [optional] 
**name** | **str** | Name that will be used to identify this environment(endpoint) | [optional] 
**public_url** | **str** | URL or IP address where exposed containers will be reachable.\\ Defaults to URL if not specified | [optional] 
**status** | **int** | The status of the environment(endpoint) (1 - up, 2 - down) | [optional] 
**tag_i_ds** | **list[int]** | List of tag identifiers to which this environment(endpoint) is associated | [optional] 
**team_access_policies** | [**PortainerTeamAccessPolicies**](PortainerTeamAccessPolicies.md) |  | [optional] 
**tls** | **bool** | Require TLS to connect against this environment(endpoint) | [optional] 
**tlsskip_client_verify** | **bool** | Skip client verification when using TLS | [optional] 
**tlsskip_verify** | **bool** | Skip server verification when using TLS | [optional] 
**url** | **str** | URL or IP address of a Docker host | [optional] 
**user_access_policies** | [**PortainerUserAccessPolicies**](PortainerUserAccessPolicies.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


