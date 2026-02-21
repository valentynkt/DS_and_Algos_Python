import pytest


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_to_opening = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch not in closing_to_opening:
                stack.append(ch)
            elif ch in closing_to_opening:
                if not stack:
                    return False
                top = stack.pop()
                if top != closing_to_opening[ch]:
                    return False
        return not stack


@pytest.fixture
def s():
    return Solution()


def test_basics2(s):
    assert s.isValid("[]")


def test_basics3(s):
    assert s.isValid("[")
