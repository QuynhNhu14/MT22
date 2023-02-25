import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        testcase = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(testcase, expect, 101))

    def test_under_identifier(self):
        """test identifiers"""
        testcase = "_12"
        expect = "_12,<EOF>"
        self.assertTrue(TestLexer.test(testcase, expect, 102))

    def test_error_special_char_identifier(self):
        """test identifiers"""
        testcase = "a?c"
        expect = "a,Error Token ?"
        self.assertTrue(TestLexer.test(testcase, expect, 103))

    def test_uppercase_identifier(self):
        """test identifiers"""
        testcase = "ABC"
        expect = "ABC,<EOF>"
        self.assertTrue(TestLexer.test(testcase, expect, 101))