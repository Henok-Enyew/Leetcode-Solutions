class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd

            while stack and stack[-1] <= time:
                stack.pop()

            stack.append(time)

        return len(stack)