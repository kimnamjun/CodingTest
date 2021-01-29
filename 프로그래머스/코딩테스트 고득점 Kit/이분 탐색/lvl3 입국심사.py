def solution(n, times):
    left = 1
    right = n * max(times) // len(times)
    mid = (left + right) // 2
    
    while left <= right:
        ans = 0
        for time in times:
            ans += mid // time

        if ans < n:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2
        
    return mid + 1