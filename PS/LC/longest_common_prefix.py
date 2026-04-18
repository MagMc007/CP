# https://leetcode.com/problems/longest-common-prefix?envType=problem-list-v2&envId=array
# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pref = strs[0]

        for i in range(1, len(strs)):
            # iterate over both till only they are equal
            j = 0
            while j < min(len(pref), len(strs[i])):
                if pref[j] == strs[i][j]:
                    j += 1
                else:
                    break
            
            if not j:
                return ""

            pref = pref[:j]

        return pref
    
print(Solution().longestCommonPrefix(["flower","flow","flight"]))