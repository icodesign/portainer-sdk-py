# coding: utf-8

"""
    PortainerCE API

    Portainer API is an HTTP API served by Portainer. It is used by the Portainer UI and everything you can do with the UI can be done using the HTTP API. Examples are available at https://documentation.portainer.io/api/api-examples/ You can find out more about Portainer at [http://portainer.io](http://portainer.io) and get some support on [Slack](http://portainer.io/slack/).  # Authentication  Most of the API environments(endpoints) require to be authenticated as well as some level of authorization to be used. Portainer API uses JSON Web Token to manage authentication and thus requires you to provide a token in the **Authorization** header of each request with the **Bearer** authentication mechanism.  Example:  ``` Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInJvbGUiOjEsImV4cCI6MTQ5OTM3NjE1NH0.NJ6vE8FY1WG6jsRQzfMqeatJ4vh2TWAeeYfDhP71YEE ```  # Security  Each API environment(endpoint) has an associated access policy, it is documented in the description of each environment(endpoint).  Different access policies are available:  - Public access - Authenticated access - Restricted access - Administrator access  ### Public access  No authentication is required to access the environments(endpoints) with this access policy.  ### Authenticated access  Authentication is required to access the environments(endpoints) with this access policy.  ### Restricted access  Authentication is required to access the environments(endpoints) with this access policy. Extra-checks might be added to ensure access to the resource is granted. Returned data might also be filtered.  ### Administrator access  Authentication as well as an administrator role are required to access the environments(endpoints) with this access policy.  # Execute Docker requests  Portainer **DO NOT** expose specific environments(endpoints) to manage your Docker resources (create a container, remove a volume, etc...).  Instead, it acts as a reverse-proxy to the Docker HTTP API. This means that you can execute Docker requests **via** the Portainer HTTP API.  To do so, you can use the `/endpoints/{id}/docker` Portainer API environment(endpoint) (which is not documented below due to Swagger limitations). This environment(endpoint) has a restricted access policy so you still need to be authenticated to be able to query this environment(endpoint). Any query on this environment(endpoint) will be proxied to the Docker API of the associated environment(endpoint) (requests and responses objects are the same as documented in the Docker API).  **NOTE**: You can find more information on how to query the Docker API in the [Docker official documentation](https://docs.docker.com/engine/api/v1.30/) as well as in [this Portainer example](https://documentation.portainer.io/api/api-examples/).   # noqa: E501

    OpenAPI spec version: 2.11.0
    Contact: info@portainer.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from portainer.api_client import ApiClient


class HelmApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def helm_delete(self, id, release, namespace, **kwargs):  # noqa: E501
        """Delete Helm Release  # noqa: E501

        **Access policy**: authenticated  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_delete(id, release, namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Environment(Endpoint) identifier (required)
        :param str release: The name of the release/application to uninstall (required)
        :param str namespace: An optional namespace (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.helm_delete_with_http_info(id, release, namespace, **kwargs)  # noqa: E501
        else:
            (data) = self.helm_delete_with_http_info(id, release, namespace, **kwargs)  # noqa: E501
            return data

    def helm_delete_with_http_info(self, id, release, namespace, **kwargs):  # noqa: E501
        """Delete Helm Release  # noqa: E501

        **Access policy**: authenticated  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_delete_with_http_info(id, release, namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Environment(Endpoint) identifier (required)
        :param str release: The name of the release/application to uninstall (required)
        :param str namespace: An optional namespace (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'release', 'namespace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method helm_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `helm_delete`")  # noqa: E501
        # verify the required parameter 'release' is set
        if self.api_client.client_side_validation and ('release' not in params or
                                                       params['release'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `release` when calling `helm_delete`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in params or
                                                       params['namespace'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `namespace` when calling `helm_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'release' in params:
            path_params['release'] = params['release']  # noqa: E501

        query_params = []
        if 'namespace' in params:
            query_params.append(('namespace', params['namespace']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/endpoints/{id}/kubernetes/helm/{release}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def helm_install(self, id, payload, **kwargs):  # noqa: E501
        """Install Helm Chart  # noqa: E501

        **Access policy**: authenticated  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_install(id, payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Environment(Endpoint) identifier (required)
        :param HelmInstallChartPayload payload: Chart details (required)
        :return: ReleaseRelease
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.helm_install_with_http_info(id, payload, **kwargs)  # noqa: E501
        else:
            (data) = self.helm_install_with_http_info(id, payload, **kwargs)  # noqa: E501
            return data

    def helm_install_with_http_info(self, id, payload, **kwargs):  # noqa: E501
        """Install Helm Chart  # noqa: E501

        **Access policy**: authenticated  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_install_with_http_info(id, payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Environment(Endpoint) identifier (required)
        :param HelmInstallChartPayload payload: Chart details (required)
        :return: ReleaseRelease
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'payload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method helm_install" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `helm_install`")  # noqa: E501
        # verify the required parameter 'payload' is set
        if self.api_client.client_side_validation and ('payload' not in params or
                                                       params['payload'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `payload` when calling `helm_install`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payload' in params:
            body_params = params['payload']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/endpoints/{id}/kubernetes/helm', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReleaseRelease',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def helm_list(self, id, namespace, filter, selector, **kwargs):  # noqa: E501
        """List Helm Releases  # noqa: E501

        **Access policy**: authenticated  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_list(id, namespace, filter, selector, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Environment(Endpoint) identifier (required)
        :param str namespace: specify an optional namespace (required)
        :param str filter: specify an optional filter (required)
        :param str selector: specify an optional selector (required)
        :return: list[ReleaseReleaseElement]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.helm_list_with_http_info(id, namespace, filter, selector, **kwargs)  # noqa: E501
        else:
            (data) = self.helm_list_with_http_info(id, namespace, filter, selector, **kwargs)  # noqa: E501
            return data

    def helm_list_with_http_info(self, id, namespace, filter, selector, **kwargs):  # noqa: E501
        """List Helm Releases  # noqa: E501

        **Access policy**: authenticated  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_list_with_http_info(id, namespace, filter, selector, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Environment(Endpoint) identifier (required)
        :param str namespace: specify an optional namespace (required)
        :param str filter: specify an optional filter (required)
        :param str selector: specify an optional selector (required)
        :return: list[ReleaseReleaseElement]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'namespace', 'filter', 'selector']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method helm_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `helm_list`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in params or
                                                       params['namespace'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `namespace` when calling `helm_list`")  # noqa: E501
        # verify the required parameter 'filter' is set
        if self.api_client.client_side_validation and ('filter' not in params or
                                                       params['filter'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `filter` when calling `helm_list`")  # noqa: E501
        # verify the required parameter 'selector' is set
        if self.api_client.client_side_validation and ('selector' not in params or
                                                       params['selector'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `selector` when calling `helm_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'namespace' in params:
            query_params.append(('namespace', params['namespace']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'selector' in params:
            query_params.append(('selector', params['selector']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/endpoints/{id}/kubernetes/helm', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ReleaseReleaseElement]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def helm_repo_search(self, repo, **kwargs):  # noqa: E501
        """Search Helm Charts  # noqa: E501

        **Access policy**: authenticated  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_repo_search(repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Helm repository URL (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.helm_repo_search_with_http_info(repo, **kwargs)  # noqa: E501
        else:
            (data) = self.helm_repo_search_with_http_info(repo, **kwargs)  # noqa: E501
            return data

    def helm_repo_search_with_http_info(self, repo, **kwargs):  # noqa: E501
        """Search Helm Charts  # noqa: E501

        **Access policy**: authenticated  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_repo_search_with_http_info(repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Helm repository URL (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method helm_repo_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo' is set
        if self.api_client.client_side_validation and ('repo' not in params or
                                                       params['repo'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repo` when calling `helm_repo_search`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'repo' in params:
            query_params.append(('repo', params['repo']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/templates/helm', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def helm_show(self, repo, chart, command, **kwargs):  # noqa: E501
        """Show Helm Chart Information  # noqa: E501

        **Access policy**: authenticated  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_show(repo, chart, command, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Helm repository URL (required)
        :param str chart: Chart name (required)
        :param str command: chart/values/readme (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.helm_show_with_http_info(repo, chart, command, **kwargs)  # noqa: E501
        else:
            (data) = self.helm_show_with_http_info(repo, chart, command, **kwargs)  # noqa: E501
            return data

    def helm_show_with_http_info(self, repo, chart, command, **kwargs):  # noqa: E501
        """Show Helm Chart Information  # noqa: E501

        **Access policy**: authenticated  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_show_with_http_info(repo, chart, command, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Helm repository URL (required)
        :param str chart: Chart name (required)
        :param str command: chart/values/readme (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo', 'chart', 'command']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method helm_show" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo' is set
        if self.api_client.client_side_validation and ('repo' not in params or
                                                       params['repo'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `repo` when calling `helm_show`")  # noqa: E501
        # verify the required parameter 'chart' is set
        if self.api_client.client_side_validation and ('chart' not in params or
                                                       params['chart'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `chart` when calling `helm_show`")  # noqa: E501
        # verify the required parameter 'command' is set
        if self.api_client.client_side_validation and ('command' not in params or
                                                       params['command'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `command` when calling `helm_show`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'command' in params:
            path_params['command'] = params['command']  # noqa: E501

        query_params = []
        if 'repo' in params:
            query_params.append(('repo', params['repo']))  # noqa: E501
        if 'chart' in params:
            query_params.append(('chart', params['chart']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/templates/helm/{command}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def helm_user_repositories_list(self, id, **kwargs):  # noqa: E501
        """List a users helm repositories  # noqa: E501

        Inspect a user helm repositories. **Access policy**: authenticated  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_user_repositories_list(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: User identifier (required)
        :return: HelmHelmUserRepositoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.helm_user_repositories_list_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.helm_user_repositories_list_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def helm_user_repositories_list_with_http_info(self, id, **kwargs):  # noqa: E501
        """List a users helm repositories  # noqa: E501

        Inspect a user helm repositories. **Access policy**: authenticated  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_user_repositories_list_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: User identifier (required)
        :return: HelmHelmUserRepositoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method helm_user_repositories_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `helm_user_repositories_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/endpoints/{id}/kubernetes/helm/repositories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HelmHelmUserRepositoryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def helm_user_repository_create(self, id, payload, **kwargs):  # noqa: E501
        """Create a user helm repository  # noqa: E501

        Create a user helm repository. **Access policy**: authenticated  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_user_repository_create(id, payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Environment(Endpoint) identifier (required)
        :param HelmAddHelmRepoUrlPayload payload: Helm Repository (required)
        :return: PortainerHelmUserRepository
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.helm_user_repository_create_with_http_info(id, payload, **kwargs)  # noqa: E501
        else:
            (data) = self.helm_user_repository_create_with_http_info(id, payload, **kwargs)  # noqa: E501
            return data

    def helm_user_repository_create_with_http_info(self, id, payload, **kwargs):  # noqa: E501
        """Create a user helm repository  # noqa: E501

        Create a user helm repository. **Access policy**: authenticated  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.helm_user_repository_create_with_http_info(id, payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Environment(Endpoint) identifier (required)
        :param HelmAddHelmRepoUrlPayload payload: Helm Repository (required)
        :return: PortainerHelmUserRepository
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'payload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method helm_user_repository_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `helm_user_repository_create`")  # noqa: E501
        # verify the required parameter 'payload' is set
        if self.api_client.client_side_validation and ('payload' not in params or
                                                       params['payload'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `payload` when calling `helm_user_repository_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payload' in params:
            body_params = params['payload']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/endpoints/{id}/kubernetes/helm/repositories', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PortainerHelmUserRepository',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
