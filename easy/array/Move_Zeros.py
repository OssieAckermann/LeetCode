#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n_zero = nums.count(0)
        print(n_zero)
        for i in range(n_zero):
            nums.remove(0)
            nums.append(0)
        