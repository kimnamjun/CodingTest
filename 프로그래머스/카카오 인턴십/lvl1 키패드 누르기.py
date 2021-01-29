def get_distance(position, target):
    return abs(position // 3 - target // 3) + abs(position % 3 - target % 3)

def solution(numbers, hand):
    answer = str()
    left, right = 9, 11
    hand_adv = -0.5 if hand == 'left' else 0.5
    
    for num in numbers:
        number = num - 1 if num else 10
        if number % 3 == 0:
            left = number
            answer += 'L'
        elif number % 3 == 2:
            right = number
            answer += 'R'
        else:
            if get_distance(left, number) - get_distance(right, number) + hand_adv < 0:
                left = number
                answer += 'L'
            else:
                right = number
                answer += 'R'
    return answer