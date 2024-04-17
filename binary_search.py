def sequential_search(list, key):
    for j in list:
        if j == key:
            return key 
        elif j > key:
            return None 

    return None  


list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
i = 11

result = sequential_search(list, i)

if result is not None:
    print(f"{i}를 찾았습니다!")
else:
    print(f"{i}를 찾지 못했습니다.")