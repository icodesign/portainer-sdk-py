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


class StacksStackGitUpdatePayload(object):
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
        'auto_update': 'PortainerStackAutoUpdate',
        'env': 'list[PortainerPair]',
        'repository_authentication': 'bool',
        'repository_password': 'str',
        'repository_reference_name': 'str',
        'repository_username': 'str'
    }

    attribute_map = {
        'auto_update': 'autoUpdate',
        'env': 'env',
        'repository_authentication': 'repositoryAuthentication',
        'repository_password': 'repositoryPassword',
        'repository_reference_name': 'repositoryReferenceName',
        'repository_username': 'repositoryUsername'
    }

    def __init__(self, auto_update=None, env=None, repository_authentication=None, repository_password=None, repository_reference_name=None, repository_username=None, _configuration=None):  # noqa: E501
        """StacksStackGitUpdatePayload - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_update = None
        self._env = None
        self._repository_authentication = None
        self._repository_password = None
        self._repository_reference_name = None
        self._repository_username = None
        self.discriminator = None

        if auto_update is not None:
            self.auto_update = auto_update
        if env is not None:
            self.env = env
        if repository_authentication is not None:
            self.repository_authentication = repository_authentication
        if repository_password is not None:
            self.repository_password = repository_password
        if repository_reference_name is not None:
            self.repository_reference_name = repository_reference_name
        if repository_username is not None:
            self.repository_username = repository_username

    @property
    def auto_update(self):
        """Gets the auto_update of this StacksStackGitUpdatePayload.  # noqa: E501


        :return: The auto_update of this StacksStackGitUpdatePayload.  # noqa: E501
        :rtype: PortainerStackAutoUpdate
        """
        return self._auto_update

    @auto_update.setter
    def auto_update(self, auto_update):
        """Sets the auto_update of this StacksStackGitUpdatePayload.


        :param auto_update: The auto_update of this StacksStackGitUpdatePayload.  # noqa: E501
        :type: PortainerStackAutoUpdate
        """

        self._auto_update = auto_update

    @property
    def env(self):
        """Gets the env of this StacksStackGitUpdatePayload.  # noqa: E501


        :return: The env of this StacksStackGitUpdatePayload.  # noqa: E501
        :rtype: list[PortainerPair]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this StacksStackGitUpdatePayload.


        :param env: The env of this StacksStackGitUpdatePayload.  # noqa: E501
        :type: list[PortainerPair]
        """

        self._env = env

    @property
    def repository_authentication(self):
        """Gets the repository_authentication of this StacksStackGitUpdatePayload.  # noqa: E501


        :return: The repository_authentication of this StacksStackGitUpdatePayload.  # noqa: E501
        :rtype: bool
        """
        return self._repository_authentication

    @repository_authentication.setter
    def repository_authentication(self, repository_authentication):
        """Sets the repository_authentication of this StacksStackGitUpdatePayload.


        :param repository_authentication: The repository_authentication of this StacksStackGitUpdatePayload.  # noqa: E501
        :type: bool
        """

        self._repository_authentication = repository_authentication

    @property
    def repository_password(self):
        """Gets the repository_password of this StacksStackGitUpdatePayload.  # noqa: E501


        :return: The repository_password of this StacksStackGitUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._repository_password

    @repository_password.setter
    def repository_password(self, repository_password):
        """Sets the repository_password of this StacksStackGitUpdatePayload.


        :param repository_password: The repository_password of this StacksStackGitUpdatePayload.  # noqa: E501
        :type: str
        """

        self._repository_password = repository_password

    @property
    def repository_reference_name(self):
        """Gets the repository_reference_name of this StacksStackGitUpdatePayload.  # noqa: E501


        :return: The repository_reference_name of this StacksStackGitUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._repository_reference_name

    @repository_reference_name.setter
    def repository_reference_name(self, repository_reference_name):
        """Sets the repository_reference_name of this StacksStackGitUpdatePayload.


        :param repository_reference_name: The repository_reference_name of this StacksStackGitUpdatePayload.  # noqa: E501
        :type: str
        """

        self._repository_reference_name = repository_reference_name

    @property
    def repository_username(self):
        """Gets the repository_username of this StacksStackGitUpdatePayload.  # noqa: E501


        :return: The repository_username of this StacksStackGitUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._repository_username

    @repository_username.setter
    def repository_username(self, repository_username):
        """Sets the repository_username of this StacksStackGitUpdatePayload.


        :param repository_username: The repository_username of this StacksStackGitUpdatePayload.  # noqa: E501
        :type: str
        """

        self._repository_username = repository_username

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
        if issubclass(StacksStackGitUpdatePayload, dict):
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
        if not isinstance(other, StacksStackGitUpdatePayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StacksStackGitUpdatePayload):
            return True

        return self.to_dict() != other.to_dict()
