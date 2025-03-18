install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

fix:
	uv run ruff check --fix brain_games

uninstall hexlet-code:
	uv tool uninstall hexlet-code
	
test-coverage:
	uv run pytest --cov=gendiff tests --cov-report xml

check:
	uv run pytest
