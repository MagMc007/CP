# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/
# 2006. Count Number of Pairs With Absolute Difference K
from collections import Counter


class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        
        hash = Counter(nums)
        ans = 0

        for i in range(len(nums)):
            hash[nums[i]] -= 1

            if nums[i] - k in hash:
                ans += hash[nums[i]-k]

            if nums[i] + k in hash:
                ans += hash[nums[i]+k]

        return ans


print(Solution().countKDifference(nums=[1,2,2,1], k=1))
print(Solution().countKDifference(nums=[1], k=1))