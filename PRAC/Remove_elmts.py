# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # take them to the end
        if not nums:
            return 0
        
        # swap
        p1 = 0
        p2 = len(nums) - 1

        while p1 <= p2:
            if nums[p2] == val:
                p2 -= 1
                continue

            if nums[p1] != val:
                p1 += 1
                continue

            if nums[p1] == val:
                # swap
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
                p1 += 1

        return p2 + 1
    
print(Solution().removeElement(nums = [2, 2], val = 2))