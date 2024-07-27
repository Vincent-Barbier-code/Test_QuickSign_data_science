poetry install
./lint_module.sh
poetry run pytest . -ra -q -vv --cov-config=./pyproject.toml --cov=./qsdata --cov-report=term