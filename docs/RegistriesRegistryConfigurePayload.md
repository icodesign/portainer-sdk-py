# RegistriesRegistryConfigurePayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **bool** | Is authentication against this registry enabled | 
**password** | **str** | Password used to authenticate against this registry. required when Authentication is true | [optional] 
**region** | **str** | ECR region | [optional] 
**tls** | **bool** | Use TLS | [optional] 
**tlscacert_file** | **list[int]** | The TLS CA certificate file | [optional] 
**tlscert_file** | **list[int]** | The TLS client certificate file | [optional] 
**tlskey_file** | **list[int]** | The TLS client key file | [optional] 
**tlsskip_verify** | **bool** | Skip the verification of the server TLS certificate | [optional] 
**username** | **str** | Username used to authenticate against this registry. Required when Authentication is true | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


