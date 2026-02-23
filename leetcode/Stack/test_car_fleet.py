import pytest


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = sorted(list(zip(position, speed)), reverse=True)
        fleets = curtime = 0
        for cur_pos, cur_speed in pairs:
            destination_time = (target - cur_pos) / cur_speed
            if curtime < destination_time:
                fleets += 1
                curtime = destination_time
        return fleets


@pytest.fixture
def s():
    return Solution()


def test_basic2(s):
    assert s.carFleet(10, [4, 1, 0, 7], [2, 2, 1, 1]) == 3
