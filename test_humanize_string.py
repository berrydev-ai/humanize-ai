#!/usr/bin/env python3
"""
Tests for the humanize_string module
"""

import unittest
from humanize_ai import humanize_string, HumanizeOptions


class TestHumanizeString(unittest.TestCase):
    def test_whitespaces(self):
        self.assertEqual(
            humanize_string("Hello\u200b\xa0World!  "),
            {
                "text": "Hello World!",
                "count": 4,
            },
        )

        self.assertEqual(
            humanize_string(
                "Hello\u200b\xa0World!  ",
                HumanizeOptions(transform_trailing_whitespace=False),
            ),
            {
                "text": "Hello World!  ",
                "count": 2,
            },
        )

        self.assertEqual(
            humanize_string(
                "Hello\u200b\xa0World!  ", HumanizeOptions(transform_hidden=False)
            ),
            {
                "text": "Hello\u200b World!",
                "count": 3,
            },
        )

        self.assertEqual(
            humanize_string(
                "Hello\u200b\xa0World!  ", HumanizeOptions(transform_nbs=False)
            ),
            {
                "text": "Hello\xa0World!",
                "count": 3,
            },
        )

    def test_dashes(self):
        self.assertEqual(
            humanize_string("I — super — man – 💪"),
            {
                "text": "I - super - man - 💪",
                "count": 3,
            },
        )

    def test_quotes(self):
        self.assertEqual(
            humanize_string('Angular "quote" «marks» looks„ like Christmas «« tree'),
            {
                "text": 'Angular "quote" "marks" looks" like Christmas "" tree',
                "count": 7,
            },
        )


if __name__ == "__main__":
    unittest.main()
