"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        current_rooms = max_rooms = 0
        s_ptr = e_ptr = 0
        while s_ptr < len(intervals):
            if starts[s_ptr] < ends[e_ptr]:
                current_rooms += 1
                s_ptr += 1
            else:
                current_rooms -= 1
                e_ptr += 1
            max_rooms = max(max_rooms, current_rooms)
        return max_rooms