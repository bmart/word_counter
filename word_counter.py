import re
import argparse

SUMMARY_MAX = 10

class WordCounter(object):
    """Class to count number of words in a file or text string. Assumes files by default"""
    
    def __init__(self, fileName = None):
        self.wordList = {}
        self.wordPattern = re.compile(r'[a-zA-Z\-0-9][a-zA-Z0-9\'\-]*')
        
        if fileName is not None:
            self.processFile(fileName)
    
    def _extractWords(self,line):
        """tokenize a line of text into an array of words"""
        return self.wordPattern.findall(line)
    
    def _computeWordList(self, matches):
        """iterate through matched words and group common items"""
        for m in matches:
            if m not in self.wordList:
                self.wordList[m] = 1
            else:
                self.wordList[m] += 1
    
    def processString(self,text):
        """process a single line of text"""
        self.numWords = 0
        matches = self._extractWords(text)
        
        self.numWords = len(matches)
        self._computeWordList(matches)
        
        
    def processFile(self,fileName):
        """Process a file line by line"""
        
        self.numWords = 0
        
        with open(args.f) as f:
            line = f.readline()
             
            while line: 
                matches = self._extractWords(line)
                
                self.numWords += len(matches)
                self._computeWordList(matches)

                line = f.readline()
    
    def getWordList(self):
        """Return a summary list of words and totals"""
        return self.wordList
    
    def getWordCount(self):
        """Return total words counted"""
        return self.numWords
    
    
if __name__ == '__main__':    
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help="file to parse")

    args = parser.parse_args()
    
    if(args.f):
        wc = WordCounter(args.f)
        
        print("Total words: {0}".format(wc.getWordCount()))
        print("_____" * 8)
        
        resultCount = 0
        
        for key, value in sorted(wc.getWordList().items(), key=lambda item: item[1],reverse=True):
            print("%s: %s" % (key, value))
            resultCount += 1
            if resultCount == SUMMARY_MAX:
                break
    else:
        print(parser.print_help())


