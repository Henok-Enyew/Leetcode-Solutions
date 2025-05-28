# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        N = len(arr)
        prev_small = [-1 for _ in range(N)]
        #
        stack = []

        MOD= 1000000000 + 7


        for index in range(N):
            while stack and arr[stack[-1]] > arr[index]:
                stack.pop()
            if stack:
                prev_small[index] = stack[-1]
            stack.append(index)
        next_small = [N for _ in range(N)]

        stack = []


        for index in range(N -1, -1, -1):
            while stack and arr[stack[-1]] >= arr[index]:
                stack.pop()
            if stack:
                next_small[index] = stack[-1]
            stack.append(index)
        ans = 0
        for i in range(N):
            right = prev_small[i]
            left = next_small[i]

            windows = (right - i) * (i - left)

            ans += windows * arr[i]
        return ans % MOD
