class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if c == '(':
                stack.append(c)

            elif c == ')':
                if not stack:
                    return False
                if stack.pop() != '(':
                    return False

            elif c == '[':
                stack.append(c)

            elif c == ']':
                if not stack:
                    return False
                if stack.pop() != '[':
                    return False

            elif c == '{':
                stack.append(c)

            elif c == '}':
                if not stack:
                    return False
                if stack.pop() != '{':
                    return False

        return not stack