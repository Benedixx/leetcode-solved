class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest_prefix = ""
        for str in strs :
            longest_prefix = strs[0]
            for i in str:
                if i in longest_prefix:
                    continue
                else:
                    longest_prefix = longest_prefix[:len(longest_prefix) - 1]
                    if len(longest_prefix) == 0:
                        return ""
        return longest_prefix