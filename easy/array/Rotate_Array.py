#https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/646/


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            save = nums[:-1]
            head = nums[-1]
            nums[0] = head
            nums[1:] = save
        