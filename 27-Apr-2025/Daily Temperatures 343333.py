# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) ->list[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i,temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((temp,i))
                continue
            while len(stack) > 0 and stack[-1][0] < temp:
                answer[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temp,i))
        return answer