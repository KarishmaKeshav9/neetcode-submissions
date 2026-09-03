class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i:[] for i in range(numCourses)}
        for course, preq in prerequisites:
            pre_map[course].append(preq)
        
        visit_course = set()
        def dfs(course):
            if course in visit_course:
                return False

            if pre_map[course] == []:
                return True

            visit_course.add(course)
            for preq in pre_map[course]:
                if not dfs(preq):
                    return False
            visit_course.remove(course)
            pre_map[course] = []
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
