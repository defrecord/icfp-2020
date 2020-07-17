init:
	brew install swagger-codegen

codegen:
	swagger-codegen generate -i schema/swagger.json -l python
