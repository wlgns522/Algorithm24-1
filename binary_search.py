def sequential_search(list, key):
    for j in list:
        if j == key:
            return key  # 찾은 경우 해당 요소 반환
        elif j > key:
            return None  # 정렬된 리스트이므로 찾으려는 값보다 큰 값이 나오면 해당 값은 리스트에 없음을 의미

    return None  # 리스트를 모두 확인했지만 찾으려는 값이 없는 경우

# 정렬된 리스트
list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 찾고자 하는 값
i = 11

# 순차 탐색 실행
result = sequential_search(list, i)

if result is not None:
    print(f"{i}를 찾았습니다!")
else:
    print(f"{i}를 찾지 못했습니다.")