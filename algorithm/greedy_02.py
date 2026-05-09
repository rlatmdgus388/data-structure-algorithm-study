# 문제:
#   각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때,왼쪽부터 오른쪽으로 하나씩 
#   모든 숫자를 확인하며 숫자 사이에 'X' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 
#   큰 수를 구하는 프로그램을 작성해라.
#   단, +보다 X를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다 가정.
#   예를 들어 02984라는 문자열로 만들 수 있는 가장 큰 수는 (((((0 + 2)) X 9) X 8) X 4) = 576이다.
#   또한 만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어진다.
# 조건:
#   풀이 시간: 30분, 시간 제한: 1초, 메모리 제한: 128mb
#   입력 조건: 첫 째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어진다. (1 <= S의 길이 <= 20)
#   출력 조건: 첫 째 줄에 만들어질 수 있는 가장 큰 수를 출력.



# 내 풀이
# 곱하기가 가능한 경우 곱하기를 선택
# 단, 곱하기를 해도 덧셈보다 작은 경우 존재
# ->  0 or 1이 포함된 경우
s = input()

def solution(s):
    numbers = list(map(int, s))
    
    answer = 0
    first_num = numbers[0]
    answer += first_num
    numbers = numbers[1:]
    
    for indx in range(len(numbers)):
        if (answer == 0):
            answer += numbers[indx]
        elif (numbers[indx] == 0) or (numbers[indx] == 1):
            answer += numbers[indx]
        else:
            answer *= numbers[indx]
    return answer


# 답
# 현재까지의 결과나 다음 숫자가 1이하(0혹은 1)라면 더하기
# 그 외에는 무조건 곱하기
def answer_solution(s):
    numbers = list(map(int, s))
    
    result = numbers[0]
    
    for num in numbers[1:]:
        if result <= 1 or num <= 1:
            result += num
        else:
            result *= num

print(solution(s))