# SettingsSettingsUpdatePayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_method** | **int** | Active authentication method for the Portainer instance. Valid values are: 1 for internal, 2 for LDAP, or 3 for oauth | [optional] 
**black_listed_labels** | [**list[PortainerPair]**](PortainerPair.md) | A list of label name &amp; value that will be used to hide containers when querying containers | [optional] 
**edge_agent_checkin_interval** | **int** | The default check in interval for edge agent (in seconds) | [optional] 
**enable_edge_compute_features** | **bool** | Whether edge compute features are enabled | [optional] 
**enable_telemetry** | **bool** | Whether telemetry is enabled | [optional] 
**helm_repository_url** | **str** | Helm repository URL | [optional] 
**kubeconfig_expiry** | **str** | The expiry of a Kubeconfig | [optional] [default to '0']
**kubectl_shell_image** | **str** | Kubectl Shell Image | [optional] 
**ldapsettings** | [**PortainerLDAPSettings**](PortainerLDAPSettings.md) |  | [optional] 
**logo_url** | **str** | URL to a logo that will be displayed on the login page as well as on top of the sidebar. Will use default Portainer logo when value is empty string | [optional] 
**oauth_settings** | [**PortainerOAuthSettings**](PortainerOAuthSettings.md) |  | [optional] 
**snapshot_interval** | **str** | The interval in which environment(endpoint) snapshots are created | [optional] 
**templates_url** | **str** | URL to the templates that will be displayed in the UI when navigating to App Templates | [optional] 
**user_session_timeout** | **str** | The duration of a user session | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


