def convert_base_x(number: int, x: int) -> str:
    ret = str()
    while number:
        ret += str(number % x)
        number //= x
    return ret[::-1]

def is_prime_number(x):
    if x == 1:
        return 0
    for i in range(2, int(x ** (1/2)) + 1):
        if x % i == 0:
            return 0
    return 1

def solution(n, k):
    answer = 0
    number = convert_base_x(n, k)
    n_split = number.split('0')
    for num in n_split:
        if num:
            answer += is_prime_number(int(num))
    return answer