class Solution:
    def encode(self, strs: list[str]) -> str:
        result = ""
        for str in strs:
            result += f"{len(str)}|{str}"
        return result

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.index("|", i)
            length = int(s[i:j])
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return result
