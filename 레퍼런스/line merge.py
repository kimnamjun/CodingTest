# 라인 합하기
# 프로그래머스 문제 중 '광고 시간'의 예시

# 시청 시간이 다음과 같을 때, 시간별 view는 어떻게 되는가?
views = [[4815, 6314], [2431, 3600], [1550, 2909], [5459, 6809], [5864, 7350]]
print('views :', views)
# views : [[4815, 6314], [2431, 3600], [1550, 2909], [5459, 6809], [5864, 7350]]

# 시청 시간이 변화하는 순간 확인
# 시청 시작 = 시청자 수 1 증가, 시청 끝 = 시청자 수 1 감소
lines_dict = dict()
for left, right in views:
    lines_dict[left] = lines_dict.get(left, 0) + 1
    lines_dict[right] = lines_dict.get(right, 0) - 1

# 시간에 따른 시청자 수 변화
lines_list = sorted(lines_dict.items())
print('lines list :', lines_list)
# lines list : [(1550, 1), (2431, 1), (2909, -1), (3600, -1), (4815, 1), (5459, 1), (5864, 1), (6314, -1), (6809, -1), (7350, -1)]

# 변화량을 바탕으로 시청자 수 계산
height = 0
lines = list()
for idx in range(len(lines_dict) - 1):
    height += lines_list[idx][1]
    lines.append([lines_list[idx][0], lines_list[idx + 1][0], height])
print('lines :', lines_list)
# lines : [(1550, 1), (2431, 1), (2909, -1), (3600, -1), (4815, 1), (5459, 1), (5864, 1), (6314, -1), (6809, -1), (7350, -1)]