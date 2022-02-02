from collections import defaultdict

def solution(fees, records):
    base_time, base_fee, add_time, add_fee = fees

    answer = list()
    table = defaultdict(int)
    isin_park = dict()

    for record in records:
        t, car, io = record.split()
        t2 = int(t[:2]) * 60 + int(t[3:])
        if io == 'IN':
            table[car] -= t2
            isin_park[car] = 1
        elif io == 'OUT':
            table[car] += t2
            isin_park[car] = 0

    for car in isin_park:
        if isin_park[car]:
            table[car] += 24 * 60 - 1

    for car, time in table.items():
        fee = base_fee
        if time > base_time:
            fee += ((time - base_time - 1) // add_time + 1) * add_fee
        answer.append([car, fee])

    return list(map(lambda x: x[1], sorted(answer)))