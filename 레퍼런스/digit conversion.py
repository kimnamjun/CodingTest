def convert_base_x(number:int, x: int) -> str:
    ret = str()
    while number:
        ret += str(number % x)
        number //= x
    return ret[::-1]


def convert_base_10_from_x(number_s: str, x: int) -> int:
    ret = 0
    for i, n in enumerate(number_s[::-1]):
        ret += int(n) * x ** i
    return ret


print(convert_base_x(17, 3))
print(convert_base_10_from_x('122', 3))