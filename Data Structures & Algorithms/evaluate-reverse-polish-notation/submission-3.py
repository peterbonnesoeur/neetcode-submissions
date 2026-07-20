class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Pure stack problem
        """
        stack = []
        
        for token in tokens:
            # print(stack, token)
            if token.replace("-","").isnumeric():
                stack.append(int(token))
            else:
                
                right_op = stack.pop()
                left_op = stack.pop()
                match token:
                    case "+":
                        stack.append(right_op + left_op)
                    case "-":
                        stack.append(left_op - right_op )
                    case "*":
                        stack.append(right_op * left_op)
                    case "/" :
                        stack.append(int(left_op / right_op))
                    case _:
                        print("nope")
        return stack[0]