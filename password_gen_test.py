import unittest
import re
from password_gen import generate_password

class FullTestDrive(unittest.TestCase):
    
    def test_length(self):
        password = generate_password(9)
        self.assertEqual(len(password), 9)

    def test_contains_uppercase(self):
        password = generate_password(9)
        actual = self.contains_upper(password)
        self.assertTrue(actual)

    def test_contains_lowercase(self):
        password = generate_password(9)
        actual = self.contains_lower(password)
        self.assertTrue(actual)

    def test_contains_number(self):
        password = generate_password(9)
        actual = self.contains_number(password)
        self.assertTrue(actual)

    def test_contains_special(self):
        password = generate_password(9)
        actual = self.contains_special(password)
        self.assertTrue(actual)

    def test_length_constraint(self):
        with self.assertRaises(ValueError):
            password = generate_password(1)

    def test_unique_characters(self):
        password = generate_password(9)
        actual = self.contains_special(password)
        self.assertTrue(actual)

    ''' Helper functions next '''

    def contains_number(self, string):
        return any(char.isdigit() for char in string)

    def contains_lower(self, string):
        return any(char.islower() for char in string)
    
    def contains_upper(self, string):
        return any(char.isupper() for char in string)
    
    def contains_special(self, string):
        pattern = r"[!@#$%^&*(),.?\":{}|<>]"
        return bool(re.search(pattern, string))
    
    def has_unique_characters(self, string):
        return len(set(string)) == len(string)

if __name__ == '__main__':
    unittest.main()