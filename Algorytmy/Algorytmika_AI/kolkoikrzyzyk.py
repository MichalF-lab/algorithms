import random
import copy

def board(n = 7):
    return [[0 for j in range(n)] for i in range(n)]

def possibility_move(board):
    n = len(board)
    moves = []
    # Dodaj ruchy do górnego wiersza
    for i in range(n):
        if board[0][i] == 0:
            moves.append((0, i))
    # Dodaj ruchy do reszty kolumn
    for i in range(1, n):
        for j in range(n):
            if board[i-1][j] in (1, -1) and board[i][j] == 0:
                moves.append((i, j))
    return moves


def check_win_11(tablica):
    """
    Sprawdza, czy gracz 1 (wartość 1) ma cztery symbole w linii.
    Przyjmuje tablicę 7x7 z wartościami 1, -1 i 0.
    """
    n = len(tablica)          # Rozmiar planszy (7)
    player = 1
    for i in range(n):
        for j in range(n):
            if tablica[i][j] == player:
                # Sprawdzenie poziomego ułożenia (w prawo)
                if j <= n-4 and all(tablica[i][j+k] == player for k in range(4)):
                    return True
                # Sprawdzenie pionowego ułożenia (w dół)
                if i <= n-4 and all(tablica[i+k][j] == player for k in range(4)):
                    return True
                # Sprawdzenie ukośnego ułożenia w dół-prawo
                if i <= n-4 and j <= n-4 and all(tablica[i+k][j+k] == player for k in range(4)):
                    return True
                # Sprawdzenie ukośnego ułożenia w górę-prawo
                if i >= 3 and j <= n-4 and all(tablica[i-k][j+k] == player for k in range(4)):
                    return True
    return False


def check_win_12(tablica):
    """
    Sprawdza, czy gracz 2 (wartość -1) ma cztery symbole w linii.
    Działa analogicznie do funkcji dla gracza 1, ale dla wartości -1.
    """
    n = len(tablica)          # Rozmiar planszy (7)
    player = -1
    for i in range(n):
        for j in range(n):
            if tablica[i][j] == player:
                # Sprawdzenie poziomego ułożenia (w prawo)
                if j <= n-4 and all(tablica[i][j+k] == player for k in range(4)):
                    return True
                # Sprawdzenie pionowego ułożenia (w dół)
                if i <= n-4 and all(tablica[i+k][j] == player for k in range(4)):
                    return True
                # Sprawdzenie ukośnego ułożenia w dół-prawo
                if i <= n-4 and j <= n-4 and all(tablica[i+k][j+k] == player for k in range(4)):
                    return True
                # Sprawdzenie ukośnego ułożenia w górę-prawo
                if i >= 3 and j <= n-4 and all(tablica[i-k][j+k] == player for k in range(4)):
                    return True
    return False

def full_board(board):
    for row in board:
        if 0 in row:
            return False
    return True


def play_random_game(board, who_move = 1):
    while True:
        #print(board)
        if check_win_11(board):
            #print("Player 1 wins")
            return 1
        if check_win_12(board):
            #print("Player 2 wins")
            return -1
        if full_board(board):
            return 0

        moves = possibility_move(board)
        if not moves:
            return 0
        move = random.choice(moves)
        board[move[0]][move[1]] = who_move

        if who_move == -1: who_move = 1
        elif who_move == 1: who_move = -1

        return play_random_game(board, who_move)

def random_games(board, who_move = 1):
    range_ = 140
    moves = possibility_move(board)
    tab_results = []
    for i in moves:
        tab = 0
        for _ in range(range_):
            current_board = copy.deepcopy(board)
            tab += play_random_game(current_board, who_move)

        if tab == -(range_ * who_move):
            if who_move == 1:
                priority = 99999     
            else:
                priority = -99999
            tab_results.append( (priority, i) )
        else:
            tab_results.append( (tab, i) )

    if who_move == 1:
        best = max(tab_results, key=lambda x: x[0])
    else:
        best = min(tab_results, key=lambda x: x[0])

    return best 


def move(board, move, who_move):
    new_board = copy.deepcopy(board)
    new_board[move[0]][move[1]] = who_move
    return new_board
    


def main_move(board, who_move = 1):
    moves = possibility_move(board)
    tab = []
    for i in moves:
        current_board = move(copy.deepcopy(board), i, who_move)
        score, move_ = random_games(current_board, who_move)
        tab.append( (score, i) )   # zapisujemy (wynik, ruch)

    if who_move == 1:
        best_score, best_move = max(tab, key=lambda x: x[0])
    else:
        best_score, best_move = min(tab, key=lambda x: x[0])
    
    if best_score == 99999 or best_score == -99999:
        return best_move 
    # -----------  bez tych linijek gra konczy sie szybciej
    temp = random_games(move(current_board,best_move,who_move), who_move*(-1))
    if temp[0] == 99999 or temp[0] == -99999:
        print("ZAGROZENIE")
        while True:
            best = random.choice(moves)
            if best != best_move:
                return best 
    # ---------------------------------------------------------
    return best_move 



a = board()
who_move = 1
for i in range(7*7):
    ext = main_move(a, who_move)
    print(f"Move {i+1}: Player {who_move} moves to {ext}")
    a = move(a, ext, who_move)
    if check_win_11(a):
        print("Player 1 wins!")
        break
    if check_win_12(a):
        print("Player 2 wins!")
        break
    who_move *= -1
for row in a:
    print(row)