import pytest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c.lower() for c in s if c.isalnum())
        i = 0
        j = len(cleaned) - 1
        attempt = 1
        if len(cleaned) <= 1:
            return True
        result = True
        while i < j:
            left_char = cleaned[i]
            right_char = cleaned[j]
            if left_char != right_char:
                if attempt == 1:
                    attempt -= 1
                else:
                    result = False
                    break
            i += 1
            j -= 1

        return result


@pytest.fixture
def s():
    return Solution()


def test_basics(s):
    assert s.isPalindrome("aca")


def test_basics2(s):
    assert not s.isPalindrome("abbadc")


def test_basics3(s):
    assert s.isPalindrome("abc")
