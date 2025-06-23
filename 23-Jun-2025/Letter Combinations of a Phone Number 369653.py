# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        phone_keypad = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],  
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],  
        }
        res = []
        def backtrack(ind,comb):
            print(ind, comb)
            if len(comb) == len(digits):
                res.append(comb)
                return
            for i in range(len(phone_keypad[digits[ind]])):
                comb = comb + phone_keypad[digits[ind]][i]
                backtrack(ind+1, comb)
                comb = comb[:-1]
        backtrack(0,'')
        return res