class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        """

        """
        prefix = ""
        curr_index = 0
        min_length = min((len(string) for string in strs))
        while True:
            if curr_index >= min_length:
                return prefix
            char = strs[0][curr_index]
            for curr_string in strs[1:]:                    
                if curr_string[curr_index] != char:
                    return prefix
            curr_index += 1
            prefix += char
        
        return prefix
