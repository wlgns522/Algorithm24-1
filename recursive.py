# 순환 알고리즘  프로그램
# 202010654 박지훈
def recursive1(n):
    if n==1:
        return
    else:
        print("현재 n=", n)
        recursive1(n-1)

recursive1(5)