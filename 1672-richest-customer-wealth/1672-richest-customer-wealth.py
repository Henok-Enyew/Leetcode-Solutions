class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich = 0
        for account in accounts:
            tot = sum(account)
            rich = max(tot, rich)
        return rich