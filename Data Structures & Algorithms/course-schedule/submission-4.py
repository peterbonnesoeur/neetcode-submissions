class Node:

    def __init__(self, val:int):
        self.val = val
        self.prerequisite_courses = []


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = {}
        for course_id in range(numCourses):
            if course_id not in nodes:
                nodes[course_id] = Node(course_id)
            
            for prerequisite in prerequisites:
                if prerequisite[1] not in nodes:
                    nodes[prerequisite[1]] = Node(course_id)
                if prerequisite[0] == course_id:
                    nodes[course_id].prerequisite_courses.append(nodes[prerequisite[1]])

        # print(prerequisite)
        # print(nodes)

        seenNodes = set()
        def isCycle(node):

            if node in seenNodes:
                return True

            if node.prerequisite_courses == []:
                return False

            seenNodes.add(node)
            for prereq in node.prerequisite_courses:
                if isCycle(prereq):
                    return True
            seenNodes.remove(node)
            node.prerequisites = []
            
            return False


        for i, node in nodes.items():
            if isCycle(node):
                return False

        return True

