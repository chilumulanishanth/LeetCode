class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3=[]
        length=max([len(word1),len(word2)])
        for i in range(0,length):
            if i<len(word1):
                word3.append(word1[i])
            if i<len(word2):
                word3.append(word2[i])
        return(''.join(word3))

        