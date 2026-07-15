class Solution:
    def isValid(self, s: str) -> bool:

        """
            what ifs:
            - empty array -> []
            - starting by the closing characters -> ]
            - finishing by an opening character -> [ -> non empty
        """

        CORESPONDANCE = {
            ")": "(",
            "}": "{",
            "]": "[" 
        }
        OPENERS = set(CORESPONDANCE.values())
        # CLOSERS  = set(x.values)

        stack = []

        for char in s:
            if char in OPENERS:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if stack.pop(-1) != CORESPONDANCE.get(char, None):
                    return False
        
        print(stack)
        
        return True if len(stack) == 0 else False