import string
import unittest
from password_gen import generate_password

class FullTestDrive(unittest.TestCase):
    
    def test_length_complexity1(self):
        complexity = 1
        password = generate_password(complexity)
        self.assertEqual(len(password), 9)

    def test_length_complexity2(self):
        complexity = 2
        password = generate_password(complexity)
        self.assertEqual(len(password), 18)

    def test_length_complexity3(self):
        complexity = 3
        password = generate_password(complexity)
        self.assertEqual(len(password), 27)

    def test_length_complexity_incorrect(self):
        complexity = 0
        with self.assertRaises(ValueError):
            password = generate_password(complexity)

    def test_contains_uppercase(self):
        password = generate_password(1)
        actual = self.contains_upper(password)
        self.assertTrue(actual)

    def test_contains_lowercase(self):
        password = generate_password(1)
        actual = self.contains_lower(password)
        self.assertTrue(actual)

    def test_contains_number(self):
        password = generate_password(1)
        actual = self.contains_number(password)
        self.assertTrue(actual)

    def test_contains_special(self):
        password = generate_password(1)
        actual = self.has_special_characters(password)
        self.assertTrue(actual)

    def test_unique_characters(self):
        password = generate_password(1)
        actual = self.has_unique_characters(password)
        self.assertTrue(actual)
    
    ''' Helper functions next '''
    
    def contains_number(self, password):
        return any(char.isdigit() for char in password)

    def contains_lower(self, password):
        return any(char.islower() for char in password)
    
    def contains_upper(self, password):
        return any(char.isupper() for char in password)
    
    def has_special_characters(self, password):
        return any(char in string.punctuation for char in password)
    
    def has_unique_characters(self, password):
        return len(set(password)) == len(password)

if __name__ == '__main__':
    unittest.main()