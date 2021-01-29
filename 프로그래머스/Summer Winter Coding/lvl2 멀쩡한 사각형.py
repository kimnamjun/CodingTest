# 1행과 1열에 수직선, 수평선 그어놓고, 대각선이 지나면 그 선 끌어쓰는 느낌
from math import gcd
def solution(w, h):
    return w * h - w - h + gcd(w, h)