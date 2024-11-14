# 정렬
def solution(data):
    totalPeople = len(data) # 전체 인원수
    people = int((totalPeople * 3) / 10) # 선발되야하는 인원
    if people == 0:
        return []
    select = 0 # 선발된 인원
    score = {} # 점수합 딕셔너리
    result = [] # 선발 인원 리스트

    # 점수 집계 부분
    for i in data:
        sumScore = sum(i[1:])
        if sum(i[1:]) in score:
            score[sumScore] = score[sumScore] + [i[0]]
        else:
            score[sumScore] = [i[0]]

    # 정렬 및 선발 부분
    for i in sorted(list(score.items()), reverse=True): # 딕셔너리를 배열 형태로 변경
        groupSize = len(i[1]) # 현재 각 점수마다 몇명이 있는지
        # 선발 인원을 초과하지 않는지 확인
        if select + groupSize > people:
            #  동일한 그룹의 수를 모두 선발하면 초과되므로 모두 선발하지 않음
            return []
        else:
            # 그외엔 그룹을 모두 선발
            result.extend(i[1])
            select += groupSize

        # 이미 필요한 인원을 모두 선발했다면 종료
        if select == people:
            break
    # 결과를 일므의 역순(내림차순)으로 정렬
    return sorted(result, reverse=True)


solution([['A', 25, 25, 25, 25], ['B', 10, 12, 13, 11], ['C', 24, 22, 23, 21], ['D', 13, 22, 16, 14]])
