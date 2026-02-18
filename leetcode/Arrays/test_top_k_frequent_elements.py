import heapq
from collections import defaultdict
from typing import Counter

import pytest


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        h = []
        for num, freq in count.items():
            heapq.heappush(h, (-freq, num))
        return [heapq.heappop(h)[1] for _ in range(k)]


@pytest.fixture
def s():
    return Solution()


def test_basics(s):
    assert s.topKFrequent([1, 2, 2, 3, 3, 3], 2) == [2, 3]
    assert s.topKFrequent([7, 7], 1) == [7]
