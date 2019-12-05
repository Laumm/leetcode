class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
                '(':')',
                '{':'}',
                '[':']',
                }
        stack = []
        for  c in s :
            if c in ['(','{','[']:
                stack.append(c)
                continue
            if len(stack) > 0 and c == pair[stack[-1]]:
                stack = stack[:-1]
                continue
            return False
        if len(stack) == 0 :
            return True
        return False

s =Solution()
print(s.isValid("()"))
