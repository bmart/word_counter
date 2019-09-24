import unittest

from word_counter import WordCounter

class TestMyWordCounter(unittest.TestCase):
    
    def testBasicSentence(self):
        wc = WordCounter()
        basicString = "Quick brown fox jumped over the lazy dog."
        wc.processString(basicString)
        self.assertEqual(8, wc.getWordCount())
        
    def testNumbersCounted(self):
        wc = WordCounter()
        basicString = "Quick brown fox jumped over 9 the lazy dog"
        wc.processString(basicString)
        self.assertEqual(9, wc.getWordCount())
        
    def testAppostrophesHandledOk(self):
        wc = WordCounter()
        basicString = "I'm a Quick brown fox jumped over 9 the lazy dog"
        wc.processString(basicString)
        self.assertEqual(11, wc.getWordCount())
        
        wl = wc.getWordList()
        self.assertTrue("I\'m" in wl.keys())

    def testHandlesCommasOk(self):
        wc = WordCounter()
        basicString = "I'm a Quick brown, fox jumped over 9 the lazy dog"
        wc.processString(basicString)
        self.assertEqual(11, wc.getWordCount())

    def testHandlesTemperature(self):
        wc = WordCounter()
        basicString = "The temperature outside, is -9C"
        wc.processString(basicString)
        self.assertEqual(5, wc.getWordCount())
        
    
    def testWordTally(self):
        wc = WordCounter()
        basicString = "I am bad bad bad at python, its amazing how quickly you can forget python"
        wc.processString(basicString)
        
        wordList = wc.getWordList()
        
        self.assertEqual(3, wordList['bad'])
        self.assertEqual(2, wordList['python'])

        
        

if __name__ == '__main__':
    unittest.main()
