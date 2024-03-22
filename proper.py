a = ['1','2','3',] # 집합 객체
b = ['1','2','3','4','5'] # 집합 객체
union = list(set(a)|set(b)) # 합집합
intersection = list(set(a)&set(b)) # 교집합
complement = list(set(a)-set(b))# 차집합
proper = a<b
print("합집합:",union)
print("교집합:",intersection)
print("차집합:",complement)
print("진부분집합:", proper)