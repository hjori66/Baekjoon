board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0

cards = set(board[0]) | set(board[1]) | set(board[2]) | set(board[3])
cards -= set([0])
print(cards)


