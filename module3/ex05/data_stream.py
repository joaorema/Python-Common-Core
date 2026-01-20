import math
import sys
import random
import time

class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()
    def __str__(self):
        return repr(self.message)

def fibonacci(n):
    a, b = 0, 1
    while True:
        yield a
        a , b = b, a + b

def prime_nbr(sequence):
    for num in sequence:
        if num < 2:
            continue
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num




def create_data(nums):
    names = ["Alice", "Bob", "Charlie", "Thomas", "John", "Stacy", "Peter", "Michael"]
    actions = ["killed monster", "found treasure", "leveled up"]
    levels = range(1,20)
    for i in nums:
        name = random.choice(names)
        action = random.choice(actions)
        level = random.choice(levels)
        if action == "leveled up":
            level += 1
        yield name, level, action

def data_stream(amount):
    print(f"=== Data Stream Processor ===")
    nums = create_data(range(amount))

    print(f"Processing {amount} game events")
    high_level, treasure_counter ,level_counter = 0, 0, 0
    start_time = time.time()
    for i in range(amount):
        name, level, action = next(nums)
        print(f"Event {i+1}: {name} ({level}) {action}")
        if level > 10:
            high_level += 1
        if action == "found treasure":
            treasure_counter += 1
        if action == "leveled up":
            level_counter += 1
    print(f"=== Stream Analytics ===")
    print(f"Total events processed: {amount}")
    print(f"High level players (+10): {high_level}")
    print(f"Treasure Events: {treasure_counter}")
    print(f"Level-up events: {level_counter}")
    print(f"Memory usage: Constant ({sys.getsizeof(nums)} bytes)")
    print(f"Processing time: {time.time() - start_time:.3f} seconds")
    print(f"=== Generator Demo ===")
    value = fibonacci(range(10))
    primes = prime_nbr(range(12))
    final = []
    final_primes = []
    for i in range(1,10):
        result = next(value)
        final.append(result)
    for v in primes:
        final_primes.append(v)

    print(f"Fibonacci sequence (first 10): {final}")
    print(f"Prime numbers (first 5): {final_primes}")
if __name__ == "__main__":
    number = (input("Enter amount of game events: "))
    try:
        number = int(number)
        data_stream(number)
    except (NameError, CustomError, ValueError) as e:
        print(e)

    finally:
        pass