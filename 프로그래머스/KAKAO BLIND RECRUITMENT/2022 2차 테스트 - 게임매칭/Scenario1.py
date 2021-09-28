import json
import requests

# setting
x_auth_token = 'b59556753d81ab3c233922014edb21b2'
base_url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
init_headers = {
    'X-Auth-Token': x_auth_token,
    'Content-Type': 'application/json'
}
init_data = '{"problem": 1}'
init = requests.post(f'{base_url}/start', headers=init_headers, data=init_data)
auth_key = init.json()['auth_key']
headers = {
    'Authorization': auth_key,
    'Content-Type': 'application/json'
}

# answer code
users_pred_score = {i+1: 40000 for i in range(30)}  # 유저별 예측 점수
match_count = {i+1: 9 for i in range(30)}  # 매칭 횟수 (9부터 시작)

for minute in range(596):  # 진행 시간
    print(f'\rtime: {minute}', end='')

    # 게임 결과를 이용하여 예측 점수를 변동시킴
    game_result = requests.get(f'{base_url}/game_result', headers=headers).json()
    for result in game_result['game_result']:
        winner, loser, taken = result['win'], result['lose'], result['taken']
        match_count[winner] += 1
        match_count[loser] += 1
        diff = (40 - taken) * 99000 / 35  # 예상 실력 차이
        prob = users_pred_score[loser] / (users_pred_score[winner] + users_pred_score[loser])  # 승리 확률에 따른 가중치
        users_pred_score[winner] += diff * prob * (20 / match_count[loser])  # 매칭 횟수가 적으면 데이터가 부족하므로 빠르게 변화
        users_pred_score[loser] -= diff * prob * (20 / match_count[loser])
        users_pred_score[winner] = min(users_pred_score[winner], 100000)
        users_pred_score[loser] = max(users_pred_score[loser], 1000)

    # 마지막에는 등수에 따라 등급 부여
    if minute == 595:
        grades = sorted(users_pred_score, key=lambda x: users_pred_score[x])
        json_arr = [{"id": user, "grade": rank} for rank, user in enumerate(grades)]
        data = '{"commands":' + json.dumps(json_arr) + '}'
        requests.put(f'{base_url}/change_grade', headers=headers, data=data)

    # 대기 중인 유저를 예측 점수에 따라 정렬
    waiting_line = requests.get(f'{base_url}/waiting_line', headers=headers).json()
    match_list = [user['id'] for user in waiting_line['waiting_line']]
    match_list = sorted(match_list, key=lambda x: users_pred_score[x])

    # 인접한 유저끼리 바로 매칭
    json_arr = [[match_list[i*2], match_list[i*2+1]] for i in range(len(match_list) // 2)]
    data = '{"pairs":' + json.dumps(json_arr) + '}'
    requests.put(f'{base_url}/match', headers=headers, data=data)

print('\n', requests.get(f'{base_url}/score', headers=headers).json())