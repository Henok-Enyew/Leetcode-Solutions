class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        n = 0
        for hour in hours:
            if hour>= target :
                n+=1
        return n