# CustomtemplatesCustomTemplateFromGitRepositoryPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compose_file_path_in_repository** | **str** | Path to the Stack file inside the Git repository | [optional] [default to 'docker-compose.yml']
**description** | **str** | Description of the template | 
**logo** | **str** | URL of the template&#39;s logo | [optional] 
**note** | **str** | A note that will be displayed in the UI. Supports HTML content | [optional] 
**platform** | **int** | Platform associated to the template. Valid values are: 1 - &#39;linux&#39;, 2 - &#39;windows&#39; Required for Docker stacks | [optional] 
**repository_authentication** | **bool** | Use basic authentication to clone the Git repository | [optional] 
**repository_password** | **str** | Password used in basic authentication. Required when RepositoryAuthentication is true. | [optional] 
**repository_reference_name** | **str** | Reference name of a Git repository hosting the Stack file | [optional] 
**repository_url** | **str** | URL of a Git repository hosting the Stack file | 
**repository_username** | **str** | Username used in basic authentication. Required when RepositoryAuthentication is true. | [optional] 
**title** | **str** | Title of the template | 
**type** | **int** | Type of created stack (1 - swarm, 2 - compose) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


