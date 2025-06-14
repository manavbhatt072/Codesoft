import math

# Initialize the game board
board = [' ' for _ in range(9)]

def print_board():
    print("\n")
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
    print("\n")

def available_moves():
    return [i for i, spot in enumerate(board) if spot == ' ']

def make_move(position, player):
    board[position] = player

def is_winner(player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

def is_draw():
    return ' ' not in board and not is_winner('X') and not is_winner('O')

def minimax(depth, is_maximizing):
    if is_winner('O'):
        return 1
    if is_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves():
            board[move] = 'O'
            score = minimax(depth + 1, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves():
            board[move] = 'X'
            score = minimax(depth + 1, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = None
    for i in available_moves():
        board[i] = 'O'
        score = minimax(0, False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    return move

def main():
    print("Welcome to Tic-Tac-Toe! You are X and the AI is O.")
    print_board()

    while True:
        # Human turn
        while True:
            try:
                human_move = int(input("Enter your move (0-8): "))
                if board[human_move] == ' ':
                    make_move(human_move, 'X')
                    break
                else:
                    print("That spot is taken.")
            except (ValueError, IndexError):
                print("Invalid move. Enter a number from 0 to 8.")
        print_board()

        if is_winner('X'):
            print("You win! 🎉")
            break
        if is_draw():
            print("It's a draw!")
            break

        # AI turn
        print("AI is making a move...")
        ai_move = best_move()
        make_move(ai_move, 'O')
        print_board()

        if is_winner('O'):
            print("AI wins! 💻")
            break
        if is_draw():
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
