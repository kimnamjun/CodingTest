import json
import requests

# setting
x_auth_token = 'b59556753d81ab3c233922014edb21b2'
base_url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
init_headers = {
    'X-Auth-Token': x_auth_token,
    'Content-Type': 'application/json'
}
init_data = '{"problem": 2}'
init = requests.post(f'{base_url}/start', headers=init_headers, data=init_data)
auth_key = init.json()['auth_key']
headers = {
    'Authorization': auth_key,
    'Content-Type': 'application/json'
}

# answer code
users_pred_score = {i+1: 40000 for i in range(900)}  # 유저별 예측 점수

for minute in range(596):
    print(f'\rtime: {minute}', end='')

    game_result = requests.get(f'{base_url}/game_result', headers=headers).json()
    for result in game_result['game_result']:
        winner, loser, taken = result['win'], result['lose'], result['taken']
        diff = (40 - taken) * 99000 / 35
        prob = users_pred_score[loser] / (users_pred_score[winner] + users_pred_score[loser])
        if prob > 0.5 and taken <= 10:  # 어뷰징 의심 : 패자가 예측 점수상 이길 확률이 높은데 빨리 지는 경우
            users_pred_score[winner] += diff * prob / 10  # 이긴 쪽도 불완전한 승부였으므로 승점에 패널티
        else:
            users_pred_score[winner] += diff * prob / 2
            users_pred_score[loser] -= diff * prob / 2
        users_pred_score[winner] = min(users_pred_score[winner], 100000)
        users_pred_score[loser] = max(users_pred_score[loser], 1000)

    if minute == 595:
        grades = sorted(users_pred_score, key=lambda x: users_pred_score[x])
        json_arr = [{"id": user, "grade": rank} for rank, user in enumerate(grades)]
        data = '{"commands":' + json.dumps(json_arr) + '}'
        requests.put(f'{base_url}/change_grade', headers=headers, data=data)

    waiting_line = requests.get(f'{base_url}/waiting_line', headers=headers).json()
    match_list = [user['id'] for user in waiting_line['waiting_line']]
    match_list = sorted(match_list, key=lambda x: users_pred_score[x])

    json_arr = [[match_list[i*2], match_list[i*2+1]] for i in range(len(match_list) // 2)]
    data = '{"pairs":' + json.dumps(json_arr) + '}'
    requests.put(f'{base_url}/match', headers=headers, data=data)

print('\n', requests.get(f'{base_url}/score', headers=headers).json())