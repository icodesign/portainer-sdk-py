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


class ReleaseMetadata(object):
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
        'annotations': 'dict(str, str)',
        'api_version': 'str',
        'app_version': 'str',
        'condition': 'str',
        'dependencies': 'list[ReleaseDependency]',
        'deprecated': 'bool',
        'description': 'str',
        'home': 'str',
        'icon': 'str',
        'keywords': 'list[str]',
        'kube_version': 'str',
        'maintainers': 'list[ReleaseMaintainer]',
        'name': 'str',
        'sources': 'list[str]',
        'tags': 'str',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'api_version': 'apiVersion',
        'app_version': 'appVersion',
        'condition': 'condition',
        'dependencies': 'dependencies',
        'deprecated': 'deprecated',
        'description': 'description',
        'home': 'home',
        'icon': 'icon',
        'keywords': 'keywords',
        'kube_version': 'kubeVersion',
        'maintainers': 'maintainers',
        'name': 'name',
        'sources': 'sources',
        'tags': 'tags',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, annotations=None, api_version=None, app_version=None, condition=None, dependencies=None, deprecated=None, description=None, home=None, icon=None, keywords=None, kube_version=None, maintainers=None, name=None, sources=None, tags=None, type=None, version=None, _configuration=None):  # noqa: E501
        """ReleaseMetadata - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._annotations = None
        self._api_version = None
        self._app_version = None
        self._condition = None
        self._dependencies = None
        self._deprecated = None
        self._description = None
        self._home = None
        self._icon = None
        self._keywords = None
        self._kube_version = None
        self._maintainers = None
        self._name = None
        self._sources = None
        self._tags = None
        self._type = None
        self._version = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if api_version is not None:
            self.api_version = api_version
        if app_version is not None:
            self.app_version = app_version
        if condition is not None:
            self.condition = condition
        if dependencies is not None:
            self.dependencies = dependencies
        if deprecated is not None:
            self.deprecated = deprecated
        if description is not None:
            self.description = description
        if home is not None:
            self.home = home
        if icon is not None:
            self.icon = icon
        if keywords is not None:
            self.keywords = keywords
        if kube_version is not None:
            self.kube_version = kube_version
        if maintainers is not None:
            self.maintainers = maintainers
        if name is not None:
            self.name = name
        if sources is not None:
            self.sources = sources
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def annotations(self):
        """Gets the annotations of this ReleaseMetadata.  # noqa: E501

        Annotations are additional mappings uninterpreted by Helm, made available for inspection by other applications.  # noqa: E501

        :return: The annotations of this ReleaseMetadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this ReleaseMetadata.

        Annotations are additional mappings uninterpreted by Helm, made available for inspection by other applications.  # noqa: E501

        :param annotations: The annotations of this ReleaseMetadata.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def api_version(self):
        """Gets the api_version of this ReleaseMetadata.  # noqa: E501

        The API Version of this chart. Required.  # noqa: E501

        :return: The api_version of this ReleaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ReleaseMetadata.

        The API Version of this chart. Required.  # noqa: E501

        :param api_version: The api_version of this ReleaseMetadata.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def app_version(self):
        """Gets the app_version of this ReleaseMetadata.  # noqa: E501

        The version of the application enclosed inside of this chart.  # noqa: E501

        :return: The app_version of this ReleaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this ReleaseMetadata.

        The version of the application enclosed inside of this chart.  # noqa: E501

        :param app_version: The app_version of this ReleaseMetadata.  # noqa: E501
        :type: str
        """

        self._app_version = app_version

    @property
    def condition(self):
        """Gets the condition of this ReleaseMetadata.  # noqa: E501

        The condition to check to enable chart  # noqa: E501

        :return: The condition of this ReleaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this ReleaseMetadata.

        The condition to check to enable chart  # noqa: E501

        :param condition: The condition of this ReleaseMetadata.  # noqa: E501
        :type: str
        """

        self._condition = condition

    @property
    def dependencies(self):
        """Gets the dependencies of this ReleaseMetadata.  # noqa: E501

        Dependencies are a list of dependencies for a chart.  # noqa: E501

        :return: The dependencies of this ReleaseMetadata.  # noqa: E501
        :rtype: list[ReleaseDependency]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this ReleaseMetadata.

        Dependencies are a list of dependencies for a chart.  # noqa: E501

        :param dependencies: The dependencies of this ReleaseMetadata.  # noqa: E501
        :type: list[ReleaseDependency]
        """

        self._dependencies = dependencies

    @property
    def deprecated(self):
        """Gets the deprecated of this ReleaseMetadata.  # noqa: E501

        Whether or not this chart is deprecated  # noqa: E501

        :return: The deprecated of this ReleaseMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this ReleaseMetadata.

        Whether or not this chart is deprecated  # noqa: E501

        :param deprecated: The deprecated of this ReleaseMetadata.  # noqa: E501
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def description(self):
        """Gets the description of this ReleaseMetadata.  # noqa: E501

        A one-sentence description of the chart  # noqa: E501

        :return: The description of this ReleaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReleaseMetadata.

        A one-sentence description of the chart  # noqa: E501

        :param description: The description of this ReleaseMetadata.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def home(self):
        """Gets the home of this ReleaseMetadata.  # noqa: E501

        The URL to a relevant project page, git repo, or contact person  # noqa: E501

        :return: The home of this ReleaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._home

    @home.setter
    def home(self, home):
        """Sets the home of this ReleaseMetadata.

        The URL to a relevant project page, git repo, or contact person  # noqa: E501

        :param home: The home of this ReleaseMetadata.  # noqa: E501
        :type: str
        """

        self._home = home

    @property
    def icon(self):
        """Gets the icon of this ReleaseMetadata.  # noqa: E501

        The URL to an icon file.  # noqa: E501

        :return: The icon of this ReleaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this ReleaseMetadata.

        The URL to an icon file.  # noqa: E501

        :param icon: The icon of this ReleaseMetadata.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def keywords(self):
        """Gets the keywords of this ReleaseMetadata.  # noqa: E501

        A list of string keywords  # noqa: E501

        :return: The keywords of this ReleaseMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this ReleaseMetadata.

        A list of string keywords  # noqa: E501

        :param keywords: The keywords of this ReleaseMetadata.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def kube_version(self):
        """Gets the kube_version of this ReleaseMetadata.  # noqa: E501

        KubeVersion is a SemVer constraint specifying the version of Kubernetes required.  # noqa: E501

        :return: The kube_version of this ReleaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._kube_version

    @kube_version.setter
    def kube_version(self, kube_version):
        """Sets the kube_version of this ReleaseMetadata.

        KubeVersion is a SemVer constraint specifying the version of Kubernetes required.  # noqa: E501

        :param kube_version: The kube_version of this ReleaseMetadata.  # noqa: E501
        :type: str
        """

        self._kube_version = kube_version

    @property
    def maintainers(self):
        """Gets the maintainers of this ReleaseMetadata.  # noqa: E501

        A list of name and URL/email address combinations for the maintainer(s)  # noqa: E501

        :return: The maintainers of this ReleaseMetadata.  # noqa: E501
        :rtype: list[ReleaseMaintainer]
        """
        return self._maintainers

    @maintainers.setter
    def maintainers(self, maintainers):
        """Sets the maintainers of this ReleaseMetadata.

        A list of name and URL/email address combinations for the maintainer(s)  # noqa: E501

        :param maintainers: The maintainers of this ReleaseMetadata.  # noqa: E501
        :type: list[ReleaseMaintainer]
        """

        self._maintainers = maintainers

    @property
    def name(self):
        """Gets the name of this ReleaseMetadata.  # noqa: E501

        The name of the chart. Required.  # noqa: E501

        :return: The name of this ReleaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReleaseMetadata.

        The name of the chart. Required.  # noqa: E501

        :param name: The name of this ReleaseMetadata.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sources(self):
        """Gets the sources of this ReleaseMetadata.  # noqa: E501

        Source is the URL to the source code of this chart  # noqa: E501

        :return: The sources of this ReleaseMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this ReleaseMetadata.

        Source is the URL to the source code of this chart  # noqa: E501

        :param sources: The sources of this ReleaseMetadata.  # noqa: E501
        :type: list[str]
        """

        self._sources = sources

    @property
    def tags(self):
        """Gets the tags of this ReleaseMetadata.  # noqa: E501

        The tags to check to enable chart  # noqa: E501

        :return: The tags of this ReleaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ReleaseMetadata.

        The tags to check to enable chart  # noqa: E501

        :param tags: The tags of this ReleaseMetadata.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this ReleaseMetadata.  # noqa: E501

        Specifies the chart type: application or library  # noqa: E501

        :return: The type of this ReleaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ReleaseMetadata.

        Specifies the chart type: application or library  # noqa: E501

        :param type: The type of this ReleaseMetadata.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this ReleaseMetadata.  # noqa: E501

        A SemVer 2 conformant version string of the chart. Required.  # noqa: E501

        :return: The version of this ReleaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ReleaseMetadata.

        A SemVer 2 conformant version string of the chart. Required.  # noqa: E501

        :param version: The version of this ReleaseMetadata.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(ReleaseMetadata, dict):
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
        if not isinstance(other, ReleaseMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReleaseMetadata):
            return True

        return self.to_dict() != other.to_dict()
