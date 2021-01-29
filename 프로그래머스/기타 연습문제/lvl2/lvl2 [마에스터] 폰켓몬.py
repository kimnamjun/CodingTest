def solution(nums):
    answer = 0
    count = list()
    for num in nums:
        if num not in count:
            answer += 1
            count.append(num)    
    return min(answer, len(nums) // 2)