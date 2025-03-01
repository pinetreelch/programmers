def solution(schedules, timelogs, startday):

    # 요일 만들기
    days = []

    for i in range(startday, startday + 7):
        if i > 7:
            days.append(i - 7)
        else:
            days.append(i)

    print(days)

    for time in schedules:

        # time  => 직원의 희망 시간
        time_late = time + 10  # 직원들 이 시간 보다 늦으면 지각임

        break


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
