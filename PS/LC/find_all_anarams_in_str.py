# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# 438. Find All Anagrams in a String
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        hash = Counter(p)
        L = len(p)
        S = len(s)

        if L > S:
            return []
        
        ans = []
        palin = Counter()

        for i in range(L):
            palin[s[i]] += 1

        if palin == hash:
            ans.append(0)

        j = 0

        for k in range(L, S):
            palin[s[k]] += 1

            palin[s[j]] -= 1
            if palin[s[j]] == 0:
                palin.pop(s[j])
            j += 1

            if palin == hash:
                ans.append(j)

        return ans
 

print(Solution().findAnagrams( s = "aaaaaaaaaa", p = "aaaaaaaaaaaaa"))
