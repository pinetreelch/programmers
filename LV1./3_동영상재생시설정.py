#video_len: 동영상 길이
#pos : 기능 수행전 재생위치
#op_start: 오프닝 시작 시간
#op_end  : 오프닝 끝나는 시간
#commands: 사용자 조작

# 10초 전으로 이동: 사용자가 "prev" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 전으로 이동합니다. 현재 위치가 10초 미만인 경우 영상의 처음 위치로 이동합니다. 영상의 처음 위치는 0분 0초입니다.

# 10초 후로 이동: 사용자가 "next" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 후로 이동합니다. 동영상의 남은 시간이 10초 미만일 경우 영상의 마지막 위치로 이동합니다. 영상의 마지막 위치는 동영상의 길이와 같습니다.

# 오프닝 건너뛰기: 현재 재생 위치가 오프닝 구간(op_start ≤ 현재 재생 위치 ≤ op_end)인 경우 자동으로 오프닝이 끝나는 위치로 이동합니다.

# 이때 사용자의 입력이 모두 끝난 후 동영상의 위치를 "mm:ss" 형식으로 return 하도록 solution 함수를 완성해 주세요.

def solution(video_len, pos, op_start, op_end, commands):

    #분:초 를 초로 바꾸기
    def set_time(input_time):
        min, sec = input_time.split(":")
        return_time = int(min)*60 + int(sec)

        return return_time
    
    answer = set_time(pos)

    if (set_time(op_start) <= answer) and (answer <= set_time(op_end)):
                answer = set_time(op_end)

    for command in commands:

        if command == 'next':
            # print(command)

            answer += 10
  
            if answer > set_time(video_len):
                answer = set_time(video_len)

            if (set_time(op_start) <= answer) and (answer <= set_time(op_end)):
                answer = set_time(op_end)
               

        elif command == 'prev':

            answer -= 10

            # print(command)
            if answer < 10:
                answer = 0
            
                

    return f"{answer // 60}:{answer % 60:02d}"

print(
        solution(
                "10:55",	
                "00:05",	
                "00:15",	
                "06:55",	
                ["prev", "next", "next"]
                ))