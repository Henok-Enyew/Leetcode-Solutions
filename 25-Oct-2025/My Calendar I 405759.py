# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:
    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect_left(self.bookings, (end, 0))
        if idx and self.bookings[idx-1][0] > start:
            return False
        if idx < len(self.bookings) and self.bookings[idx][1] < end:
            return False
            
        self.bookings.insert(idx, (end, start))
        return True