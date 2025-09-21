# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        seen = [False]*n
        seen[0] = True
        st = [0]
        while st:
            u = st.pop()
            for v in rooms[u]:
                if not seen[v]:
                    seen[v] = True
                    st.append(v)
        return all(seen)