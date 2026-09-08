class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_crs_map = { c:[] for c in range(numCourses)}

        for crs, preq in prerequisites:
            pre_crs_map[crs].append(preq)

        output = []
        visit_set, cur_cycle_set = set(), set()

        def dfs(crs):
            if crs in cur_cycle_set:
                return False
            
            if crs in visit_set:
                return True

            cur_cycle_set.add(crs)
            for pre in pre_crs_map[crs]:
                if not dfs(pre):
                    return False

            cur_cycle_set.remove(crs)
            visit_set.add(crs)
            output.append(crs)

            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output