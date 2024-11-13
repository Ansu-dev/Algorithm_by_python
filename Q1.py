# 입출력 예를 우선 본다.
# 입 -> 출력으로 바뀌어야한다.
# 내가 설정한 가설이 맞는지 확인후 위의 서사를 읽음
# 아스키 코드 문제
def solution(data):
    # replace(" ", "").replace("+","1").replace("-","0")
    # int('1101010', 2) -> 2진수를 10진수로 표현
    # chr(숫자) -> 문자열로 표현 (아스키코드)
    result = ''
    for i in data:
        result += chr(int(i.replace(" ", "").replace("+", "1").replace("-", "0"), 2))

    print(result)
    return result


solution([" + - - + - + - ", " + + + - + - + ", " + + - + + + - "])
