# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        block_comment = False
        temp = ''

        for i in range(len(source)):
            str = source[i]
            right = 0

            while right < len(str):
                if str[right:right+2] == '/*' and not block_comment:
                    block_comment = True
                    right += 1
                elif str[right:right+2] == '*/' and block_comment:
                    block_comment = False
                    right += 1
                elif not block_comment and str[right:right+2] == '//':
                    break
                elif not block_comment:
                    temp += str[right]

                right += 1

            if not block_comment and temp != '':
                result.append(temp)
                temp = ''

        return result
