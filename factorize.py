import time
import multiprocessing
from multiprocessing import Pool, cpu_count

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_sync(numbers):
    start_time = time.time()
    result = [factorize(number) for number in numbers]
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Synchronous execution time: {execution_time} seconds")
    return result

def factorize_parallel(numbers):
    start_time = time.time()
    with Pool(processes=4) as pool:
        result = pool.map(factorize, numbers)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Parallel execution time: {execution_time} seconds")
    return result

def test_factorize():
    numbers = [128, 255, 99999, 10651060, 198765430, ]

    factorize_sync(numbers)
    factorize_parallel(numbers)

    print("Test passed!")

if __name__ == "__main__":
    test_factorize()
