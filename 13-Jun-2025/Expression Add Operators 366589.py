# Problem: Expression Add Operators - https://leetcode.com/problems/expression-add-operators/description/

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        def dfs(cur_idx: int, cur_res: List[str], cur_sum: int, prev: int):
            if cur_idx >= len(num):
                if cur_sum == target:
                    res.append("".join(cur_res))
                return

            for i in range(cur_idx, len(num)):
                cur_str = num[cur_idx:i+1]

                if len(cur_str) > 1 and cur_str[0] == '0':
                    break

                cur_num = int(cur_str)

                if not cur_res:
                    dfs(i + 1, [cur_str], cur_num, cur_num)
                else:
                    dfs(i + 1, cur_res + ["+"] + [cur_str], cur_sum + cur_num, cur_num)
                    dfs(i + 1, cur_res + ["-"] + [cur_str], cur_sum - cur_num, -cur_num)
                    dfs(i + 1, cur_res + ["*"] + [cur_str], cur_sum - prev + prev * cur_num, prev * cur_num)

        dfs(0, [], 0, 0)
        return res