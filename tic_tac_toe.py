from random import randrange

def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print(f"|   {board[row][col]}   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def enter_move(board):
    while True:
        move = input("Enter your move: ")
        if len(move) == 1 and '1' <= move <= '9':
            move = int(move) - 1
            row, col = divmod(move, 3)
            if board[row][col] not in ['O', 'X']:
                board[row][col] = 'O'                 
                break
            else:
                print("Field already occupied - repeat your input!")
        else:
            print("Bad move - repeat your input!")

def make_list_of_free_fields(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] not in ['O', 'X']]

def victory_for(board, sgn):
    who = 'me' if sgn == 'X' else 'you' if sgn == 'O' else None
    for rc in range(3):
        if all(board[rc][col] == sgn for col in range(3)) or all(board[row][rc] == sgn for row in range(3)):
            return who
    if all(board[rc][rc] == sgn for rc in range(3)) or all(board[rc][2 - rc] == sgn for rc in range(3)):
        return who
    return None

def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'

board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1] = 'X'
human_turn = True

while True:
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board, 'O')
    else:
        draw_move(board)
        victor = victory_for(board, 'X')
    if victor is not None or not make_list_of_free_fields(board):
        break
    human_turn = not human_turn

display_board(board)

if victor == 'you':
    print("You won!")
elif victor == 'me':
    print("I won")
else:
    print("Tie!")




                  



