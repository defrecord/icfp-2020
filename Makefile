init:
	brew install swagger-codegen

codegen:
	swagger-codegen generate -i schema/swagger.json -l python

run:
	@python app/main.py $(API_URL) $(API_KEY)

team:
	@python app/teams_current.py $(API_URL) $(API_KEY)
