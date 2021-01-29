def solution(s):
    count = 0
    zero = 0
    while s != '1':
        count += 1
        zero += s.count('0')
        s = s.replace('0', '')
        s = str(bin(len(s))[2:])
    return [count, zero]