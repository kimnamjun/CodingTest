def solution(n):
    def subtask(left, right):
        if left == n:
            return 1
        if left == right:
            return subtask(left + 1, right)
        return subtask(left + 1, right) + subtask(left, right + 1)

    return subtask(0, 0)