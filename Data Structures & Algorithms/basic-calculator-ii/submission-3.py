class Solution:
    def calculate(self, s: str) -> int:
        """
            This looks like a stack problem
            [ 3,+, 2, *, 2] 

            we only have +,-, /, * operations
            The main complexity consist of the priority of the operator.

            I would say that this is a 2 pass exercise.
            First, we populate a stack
            then, we redo a stack after the * and / operations
            then, we do a stack with the + and - operations.

            But that is 3 passes.
            Can we do it in less?
            Yes, we can do 2 passes. the first populating one with the / and *
            then the second one with the populated queue.
        """

        stack = []
        num = 0
        operand = "+"
        s = s.replace(" ", "")
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num *10 + int(ch)
            if (not ch.isdigit()) or i == len(s) - 1:
                match operand:
                    case "+":
                        stack.append(num)
                    case "-":
                        stack.append(-num)
                    case "*":
                        stack.append(stack.pop()*num)
                    case "/":
                        stack.append(int(stack.pop()/num))
                num = 0
                operand = ch
        return sum(stack)

        # curr : str = ""
        # stack : list[str] = []
        # result: int = 0
        # s = s.replace(" ","")
        # # print(s)

        # for i, val in enumerate(s):
        #     if val.isnumeric():
        #         curr += val

        #     if not val.isnumeric() or i == len(s)-1 :
        #         stack.append(curr)
        #         curr = ""

        #     if len(stack)>2 and stack[-2] in ("/", "*"):
        #         right_operand = stack.pop()
        #         operation = stack.pop()
        #         left_operand = stack.pop()
        #         # print(left_operand, operation, right_operand, stack)
        #         if operation == "/":
        #             stack.append(str(int(int(left_operand) / int(right_operand))))
        #         else:
        #            stack.append(str(int(int(left_operand) * int(right_operand))))
                

        #     if not val.isnumeric():
        #         stack.append(val)

        # print(stack)
        # sign = 1
        # while stack:
        #     val = stack.pop(0)
        #     if val.isnumeric():
        #         result += sign * int(val)
        #     elif val == "-":
        #         sign = -1
        #     else:
        #         sign = 1
            
        # return result
            
                

