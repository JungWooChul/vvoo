def solution(id_list, report, k):
    id_dict = {i:[] for i in id_list}
    id_cnt = {i:0 for i in id_list}
    
    # 유저ID와 유저가 신고한 ID 매칭 & 한 유저의 중복 신고 처리
    for i in set(report):
        id_dict[i.split(' ')[0]].append(i.split(' ')[1])
    
    # 유저 별 신고당한 횟수 count
    for i in id_dict.values():
        for j in i:
            id_cnt[j] += 1
    
    # 이용 정지 유저 list
    stop_list = []
    for key, value in id_cnt.items():
        if value>=k:
            stop_list.append(key)
    
    # 각 유저별로 메일을 받을 횟수 저장
    answer = []
    for key,value in id_dict.items():
        cnt = 0
        for i in value:
            if i in stop_list:
                cnt+=1
        answer.append(cnt)
    
    return answer
