#https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/549/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            check_num = nums[0]
            nums = nums[1:]
            if check_num in nums:
                nums.remove(check_num)
            else:
                return check_num
        