'''
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
'''

def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        l=0
        for i in range(len(s)):
            if s[i] == " ":
                l=0
            else:
                l+=1
        return l