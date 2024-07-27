echo "Running pylint on project"
poetry run pylint ./qsdata --rcfile ./pyproject.toml 
echo "Running mypy on project"
poetry run mypy . --config-file ./pyproject.toml --namespace-packages
echo "Running black on project"
poetry run black . --config ./pyproject.toml
echo "Running isort on project"
poetry run isort . --settings-path ./pyproject.toml 
