#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = target - nums[i]
            try:
                if i != nums.index(a):
                    return[i,nums.index(a)]
                else:
                    pass
            except ValueError:
                pass