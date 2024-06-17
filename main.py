import random

play = True


def print_board(board):
    for row in range(3):
        for col in range(3):
            if col < 2:
                print(f" {board[row][col] if board[row][col] != '' else ' '} |", end="")
            else:
                print(f" {board[row][col] if board[row][col] != '' else ' '}", end="")
        if row < 2:
            print("\n-----------")
    print("\n")


def initialize(player):
    shape = input(f"Player {player}, choose your shape (X, O): ").upper()
    while shape not in ["X", "O"]:
        print("Wrong shape!")
        shape = input(f"Player {player}, choose your shape (X, O): ").upper()

    if player == 1:
        players = {
            1: {'shape': shape, 'score': 0},
            2: {'shape': "O" if shape == "X" else "X", 'score': 0}
        }
    else:
        players = {
            1: {'shape': "O" if shape == "X" else "X", 'score': 0},
            2: {'shape': shape, 'score': 0}
        }

    return players


def game(player, players):
    winner = False
    tie = False

    print_board(board)
    while not (winner or tie):
        while True:
            try:
                row = int(input(f"Player {player}, enter the row (1, 2, 3): ")) - 1
                col = int(input(f"Player {player}, enter the column (1, 2, 3): ")) - 1

                if (row or col) not in range(3):
                    print("The coordinates are out of bound! Try again.")
                elif board[row][col] != '':
                    print("Cell already occupied! Try again.")
                else:
                    board[row][col] = players[player]['shape']
                    break
            except ValueError:
                print("Invalid input! Please enter numbers between 1 and 3.")

        print_board(board)

        winner = check_win(board, players, player)
        if winner:
            print(f'Player {player} wins!')
            players[player]['score'] += 1
        else:
            tie = check_tie(board)
            if tie:
                print("It's a tie!")

        # Change to the other player
        if not winner and not tie:
            player = 1 if player == 2 else 2

    return player if winner else None


def check_win(board, players, player):
    # Checks if there is a winner

    # Checks rows
    for row in board:
        if all([spot == players[player]['shape'] for spot in row]):
            return True

    # Checks columns
    for col in range(3):
        if all([board[row][col] == players[player]['shape'] for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == players[player]['shape'] for i in range(3)]):
        return True
    if all([board[i][2 - i] == players[player]['shape'] for i in range(3)]):
        return True

    return False


def check_tie(board):
    # Check if all cells are filled
    for row in board:
        if '' in row:
            return False
    return True


# First game starts with a random player
starting_player = random.randint(1, 2)
print(f"Player {starting_player} starts!")
players = initialize(starting_player)

while play:
    board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]

    print(f"Player {starting_player} starts!")
    winner = game(starting_player, players)

    # Display scores
    print("Scores:")
    for player in players:
        print(f"Player {player} ({players[player]['shape']}): {players[player]['score']}")

    keep_playing = input("Do you want to start again? y/n: ").lower()
    if keep_playing == 'y':
        # Set the next starting player to the winner of the previous game
        if winner is not None:
            starting_player = winner
        else:
            # If it was a tie, start with a random player
            starting_player = random.randint(1, 2)
        play = True
    else:
        play = False
