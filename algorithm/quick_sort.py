# 퀵 정렬
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
# 벙합 정렬과 더불어 대부분으 프로그램 언어의 정렬 라이브러리의 근간이 되는 알고리즘.
# 가장 기본저인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정.

# 초기 정렬:
#   5 7 9 0 3 1 6 2 4 8
# step 0:
#   현재 피벗의 값은 '5'이다. 왼쪽에서부터 '5'보다 큰 데ㅣ터를 선택하므로 '7'이 선택되고, 오른쪽에서부터 '5'보다 작은 데이터를 선택하므로 '4'가 선택됨. 이제 이 두 데이터의 위치를  서로 변경한다.
#   5 4 9 0 3 1 6 2 7 8
# step 1:
#   현재 피벗의 값은 '5'이다. 왼쪽에서부터 '5'ㅂ보다 큰 데이터를 선택하므로 '9'가 선택되고, 오른쪽에서부터 '5'보다 작은 데이터를 선택하므로 '2'가 선택됨. 이제 이 두 데이터의 위치를 서로 변경한다.
#   5 4 2 0 3 1 6 9 7 8
# step 2:
#   현재 피벗의 값은 '5'이다. 왼쪽에서부터 '5'보다 큰 데이터를 선택하므로 '6'이 선택되고, 오른쪽에서 '5'보다 작은 데이터를 선택하므로 '1'이 선택됨. 단, 이처럼 위치가 엇갈리는 경우 '피벗'과 '작은 데이터'의 위치를 서로 변경.
#   1 4 2 0 3 5 6 9 7 8 
# 분할 완료:
#   이제 '5'의 왼쪽에 있는 데이터는 모두 5보다 작고, 오른쪽에 있는 데이터는 모두 '5'보다 크다는 특징 이있다. 이렇게 피벗을 기준으로 데이터 묶음을 나누는 작업을 분할이라 한다.
# 왼쪽 데이터 묶음 퀵정렬 시행:
#   1을 피벗으로 정하고 정렬 진행
# 오른쪽 그룹 퀵정렬 시행:
#   6을 피벗으로 정하고 정렬 진행
# 0 1 2 3 4 5 6 7 8 9

# 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로 O(NlogN)을 기대할 수 있다.
# 너비 X 높이 = N X logN = NlogN

# 평균의 경우 O(NlogN)의 시간 복잡도를 하짐.
# 하지만 최악의 경우 O(n^2)의 시간 복잡도를 가짐.
#   이미 오름차순으로 정렬이 되어있는 경우


# 일반적인 방식
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:    # 원소가 1개인 경우 종료
        return
    pivot = start   # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while (left <= right):  # 왼쪽 원소 인덱스가 오른쪽 원소 인덱스랑 같거나 작을때 계속 반복
        while (left <= end and array[left] <= array[pivot]):    # 왼쪽 원소 인덱스가 배열의 끝에 도달하기 전 and 피벗값보다 작은 경우: 오른쪽으로 이동
            left += 1                                           # 원쪽 원소가 피벗값보다 크면 반복문 탈출
        while (right > start and array[right] >= array[pivot]): # 오른쪽 원소 인덱스가 피벗 인덱스보다 큰 경우 and 피벗값보다 큰 경우: 왼쪽으로 이동
            right -= 1                                          # 오른쪽 원소가 피벗값보다 작은 경우 반복문 탈출
        if (left > right):      # 왼쪽 원소 인덱스가 오른쪽 원소 인덱스보다 큰 경우 = 원소가 교차한 경우
            array[right], array[pivot] = array[pivot], array[right]     # 두 원소중 작은 값을 피벗값과 교체
        else:
            array[left], array[right] = array[right], array[left]   # 다 아닌경우 퀵정렬 수행 = 왼쪽 원소와 오른쪽 원소 위치 교체
    quick_sort(array, start, right - 1) # 두 그룹으로 나뉜 상태 -> 두 그룹을 재귀적으로 퀵정렬 수행.
    quick_sort(array, right + 1, end)   # 퀵정렬은 무조건 인덱스가 교차하는 지점이 생김. 따라서 오른쪽 인덱스 값은 초기 피벗값이 됨.       
    
quick_sort(array, 0, len(array) - 1)
print(array)


# 파이썬의 장점을 살린 방식
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]    # 피벗보다 작은 원소들을 리스트에 담음.
    right_side = [x for x in tail if x > pivot]    # 피벗보다 큰 원소들을 리스트에 담음.
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)     # 재귀적으로 정렬된 왼쪽 리스트 + 피벗 원소 + 오른쪽 리스트

print(quick_sort(array))

