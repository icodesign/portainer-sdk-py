# coding: utf-8

"""
    PortainerCE API

    Portainer API is an HTTP API served by Portainer. It is used by the Portainer UI and everything you can do with the UI can be done using the HTTP API. Examples are available at https://documentation.portainer.io/api/api-examples/ You can find out more about Portainer at [http://portainer.io](http://portainer.io) and get some support on [Slack](http://portainer.io/slack/).  # Authentication  Most of the API environments(endpoints) require to be authenticated as well as some level of authorization to be used. Portainer API uses JSON Web Token to manage authentication and thus requires you to provide a token in the **Authorization** header of each request with the **Bearer** authentication mechanism.  Example:  ``` Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInJvbGUiOjEsImV4cCI6MTQ5OTM3NjE1NH0.NJ6vE8FY1WG6jsRQzfMqeatJ4vh2TWAeeYfDhP71YEE ```  # Security  Each API environment(endpoint) has an associated access policy, it is documented in the description of each environment(endpoint).  Different access policies are available:  - Public access - Authenticated access - Restricted access - Administrator access  ### Public access  No authentication is required to access the environments(endpoints) with this access policy.  ### Authenticated access  Authentication is required to access the environments(endpoints) with this access policy.  ### Restricted access  Authentication is required to access the environments(endpoints) with this access policy. Extra-checks might be added to ensure access to the resource is granted. Returned data might also be filtered.  ### Administrator access  Authentication as well as an administrator role are required to access the environments(endpoints) with this access policy.  # Execute Docker requests  Portainer **DO NOT** expose specific environments(endpoints) to manage your Docker resources (create a container, remove a volume, etc...).  Instead, it acts as a reverse-proxy to the Docker HTTP API. This means that you can execute Docker requests **via** the Portainer HTTP API.  To do so, you can use the `/endpoints/{id}/docker` Portainer API environment(endpoint) (which is not documented below due to Swagger limitations). This environment(endpoint) has a restricted access policy so you still need to be authenticated to be able to query this environment(endpoint). Any query on this environment(endpoint) will be proxied to the Docker API of the associated environment(endpoint) (requests and responses objects are the same as documented in the Docker API).  **NOTE**: You can find more information on how to query the Docker API in the [Docker official documentation](https://docs.docker.com/engine/api/v1.30/) as well as in [this Portainer example](https://documentation.portainer.io/api/api-examples/).   # noqa: E501

    OpenAPI spec version: 2.11.0
    Contact: info@portainer.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from portainer.configuration import Configuration


class GittypesRepoConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'authentication': 'GittypesGitAuthentication',
        'config_file_path': 'str',
        'config_hash': 'str',
        'reference_name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'authentication': 'authentication',
        'config_file_path': 'configFilePath',
        'config_hash': 'configHash',
        'reference_name': 'referenceName',
        'url': 'url'
    }

    def __init__(self, authentication=None, config_file_path=None, config_hash=None, reference_name=None, url=None, _configuration=None):  # noqa: E501
        """GittypesRepoConfig - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._authentication = None
        self._config_file_path = None
        self._config_hash = None
        self._reference_name = None
        self._url = None
        self.discriminator = None

        if authentication is not None:
            self.authentication = authentication
        if config_file_path is not None:
            self.config_file_path = config_file_path
        if config_hash is not None:
            self.config_hash = config_hash
        if reference_name is not None:
            self.reference_name = reference_name
        if url is not None:
            self.url = url

    @property
    def authentication(self):
        """Gets the authentication of this GittypesRepoConfig.  # noqa: E501

        Git credentials  # noqa: E501

        :return: The authentication of this GittypesRepoConfig.  # noqa: E501
        :rtype: GittypesGitAuthentication
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this GittypesRepoConfig.

        Git credentials  # noqa: E501

        :param authentication: The authentication of this GittypesRepoConfig.  # noqa: E501
        :type: GittypesGitAuthentication
        """

        self._authentication = authentication

    @property
    def config_file_path(self):
        """Gets the config_file_path of this GittypesRepoConfig.  # noqa: E501

        Path to where the config file is in this url/refName  # noqa: E501

        :return: The config_file_path of this GittypesRepoConfig.  # noqa: E501
        :rtype: str
        """
        return self._config_file_path

    @config_file_path.setter
    def config_file_path(self, config_file_path):
        """Sets the config_file_path of this GittypesRepoConfig.

        Path to where the config file is in this url/refName  # noqa: E501

        :param config_file_path: The config_file_path of this GittypesRepoConfig.  # noqa: E501
        :type: str
        """

        self._config_file_path = config_file_path

    @property
    def config_hash(self):
        """Gets the config_hash of this GittypesRepoConfig.  # noqa: E501

        Repository hash  # noqa: E501

        :return: The config_hash of this GittypesRepoConfig.  # noqa: E501
        :rtype: str
        """
        return self._config_hash

    @config_hash.setter
    def config_hash(self, config_hash):
        """Sets the config_hash of this GittypesRepoConfig.

        Repository hash  # noqa: E501

        :param config_hash: The config_hash of this GittypesRepoConfig.  # noqa: E501
        :type: str
        """

        self._config_hash = config_hash

    @property
    def reference_name(self):
        """Gets the reference_name of this GittypesRepoConfig.  # noqa: E501

        The reference name  # noqa: E501

        :return: The reference_name of this GittypesRepoConfig.  # noqa: E501
        :rtype: str
        """
        return self._reference_name

    @reference_name.setter
    def reference_name(self, reference_name):
        """Sets the reference_name of this GittypesRepoConfig.

        The reference name  # noqa: E501

        :param reference_name: The reference_name of this GittypesRepoConfig.  # noqa: E501
        :type: str
        """

        self._reference_name = reference_name

    @property
    def url(self):
        """Gets the url of this GittypesRepoConfig.  # noqa: E501

        The repo url  # noqa: E501

        :return: The url of this GittypesRepoConfig.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GittypesRepoConfig.

        The repo url  # noqa: E501

        :param url: The url of this GittypesRepoConfig.  # noqa: E501
        :type: str
        """

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GittypesRepoConfig, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GittypesRepoConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GittypesRepoConfig):
            return True

        return self.to_dict() != other.to_dict()
