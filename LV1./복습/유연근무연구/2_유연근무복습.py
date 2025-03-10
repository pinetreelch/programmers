def solution(schedules, timelogs, startday):

    answer = 0

    # 지각 시간 고르기
    def late_time(desired_time):

        hour = desired_time // 100
        min = desired_time % 100 + 10

        if min >= 60:
            return (hour + 1) * 100 + (min) % 60
        else:
            return hour * 100 + min

    def get_time_logs(times):

        att_array = []

        for out in times:
            for att_time in out:
                att_array.append(att_time)

        return att_array

    for desired_time in schedules:

        # 이렇게 초기화를 못시키는구나
        start_day_new = startday

        # 지각시간
        late_time_chk = late_time(desired_time)

        # print(timelogs[0])

        # 한주동안 출석시간 배열 구하기
        # timelogs_real = get_time_logs(timelogs)

        # for att_time in timelogs_real:

        #     if (att_time > late_time_chk) and start_day_new in (6, 7):
        #         start_day_new += 1
        #         continue
        #     else:
        #         start_day_new += 1

        # answer += 1

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
