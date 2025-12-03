class Solution:
    def isValid(self, s: str) -> bool:
        # listi = []
        # for i in range(len(s)):
        #     if s[i] == "(" or s[i] == "[" or s[i] == "{":
        #         listi.append(s[i])
        #     top = listi.pop()
        #     if 


        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        # for ch in s:
        #     if ch in pairs.values():  # opening bracket
        #         # print(pairs.values())
        #         stack.append(ch)
        #         print(stack)
        #     elif ch in pairs:  # closing bracket
        #         if not stack or stack[-1] != pairs[ch]:
        #             return False
        #         stack.pop()
        
        # return not stack  # must be empty at the end


        for ch in s:
            if ch in pairs:  # opening bracket
                if stack and stack[-1] == pairs[ch]: # the last element in the stack list is the same as one of the keys in the pairs dictionary. 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
                
        return True if not stack else False

                # print(pairs.values())
        #         stack.append(ch)
        #         print(stack)
        #     elif ch in pairs:  # closing bracket
        #         if not stack or stack[-1] != pairs[ch]:
        #             return False
        #         stack.pop()
        
        # return not stack  # must be empty at the end


if __name__ == "__main__":
    # print(Solution().isValid("}"))      # False
    # print(Solution().isValid("()[]{}")) # True
    # print(Solution().isValid("([)]"))   # False
    print(Solution().isValid("{[]}"))   # True
