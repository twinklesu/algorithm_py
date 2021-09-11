from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    report_id_dict = defaultdict(list)
    reported_dict = defaultdict(int)
    for r in report:
        reporting, reported = r.split(" ")
        if reported not in report_id_dict[reporting]:
            reported_dict[reported] += 1
            report_id_dict[reporting].append(reported)

    for id in id_list:
        count = 0
        if id in report_id_dict:
            for reported_id in report_id_dict[id]:
                if reported_dict[reported_id] >= k:
                    count += 1
        answer.append(count)
    return answer