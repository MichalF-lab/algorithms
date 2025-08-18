import random
import time

def chess_board(n):
    return [[0 for j in range(n)] for i in range(n)]


def hetman_move(board, x, y):
    n = len(board)
    moves = []

    for i in range(n):
        if i != x:
            moves.append((i, y))
        if i != y:
            moves.append((x, i)) 

    for i in range(-n, n):
        if 0 <= x + i < n and 0 <= y + i < n and (i != 0):
            moves.append((x + i, y + i))  # Main diagonal
        if 0 <= x + i < n and 0 <= y - i < n and (i != 0):
            moves.append((x + i, y - i))  # Anti-diagonal

    moves.append((x,y))
    return moves


def hetman_posible_positions(board, i,j):
    if board[i][j] == 1:
        return False
    moves = hetman_move(board, i, j)
    if any(board[x][y] == 1 for x, y in moves):
        return False
    return True


def solve(board, actual_row = 0):
    n = len(board)
    for j in range(n):
        if hetman_posible_positions(board, actual_row, j):
            new_board = []
            for row in board:
                new_board.append(row[:])
            new_board[actual_row][j] = 1
            if actual_row + 1 == n:
                return new_board
            result = solve(new_board, actual_row + 1)
            if result: return result


#print(solve(chess_board(8)), flush=True)


def solve_permutation(board, actual_row = 0):
    n = len(board)
    permutations = 0
    for j in range(n):
        if hetman_posible_positions(board, actual_row, j):
            new_board = []
            for row in board:
                new_board.append(row[:])
            new_board[actual_row][j] = 1
            if actual_row + 1 == n:
                return 1
            permutations += solve_permutation(new_board, actual_row + 1)
    return permutations


#print(solve_permutation(chess_board(11)))

"""
Próba odopoweidzenia na pytanie ile pozyzji jest równoważnych

def solve_sym(board, actual_row = 0, hetman_count = 0):
    n = len(board)
    result = []
    for j in range(n):
        if hetman_posible_positions(board, actual_row, j):
            new_board = []
            for row in board:
                new_board.append(row[:])
            new_board[actual_row][j] = 1
            if hetman_count + 1 == n:
                return [new_board]
            ext = solve_sym(new_board, actual_row + 1, hetman_count + 1)
            if ext:
                result.extend(ext)
    return result

full_posibilty = solve_sym(chess_board(8))
posibilty = full_posibilty[:]

tab = []
n = len(full_posibilty[0])

# Tworzymy odwrócone pionowo plansze
for board in full_posibilty:
    temp = []
    for i in reversed(range(n)):
        temp.append(board[i][:])
    tab.append(temp)

# Konwertujemy plansze na tuple dla porównania
def board_to_tuple(board):
    return tuple(tuple(row) for row in board)

set1 = set(board_to_tuple(board) for board in full_posibilty)
set2 = set(board_to_tuple(board) for board in tab)

common_count = len(set1 & set2)
print(common_count)
"""



def random_solve(board, actual_row = 0):
    n = len(board)
    temp = list(range(n))
    random.shuffle(temp)
    for j in temp:
        if hetman_posible_positions(board, actual_row, j):
            new_board = [row[:] for row in board]
            new_board[actual_row][j] = 1
            if actual_row + 1 == n:
                return new_board
            result = random_solve(new_board, actual_row + 1)
            if result: return result

# Porównanie czasu działania funkcji random_solve i solve

# for i in range(3,22):
#     start_time = time.time()
#     a = random_solve(chess_board(i))
#     end_time = time.time()  # czas po wykonaniu operacji
#     elapsed_time = end_time - start_time 
#     print(i," ",elapsed_time, "sekundy")

#     start_time = time.time()
#     a = solve(chess_board(i))
#     end_time = time.time()  # czas po wykonaniu operacji
#     elapsed_time = end_time - start_time 
#     print(i," ",elapsed_time, "sekundy")

def bounded_gauss_random(mu=0.5, sigma=0.15):
    while True:
        x = random.gauss(mu, sigma)
        if 0 <= x < 1:
            return x

def random_solve_gauss1(board, actual_row = 0):
    n = len(board)
    temp = list(range(n))
    random.shuffle(temp, random=bounded_gauss_random)
    for j in temp:
        if hetman_posible_positions(board, actual_row, j):
            new_board = [row[:] for row in board]
            new_board[actual_row][j] = 1
            if actual_row + 1 == n:
                return new_board
            result = random_solve_gauss1(new_board, actual_row + 1)
            if result: return result
        #else: print(actual_row)

import numpy as np

def bounded_gauss_random2():
    x = np.clip(np.random.normal(0.5, 0.06), 0.00001,  0.999999)
    return x

def random_solve_gauss2(board, actual_row = 0):
    n = len(board)
    temp = list(range(n))
    random.shuffle(temp, random=bounded_gauss_random2)
    for j in temp:
        if hetman_posible_positions(board, actual_row, j):
            new_board = [row[:] for row in board]
            new_board[actual_row][j] = 1
            if actual_row + 1 == n:
                return new_board
            result = random_solve_gauss2(new_board, actual_row + 1)
            if result: return result

        

from concurrent.futures import ProcessPoolExecutor, TimeoutError
import time

global seed
seed = 64

def solve_and_measure(solve_func, board, seed_value):
    random.seed(seed_value)
    np.random.seed(seed_value)
    start_time = time.time()
    result = solve_func(board)
    end_time = time.time()
    return end_time - start_time if result else None

# import numpy as np
# from concurrent.futures import ProcessPoolExecutor, as_completed, TimeoutError
# import multiprocessing
# import os
# import signal

# def solve_and_measure_safe(func, board, seed):
#     """Wrapper z obsługą błędów dla funkcji solve_and_measure"""
#     try:
#         return solve_and_measure(func, board, seed)
#     except Exception as e:
#         print(f"Błąd w funkcji: {e}")
#         return None

# if __name__ == "__main__":
#     # Ważne dla Windows - ustaw sposób uruchamiania procesów
#     multiprocessing.set_start_method('spawn', force=True)
    
#     wynik1, wynik2, wynik3 = [], [], []
    
#     # Jeden ProcessPoolExecutor dla całego programu
#     for j in range(0, 1000): 
#         i = 120 # seed 65 i = 453
#         print(f"\nPrzetwarzanie planszy {i}... seed({seed + j})")
#         board = chess_board(i)
#         with ProcessPoolExecutor(max_workers=3) as executor:            
#             # Uruchom wszystkie 3 funkcje równolegle
#             tasks = [
#                 (executor.submit(solve_and_measure_safe, random_solve, board, seed + j), 1, "funkcja1"),
#                 (executor.submit(solve_and_measure_safe, random_solve_gauss1, board, seed + j), 1, "funkcja2"),
#                 (executor.submit(solve_and_measure_safe, random_solve_gauss2, board, seed + j), 1, "funkcja3")
#             ]
            
#             results = {1: None, 2: None, 3: None}
#             completed_count = 0
            
#             try:
#                 # Czekaj maksymalnie 20 sekund na wszystkie wyniki
#                 for future in as_completed([task[0] for task in tasks], timeout=20):
#                     # Znajdź które zadanie się ukończyło
#                     for task_future, func_num, func_name in tasks:
#                         if task_future == future:
#                             try:
#                                 elapsed = future.result()
#                                 if elapsed is not None:
#                                     results[func_num] = elapsed
#                                     print(f"{i} {func_name}: {elapsed:.2f}s")
#                                 else:
#                                     print(f"{i} {func_name}: ERROR")
#                                 completed_count += 1
#                                 break
#                             except Exception as e:
#                                 print(f"{i} {func_name}: EXCEPTION - {e}")
#                                 completed_count += 1
#                                 break
                        
                                
#             except TimeoutError:
#                 print(f"{i}: TIMEOUT po 10s - ukończono {completed_count}/3 funkcji")
                
#                 # Sprawdź które zadania się już ukończyły
#                 for task_future, func_num, func_name in tasks:
#                     if task_future.done() and results[func_num] is None:
#                         try:
#                             elapsed = task_future.result(timeout=0.1)  # Bardzo krótki timeout
#                             if elapsed is not None:
#                                 results[func_num] = elapsed
#                                 print(f"{i} {func_name}: {elapsed:.2f}s (ukończone przed timeout)")
#                         except:
#                             print(f"{i} {func_name}: TIMEOUT lub ERROR")
#                     elif not task_future.done():
#                         print(f"{i} {func_name}: NIEUKOŃCZONE (timeout)")
#             finally:
#                 # KLUCZOWE: Najpierw zabij procesy, potem zamknij executor
                
#                 # Zabij wszystkie procesy z puli
#                 if hasattr(executor, '_processes') and executor._processes:
#                     for pid, process in executor._processes.items():
#                         try:
#                             if process.is_alive():
#                                 process.terminate()  # Łagodne zakończenie
#                                 process.join(timeout=0.1)  # Czekaj krótko
#                                 if process.is_alive():
#                                     process.kill()  # Siłowe zabicie
#                         except:
#                             pass
                
#                 # Teraz zamknij executor
#                 executor.shutdown(wait=False, cancel_futures=True)
                

                
# # seed 65 i = 453