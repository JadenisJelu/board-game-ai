import random
from copy import deepcopy

# variables definition
rows = 6
cols = 6
mines = 0

# check number of mines
if mines > rows*cols:
    raise ValueError("Mines = {} is too large".format(mines))

# board initialisation
board_ori = [[0 for i in range(cols)] for j in range(rows)]
#print("board ori")
#[print (i) for i in board_ori]


# dup board with mines
board_mines = deepcopy(board_ori)

# generate board with mines
def mines_generation(mines):
    ls = []
    # generate random 
    for _ in range(mines):
        # data structure problem
        ls.append((random.randint(0, rows-1),random.randint(0, cols-1)))
    # check distinct
    if len(ls) > len(set(ls)):
        new_ls = mines_generation(mines)
    else:
        new_ls = ls
    # generate board with mines
    for sets in new_ls:
        a, b = sets
        board_mines[a][b] = 1
    return new_ls

mines_generation(mines)

#print("board mines")
#[print (i) for i in board_mines]


# check mine
def mine_check(board, x, y):
    ls = []
    for a,b in [i for i in [(x-1,y-1), (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1), (x,y+1), (x-1, y+1), (x-1, y)]]:
        if a < 0 or b < 0:
            pass
        else:
            try:
                j = board[a][b]
            except IndexError:
                j = 0
            ls.append(j)
    return sum(ls)

# mine_check checker
#print(mine_check(board_mines, 4, 4))

answer_board = deepcopy(board_ori)
# [print (i) for i in answer_board]

# mine_check checker
#print(mine_check(board_mines, 0, 0))

# check mines
for i in range(rows):
    for j in range(cols):
        if board_mines[i][j] != 1:
            answer_board[i][j] = mine_check(board_mines, i, j)
        else: 
            answer_board[i][j] = "x"

#print("board answer")
#[print (i) for i in answer_board]

def key_input(dic, x, y):
    dic[(x, y)] = []
    for i in [(x-1,y-1), (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1), (x,y+1), (x-1, y+1), (x-1, y)]:
        a , b = i
        if a < 0 or b < 0:
            continue
        if i not in visited:
            dic[(x, y)].append(i)
    return None

# depth first search for non-0
visited = []
stack = []

def dfs(board, x, y, rows, cols):
    visited.append((x,y))
    stack.append((x,y))

    # key error cause dic is not inputed recursively
    dic = {
        (x,y):[(x-1,y-1), (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1), (x,y+1), (x-1, y+1), (x-1, y)]
    }
       
    while stack:
        s = stack.pop(0)
        print(s)
        print(stack)
        
        if s not in dic.keys():
            a, b = s
            key_input(dic, a, b)
        
        for neighbour in dic[s]:
            a, b = neighbour
            if neighbour not in visited and a < rows and b < cols:
                visited.append(neighbour)
                stack[0:0] = [neighbour]
        

dfs(answer_board, 3,3, rows, cols)