from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)

        for courses in prerequisites:
            adj[courses[0]].append(courses[1])

        # visiting = set()

        # OR we precomputre it...

        def dfs(course) -> set[int]:
            if course not in preMap:
                for prereq in adj[course]:
                    preMap[course] |= {prereq} |dfs(prereq)
                # preMap[course].add(course)
            return preMap[course]
        preMap = defaultdict(set)
        for course in range(numCourses):
            dfs(course)
        
        res = []
        for u,v in queries:
            res.append(v in preMap[u])
        return res
                
        # def isPrereq(course, target, visited):

        #     if course in visited:
        #         return False
        #     visited.add(course)

        #     for pre_course in preMap[course]:
        #         if pre_course == target:
        #             return True
        #         if isPrereq(pre_course, target, visited):
        #             preMap[course].insert(0, target)
        #             return True
        #     return False

        # result = []
        # for query in queries:
        #     visited = set()
        #     if isPrereq(query[0], query[1], visited):
        #        result.append(True)
        #     else:
        #         result.append(False)
        # return result