# CLAUDE.md - Humanize AI Project Guide

## Build & Test Commands
- Install dev dependencies: `pip install -e ".[dev]"`
- Run all tests: `python -m unittest discover`
- Run single test: `python -m unittest test_humanize_string.TestHumanizeString.test_quotes`
- Format code: `black .`
- Lint: `flake8`
- Type check: `mypy .`

## Code Style Guidelines
- Follow PEP 8 standards (Python standard library style guide)
- Use type hints for function parameters and return values
- Format with Black for consistent code style
- Imports: standard library first, then third-party, then local modules
- Variable/function names: lowercase with underscores (snake_case)
- Class names: CamelCase
- Constants: ALL_CAPS_WITH_UNDERSCORES
- Add docstrings for all functions, classes, and modules (Google style)
- Include detailed error handling with specific exception types
- Return a dictionary with 'text' and 'count' keys from processing functions

## Project Structure
- Core functionality in `python_humanize_ai/humanize_string.py`
- CLI interface in `cli.py`
- Tests in `test_humanize_string.py`