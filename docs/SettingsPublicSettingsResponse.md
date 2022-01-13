# SettingsPublicSettingsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_method** | **int** | Active authentication method for the Portainer instance. Valid values are: 1 for internal, 2 for LDAP, or 3 for oauth | [optional] 
**enable_edge_compute_features** | **bool** | Whether edge compute features are enabled | [optional] 
**enable_telemetry** | **bool** | Whether telemetry is enabled | [optional] 
**features** | **dict(str, bool)** | Supported feature flags | [optional] 
**logo_url** | **str** | URL to a logo that will be displayed on the login page as well as on top of the sidebar. Will use default Portainer logo when value is empty string | [optional] 
**o_auth_login_uri** | **str** | The URL used for oauth login | [optional] 
**o_auth_logout_uri** | **str** | The URL used for oauth logout | [optional] 
**kubeconfig_expiry** | **str** | The expiry of a Kubeconfig | [optional] [default to '0']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


