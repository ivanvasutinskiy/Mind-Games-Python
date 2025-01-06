install:
	uv sync
brain-games:
	uv run brain-games
build:
	uv build
package-install:
	uv tool install dist/*.whl
lint:
	uv run ruff check brain-games
fix:
	uv run ruff check --fix brain-games
uninstall hexlet-code:
	uv tool uninstall hexlet-code
