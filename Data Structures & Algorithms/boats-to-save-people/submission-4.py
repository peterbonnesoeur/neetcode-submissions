from collections import Counter

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        l,r = 0, len(people) - 1
        num_boats = 0

        # [1 , 1, 1, 1, 1]
        while l < r:
            # print(num_boats, people[l:r+1])
            if people[l] + people[r] > limit:
                r-=1
                num_boats += 1
            elif people[l] + people[r] <= limit:
                r-=1
                l+=1
                num_boats += 1
            # print(num_boats, people[l:r+1])

        if l == r:
            num_boats += 1
        
        return num_boats




    def numRescueBoatsEfficient(self, people: List[int], limit: int) -> int:
        """
            This sounds like a greedy exercise

            No, only 2 people, we can get smarter

            # edge case -> on;y 1 weight
            # edge case: same weight as lim
            # edge case: weight >limit or = 0 -> impossible

            count = Counter(people)
            num_boats = 0
            hig_weight, low_weight = limit, 0

            while len(count) != 0:
                if high_weight in count:
                    if low_weight in count:
                        num_boats += min(count[low_weight], count[high_weight])
                        if count[low_weight] == count[high_weight]:
                            count.remove(low_weight)
                            count.remobe(high_weight)
                        elif count[low_weight] > count[high_weight]:
                            count.remove(high_weight)
                            count[low_weight] = count[low_weight] - count[high_weight]
                        else:
                            count.remove(low_weight)
                            count[high_weight] = count[high_weight] - count[low_weight]
                    else:
                        low_weight -= 1
                else:
                    high_weight -=1

            return num_boats

        """

        count = Counter(people) # n
        # o(n) 
        num_boats = 0
        high_weight, low_weight = max(count.keys()), min(count.keys())

        while len(count) != 0:
            print(count)
            # break
            if high_weight in count:
                print(high_weight)
                # break
                if low_weight in count:

                    if high_weight + low_weight > limit:
                        num_boats += count[high_weight]
                        count.pop(high_weight)
                        high_weight -= 1
                    elif high_weight == low_weight:
                        num_boats += count[high_weight] //2 + count[high_weight]%2
                        count.pop(high_weight)
                    else:
                        num_boats += min(count[low_weight], count[high_weight])
                        # print(num_boats)
                        if count[low_weight] == count[high_weight]:
                            count.pop(low_weight)
                            count.pop(high_weight)
                        elif count[low_weight] > count[high_weight]:
                            count[low_weight] = count[low_weight] - count[high_weight]
                            count.pop(high_weight)
                        else:
                            count[high_weight] = count[high_weight] - count[low_weight]
                            count.pop(low_weight)

                else:
                    low_weight += 1
            else:

                high_weight -=1

        return num_boats
            

