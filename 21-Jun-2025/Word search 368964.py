# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def bt(row, col, ind):
            if ind == len(word):
                return True
            if (0 > row or row >= len(board)) or (0 > col or col >= len(board[0])):
                return False
            x = board[row][col]
            if word[ind] != x:
                return False
            board[row][col] = '$'
            val = bt(row+1, col, ind+1) or bt(row, col+1,ind+1) or bt(row-1, col,ind+1) or bt(row,col-1,ind+1)
            if val:
                return True
            board[row][col] = x
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                start = (row, col)
                if bt(*start,0):
                    return True
        return False