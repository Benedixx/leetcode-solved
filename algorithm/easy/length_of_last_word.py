class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitted_word = s.split()
        
        return len(splitted_word[-1])