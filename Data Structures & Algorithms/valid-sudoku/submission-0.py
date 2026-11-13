class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowhash = defaultdict(set)
        colhash = defaultdict(set)
        squarehash = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rowhash[r] or
                    board[r][c] in colhash[c] or
                    board[r][c] in squarehash[(r // 3, c // 3)]):
                    return False
                rowhash[r].add(board[r][c])
                colhash[c].add(board[r][c])
                squarehash[(r // 3, c // 3)].add(board[r][c])
        return True