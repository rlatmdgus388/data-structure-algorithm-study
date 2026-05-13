# 금광
# 문제 설명:
#   n x m 크기의 금광이 있다. 금광은 1 x 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어있다.
#   채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작한다. 맨 처음에는 첫 번째 열의 어능 행에서든 출발할 수 있다. 이후에 m - 1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다. 결괴적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성해라.
#   예시: 1 | 3 | 3 | 2
#        2 | 1 | 4 | 1
#        0 | 6 | 4 | 7    / 얻을 수 있는 금의 최대 크기: 2 + 6 + 4 + 7 = 19
# 문제 조건:
#   풀이 시간: 30분, 시간 제한: 1초, 메모리 제한: 128MB
# 입력 조건: 
#   첫째 줄에 테스트 케잏스 T가 입력됨. (1 <= T <= 1000)
#   매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력됨. (1 <= n, m <= 20)
#   둘째 줄에 n x m개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됨. (1 <= 각 위치에 매장된 금의 개수 <= 100)
# 출력 조건:
#   테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력. 각 테스트 케이스는 줄 바꿈을 이용해 구분함



# 그리디로 못구함
# 구하는게 금의 최대 크기
#   array[i][j]: 1행 j열에 존재하는 금의 양
#   dp[i][j]: i행 j열까지의 최적의 해(얻을 수 있는 금의 최댓값)
# 점화식: 
#                                 왼쪽 위            왼쪽         왼쪽 아래
#   dp[i][j] = array[i][j] + max(dp[i - 1][j-1], dp[i][j - 1], dp[i + 1][j - 1])
def solution(n, m, array):
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
    result = 0
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0: left_up = 0                    
            else: left_down = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1: left_down = 0
            else: left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)                    
            
    for i in range(n):
        result = max(result, dp[i][m - 1])
    return result

for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    print(solution(n, m, array))
    
        

    

    