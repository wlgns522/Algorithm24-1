count = int(input("노드의 개수 : ")) # count 함수에 int(input)을 이용하여 입력 받을 수를 count에 저장
list = []
for i in range(count):   # range()함수를 사용해 count함수에 입력 받은 수 만큼 반복
    data = int(input("노드 #%d의 데이터: " %(i+1))) # 수가 0부터 나오기 때문에 +1을 해주고 입력받은 데이터들을 data함수에 저장
    list.append(data) # data에 입력 받은 수를 append()함수를 사용하여 list함수에 추가한다

print("리스트의 내용:", list) # append()를 사용해 list에 추가된 수를 나타낸다