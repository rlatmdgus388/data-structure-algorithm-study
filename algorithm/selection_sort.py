# 선택 정렬:
# 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복.

# 초기 정렬: 7 5 9 0 3 1 6 2 4 8
# step 0: 
#   처리되지 않은 데이터 중 가장 작은 '0'을 선택해 가장 앞의 '7'과 바꾼다.
#   0 5 9 7 3 1 6 2 4 8
# step 1:
#   처리되지 않은 데이터 중 가장 작은 '1'을 선택해 가장 앞의 '5'와 바꾼다.
#   0 1 9 7 3 5 6 2 4 8
# step 2:
#   처리되지 않은 데이터 중 가장 작은 '2'를 선텍헤 가장 앞의 '9'와 바꾼다.
#   0 1 2 7 3 5 6 9 4 8
# 이러한 과정을 반복하면 다음과 같이 정렬된다.
#   0 1 2 3 4 5 6 7 8 9

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = 1   # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)    