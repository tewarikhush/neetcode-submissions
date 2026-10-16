class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] += 1
        
        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for neighbor in adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return finish == numCourses