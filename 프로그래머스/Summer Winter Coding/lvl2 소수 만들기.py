from math import sqrt
from itertools import combinations


def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            return False
    return True


def solution(nums):
    lst = [p[0] + p[1] + p[2] for p in combinations(nums, 3)]
    answer = sum([1 for l in lst if is_prime_number(l)])
    return answer