import unittest
from corrupter import create_substitution_dict, transform_text, replace_spaces, add_random_underscore


class TestTextTransform(unittest.TestCase):

    def test_create_substitution_dict(self):
        substitutions = create_substitution_dict()
        self.assertIsInstance(substitutions, dict)
        self.assertTrue(len(substitutions) > 0)

    def test_transform_text(self):
        substitutions = create_substitution_dict()
        input_text = "Hello World"
        transformed_text = transform_text(input_text, substitutions)
        self.assertNotEqual(input_text, transformed_text)

    def test_replace_spaces(self):
        input_text = "Hello World"
        replaced_text = replace_spaces(input_text)
        self.assertNotIn(" ", replaced_text)
        self.assertIn("_", replaced_text)
        self.assertIn("-", replaced_text)

    def test_add_random_underscore(self):
        input_text = "HelloWorld"
        underscored_text = add_random_underscore(input_text)
        self.assertIn("_", underscored_text)
        self.assertTrue(underscored_text.startswith(
            "_") or underscored_text.endswith("_"))


if __name__ == "__main__":
    unittest.main()
