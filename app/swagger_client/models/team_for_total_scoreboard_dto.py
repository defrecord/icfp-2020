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


class TeamForTotalScoreboardDto(object):
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
        'team': 'TeamDto',
        'score': 'int',
        'tournaments': 'dict(str, TeamTournamentDto)'
    }

    attribute_map = {
        'team': 'team',
        'score': 'score',
        'tournaments': 'tournaments'
    }

    def __init__(self, team=None, score=None, tournaments=None):  # noqa: E501
        """TeamForTotalScoreboardDto - a model defined in Swagger"""  # noqa: E501
        self._team = None
        self._score = None
        self._tournaments = None
        self.discriminator = None
        if team is not None:
            self.team = team
        if score is not None:
            self.score = score
        if tournaments is not None:
            self.tournaments = tournaments

    @property
    def team(self):
        """Gets the team of this TeamForTotalScoreboardDto.  # noqa: E501


        :return: The team of this TeamForTotalScoreboardDto.  # noqa: E501
        :rtype: TeamDto
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this TeamForTotalScoreboardDto.


        :param team: The team of this TeamForTotalScoreboardDto.  # noqa: E501
        :type: TeamDto
        """

        self._team = team

    @property
    def score(self):
        """Gets the score of this TeamForTotalScoreboardDto.  # noqa: E501


        :return: The score of this TeamForTotalScoreboardDto.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this TeamForTotalScoreboardDto.


        :param score: The score of this TeamForTotalScoreboardDto.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def tournaments(self):
        """Gets the tournaments of this TeamForTotalScoreboardDto.  # noqa: E501


        :return: The tournaments of this TeamForTotalScoreboardDto.  # noqa: E501
        :rtype: dict(str, TeamTournamentDto)
        """
        return self._tournaments

    @tournaments.setter
    def tournaments(self, tournaments):
        """Sets the tournaments of this TeamForTotalScoreboardDto.


        :param tournaments: The tournaments of this TeamForTotalScoreboardDto.  # noqa: E501
        :type: dict(str, TeamTournamentDto)
        """

        self._tournaments = tournaments

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
        if issubclass(TeamForTotalScoreboardDto, dict):
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
        if not isinstance(other, TeamForTotalScoreboardDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other