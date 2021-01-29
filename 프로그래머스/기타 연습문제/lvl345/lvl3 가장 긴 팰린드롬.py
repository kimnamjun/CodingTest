def solution(s):
    answer = 1
    for idx in range(len(s)):
        start, end, length_odd = idx-1, idx+1, 1
        while start >= 0 and end < len(s):
            if s[start] == s[end]:
                start -= 1
                end += 1
                length_odd += 2
            else:
                break

        start, end, length_even = idx, idx + 1, 0
        while start >= 0 and end < len(s):
            if s[start] == s[end]:
                start -= 1
                end += 1
                length_even += 2
            else:
                break
        answer = max(answer, length_odd, length_even)
    return answer