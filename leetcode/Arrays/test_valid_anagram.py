from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        occurence = [0] * 26
        for cs, ct in zip(s, t):
            index_cs = ord(cs) - ord("a")
            index_ct = ord(ct) - ord("a")
            occurence[index_cs] += 1
            occurence[index_ct] -= 1
        for i in occurence:
            if i != 0:
                return False
        return True
