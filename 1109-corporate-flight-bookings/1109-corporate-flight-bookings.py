class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        array = [0] * (n+1)
        for booking in  bookings:
            array[booking[0] - 1] += booking[2]
            array[booking[1]] -= booking[2]
        for i in range(1, len(array)):
            array[i] += array[i-1]
        return array[:-1]