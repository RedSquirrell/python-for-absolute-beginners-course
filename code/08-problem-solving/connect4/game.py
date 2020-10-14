# Maak een bord
# kies eerste speler
# totdat iemand wint
#   laat bord zien
#   kies locatie, markeer het
#   toggle active player

import random
from typing import List, Optional


def main():
    # MAAK HET BORD
    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
    ]

    # KIES EEN SPELER
    active_player_index = 0
    players = ["Bart", "Computer"]
    symbols = ["X", "O"]
    player = players[active_player_index]

    while not find_winner(board):
        # LAAT HET BORD ZIEN
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)

        if not choose_location(board, symbol, active_player_index == 1):
            print("Dit is niet een juiste input, probeer opnieuw.")
            continue

        # Verander van speler
        active_player_index = (active_player_index + 1) % len(players)

    print()
    print(f"GAME OVER! {player} has won with the board: ")
    print()
    show_board(board)


def choose_location(board, symbol, is_computer):
    if not is_computer:
        column = int(input("Kies een kollom: "))
    else:
        column = random.randint(1, len(board[0]))
        print(f"Computer chooses column {column}")

    column -= 1

    if column < 0 or column >= len(board[0]):
        return False

    row = 5
    cell = board[row][column]

    while cell is not None:
        row -= 1
        if row < 0:
            return False

        cell = board[row][column]

    board[row][column] = symbol
    return True


def show_board(board):
    for row in board:
        print("|", end=' ')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=" | ")
        print()
    return False

    # for row_idx, row in enumerate(board, start=1):
    #     print("| ", end='')
    #     for col_idx, cell in enumerate(row, start=1):
    #         empty_text = f"({row_idx}, {col_idx})"
    #         symbol = f'  {cell}   ' if cell is not None else empty_text
    #         print(symbol, end=" | ")
    #     print()


def announce_turn(player):
    print()
    print(f"It's {player}'s turn. Here's the board: ")
    print()


def find_winner(board):
    sequences = get_winning_sequences(board)

    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True


def get_winning_sequences(board):
    sequences = []

    # Win in regels
    rows = board

    for row in rows:
        fours_across = find_sequences_of_four_cells_in_a_row(row)
        sequences.extend(fours_across)

    # Win in kolommen
    for col_idx in range(0, 7):
        col = [
            board[0][col_idx],
            board[1][col_idx],
            board[2][col_idx],
            board[3][col_idx],
            board[4][col_idx],
            board[5][col_idx],
        ]

        fours_down = find_sequences_of_four_cells_in_a_row(col)
        sequences.extend(fours_down)

    diagonals = [
        # Down to the right diagonals
        [board[5][0]],  # Not really used, too short, but here for building the pattern
        [board[4][0], board[5][1]],  # Not really used, too short, but here for building the pattern
        [board[3][0], board[4][1], board[5][2]],  # Not really used, too short, but here for building the pattern
        [board[2][0], board[3][1], board[4][2], board[5][3]],
        [board[1][0], board[2][1], board[3][2], board[4][3], board[5][4]],
        [board[0][0], board[1][1], board[2][2], board[3][3], board[4][4], board[5][5]],
        [board[0][1], board[1][2], board[2][3], board[3][4], board[4][5], board[5][6]],
        [board[0][2], board[1][3], board[2][4], board[3][5], board[4][6]],
        [board[0][3], board[1][4], board[2][5], board[3][6]],
        [board[0][4], board[1][5], board[2][6]],  # Not really used, too short, but here for building the pattern
        [board[0][5], board[1][6]],  # Not really used, too short, but here for building the pattern
        [board[0][6]],  # Not really used, too short, but here for building the pattern

        # Down to the left diagonals
        [board[0][0]],  # Not really used, too short, but here for building the pattern
        [board[0][1], board[1][0]],  # Not really used, too short, but here for building the pattern
        [board[2][0], board[1][1], board[0][2]],  # Not really used, too short, but here for building the pattern
        [board[0][3], board[1][2], board[2][1], board[3][0]],
        [board[0][4], board[1][3], board[2][2], board[3][1], board[4][0]],
        [board[0][5], board[1][4], board[2][3], board[3][2], board[4][1], board[5][0]],
        [board[0][6], board[1][5], board[2][4], board[3][3], board[4][2], board[5][1]],
        [board[1][6], board[2][5], board[3][4], board[4][3], board[5][2]],
        [board[2][6], board[3][5], board[4][4], board[5][3]],
        [board[3][6], board[4][5], board[5][4]],  # Not really used, too short, but here for building the pattern
        [board[4][6], board[5][5]],  # Not really used, too short, but here for building the pattern
        [board[5][6]],  # Not really used, too short, but here for building the pattern
    ]

    for diag in diagonals:
        fours_diagonals = find_sequences_of_four_cells_in_a_row(diag)
        sequences.extend(fours_diagonals)

    return sequences


def find_sequences_of_four_cells_in_a_row(cells: List[str]):
    sequences = []

    for n in range(0, len(cells) - 3):
        candidate = cells[n:n + 4]
        if len(candidate) == 4:
            sequences.append(candidate)

    return sequences


if __name__ == '__main__':
    main()
