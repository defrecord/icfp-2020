# swagger-client
See <a href='https://github.com/icfpcontest2020/aliens-proxy-protocol' target='_blank'>https://github.com/icfpcontest2020/aliens-proxy-protocol<a/>

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ICFPC-ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AliensApiApi(swagger_client.ApiClient(configuration))
response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_instance.aliens_response_id_get(response_id)
except ApiException as e:
    print("Exception when calling AliensApiApi->aliens_response_id_get: %s\n" % e)

# Configure API key authorization: ICFPC-ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AliensApiApi(swagger_client.ApiClient(configuration))
body = 'body_example' # str |  (optional)

try:
    api_instance.aliens_send_post(body=body)
except ApiException as e:
    print("Exception when calling AliensApiApi->aliens_send_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AliensApiApi* | [**aliens_response_id_get**](docs/AliensApiApi.md#aliens_response_id_get) | **GET** /aliens/{responseId} | 
*AliensApiApi* | [**aliens_send_post**](docs/AliensApiApi.md#aliens_send_post) | **POST** /aliens/send | 
*GamesApiApi* | [**games_game_id_get**](docs/GamesApiApi.md#games_game_id_get) | **GET** /games/{gameId} | 
*GamesApiApi* | [**games_get**](docs/GamesApiApi.md#games_get) | **GET** /games | 
*GamesApiApi* | [**games_non_rating_get**](docs/GamesApiApi.md#games_non_rating_get) | **GET** /games/non-rating | 
*GamesApiApi* | [**games_non_rating_run_post**](docs/GamesApiApi.md#games_non_rating_run_post) | **POST** /games/non-rating/run | 
*LogsApiApi* | [**logs_get**](docs/LogsApiApi.md#logs_get) | **GET** /logs | 
*ScoreboardApiApi* | [**scoreboard_get**](docs/ScoreboardApiApi.md#scoreboard_get) | **GET** /scoreboard | 
*ScoreboardApiApi* | [**scoreboard_lightning_get**](docs/ScoreboardApiApi.md#scoreboard_lightning_get) | **GET** /scoreboard/lightning | 
*ScoreboardApiApi* | [**scoreboard_tournament_id_get**](docs/ScoreboardApiApi.md#scoreboard_tournament_id_get) | **GET** /scoreboard/{tournamentId} | 
*SubmissionsApiApi* | [**submissions_get**](docs/SubmissionsApiApi.md#submissions_get) | **GET** /submissions | 
*SubmissionsApiApi* | [**submissions_other_teams_get**](docs/SubmissionsApiApi.md#submissions_other_teams_get) | **GET** /submissions/other-teams | 
*SubmissionsApiApi* | [**submissions_submission_id_activate_post**](docs/SubmissionsApiApi.md#submissions_submission_id_activate_post) | **POST** /submissions/{submissionId}/activate | 
*SubmissionsApiApi* | [**submissions_submission_id_get**](docs/SubmissionsApiApi.md#submissions_submission_id_get) | **GET** /submissions/{submissionId} | 
*TeamsApiApi* | [**teams_current_get**](docs/TeamsApiApi.md#teams_current_get) | **GET** /teams/current | 
*TeamsApiApi* | [**teams_current_problems_get**](docs/TeamsApiApi.md#teams_current_problems_get) | **GET** /teams/current/problems | 
*TournamentsApiApi* | [**tournaments_current_get**](docs/TournamentsApiApi.md#tournaments_current_get) | **GET** /tournaments/current | 
*TournamentsApiApi* | [**tournaments_get**](docs/TournamentsApiApi.md#tournaments_get) | **GET** /tournaments | 
*TournamentsApiApi* | [**tournaments_tournament_id_get**](docs/TournamentsApiApi.md#tournaments_tournament_id_get) | **GET** /tournaments/{tournamentId} | 

## Documentation For Models

 - [BuildSystemRegistrationInfoDto](docs/BuildSystemRegistrationInfoDto.md)
 - [BuildSystemRegistrationStatus](docs/BuildSystemRegistrationStatus.md)
 - [GameDto](docs/GameDto.md)
 - [GameWinner](docs/GameWinner.md)
 - [GamesListDto](docs/GamesListDto.md)
 - [LightningScoreboardDto](docs/LightningScoreboardDto.md)
 - [PlayerDto](docs/PlayerDto.md)
 - [ProblemDescriptionDto](docs/ProblemDescriptionDto.md)
 - [ProblemDto](docs/ProblemDto.md)
 - [RatingDto](docs/RatingDto.md)
 - [RegisteredTeamDto](docs/RegisteredTeamDto.md)
 - [SubmissionDto](docs/SubmissionDto.md)
 - [SubmissionForTournamentScoreboardDto](docs/SubmissionForTournamentScoreboardDto.md)
 - [SubmissionStatus](docs/SubmissionStatus.md)
 - [TeamDto](docs/TeamDto.md)
 - [TeamForProblemsScoreboardDto](docs/TeamForProblemsScoreboardDto.md)
 - [TeamForTotalScoreboardDto](docs/TeamForTotalScoreboardDto.md)
 - [TeamForTournamentScoreboardDto](docs/TeamForTournamentScoreboardDto.md)
 - [TeamSubmissionDto](docs/TeamSubmissionDto.md)
 - [TeamTournamentDto](docs/TeamTournamentDto.md)
 - [TotalScoreboardDto](docs/TotalScoreboardDto.md)
 - [TournamentDto](docs/TournamentDto.md)
 - [TournamentDtoType](docs/TournamentDtoType.md)
 - [TournamentScoreboardDto](docs/TournamentScoreboardDto.md)

## Documentation For Authorization


## ICFPC-ApiKey

- **Type**: API key
- **API key parameter name**: apiKey
- **Location**: URL query string


## Author


