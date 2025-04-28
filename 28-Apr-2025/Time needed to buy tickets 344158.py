# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        target = tickets[k]
        while target > 0:
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    break
                if tickets[i] <= 0:
                    continue
                tickets[i] -= 1
                count += 1
            target = tickets[k]
        return count