# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for each in nums1.copy():
            if each in nums2:
                output.append(each)
                nums2.remove(each)
        return output
                
                
                
       