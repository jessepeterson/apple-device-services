all: generate-dep

generate-dep:
	tools/dev_docs_schema.py generate devicemanagement/device-assignment.json dep/schemas
	rm dep/schemas/MachineInfo.json dep/schemas/SkipKeys.json
	tools/dev_docs_schema.py generate devicemanagement/accountdetail.json dep/schemas
	tools/sortkeys.py dep/patches/*.json
	tools/apply_schema_patches.py dep/patches dep/schemas
	tools/sortkeys.py dep/schemas/*.json
	jsonschema fmt dep/schemas

fetch-dep:
	tools/dev_docs_schema.py fetch devicemanagement/device-assignment.json
	tools/dev_docs_schema.py fetch devicemanagement/accountdetail.json

.PHONY: all generate-dep fetch-dep
