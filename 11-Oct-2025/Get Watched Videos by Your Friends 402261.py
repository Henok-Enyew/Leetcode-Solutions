# Problem: Get Watched Videos by Your Friends - https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], _id: int, level: int) -> List[str]:
        res = defaultdict(int)

        q = deque([(_id, 0)])
        visited = set({_id})

        while q:
            curr_id, curr_level = q.popleft()
            if curr_level == level:
                for wv in watchedVideos[curr_id]:
                    res[wv] += 1
            elif curr_level < level:
                for friend in friends[curr_id]:
                    if friend not in visited:
                        visited.add(friend)
                        q.append((friend, curr_level + 1))
        


        return sorted(res.keys(), key=lambda x: (res[x], x))