class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preMap = {i: [] for i in range(numCourses)}

        for courses in prerequisites:
            if len(courses) != 2:
                continue
            preMap[courses[0]].append(courses[1])

        # visiting = set()

        def isPrereq(course, target, visited):

            if course in visited:
                return False
            visited.add(course)

            for pre_course in preMap[course]:
                if pre_course == target:
                    return True
                if isPrereq(pre_course, target, visited):
                    preMap[course].insert(0, target)
                    return True
            return False

        result = []
        for query in queries:
            visited = set()
            if isPrereq(query[0], query[1], visited):
               result.append(True)
            else:
                result.append(False)
        return result