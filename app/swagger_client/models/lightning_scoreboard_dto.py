# coding: utf-8

"""
    ICFP Contest 2020 API

    See <a href='https://github.com/icfpcontest2020/aliens-proxy-protocol' target='_blank'>https://github.com/icfpcontest2020/aliens-proxy-protocol<a/>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class LightningScoreboardDto(object):
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
        'frozen_at': 'datetime',
        'problems': 'list[ProblemDescriptionDto]',
        'teams': 'list[TeamForProblemsScoreboardDto]'
    }

    attribute_map = {
        'frozen_at': 'frozenAt',
        'problems': 'problems',
        'teams': 'teams'
    }

    def __init__(self, frozen_at=None, problems=None, teams=None):  # noqa: E501
        """LightningScoreboardDto - a model defined in Swagger"""  # noqa: E501
        self._frozen_at = None
        self._problems = None
        self._teams = None
        self.discriminator = None
        if frozen_at is not None:
            self.frozen_at = frozen_at
        if problems is not None:
            self.problems = problems
        if teams is not None:
            self.teams = teams

    @property
    def frozen_at(self):
        """Gets the frozen_at of this LightningScoreboardDto.  # noqa: E501


        :return: The frozen_at of this LightningScoreboardDto.  # noqa: E501
        :rtype: datetime
        """
        return self._frozen_at

    @frozen_at.setter
    def frozen_at(self, frozen_at):
        """Sets the frozen_at of this LightningScoreboardDto.


        :param frozen_at: The frozen_at of this LightningScoreboardDto.  # noqa: E501
        :type: datetime
        """

        self._frozen_at = frozen_at

    @property
    def problems(self):
        """Gets the problems of this LightningScoreboardDto.  # noqa: E501


        :return: The problems of this LightningScoreboardDto.  # noqa: E501
        :rtype: list[ProblemDescriptionDto]
        """
        return self._problems

    @problems.setter
    def problems(self, problems):
        """Sets the problems of this LightningScoreboardDto.


        :param problems: The problems of this LightningScoreboardDto.  # noqa: E501
        :type: list[ProblemDescriptionDto]
        """

        self._problems = problems

    @property
    def teams(self):
        """Gets the teams of this LightningScoreboardDto.  # noqa: E501


        :return: The teams of this LightningScoreboardDto.  # noqa: E501
        :rtype: list[TeamForProblemsScoreboardDto]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this LightningScoreboardDto.


        :param teams: The teams of this LightningScoreboardDto.  # noqa: E501
        :type: list[TeamForProblemsScoreboardDto]
        """

        self._teams = teams

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
        if issubclass(LightningScoreboardDto, dict):
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
        if not isinstance(other, LightningScoreboardDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
