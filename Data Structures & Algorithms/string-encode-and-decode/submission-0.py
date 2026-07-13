class Solution:
    """
    We want to decode the strings in the output.
    What could happen?  we could have a special parameter deliminating it.

    Issue -> we would lose it if this special parameter is in it.
    We could use the length of the array and a special char as a separator.
    The goal being to use the separator as a way to check if the array is well finished.
    """

    def encode(self, strs: List[str]) -> str:
        strs = [str(len(string)) + "#" + string for string in strs]
        return "#".join(strs)

    def decode(self, s: str) -> List[str]:
        result: list[str] = []
        length: str = ""
        i = 0
        while i < len(s):
            if s[i] == "#":
                result.append(s[i+1: i+int(length) + 1])
                i += int(length) + 2
                length = ""
            else:
                length += s[i]
                i+=1
        return result