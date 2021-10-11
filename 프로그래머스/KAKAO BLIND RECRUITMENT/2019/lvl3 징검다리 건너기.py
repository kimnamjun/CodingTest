def solution(stones, k):
    left, right = 0, 200000000
    while left <= right:
        mid = (left + right) // 2

        temp_stones = [stone - mid for stone in stones]
        stone_index = [-1] + [index for index, stone in enumerate(temp_stones) if stone > 0] + [len(stones)]

        for i in range(len(stone_index) - 1):
            if stone_index[i + 1] - stone_index[i] > k:
                right = mid - 1
                break
        else:
            left = mid + 1

    return left