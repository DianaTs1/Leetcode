class Solution(object):
    def getLength(self,word):
        return len(word)
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        words = sorted(words,key=self.getLength)
        licensePlate=licensePlate.lower()
        i = 0
        flag = False
        while(1):
            for char in licensePlate:
                if(char<'a' or char>'z'):
                    continue
                
                if(words[i].count(char) >= licensePlate.count(char)):
                    flag = True
                else:
                    i += 1
                    flag = False
                    break
                    
            if(flag):
                return words[i]