class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        table = {
            "1" : 0,
            "2" : 0,
            "3" : 0,
            "4" : 0,
            "5" : 0,
            "6" : 0,
            "7" : 0,
            "8" : 0,
            "9" : 0
        }
        row = 0
        col = 0
        while row < 9:
            col = 0
            while col < 9:
                d_row = row
                d_col = col
                while d_row < row + 3:
                    d_col = col
                    while d_col < col + 3:
                        if board[d_row][d_col] in table:
                            table[board[d_row][d_col]] += 1
                        d_col += 1
                    d_row += 1
                for n in table:
                    if table[n] > 1:
                        return False
                    else:
                        table[n] = 0
                col += 3
            row += 3
        row = 0
        col = 0
        while row < 9:
            col = 0
            while col < 9:
                if board[col][row] in table:
                    table[board[col][row]] += 1
                col += 1
            for n in table:
                if table[n] > 1:
                    return False
                else:
                    table[n] = 0
            row += 1
        row = 0
        col = 0
        while row < 9:
            col = 0
            while col < 9:
                if board[row][col] in table:
                    table[board[row][col]] += 1
                col += 1
            for n in table:
                if table[n] > 1:
                    return False
                else:
                    table[n] = 0
            row += 1
        return True