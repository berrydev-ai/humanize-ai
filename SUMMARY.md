# Humanize AI - Implementation Summary

This is a Python implementation of the [humanize-ai-lib](https://github.com/Nordth/humanize-ai-lib) JavaScript package.

## Key Features

1. **Humanizes AI-generated text** by normalizing Unicode characters to standard keyboard equivalents
2. **Removes subtle AI markers** like fancy quotes, em-dashes, and hidden characters
3. **Provides fine-grained control** through configuration options
4. **Command-line interface** for easy integration with scripts and workflows
5. **Simple API** for use in Python applications

## Implementation Details

- Used Python's `re` module for most pattern matching
- Used the `regex` library for Unicode property support (needed for keyboard-only mode)
- Implemented the same transformation options as the original JavaScript version
- Added a command-line interface for terminal usage
- Followed Python packaging best practices

## Installation and Usage

After installation, you can use the library in two ways:

1. **As a Python library**:
   ```python
   from humanize_ai import humanize_string
   result = humanize_string("Hello — world")
   print(result['text'])  # "Hello - world"
   ```

2. **As a command-line tool**:
   ```bash
   humanize-ai "Hello — world with fancy "quotes" and…more"
   ```

## Testing

The implementation includes unit tests that match the original JavaScript test cases to ensure compatibility.