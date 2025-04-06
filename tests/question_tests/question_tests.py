#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import get_person_category
from src.question_b.question_b import get_random_number

class Test_Config(unittest.TestCase):

    def test_get_person_category(self):
        self.assertEqual(get_person_category(1), "infant")
        self.assertEqual(get_person_category(2), "child")
        self.assertEqual(get_person_category(14), "teenager")
        self.assertEqual(get_person_category(20), "adult")

    def test_get_random_number(self):
        self.assertEqual(get_random_number)