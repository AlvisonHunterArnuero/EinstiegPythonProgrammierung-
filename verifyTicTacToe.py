import itertools
values_dict = {0:"Empty",1:"X",2:"O"}
board = [[0, 0, 1], [0, 1, 2],[0, 1, 0]]
result = ''
def is_solved(board):
    flatten_list = list(itertools.chain(*board))
    board = {str(i+1):str(elem) for i, elem in enumerate(flatten_list)}
    print('Current Board: \n',board)
    if board['7'] == board['8'] == board['9'] != ' ': # across the top
        result = board['7']
        print('Resultado es: ',result)
    elif board['4'] == board['5'] == board['6'] != ' ': # across the middle
        result = board['4']
        print('Resultado es: ',result)
    elif board['1'] == board['2'] == board['3'] != ' ': # across the bottom
        result = board['1']
        print('Resultado es: ',result)
    elif board['1'] == board['4'] == board['7'] != ' ': # down the left side
        result = board['1']
        print('Resultado es: ',result)
    elif board['2'] == board['5'] == board['8'] != ' ': # down the middle
        result = board['2']
        print('Resultado es: ',result)
    elif board['3'] == board['6'] == board['9'] != ' ': # down the right side
        result = board['3']
        print('Resultado es: ',result)
    elif board['7'] == board['5'] == board['3'] != ' ': # diagonal
        result = board['7']
        print('Resultado es: ',result)
    elif board['1'] == board['5'] == board['9'] != ' ': # diagonal
        result = board['1']
        print('Resultado es: ',result)
# Test the function
is_solved(board)

# # not yet finished
# board = [[0, 0, 1],[0, 1, 2],[2, 1, 0]]
# is_solved(board)
# # winning row
# board = [[1, 1, 1],[0, 2, 2],[0, 0, 0]]
# is_solved(board)
# # winning column
# board = [[2, 1, 2],[2, 1, 1],[1, 1, 2]]
# is_solved(board)
# # draw
# board = [[2, 1, 2],[2, 1, 1],[1, 2, 1]]
# is_solved(board)
