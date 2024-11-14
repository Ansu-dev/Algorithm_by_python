# 행렬
def solution(data):
    # 결과값 ['상한 당근 개수', '상한당근 주변의 비어있는땅 체크(상하좌우 대각선)']
    # #의 위치를 먼저 구함
    # #이 아닌 상하좌우,대각선의 비어있는곳을 찾음
    directions = [
        (-1,  0),  # 위
        ( 1,  0),  # 아래
        ( 0, -1),  # 왼쪽
        ( 0,  1),  # 오른쪽
        (-1, -1),  # 왼쪽 위
        (-1,  1),  # 오른쪽 위
        ( 1, -1),  # 왼쪽 아래
        ( 1,  1)   # 오른쪽 아래
    ]
    num_rows = len(data)  # 전체 행 수
    num_cols = len(data[0]) if num_rows > 0 else 0
    carrotCount = sum(data,[]).count('#')
    emptyCount = 0
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col == '#':
                # 상하좌우, 대각선의 빈땅을 카운팅한다.
                for dr, dc in directions:
                    new_row = i + dr
                    new_col = j + dc
                    # 리스트의 범위를 벗어나면 안된다.
                    if (0 <= new_row < num_rows) and (0 <= new_col < num_cols):
                        # 상한 당근의 비어있는 인접 땅이라면 카운팅
                        if data[new_row][new_col] == 0:
                            emptyCount += 1
    return [carrotCount, emptyCount]

solution([[0, 0,'#', '#'], ['#','#', 0, '#'], [0, '#', '#', 0]])