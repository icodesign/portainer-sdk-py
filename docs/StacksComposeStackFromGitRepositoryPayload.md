# StacksComposeStackFromGitRepositoryPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_files** | **list[str]** | Applicable when deploying with multiple stack files | [optional] 
**auto_update** | [**PortainerStackAutoUpdate**](PortainerStackAutoUpdate.md) | Optional auto update configuration | [optional] 
**compose_file** | **str** | Path to the Stack file inside the Git repository | [optional] [default to 'docker-compose.yml']
**env** | [**list[PortainerPair]**](PortainerPair.md) | A list of environment(endpoint) variables used during stack deployment | [optional] 
**name** | **str** | Name of the stack | 
**repository_authentication** | **bool** | Use basic authentication to clone the Git repository | [optional] 
**repository_password** | **str** | Password used in basic authentication. Required when RepositoryAuthentication is true. | [optional] 
**repository_reference_name** | **str** | Reference name of a Git repository hosting the Stack file | [optional] 
**repository_url** | **str** | URL of a Git repository hosting the Stack file | 
**repository_username** | **str** | Username used in basic authentication. Required when RepositoryAuthentication is true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


