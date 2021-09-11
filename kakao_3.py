from collections import defaultdict
from math import ceil

def solution(fees, records):
    answer = []
    acc_time = defaultdict(int)
    in_car_dict = dict()
    for r in records:
        time, num, state = r.split(" ")
        if state == "IN":
            in_car_dict[num] = time
        else:
            in_time = in_car_dict.pop(num)
            startH, startM = map(int, in_time.split(':'))
            endH, endM = map(int, time.split(':'))
            parked_time = (endH*60 + endM) - (startH*60 + startM)
            acc_time[num] += parked_time
    for car in in_car_dict:
        in_time = in_car_dict[car]
        startH, startM = map(int, in_time.split(':'))
        parked_time = (23*60 + 59) - (startH*60 + startM)
        acc_time[car] += parked_time

    for car in sorted(acc_time):
        time = acc_time[car]
        cost = fees[1] # default cost
        if time > fees[0]:
            cost += ceil((time - fees[0]) / fees[2]) * fees[3]
        answer.append(cost)
    return answer