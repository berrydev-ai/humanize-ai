#!/usr/bin/env python3
"""
Tests for the humanize_json function
"""

import unittest
from humanize_ai import humanize_json, HumanizeOptions

class TestHumanizeJson(unittest.TestCase):
    def test_flat_dict(self):
        data = {"a": "Hello\u200b World!  ", "b": 123, "c": None}
        cleaned, count = humanize_json(data)
        self.assertEqual(cleaned["a"], "Hello World!")
        self.assertEqual(cleaned["b"], 123)
        self.assertEqual(cleaned["c"], None)
        self.assertGreater(count, 0)

    def test_nested_dict_and_list(self):
        data = {
            "dto": {
                "topic": "Your Home Office Makeover Starts With These 10 Game-Changers",
                "key_concepts": [
                    {"concept": "Ergonomic furniture essentials", "description": "Key pieces that support comfort and productivity."},
                    {"concept": "Lighting optimization techniques", "description": "Ways to enhance visibility and reduce eye strain."},
                ],
                "outline": {
                    "title": "Your Home Office Makeover Starts With These 10 Game-Changers",
                    "sections": [
                        {"section_identifier": "secret-your-boss-wont-tell-you", "section_description": "Hook with surprising productivity stats about home offices, establishing pain points of poor workspace design."}
                    ],
                    "suggested_formats": [
                        "Hybrid narrative/how-to approach",
                        "Problem-solution framework"
                    ]
                },
                "emotional_triggers": [
                    "Aspiration",
                    "Frustration"
                ]
            },
            "thoughts": "Here's the content plan based on your topic analysis and research:\n\n**Selected Topic:**\n..."
        }
        cleaned, count = humanize_json(data)
        self.assertIsInstance(cleaned, dict)
        self.assertIsInstance(cleaned["dto"], dict)
        self.assertIsInstance(cleaned["dto"]["key_concepts"], list)
        self.assertIsInstance(cleaned["dto"]["key_concepts"][0]["concept"], str)
        self.assertGreater(count, 0)

    def test_list_of_strings(self):
        data = ["Hello\u200b World!  ", "Test\u00a0string"]
        cleaned, count = humanize_json(data)
        self.assertEqual(cleaned[0], "Hello World!")
        self.assertEqual(cleaned[1], "Test string")
        self.assertGreater(count, 0)

    def test_non_string_leaves(self):
        data = {"a": 1, "b": [2, 3, None], "c": {"d": False}}
        cleaned, count = humanize_json(data)
        self.assertEqual(cleaned, data)
        self.assertEqual(count, 0)

if __name__ == "__main__":
    unittest.main()
