init:
	brew install swagger-codegen

codegen:
	swagger-codegen generate -i schema/swagger.json -l python

run:
	@sh run.sh $(API_URL) $(API_URL)
