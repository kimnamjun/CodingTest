def solution(n):
    binary = format(n, 'b')

    if binary.find('0') == -1:
        return int('10' + binary[1:], 2)

    cnt = -1
    for b in range(len(binary)-1, -1, -1):
        if cnt == -1 and binary[b] == '1':
            cnt = 0
        elif cnt != -1 and binary[b] == '1':
            cnt += 1
        elif cnt != -1 and binary[b] == '0':
            binary = binary[:b] + '1' + '0' * (len(binary) -b -cnt -1) + '1' * cnt
            break
        if b == 0:
            binary = '1' + '0' * (len(binary) - b - cnt) + '1' * cnt

    return int(binary, 2)