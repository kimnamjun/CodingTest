from math import sqrt
from itertools import permutations

def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    lst = list()
    for i in range(len(numbers)):
        lst.extend(map(lambda x: int(''.join(x)), permutations(numbers, i+1)))

    answer = sum([1 for l in set(lst) if is_prime_number(l)])
    return answer