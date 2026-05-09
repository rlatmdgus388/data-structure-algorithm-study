# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수해
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다.
# N과 K가 주얼질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성해라.
# 조건:
#  시간제한 2초. 메모리 제한: 128MB
#  입력 조건: 첫째 줄에서 N(1 <= 100,000)과 K(2 <= K <= 100,000)가 공백을 기준으로 하여 각각 자연수로 주어짐
#  출력 조건: 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야하는 횟수의 최솟값을 출력



# K로 나누는게 1을 빼는 것보다 더 적은 횟수로 1로 만들 수 있다.
# 매번 N을 K로 나눌 수 있는지 확인.
# 안되면 1을 빼게 설계
# O(N) 시간 복잡도
n, k = map(int, input().split())

def solution(n, k):
    count = 0
    while (n > 1):
        if (n % k != 0):
            n -= 1
        else:
            n = (n // k)
        count += 1
    return count


# 만약 N이 100,000이 아니라 매우 큰 수이면 1씩 빼는 과정이 오래 걸려 시간 초과가 날 수 있다.
# -> 한 번에 여러번 빼는 방식 사용
# O(logN) 시간 복잡도
def optimized_solution(n, k):
    count = 0
    while True:
        target = (n // k) * k
        count += (n - target)
        n = target
        
        if n < k:
            break
        
        count += 1
        n //= k
        
    count += (n - 1)
    return count

print(solution(n, k))
print(optimized_solution(n, k))
