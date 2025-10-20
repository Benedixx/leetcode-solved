class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        # search for the shortest string in the list
        shortest = min(strs, key=len)
        # compare the shortest string with the rest of the strings
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest
        