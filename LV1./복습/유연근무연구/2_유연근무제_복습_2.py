def solution(schedules, timelogs, startday):

    answer = 0
    result = []

    start_day_set = startday

    for log in timelogs:
        for time in schedules:
            # time  => 직원의 희망 시간

            time_late = time + 10  # 직원들 이 시간 보다 늦으면 지각임
            result_p = []
            startday = start_day_set

            for log_real in log:
                if startday == 6 or startday == 7:
                    result_p.append("O")
                    startday += 1
                    continue
                else:
                    if log_real <= time_late:
                        result_p.append("O")
                    else:
                        result_p.append("X")
                    startday += 1

            if "X" not in result_p:
                answer += 1
        break

    return answer


print(
    solution(
        [700, 800, 1100],  # 직원들 n 명이 설정한 출근 희망 시각
        [
            # 직원들이 일주일 동안 출근한 시각
            [710, 2359, 1050, 700, 650, 631, 659],
            [800, 801, 805, 800, 759, 810, 809],
            [1105, 1001, 1002, 600, 1059, 1001, 1100],
        ],
        5,
    )
)
