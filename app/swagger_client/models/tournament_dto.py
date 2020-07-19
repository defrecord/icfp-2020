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


class TournamentDto(object):
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
        'tournament_id': 'int',
        'tournament_type': 'TournamentDtoType',
        'accept_submissions': 'bool',
        'run_games': 'bool',
        'is_test': 'bool',
        'started_at': 'datetime',
        'finished_at': 'datetime',
        'frozen_at': 'datetime'
    }

    attribute_map = {
        'tournament_id': 'tournamentId',
        'tournament_type': 'tournamentType',
        'accept_submissions': 'acceptSubmissions',
        'run_games': 'runGames',
        'is_test': 'isTest',
        'started_at': 'startedAt',
        'finished_at': 'finishedAt',
        'frozen_at': 'frozenAt'
    }

    def __init__(self, tournament_id=None, tournament_type=None, accept_submissions=None, run_games=None, is_test=None, started_at=None, finished_at=None, frozen_at=None):  # noqa: E501
        """TournamentDto - a model defined in Swagger"""  # noqa: E501
        self._tournament_id = None
        self._tournament_type = None
        self._accept_submissions = None
        self._run_games = None
        self._is_test = None
        self._started_at = None
        self._finished_at = None
        self._frozen_at = None
        self.discriminator = None
        if tournament_id is not None:
            self.tournament_id = tournament_id
        if tournament_type is not None:
            self.tournament_type = tournament_type
        if accept_submissions is not None:
            self.accept_submissions = accept_submissions
        if run_games is not None:
            self.run_games = run_games
        if is_test is not None:
            self.is_test = is_test
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at
        if frozen_at is not None:
            self.frozen_at = frozen_at

    @property
    def tournament_id(self):
        """Gets the tournament_id of this TournamentDto.  # noqa: E501


        :return: The tournament_id of this TournamentDto.  # noqa: E501
        :rtype: int
        """
        return self._tournament_id

    @tournament_id.setter
    def tournament_id(self, tournament_id):
        """Sets the tournament_id of this TournamentDto.


        :param tournament_id: The tournament_id of this TournamentDto.  # noqa: E501
        :type: int
        """

        self._tournament_id = tournament_id

    @property
    def tournament_type(self):
        """Gets the tournament_type of this TournamentDto.  # noqa: E501


        :return: The tournament_type of this TournamentDto.  # noqa: E501
        :rtype: TournamentDtoType
        """
        return self._tournament_type

    @tournament_type.setter
    def tournament_type(self, tournament_type):
        """Sets the tournament_type of this TournamentDto.


        :param tournament_type: The tournament_type of this TournamentDto.  # noqa: E501
        :type: TournamentDtoType
        """

        self._tournament_type = tournament_type

    @property
    def accept_submissions(self):
        """Gets the accept_submissions of this TournamentDto.  # noqa: E501


        :return: The accept_submissions of this TournamentDto.  # noqa: E501
        :rtype: bool
        """
        return self._accept_submissions

    @accept_submissions.setter
    def accept_submissions(self, accept_submissions):
        """Sets the accept_submissions of this TournamentDto.


        :param accept_submissions: The accept_submissions of this TournamentDto.  # noqa: E501
        :type: bool
        """

        self._accept_submissions = accept_submissions

    @property
    def run_games(self):
        """Gets the run_games of this TournamentDto.  # noqa: E501


        :return: The run_games of this TournamentDto.  # noqa: E501
        :rtype: bool
        """
        return self._run_games

    @run_games.setter
    def run_games(self, run_games):
        """Sets the run_games of this TournamentDto.


        :param run_games: The run_games of this TournamentDto.  # noqa: E501
        :type: bool
        """

        self._run_games = run_games

    @property
    def is_test(self):
        """Gets the is_test of this TournamentDto.  # noqa: E501


        :return: The is_test of this TournamentDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_test

    @is_test.setter
    def is_test(self, is_test):
        """Sets the is_test of this TournamentDto.


        :param is_test: The is_test of this TournamentDto.  # noqa: E501
        :type: bool
        """

        self._is_test = is_test

    @property
    def started_at(self):
        """Gets the started_at of this TournamentDto.  # noqa: E501


        :return: The started_at of this TournamentDto.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this TournamentDto.


        :param started_at: The started_at of this TournamentDto.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def finished_at(self):
        """Gets the finished_at of this TournamentDto.  # noqa: E501


        :return: The finished_at of this TournamentDto.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this TournamentDto.


        :param finished_at: The finished_at of this TournamentDto.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def frozen_at(self):
        """Gets the frozen_at of this TournamentDto.  # noqa: E501


        :return: The frozen_at of this TournamentDto.  # noqa: E501
        :rtype: datetime
        """
        return self._frozen_at

    @frozen_at.setter
    def frozen_at(self, frozen_at):
        """Sets the frozen_at of this TournamentDto.


        :param frozen_at: The frozen_at of this TournamentDto.  # noqa: E501
        :type: datetime
        """

        self._frozen_at = frozen_at

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
        if issubclass(TournamentDto, dict):
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
        if not isinstance(other, TournamentDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other