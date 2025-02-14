# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = collections.defaultdict(int)
        for rabbit in answers:
            counts[rabbit] += 1

        results = 0
        for key in counts.keys():
            count = counts[key]

            number = ((count - 1) // (key + 1)) + 1
            results += number * (key + 1)

        return results