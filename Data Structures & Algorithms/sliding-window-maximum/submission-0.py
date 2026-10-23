class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        res = []
        q = collections.deque()
        for i, num in enumerate(nums):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if q[0] < i - k + 1:
                q.popleft()
            if i >= k - 1:
                res.append(nums[q[0]])
        return res

