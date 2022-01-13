# PortainerEndpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorized_teams** | **list[int]** |  | [optional] 
**authorized_users** | **list[int]** | Deprecated in DBVersion &#x3D;&#x3D; 18 | [optional] 
**azure_credentials** | [**PortainerAzureCredentials**](PortainerAzureCredentials.md) |  | [optional] 
**compose_syntax_max_version** | **str** | Maximum version of docker-compose | [optional] 
**edge_checkin_interval** | **int** | The check in interval for edge agent (in seconds) | [optional] 
**edge_id** | **str** | The identifier of the edge agent associated with this environment(endpoint) | [optional] 
**edge_key** | **str** | The key which is used to map the agent to Portainer | [optional] 
**extensions** | [**list[PortainerEndpointExtension]**](PortainerEndpointExtension.md) |  | [optional] 
**group_id** | **int** | Environment(Endpoint) group identifier | [optional] 
**id** | **int** | Environment(Endpoint) Identifier | [optional] 
**kubernetes** | [**PortainerKubernetesData**](PortainerKubernetesData.md) | Associated Kubernetes data | [optional] 
**name** | **str** | Environment(Endpoint) name | [optional] 
**public_url** | **str** | URL or IP address where exposed containers will be reachable | [optional] 
**snapshots** | [**list[PortainerDockerSnapshot]**](PortainerDockerSnapshot.md) | List of snapshots | [optional] 
**status** | **int** | The status of the environment(endpoint) (1 - up, 2 - down) | [optional] 
**tls** | **bool** | Deprecated fields Deprecated in DBVersion &#x3D;&#x3D; 4 | [optional] 
**tlsca_cert** | **str** |  | [optional] 
**tls_cert** | **str** |  | [optional] 
**tls_config** | [**PortainerTLSConfiguration**](PortainerTLSConfiguration.md) |  | [optional] 
**tls_key** | **str** |  | [optional] 
**tag_ids** | **list[int]** | List of tag identifiers to which this environment(endpoint) is associated | [optional] 
**tags** | **list[str]** | Deprecated in DBVersion &#x3D;&#x3D; 22 | [optional] 
**team_access_policies** | [**PortainerTeamAccessPolicies**](PortainerTeamAccessPolicies.md) | List of team identifiers authorized to connect to this environment(endpoint) | [optional] 
**type** | **int** | Environment(Endpoint) environment(endpoint) type. 1 for a Docker environment(endpoint), 2 for an agent on Docker environment(endpoint) or 3 for an Azure environment(endpoint). | [optional] 
**url** | **str** | URL or IP address of the Docker host associated to this environment(endpoint) | [optional] 
**user_access_policies** | [**PortainerUserAccessPolicies**](PortainerUserAccessPolicies.md) | List of user identifiers authorized to connect to this environment(endpoint) | [optional] 
**last_check_in_date** | **int** | LastCheckInDate mark last check-in date on checkin | [optional] 
**security_settings** | [**PortainerEndpointSecuritySettings**](PortainerEndpointSecuritySettings.md) | Environment(Endpoint) specific security settings | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


