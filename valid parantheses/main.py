s = "()"
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        # iterate char in s
        for char in s:
            # check if char is in bracket_map
            if char in bracket_map:
                # pop the top element from stack if stack is not empty
                top_element = stack.pop() if stack else '#'
                # if char is not the corresponding opening bracket of the top element
                if bracket_map[char] != top_element:
                    return False
            else:
                # append char to stack if char is not in bracket_map
                stack.append(char)

        return not stack
        
            
            
            
if __name__ == "__main__" :
    sol = Solution()
    print(sol.isValid(s=s))
            