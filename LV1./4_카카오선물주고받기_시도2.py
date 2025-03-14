def solution(friends, gifts):
    # 1. 선물 기록 세팅 (누가 누구에게 얼마나 줬는지)  - O
    gift_record = {f: {f2: 0 for f2 in friends} for f in friends}


    for record in gifts:
        giver, receiver = record.split()
        gift_record[giver][receiver] += 1

    # 2. 선물 지수 계산 (준 선물 - 받은 선물)
    gift_index = {}
    for friend in friends:
        given = sum(gift_record[friend].values())  # 준 선물
        received = sum(gift_record[f][friend] for f in friends)  # 받은 선물
        gift_index[friend] = given - received

    # 3. 다음 달에 받을 선물 개수 계산
    next_gifts = {f: 0 for f in friends}

    # 조합
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            a, b = friends[i], friends[j]
            a_to_b = gift_record[a][b]
            b_to_a = gift_record[b][a]

            # 선물 기록이 다르면 더 많이 준 사람이 받음
            if a_to_b > b_to_a:
                next_gifts[a] += 1
            elif b_to_a > a_to_b:
                next_gifts[b] += 1
            else:
                # 기록이 같으면 선물 지수 비교
                if gift_index[a] > gift_index[b]:
                    next_gifts[a] += 1
                elif gift_index[b] > gift_index[a]:
                    next_gifts[b] += 1
                # 같으면 아무도 받지 않음

    # 4. 가장 많이 받을 친구의 선물 수 리턴
    return max(next_gifts.values())

# 테스트
print(
    solution(
        ["muzi", "ryan", "frodo", "neo"],
        [
            "muzi frodo",
            "muzi frodo",
            "ryan muzi",
            "ryan muzi",
            "ryan muzi",
            "frodo muzi",
            "frodo ryan",
            "neo muzi",
        ],
    )
)
