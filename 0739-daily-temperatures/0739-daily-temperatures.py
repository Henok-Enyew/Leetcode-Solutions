class Solution:
    def dailyTemperatures(self, temperatures: list[int]) ->list[int]:
        temp = [0] * len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            if len(stack) == 0:
                stack.append([i,t])
                continue
            elif stack[-1][1] < t:
                last = stack[-1]
                while(last[1] < t):
                    temp[last[0]] = i - last[0]
                    stack.pop()
                    if len(stack) > 0:
                        last = stack[-1]
                    else:
                        break
            stack.append([i,t])
        return temp
