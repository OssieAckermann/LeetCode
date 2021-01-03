#https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/880/

class Solution:
    def reverse(self, x: int) -> int:
        word = ''
        l = list(str(x))
        l.reverse()
        for i in l:
            if i != '-':
                word += i
        if l[-1] == '-':
            word = '-'+word
        n = int(word)
        if n < 2**31 -1 and n > -(2**31):
            return n
        else:
            return 0