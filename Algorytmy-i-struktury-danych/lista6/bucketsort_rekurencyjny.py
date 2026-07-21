import time
import numpy
import random

def COIN_CHANGING(nominals, value):
    ext = []
    for coin in nominals:
        while(value != 0):
            if value >= coin: 
                ext.append(coin)
                value -= coin
            else: break
    return len(ext)

#print(COIN_CHANGING([10,5,2,1],27))

def DYNAMIC_COIN_CHANGING(nominaly, kwota):
    result = [float('inf')] * (kwota + 1)
    result[0] = 0

    for i in range(1, len(nominaly) + 1):
        for j in range(nominaly[i - 1], kwota + 1):
            result[j] = min(result[j], 1 + result[j - nominaly[i - 1]])

    return result[kwota]



def generate_schedule_data(n):
    activities = [(random.uniform(0, 24), 0) for _ in range(n)]
    
    for i in range(n):
        activities[i] = (activities[i][0], activities[i][0] + random.uniform(1, 5))

    activities.sort(key=lambda x: x[1])

    s, f = zip(*activities)

    return s, f



def dynamic_activity_selector(start_times, end_times):
    n = len(start_times)
    activities = [(0, 0)] + list(zip(start_times, end_times))
    activities.sort(key=lambda x: x[1])
    
    opt = [0] * (n + 1)
    
    for j in range(1, n + 1):
        opt[j] = max(opt[j - 1], activities[j][0] + opt[find_latest_compatible(activities, j)])
    
    return opt

def find_latest_compatible(activities, j):
    for i in range(j - 1, 0, -1):
        if activities[i][1] <= activities[j][0]:
            return i
    return 0

def RECURSIVE_ACTIVITY_SELECTOR(start_times, end_times, k, n):
    m = k + 1
    while m <= n and start_times[m] < end_times[k]:
        m += 1
    if m <= n:
        return [m] + RECURSIVE_ACTIVITY_SELECTOR(start_times, end_times, m, n)
    else:
        return []

def ACTIVITY_SELECTOR(start_times, end_times):
    n = len(start_times)
    selected = [1]
    k = 1
    for m in range(2, n):
        if m <= n and start_times[m] >= end_times[k]:
            selected.append(m)
            k = m
    return selected

if __name__ =='__main__':
    # Przykład danych dla których lepszy jest algorytm dynamiczny
    print(DYNAMIC_COIN_CHANGING([100, 50, 20, 1], 260))
    print(COIN_CHANGING([100, 50, 20, 1], 260))


    n = 10
    start_times, end_times = generate_schedule_data(n)

    print("Czasy rozpoczęcia zajęć:", start_times)
    print("Czasy zakończenia zajęć:", end_times)

    n = 20000
    start_times, end_times = generate_schedule_data(n)

    # Pomiar czasu dla algorytmu dynamicznego
    start_time = time.time()
    dynamic_result = dynamic_activity_selector(start_times, end_times)
    dynamic_time = time.time() - start_time

    # Pomiar czasu dla algorytmu rekurencyjnego
    start_time = time.time()
    recursive_result = RECURSIVE_ACTIVITY_SELECTOR([0] + list(start_times), [0] + list(end_times), 0, n)
    recursive_time = time.time() - start_time

    # Pomiar czasu dla algorytmu iteracyjnego
    start_time = time.time()
    iterative_result = ACTIVITY_SELECTOR(list(start_times), list(end_times))
    iterative_time = time.time() - start_time

    print("Dynamiczny Czas:", dynamic_time)
    print("Rekurencyjny Czas:", recursive_time)
    print("Iteracyjny Czas:", iterative_time)
