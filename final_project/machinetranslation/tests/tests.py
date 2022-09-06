import unittest

from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self):
        self.assertEqual(french_to_english(''), None) # Test for Null input 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test that Bonjour translates to Hello

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(''), None) # Test for Null input 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test that Hello translates to Bonjour

unittest.main()