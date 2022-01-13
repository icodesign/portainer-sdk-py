# PortainerSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_bind_mounts_for_regular_users** | **bool** |  | [optional] 
**allow_container_capabilities_for_regular_users** | **bool** |  | [optional] 
**allow_device_mapping_for_regular_users** | **bool** |  | [optional] 
**allow_host_namespace_for_regular_users** | **bool** |  | [optional] 
**allow_privileged_mode_for_regular_users** | **bool** |  | [optional] 
**allow_stack_management_for_regular_users** | **bool** |  | [optional] 
**allow_volume_browser_for_regular_users** | **bool** |  | [optional] 
**authentication_method** | **int** | Active authentication method for the Portainer instance. Valid values are: 1 for internal, 2 for LDAP, or 3 for oauth | [optional] 
**black_listed_labels** | [**list[PortainerPair]**](PortainerPair.md) | A list of label name &amp; value that will be used to hide containers when querying containers | [optional] 
**edge_agent_checkin_interval** | **int** | The default check in interval for edge agent (in seconds) | [optional] 
**enable_edge_compute_features** | **bool** | Whether edge compute features are enabled | [optional] 
**enable_host_management_features** | **bool** | Deprecated fields v26 | [optional] 
**enable_telemetry** | **bool** | Whether telemetry is enabled | [optional] 
**feature_flag_settings** | **dict(str, bool)** |  | [optional] 
**helm_repository_url** | **str** | Helm repository URL, defaults to \&quot;https://charts.bitnami.com/bitnami\&quot; | [optional] 
**kubeconfig_expiry** | **str** | The expiry of a Kubeconfig | [optional] 
**kubectl_shell_image** | **str** | KubectlImage, defaults to portainer/kubectl-shell | [optional] 
**ldap_settings** | [**PortainerLDAPSettings**](PortainerLDAPSettings.md) |  | [optional] 
**logo_url** | **str** | URL to a logo that will be displayed on the login page as well as on top of the sidebar. Will use default Portainer logo when value is empty string | [optional] 
**o_auth_settings** | [**PortainerOAuthSettings**](PortainerOAuthSettings.md) |  | [optional] 
**snapshot_interval** | **str** | The interval in which environment(endpoint) snapshots are created | [optional] 
**templates_url** | **str** | URL to the templates that will be displayed in the UI when navigating to App Templates | [optional] 
**user_session_timeout** | **str** | The duration of a user session | [optional] 
**display_donation_header** | **bool** | Deprecated fields | [optional] 
**display_external_contributors** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


