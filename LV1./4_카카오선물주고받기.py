import itertools

def get_index(dictionary, giver, receiver):

    result = {}
    
    for keys, values in dictionary.items():
        result[keys] ={}
        result[keys]['give'] = 0
        result[keys]['rec'] = 0    

        for key, val in values.items():
            result[keys]['give']  += val


        for name in dictionary:
            if name == keys:
                continue
            else:
                result[keys]['rec'] += dictionary[name][keys]

    for i,j in result.items():
       result[i]["index"] =  j["give"]-j['rec']
    

    return result

def solution(friends, gifts):

    gift_record = {}

    for name in friends:
        
        gift_record[name] = {}
        # gift_record["no"] = 0

        for name2 in friends:
            if(name != name2):
                gift_record[name][name2] =  0
    
    for record in gifts:
        
        a, b = record.split(" ")
        gift_record[a][b] += 1

    # print(gift_record)

    answer = {}

    

    #한명씩 돌면서 두 사람이 선물을 주고받은 기록이 있는지와, 기록이 없다면 지수로서 받을 각 사람마다 받을 선물의 총합을 구해야함
    for key, value in gift_record.items():
        # print(key)
        answer[key] = 0

        for val, val_key in value.items():

            no_gift = 0
            val_to_key = gift_record[val][key]

            if val_key == 0:
                # key가 val한테는 선물한 기록이 없다.
                if val_to_key == 0:
                    # print("이것있을까?? => ", val , "to" , key , " ==>" ,gift_record[val][key])
                    # val도 key 한테 선물한 기록이 없다.
                    # 진짜로 두사람이 선물을 주고받은 기록이 없는것 => 지수로서 측정
                    index_array = get_index(gift_record, key, val)

                    if index_array[key]['index'] > index_array[val]['index']:
                        answer[key] += 1




                    # print(index_array)
            else:
                # 두 사람이 선물을 주고받은 기록이 있다. 더 많이 줬으니까 담달에 한개 받음
                if val_key > val_to_key:
                    answer[key] += 1
                else:
                # 주고 받은 갯수가 똑같으면 => 지수로 측정
                    index_array = get_index(gift_record, key, val)
                
                    if index_array[key]['index'] > index_array[val]['index']:
                        answer[key] += 1
                    


    print(answer)

    return ''


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

