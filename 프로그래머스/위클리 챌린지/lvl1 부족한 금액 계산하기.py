def solution(price, money, count):
    return max(price * sum(i for i in range(count+1)) - money, 0)
