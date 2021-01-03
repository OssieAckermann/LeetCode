#https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/883/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        w = ''
        for char in s:
            if char.isalpha() or char.isdigit():
                w += char
        if w == '':
            return True
        w = w.upper()
        for i in range((len(w)//2)+1):
            if w[i] != w[-(i+1)]:
                return False
        return True