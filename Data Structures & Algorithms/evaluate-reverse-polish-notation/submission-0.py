class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = deque()

        for s in tokens:

            if s == '+' or s == '-' or s == '*' or s == '/':
                a = stack.pop()
                b = stack.pop()

                if s == '+':
                    stack.append(b + a)
                elif s == '-':
                    stack.append(b - a)
                elif s == '*':
                    stack.append(b * a)
                elif s == '/':
                    stack.append(int(b / a))

            else:
                stack.append(int(s))

        return stack[-1]