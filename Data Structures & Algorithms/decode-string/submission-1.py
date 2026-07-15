class Solution:
    def decodeString(self, s: str) -> str:
        
        """
            We want to have a recursive algo that will be repeating a character within its bracket
            The repeating element is a string right before the first opening character.

            The element that starts the recursion is a [

            The element that ends the recursion and makes the input come back is ]
            inputs:

            can we have 2[4] -> no 
            2[a]

            result
            curr_number = ""

            edge case: "asd"
        """
        result = ""

        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                sub_res = ""
                
                while stack[-1] != "[":
                    sub_res = stack.pop() + sub_res
                stack.pop()

                curr_multiplicator =""
                while len(stack) > 0 and stack[-1].isnumeric():
                    curr_multiplicator = stack.pop(-1) + curr_multiplicator

                stack.append(int(curr_multiplicator) * sub_res)

        return "".join(stack)

        def decoder(s: str) -> tuple[str, int]:
            result = ""
            curr_number = ""
            i = 0
            while i < len(s):
                char = s[i]
                if char.isnumeric():
                    curr_number += char
                elif char == "[":
                    repeated, offset = decoder(s[i+1:])
                    result += int(curr_number) * repeated
                    curr_number = ""
                    i += offset
                elif char == "]":
                    return result, i+1
                else:
                    result += char
                i+=1
            return result, i
                
            
        return decoder(s)[0]
