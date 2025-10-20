class Solution:
    def mySqrt(self, x: int) -> int:
        base_subs = 1
        result = 0
        while x > 0 :
            result = result + 1
            x = x - base_subs
            base_subs = base_subs + 2
        
        if x < 0 :
            result = result - 1