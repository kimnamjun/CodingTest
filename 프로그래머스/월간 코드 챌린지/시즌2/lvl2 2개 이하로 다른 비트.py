def solution(numbers):
    answer = list()
    for number in numbers:
        binary = list(bin(number)[2:])
        zero, one = -1, -1
        for idx, val in enumerate(binary):
            if val == '0':
                zero = idx
                one = -1
            elif val == '1' and one == -1:
                one = idx

        if zero == -1:
            binary = ['1', '0'] + binary[1:]
        else:
            binary[zero] = '1'
            if zero < one:
                binary[one] = '0'
        answer.append(sum(int(val) * 2 ** idx for idx, val in enumerate(''.join(binary)[::-1])))

    return answer