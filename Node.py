class Node: #Node 클래스를 사용하여 리스트들을 연결
    def __init__(self, elem, next=None):
        self.data = elem # 리스트에 저장된 값을 data에 저장
        self.link = next # 다음 항목과 연결

def printList(head, msg="생성된 연결 리스트:"): # 제일 앞에 있는 리스트부터 입력
    print(msg, end="") 
    n = head # 앞에 있는 데이터를 n에 복사
    while n != None : # None과 n의 값이 같지 않을 경우
        print(n.data, end="->") # 앞에 있는 데이터 입력 후 추가로->입력
        n= n.link # 다음 항목의 값을 n에 복사
    print()

head = None 
tail = None
count = int(input("노드의 개수: "))
for i in range(count):
    data = int(input("노드 %d의 데이터 : "%(i+1)))
    n = Node(data, None) 
    if head==None : 
        head = tail = n 
    else :
        tail.link =n 
        tail = n
printList(head) # 리스트 내용 출력