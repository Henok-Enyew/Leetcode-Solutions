class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        x = 1
        ans = [1]
        while len(ans) < n:
            if x * 10 <= n:
                x = x * 10
            else:
                if x + 1 <= n:
                    x = x + 1
                else:
                    x = x // 10 + 1
                while x % 10 == 0:
                    x //= 10
            ans.append(x)
        return ans