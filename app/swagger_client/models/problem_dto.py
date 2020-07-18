# coding: utf-8

"""
    ICFP Contest 2020 API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ProblemDto(object):
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
        'score': 'int',
        'solved_at': 'datetime'
    }

    attribute_map = {
        'score': 'score',
        'solved_at': 'solvedAt'
    }

    def __init__(self, score=None, solved_at=None):  # noqa: E501
        """ProblemDto - a model defined in Swagger"""  # noqa: E501
        self._score = None
        self._solved_at = None
        self.discriminator = None
        if score is not None:
            self.score = score
        if solved_at is not None:
            self.solved_at = solved_at

    @property
    def score(self):
        """Gets the score of this ProblemDto.  # noqa: E501


        :return: The score of this ProblemDto.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this ProblemDto.


        :param score: The score of this ProblemDto.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def solved_at(self):
        """Gets the solved_at of this ProblemDto.  # noqa: E501


        :return: The solved_at of this ProblemDto.  # noqa: E501
        :rtype: datetime
        """
        return self._solved_at

    @solved_at.setter
    def solved_at(self, solved_at):
        """Sets the solved_at of this ProblemDto.


        :param solved_at: The solved_at of this ProblemDto.  # noqa: E501
        :type: datetime
        """

        self._solved_at = solved_at

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
        if issubclass(ProblemDto, dict):
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
        if not isinstance(other, ProblemDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other