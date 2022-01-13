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


class RegistriesRegistryCreatePayload(object):
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
        'authentication': 'bool',
        'base_url': 'str',
        'ecr': 'PortainerEcrData',
        'gitlab': 'PortainerGitlabRegistryData',
        'name': 'str',
        'password': 'str',
        'quay': 'PortainerQuayRegistryData',
        'type': 'int',
        'url': 'str',
        'username': 'str'
    }

    attribute_map = {
        'authentication': 'authentication',
        'base_url': 'baseURL',
        'ecr': 'ecr',
        'gitlab': 'gitlab',
        'name': 'name',
        'password': 'password',
        'quay': 'quay',
        'type': 'type',
        'url': 'url',
        'username': 'username'
    }

    def __init__(self, authentication=None, base_url=None, ecr=None, gitlab=None, name=None, password=None, quay=None, type=None, url=None, username=None, _configuration=None):  # noqa: E501
        """RegistriesRegistryCreatePayload - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._authentication = None
        self._base_url = None
        self._ecr = None
        self._gitlab = None
        self._name = None
        self._password = None
        self._quay = None
        self._type = None
        self._url = None
        self._username = None
        self.discriminator = None

        self.authentication = authentication
        if base_url is not None:
            self.base_url = base_url
        if ecr is not None:
            self.ecr = ecr
        if gitlab is not None:
            self.gitlab = gitlab
        self.name = name
        if password is not None:
            self.password = password
        if quay is not None:
            self.quay = quay
        self.type = type
        self.url = url
        if username is not None:
            self.username = username

    @property
    def authentication(self):
        """Gets the authentication of this RegistriesRegistryCreatePayload.  # noqa: E501

        Is authentication against this registry enabled  # noqa: E501

        :return: The authentication of this RegistriesRegistryCreatePayload.  # noqa: E501
        :rtype: bool
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this RegistriesRegistryCreatePayload.

        Is authentication against this registry enabled  # noqa: E501

        :param authentication: The authentication of this RegistriesRegistryCreatePayload.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and authentication is None:
            raise ValueError("Invalid value for `authentication`, must not be `None`")  # noqa: E501

        self._authentication = authentication

    @property
    def base_url(self):
        """Gets the base_url of this RegistriesRegistryCreatePayload.  # noqa: E501

        BaseURL required for ProGet registry  # noqa: E501

        :return: The base_url of this RegistriesRegistryCreatePayload.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this RegistriesRegistryCreatePayload.

        BaseURL required for ProGet registry  # noqa: E501

        :param base_url: The base_url of this RegistriesRegistryCreatePayload.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def ecr(self):
        """Gets the ecr of this RegistriesRegistryCreatePayload.  # noqa: E501

        ECR specific details, required when type = 7  # noqa: E501

        :return: The ecr of this RegistriesRegistryCreatePayload.  # noqa: E501
        :rtype: PortainerEcrData
        """
        return self._ecr

    @ecr.setter
    def ecr(self, ecr):
        """Sets the ecr of this RegistriesRegistryCreatePayload.

        ECR specific details, required when type = 7  # noqa: E501

        :param ecr: The ecr of this RegistriesRegistryCreatePayload.  # noqa: E501
        :type: PortainerEcrData
        """

        self._ecr = ecr

    @property
    def gitlab(self):
        """Gets the gitlab of this RegistriesRegistryCreatePayload.  # noqa: E501

        Gitlab specific details, required when type = 4  # noqa: E501

        :return: The gitlab of this RegistriesRegistryCreatePayload.  # noqa: E501
        :rtype: PortainerGitlabRegistryData
        """
        return self._gitlab

    @gitlab.setter
    def gitlab(self, gitlab):
        """Sets the gitlab of this RegistriesRegistryCreatePayload.

        Gitlab specific details, required when type = 4  # noqa: E501

        :param gitlab: The gitlab of this RegistriesRegistryCreatePayload.  # noqa: E501
        :type: PortainerGitlabRegistryData
        """

        self._gitlab = gitlab

    @property
    def name(self):
        """Gets the name of this RegistriesRegistryCreatePayload.  # noqa: E501

        Name that will be used to identify this registry  # noqa: E501

        :return: The name of this RegistriesRegistryCreatePayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RegistriesRegistryCreatePayload.

        Name that will be used to identify this registry  # noqa: E501

        :param name: The name of this RegistriesRegistryCreatePayload.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this RegistriesRegistryCreatePayload.  # noqa: E501

        Password used to authenticate against this registry. required when Authentication is true  # noqa: E501

        :return: The password of this RegistriesRegistryCreatePayload.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RegistriesRegistryCreatePayload.

        Password used to authenticate against this registry. required when Authentication is true  # noqa: E501

        :param password: The password of this RegistriesRegistryCreatePayload.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def quay(self):
        """Gets the quay of this RegistriesRegistryCreatePayload.  # noqa: E501

        Quay specific details, required when type = 1  # noqa: E501

        :return: The quay of this RegistriesRegistryCreatePayload.  # noqa: E501
        :rtype: PortainerQuayRegistryData
        """
        return self._quay

    @quay.setter
    def quay(self, quay):
        """Sets the quay of this RegistriesRegistryCreatePayload.

        Quay specific details, required when type = 1  # noqa: E501

        :param quay: The quay of this RegistriesRegistryCreatePayload.  # noqa: E501
        :type: PortainerQuayRegistryData
        """

        self._quay = quay

    @property
    def type(self):
        """Gets the type of this RegistriesRegistryCreatePayload.  # noqa: E501

        Registry Type. Valid values are:  1 (Quay.io),  2 (Azure container registry),  3 (custom registry),  4 (Gitlab registry),  5 (ProGet registry),  6 (DockerHub)  7 (ECR)  # noqa: E501

        :return: The type of this RegistriesRegistryCreatePayload.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RegistriesRegistryCreatePayload.

        Registry Type. Valid values are:  1 (Quay.io),  2 (Azure container registry),  3 (custom registry),  4 (Gitlab registry),  5 (ProGet registry),  6 (DockerHub)  7 (ECR)  # noqa: E501

        :param type: The type of this RegistriesRegistryCreatePayload.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def url(self):
        """Gets the url of this RegistriesRegistryCreatePayload.  # noqa: E501

        URL or IP address of the Docker registry  # noqa: E501

        :return: The url of this RegistriesRegistryCreatePayload.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RegistriesRegistryCreatePayload.

        URL or IP address of the Docker registry  # noqa: E501

        :param url: The url of this RegistriesRegistryCreatePayload.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def username(self):
        """Gets the username of this RegistriesRegistryCreatePayload.  # noqa: E501

        Username used to authenticate against this registry. Required when Authentication is true  # noqa: E501

        :return: The username of this RegistriesRegistryCreatePayload.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this RegistriesRegistryCreatePayload.

        Username used to authenticate against this registry. Required when Authentication is true  # noqa: E501

        :param username: The username of this RegistriesRegistryCreatePayload.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(RegistriesRegistryCreatePayload, dict):
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
        if not isinstance(other, RegistriesRegistryCreatePayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegistriesRegistryCreatePayload):
            return True

        return self.to_dict() != other.to_dict()