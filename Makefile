init:
	brew install swagger-codegen

codegen:
	swagger-codegen generate -i schema/swagger.json -l python

run:
	@python app/main.py $(API_URL) $(API_KEY)

team:
	@python app/teams_current.py $(API_URL) $(API_KEY)

submissions:
	@python app/submissions.py $(API_URL) $(API_KEY)

scoreboard_lightning:
	@python app/scoreboard_lightning.py $(API_URL) $(API_KEY)

aliens_response_id:
	@python app/aliens_response_id.py $(API_URL) $(API_KEY)

aliens_send:
	@python app/aliens_send.py $(API_URL) $(API_KEY)

logs:
	@python app/logs.py $(API_URL) $(API_KEY)
