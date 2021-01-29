def convert(num, base):
    ret = str()
    while num:
        ret += str(hex(num % base)[2:]).upper()
        num //= base
    return ret[::-1]

def solution(n, t, m, p):
    answer = str()
    num = 0
    player = 1
    s_index = 0
    string = '0'
    while True:
        if s_index >= len(string):
            s_index = 0
            num += 1
            string = convert(num, n)

        if player == p:
            answer += string[s_index]
            if len(answer) == t:
                break

        s_index += 1
        player = player + 1 if player < m else 1

    return answer