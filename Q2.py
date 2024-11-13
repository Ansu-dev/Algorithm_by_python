import re


# 정규표현식
# 패턴이 나오면 정규표현식이라는걸 알아야함
# 문자열 중에 r, e, v 뒤에 나오는 값을 더하여 나온 최종 숫자에서 앞자리를 월로 뒷자리를 일로 판단합니다.
# r, e, v 뒤에 나오는 숫자는 1부터 10까지입니다. 이를 넘어가는 숫자가 나올 경우 앞 숫자만 뽑아냅니다. => 33이 나오면 3만 숫자를뽑아넴
# 패턴에 맞게 뽑아낸 값은 아래와 같습니다. e33은 e3으로 인식해서 3만 뽑아내야 합니다.
def solution(data):
    result = 0
    # 구조 분해 할당
    data = re.findall('([rev])(10|[1-9])', data)
    for _, j in data:
        result += int(j)
    result = str(result)
    return f'{result[0]}월 {result[1]}일'


# 제한 사항
# 1 ≤ r, e, v 뒤의 숫자 ≤ 10
# 11 ≤ 합한 값 ≤ 99
solution('a10b9r1ce33uab8wc918v2cv11v9')  # 1월 16일
