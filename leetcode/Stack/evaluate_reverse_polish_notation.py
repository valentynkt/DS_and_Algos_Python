import operator


class Solution:
    # So we should use stack, for example [1, 2, +, 3, *, 4, -]
    # If it is number we push it into the stack, if it is operator we pop the last two numbers from stack and apply the operator into them, and put the result back.
    # step 1:[1] step 2:[1, 2] step 3: + in operators, we pop 1, 2 use the + operator on them = 3 and put it into stack : [3]
    # step 4: [3,3] step 5 pop 2 numbers from stack and apply operator [9] step 5: [9, 4] step 6: [5]  if len(stack) == 1: return result, else None
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

        for i in tokens:
            if i in ops and len(stack) == 0:
                return 0
            elif i in ops:
                item1 = stack.pop()
                item2 = stack.pop()
                res_ops = ops[i](item2, item1)
                stack.append(int(res_ops))
                continue
            stack.append(int(i))
        if len(stack) == 1:
            return stack.pop()

        return 0
