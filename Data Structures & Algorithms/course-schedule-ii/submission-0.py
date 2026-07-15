class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        """
            The goal is to find an optimal course path go do all the course and their prerequisites
            In order.

            We could brute force it -> for each course (N) we would search its prerequisiste and append them
            to a possibility list making it N^2 to test all the courser combination until we find a good one.

            What we want to do here is go through a 'path'
            The goal being to do a dfs to go over the prerequisites of each course and then jump to the prerequisistes
            of the prerequisites -> in a graph fashion.

            This exercise forces us to have both a cycle detection + a tracking of the past visited nodes per dependencies

            First, I would create a premap based on our adjacency list.
            Then, run a dfs on each course.

            But how do we find the longest set of requirement - ex:
            0: [2,3], 1: [0], 2: [3], 3:[]

            if we start by 0, we have 3 2 0 and then 1 -> this is thus just about knowing where to place 1
            -> always at the end?

            0: [3], 1 :[0,2] 2: [], 3:1
            3 0 2 1
        """
        preMap: dict[int,int] = dict()
        for i in range(numCourses):
            preMap[i] = []
            for prerequisite in prerequisites:
                if i == prerequisite[0]:
                    preMap[i].append(prerequisite[1])

        cycle : set[int] = set()
        visited: set[int] = set()
        result: list[int] = []

        def dfs(course: int) -> bool:

            if course in cycle:
                return True
            
            if course in visited:
                return False # We want to not repeat existing path -> this here indicates
                             # That we already went trhough the requisites of that one 
                             # and that it is already added to the answer.
            cycle.add(course)
            for preq in preMap[course]:
                if dfs(preq):
                    return True

            visited.add(course) # We already considered that path -> already out
            cycle.remove(course)
            result.append(course)
            return False

        for course in range(numCourses):
            if dfs(course):
                return []

        return result

            