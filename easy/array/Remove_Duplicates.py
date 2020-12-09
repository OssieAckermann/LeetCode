#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for k in range(len(nums)):
            if nums[i] in nums[i+1:]:
                nums.remove(nums[i])
            else:
                i += 1
        print(len(nums), nums)
            

        