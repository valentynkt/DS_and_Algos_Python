from collections import defaultdict

import pytest


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                c_index = ord(c) - ord("a")
                count[c_index] += 1
            res[tuple(count)].append(word)

        return list(res.values())


@pytest.fixture
def s():
    return Solution()


def test_basic(s):
    assert s.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]) == [
        ["hat"],
        ["act", "cat"],
        ["stop", "pots", "tops"],
    ]
