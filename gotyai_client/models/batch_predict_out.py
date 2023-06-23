# coding: utf-8

"""
    Gotyai API v3

    Gotyai API : the Spartan explainable AI   # noqa: E501

    OpenAPI spec version: 3.0.2
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BatchPredictOut(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'rows': 'list[PredictOut]'
    }

    attribute_map = {
        'rows': 'rows'
    }

    def __init__(self, rows=None):  # noqa: E501
        """BatchPredictOut - a model defined in OpenAPI"""  # noqa: E501

        self._rows = None
        self.discriminator = None

        if rows is not None:
            self.rows = rows

    @property
    def rows(self):
        """Gets the rows of this BatchPredictOut.  # noqa: E501

        Classified genderized names  # noqa: E501

        :return: The rows of this BatchPredictOut.  # noqa: E501
        :rtype: list[PredictOut]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this BatchPredictOut.

        Classified genderized names  # noqa: E501

        :param rows: The rows of this BatchPredictOut.  # noqa: E501
        :type: list[PredictOut]
        """

        self._rows = rows

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchPredictOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
