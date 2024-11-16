import unittest
from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Hassan Miskawi"), "Hello, World from Hassan Miskawi!")

if __name__ == "__main__":
    unittest.main()
