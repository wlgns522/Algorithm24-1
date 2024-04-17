def sequential_search(sorted_list, target):
    for index, item in enumerate(sorted_list):
        if item == target:
            return index  # 찾은 경우 해당 요소의 인덱스 반환
        elif item > target:
            return -1  # 정렬된 리스트이므로 찾으려는 값보다 큰 값이 나오면 해당 값은 리스트에 없음을 의미

    return -1  # 리스트를 모두 확인했지만 찾으려는 값이 없는 경우

# 정렬된 리스트
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 찾고자 하는 값
target = 11

# 순차 탐색 실행
index = sequential_search(sorted_list, target)

if index != -1:
    print(f"{target}는 리스트의 인덱스 {index}에 위치해 있습니다.")
else:
    print(f"{target}는 리스트에 존재하지 않습니다.")