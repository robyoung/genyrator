
deps:
	pipenv install --dev

test: pep8 behave

behave:
	pipenv run behave test/e2e

pep8:
	pipenv run pycodestyle

.PHONY: deps test behave pep8
