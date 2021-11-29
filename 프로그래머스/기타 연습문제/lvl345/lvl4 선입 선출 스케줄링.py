"""
마지막 작업을 실행하기 1초 전의 시간의
남은 작업 수와 1초 후 작업을 받을 수 있는 코어의 번호를 구한 뒤
마지막 작업을 실행할 때 하나씩 할당
"""
def solution(n, cores):
    left, right = 0, 10000000
    number_of_jobs_processed = list()
    while left <= right:
        tm = (left + right) // 2
        number_of_jobs_processed = [tm // c + 1 for c in cores]
        if sum(number_of_jobs_processed) >= n:
            right = tm - 1
        else:
            left = tm + 1

    tm = left - 1  # 마지막 작업을 실행하기 1초 전의 시간
    return [i for i, v in enumerate([c - tm % c for c in cores]) if v == 1][n - sum([tm // c + 1 for c in cores]) - 1] + 1