#!/usr/bin/env python3
"""
Command-line interface for humanize-ai
"""

import argparse
import sys
from humanize_ai.humanize_string import humanize_string, HumanizeOptions


def main():
    parser = argparse.ArgumentParser(description="Humanize AI-generated text")

    parser.add_argument(
        "text", nargs="?", help="Text to humanize. If not provided, reads from stdin"
    )

    parser.add_argument(
        "--no-hidden",
        action="store_false",
        dest="transform_hidden",
        help="Do not remove hidden Unicode characters",
    )

    parser.add_argument(
        "--no-trailing",
        action="store_false",
        dest="transform_trailing_whitespace",
        help="Do not remove trailing whitespace",
    )

    parser.add_argument(
        "--no-nbs",
        action="store_false",
        dest="transform_nbs",
        help="Do not transform non-breaking spaces",
    )

    parser.add_argument(
        "--no-dashes",
        action="store_false",
        dest="transform_dashes",
        help="Do not transform fancy dashes",
    )

    parser.add_argument(
        "--no-quotes",
        action="store_false",
        dest="transform_quotes",
        help="Do not transform fancy quotes",
    )

    parser.add_argument(
        "--no-other",
        action="store_false",
        dest="transform_other",
        help="Do not transform other symbols (e.g., …)",
    )

    parser.add_argument(
        "--keyboard-only",
        action="store_true",
        help="Only keep keyboard-typeable characters",
    )

    parser.add_argument(
        "--show-count",
        action="store_true",
        help="Print the number of transformed characters",
    )

    args = parser.parse_args()

    # Get text from argument or stdin
    if args.text:
        input_text = args.text
    else:
        input_text = sys.stdin.read()

    # Create options from arguments
    options = HumanizeOptions(
        transform_hidden=args.transform_hidden,
        transform_trailing_whitespace=args.transform_trailing_whitespace,
        transform_nbs=args.transform_nbs,
        transform_dashes=args.transform_dashes,
        transform_quotes=args.transform_quotes,
        transform_other=args.transform_other,
        keyboard_only=args.keyboard_only,
    )

    # Process the text
    result = humanize_string(input_text, options)

    # Output
    print(result["text"], end="")
    if args.show_count:
        print(f"\nTransformed {result['count']} characters.", file=sys.stderr)


if __name__ == "__main__":
    main()
