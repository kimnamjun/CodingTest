def solution(arr, divisor):
    b = sorted([a for a in arr if not a % divisor])
    return b if b else [-1]