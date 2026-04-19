# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=problem-list-v2&envId=hash-table
# 350. Intersection of Two Arrays II
from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hash = Counter(nums1)

        ans = []

        for i in nums2:
            if i in hash and hash[i]:
                ans.append(i)
                hash[i] -= 1
        
        return ans
    
print(Solution().intersect(nums1 = [1,1], nums2 = [1]))
