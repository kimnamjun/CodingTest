from copy import deepcopy
from itertools import permutations

def solution(expression):
    original_equation = list()
    num = 0
    for s in expression:
        if '0' <= s <= '9':
            num = (num * 10) + int(s)
        else:
            original_equation.append(num)
            original_equation.append(s)
            num = 0
    original_equation.append(num)

    answer = 0
    for operator_order in permutations('+-*'):
        equation = deepcopy(original_equation)
        for operator in operator_order:
            idx = 1
            while idx < len(equation):
                if equation[idx] == operator:
                    equation[idx-1] = eval(f'{equation[idx-1]}{operator}{equation[idx+1]}')
                    equation.pop(idx+1)
                    equation.pop(idx)
                else:
                    idx += 2
        answer = max(answer, abs(equation[0]))
    
    return answer