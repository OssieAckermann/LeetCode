# https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/881/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d ={}
        for each in s:
            if each not in d:
                d[each] = 1
            else:
                d[each] += 1
        for key in d:
            if d[key] == 1:
                return s.find(key)
        return -1