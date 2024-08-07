class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        result = 0
        for opr in operations:
            if opr == '--X' or opr == 'X--':
                result -= 1
            elif opr == '++X' or opr == 'X++':
                result += 1
        return result
