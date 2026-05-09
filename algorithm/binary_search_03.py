# 정렬된 배열에서 특정 수의 개수 구하기
# 문제 설명:
#   N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다. 이때 이 수열에서 x가 등장하는 횟수를 계한해라. 
#   예를 들어 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4이므로 4를 출력한다.
#   단, 이 문제는 시간 복잡도O(logN)으로 알고리즘으로 설계하지 않으면 시간 초과 판정을 받는다.
# 문제 조건:
#   풀이 시간: 30분, 시간 제한: 1초, 메모리 제한: 128mb
# 입력 조건:
#   첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력됨.  (1 <= N <= 1,000,000), (-10^9 <= x <= 10^9)
#   둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됨.    (-10^9 <= 각 원소의 값 <= 10^9)
# 출력 조건:
#   수열의 원소 중에서 값이 x인 원소의 개수를 출력해라. 단, 값이 x인 원소가 하나도 없다면 -1을 출력.



# 시간 복잡도 O(logN)으로 동작하는 알고리즘 요구
#   일반적인 선형 탐색으로는 시간 초과 판정
#   데이터가 정렬되어 있기 때문에 이진 탐색을 수행할 수 있다
# 특정 값이 등장하는 첫 번째 위치와 마지막 위치를 찾아 위치 차이를 계산해 문제를 해결
#   x가 등장하는 첫 위치와 마지막 위치 총 두번의 이진 탐색 실행 
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count == 0:
    print(-1) 
else:
    print(count)
    
