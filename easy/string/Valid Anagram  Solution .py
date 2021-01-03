
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/882/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for char in s:
            if s.count(char) != t.count(char):
                return False
        return True
        