# 순환호출을 이용하여 *의 개수 구하기
# 202010654 박지훈

def asterisk(i):
    if i>1:
        asterisk(i/2)
        asterisk(i/2)
    print("*", end='')

asterisk(5)

