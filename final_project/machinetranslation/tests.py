import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('How are you?'), 'Comment es-tu?') 
        


class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Comment es-tu?'), 'How are you?')
       

unittest.main()