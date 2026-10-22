class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses
        order = []

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] += 1

        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            order.append(node)
            for neighbor in adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return order if len(order) == numCourses else []