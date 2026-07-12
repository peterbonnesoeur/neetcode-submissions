class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
            I am thinking about a recursive alg that does a selection of 1, 2 or 3 char
            -> if the 3 char //255 = 1 -> we pass it.
            Then, we go one layer deeper and have num of 

            if dot_count < len(s):
                return None
            if dot_count == 0 and len(substring) > 3:
                return None
        """

        results: list[list[str]] = []

        POSSIBILITIES = [ 1, 2, 3]
        MAX_VAL = 256
        MAX_DOTS = 3

        def pointPlace(substring: str, num_dots:int, prev_res: list[str]):
            # "101023" 3

            # "01023" 2 "1"
            # "1023" 1 "1" "0"
            # "023" 0 "1" "0" "1"
            # "23" 0 "1" "0" "10"
            # "3" 0 "1" "0" "102"
            # "023" 1 "1" "01"
            # "23" 0 "1" "01" "0"
            # "3" 0 "1" "01" "02"

            

            if len(substring) == 0 or num_dots >= len(substring):
                return None

            for possibility in POSSIBILITIES:
                if possibility == 3 and int(substring[:possibility]) // MAX_VAL != 0:
                    continue
                if possibility > 1 and substring[0] == "0":
                    continue
                
                prev_res.append(substring[:possibility])
                if len(substring) == possibility and num_dots == 0:
                    # print(prev_res, results)
                    results.append(prev_res.copy())
                    # print(results)

                pointPlace(substring[possibility:], num_dots = num_dots - 1, prev_res = prev_res)
                prev_res.pop(-1)
        
        pointPlace(substring = s, num_dots = MAX_DOTS, prev_res = [])

        # print(results)
        return [ ".".join(res) for res in results]



