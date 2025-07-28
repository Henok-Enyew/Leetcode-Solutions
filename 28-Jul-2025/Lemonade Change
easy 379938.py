# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billsmp = {5:0, 10:0}
        for bill in bills:
            if bill == 5:
                billsmp[5] += 1
            elif bill == 10:
                if billsmp[5] <= 0:
                    return False
                else:
                    billsmp[5] -= 1
                    billsmp[10] += 1
            else:
                if (billsmp[5] <= 0 or billsmp[10] <= 0 ) and billsmp[5] < 3:
                    return False
                else:
                    if billsmp[10] > 0:
                        billsmp[5] -= 1
                        billsmp[10] -= 1
                    else:
                        billsmp[5] -= 3
        return True