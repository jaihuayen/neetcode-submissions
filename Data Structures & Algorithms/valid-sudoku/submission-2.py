class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowhash = defaultdict(set)
        colhash = defaultdict(set)
        squarehash = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rowhash[i]
                   or board[i][j] in colhash[j]
                   or board[i][j] in squarehash[i // 3, j // 3]):
                   return False
                
                colhash[j].add(board[i][j])
                rowhash[i].add(board[i][j])
                squarehash[i // 3, j // 3].add(board[i][j])
        return True