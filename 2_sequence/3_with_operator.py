# sequence with operator 

l = [1, 2, 3]
print(l*5)
print(5*'abcdef')

#caution 
print([[]] *3) # [[], [], []]


## make list of list 
board = [['_'] * 3 for i in range(3)] # each list element has each reference 
print(board)
board[1][2] = 'X'
print(board) # the result is [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]
print()

## caution : mutable object and its reference 
board = [['_'] *3] *3 # != line 11 (because each list element in line17 are reference same list)
print(board)
board[1][2] = 'X' # so the result is [['_', '_', 'X'], ['_', '_', 'X'], ['_', '_', 'X']]
print(board)

# line 11 is same with below 
board = [] 
for i in range(3):
    row = ['_']*3
    board.append(row)

# but line 18 is same with below 
row = ['_'] * 3
board = [] 
for i in range(3):
    board.append(row)
