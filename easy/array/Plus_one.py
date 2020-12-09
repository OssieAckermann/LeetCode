#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[0] == 0:
            digits[-1] = 1
            return digits
        a = len(digits)
        n = 1
        for i in range(a-1,-1,-1):
            n += (10**i) * digits[a-1-i]
        return [int(x) for x in str(n)]
            
