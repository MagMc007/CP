# https://leetcode.com/problems/majority-element/
# 169. Majority Elementfrom math import floor
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority = n // 2
        nums = Counter(nums)

        for number, num_count in nums.items():
            if num_count > majority:
                return number
