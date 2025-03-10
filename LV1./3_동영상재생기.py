def solution(video_len, pos, op_start, op_end, commands):

    def transfer_into_sec(tar_time):
        min, sec = tar_time.split(":")

        return int(min)*60 + int(sec)

    video_len_sec = transfer_into_sec(video_len) #전체 비디오길이
    pos_sec       = transfer_into_sec(pos)       #현재 위치
    op_start_sec  = transfer_into_sec(op_start)  #오프닝 위치
    op_end_sec        = transfer_into_sec(op_end)    #오프닝 엔딩

    if pos_sec >= op_start_sec and pos_sec <= op_end_sec:
        pos_sec = op_end_sec

    
    for command in commands:

        if command == "next":
            pos_sec += 10

            if video_len_sec-pos_sec < 10:
                pos_sec = video_len_sec

        elif command == "prev":
            pos_sec -= 10

            if pos_sec < 10:
                pos_sec = 0
            

        if pos_sec >= op_start_sec and pos_sec <= op_end_sec:
            pos_sec = op_end_sec

    return f"{pos_sec // 60:02d}:{pos_sec % 60:02d}"





print(
        solution
        (
            "10:55",	
            "00:05",	
            "00:15",	
            "06:55",	
            ["prev", "next", "next"]
        )
    )