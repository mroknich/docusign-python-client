# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Jurisdiction(object):
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
        'allow_system_created_seal': 'str',
        'allow_user_uploaded_seal': 'str',
        'commission_id_in_seal': 'str',
        'county': 'str',
        'county_in_seal': 'str',
        'enabled': 'str',
        'jurisdiction_id': 'str',
        'name': 'str',
        'notary_public_in_seal': 'str',
        'state_name_in_seal': 'str'
    }

    attribute_map = {
        'allow_system_created_seal': 'allowSystemCreatedSeal',
        'allow_user_uploaded_seal': 'allowUserUploadedSeal',
        'commission_id_in_seal': 'commissionIdInSeal',
        'county': 'county',
        'county_in_seal': 'countyInSeal',
        'enabled': 'enabled',
        'jurisdiction_id': 'jurisdictionId',
        'name': 'name',
        'notary_public_in_seal': 'notaryPublicInSeal',
        'state_name_in_seal': 'stateNameInSeal'
    }

    def __init__(self, allow_system_created_seal=None, allow_user_uploaded_seal=None, commission_id_in_seal=None, county=None, county_in_seal=None, enabled=None, jurisdiction_id=None, name=None, notary_public_in_seal=None, state_name_in_seal=None):  # noqa: E501
        """Jurisdiction - a model defined in Swagger"""  # noqa: E501

        self._allow_system_created_seal = None
        self._allow_user_uploaded_seal = None
        self._commission_id_in_seal = None
        self._county = None
        self._county_in_seal = None
        self._enabled = None
        self._jurisdiction_id = None
        self._name = None
        self._notary_public_in_seal = None
        self._state_name_in_seal = None
        self.discriminator = None

        if allow_system_created_seal is not None:
            self.allow_system_created_seal = allow_system_created_seal
        if allow_user_uploaded_seal is not None:
            self.allow_user_uploaded_seal = allow_user_uploaded_seal
        if commission_id_in_seal is not None:
            self.commission_id_in_seal = commission_id_in_seal
        if county is not None:
            self.county = county
        if county_in_seal is not None:
            self.county_in_seal = county_in_seal
        if enabled is not None:
            self.enabled = enabled
        if jurisdiction_id is not None:
            self.jurisdiction_id = jurisdiction_id
        if name is not None:
            self.name = name
        if notary_public_in_seal is not None:
            self.notary_public_in_seal = notary_public_in_seal
        if state_name_in_seal is not None:
            self.state_name_in_seal = state_name_in_seal

    @property
    def allow_system_created_seal(self):
        """Gets the allow_system_created_seal of this Jurisdiction.  # noqa: E501

          # noqa: E501

        :return: The allow_system_created_seal of this Jurisdiction.  # noqa: E501
        :rtype: str
        """
        return self._allow_system_created_seal

    @allow_system_created_seal.setter
    def allow_system_created_seal(self, allow_system_created_seal):
        """Sets the allow_system_created_seal of this Jurisdiction.

          # noqa: E501

        :param allow_system_created_seal: The allow_system_created_seal of this Jurisdiction.  # noqa: E501
        :type: str
        """

        self._allow_system_created_seal = allow_system_created_seal

    @property
    def allow_user_uploaded_seal(self):
        """Gets the allow_user_uploaded_seal of this Jurisdiction.  # noqa: E501

          # noqa: E501

        :return: The allow_user_uploaded_seal of this Jurisdiction.  # noqa: E501
        :rtype: str
        """
        return self._allow_user_uploaded_seal

    @allow_user_uploaded_seal.setter
    def allow_user_uploaded_seal(self, allow_user_uploaded_seal):
        """Sets the allow_user_uploaded_seal of this Jurisdiction.

          # noqa: E501

        :param allow_user_uploaded_seal: The allow_user_uploaded_seal of this Jurisdiction.  # noqa: E501
        :type: str
        """

        self._allow_user_uploaded_seal = allow_user_uploaded_seal

    @property
    def commission_id_in_seal(self):
        """Gets the commission_id_in_seal of this Jurisdiction.  # noqa: E501

          # noqa: E501

        :return: The commission_id_in_seal of this Jurisdiction.  # noqa: E501
        :rtype: str
        """
        return self._commission_id_in_seal

    @commission_id_in_seal.setter
    def commission_id_in_seal(self, commission_id_in_seal):
        """Sets the commission_id_in_seal of this Jurisdiction.

          # noqa: E501

        :param commission_id_in_seal: The commission_id_in_seal of this Jurisdiction.  # noqa: E501
        :type: str
        """

        self._commission_id_in_seal = commission_id_in_seal

    @property
    def county(self):
        """Gets the county of this Jurisdiction.  # noqa: E501

          # noqa: E501

        :return: The county of this Jurisdiction.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this Jurisdiction.

          # noqa: E501

        :param county: The county of this Jurisdiction.  # noqa: E501
        :type: str
        """

        self._county = county

    @property
    def county_in_seal(self):
        """Gets the county_in_seal of this Jurisdiction.  # noqa: E501

          # noqa: E501

        :return: The county_in_seal of this Jurisdiction.  # noqa: E501
        :rtype: str
        """
        return self._county_in_seal

    @county_in_seal.setter
    def county_in_seal(self, county_in_seal):
        """Sets the county_in_seal of this Jurisdiction.

          # noqa: E501

        :param county_in_seal: The county_in_seal of this Jurisdiction.  # noqa: E501
        :type: str
        """

        self._county_in_seal = county_in_seal

    @property
    def enabled(self):
        """Gets the enabled of this Jurisdiction.  # noqa: E501

          # noqa: E501

        :return: The enabled of this Jurisdiction.  # noqa: E501
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Jurisdiction.

          # noqa: E501

        :param enabled: The enabled of this Jurisdiction.  # noqa: E501
        :type: str
        """

        self._enabled = enabled

    @property
    def jurisdiction_id(self):
        """Gets the jurisdiction_id of this Jurisdiction.  # noqa: E501

          # noqa: E501

        :return: The jurisdiction_id of this Jurisdiction.  # noqa: E501
        :rtype: str
        """
        return self._jurisdiction_id

    @jurisdiction_id.setter
    def jurisdiction_id(self, jurisdiction_id):
        """Sets the jurisdiction_id of this Jurisdiction.

          # noqa: E501

        :param jurisdiction_id: The jurisdiction_id of this Jurisdiction.  # noqa: E501
        :type: str
        """

        self._jurisdiction_id = jurisdiction_id

    @property
    def name(self):
        """Gets the name of this Jurisdiction.  # noqa: E501

          # noqa: E501

        :return: The name of this Jurisdiction.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Jurisdiction.

          # noqa: E501

        :param name: The name of this Jurisdiction.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notary_public_in_seal(self):
        """Gets the notary_public_in_seal of this Jurisdiction.  # noqa: E501

          # noqa: E501

        :return: The notary_public_in_seal of this Jurisdiction.  # noqa: E501
        :rtype: str
        """
        return self._notary_public_in_seal

    @notary_public_in_seal.setter
    def notary_public_in_seal(self, notary_public_in_seal):
        """Sets the notary_public_in_seal of this Jurisdiction.

          # noqa: E501

        :param notary_public_in_seal: The notary_public_in_seal of this Jurisdiction.  # noqa: E501
        :type: str
        """

        self._notary_public_in_seal = notary_public_in_seal

    @property
    def state_name_in_seal(self):
        """Gets the state_name_in_seal of this Jurisdiction.  # noqa: E501

          # noqa: E501

        :return: The state_name_in_seal of this Jurisdiction.  # noqa: E501
        :rtype: str
        """
        return self._state_name_in_seal

    @state_name_in_seal.setter
    def state_name_in_seal(self, state_name_in_seal):
        """Sets the state_name_in_seal of this Jurisdiction.

          # noqa: E501

        :param state_name_in_seal: The state_name_in_seal of this Jurisdiction.  # noqa: E501
        :type: str
        """

        self._state_name_in_seal = state_name_in_seal

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
        if issubclass(Jurisdiction, dict):
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
        if not isinstance(other, Jurisdiction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
