from Rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase): #inheriting
    def test_basic(self):
        testcase = "Lovelace, Ada"
        exected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase),exected)
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)
    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)    
unittest.main()