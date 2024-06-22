class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = map(lambda x: roman[x], s)
        result = list(result)
        num = 0
        for i in range(len(result) - 1):
            if result[i] < result[i + 1]:
                num -= result[i]
            else:
                num += result[i]
        num += result[-1]
            
        return num