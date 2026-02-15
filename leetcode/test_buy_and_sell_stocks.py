import pytest


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 0:
            return 0
        profit = 0
        minimal = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - minimal > profit:
                profit = prices[i] - minimal
            elif prices[i] < minimal:
                minimal = prices[i]
        return profit


@pytest.fixture
def s():
    return Solution()


def test_basics(s):
    assert s.maxProfit([5, 3, 8, 2, 1]) == [1, 2, 3, 5, 8]


def test_already_sorted(s):
    assert s.maxProfit([1, 2, 3]) == [1, 2, 3]
