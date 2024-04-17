def binary_search(A, key, low, high):
    if(low<=high):
        mid=(low+high)//2
        if key==A[mid]:
            return mid
        elif key <A[mid]:
            return binary_search(A, key, low, mid-1)
        else :
            return binary_search(A, key, mid+1, high)
    return -1
list=[5,7,11,16,20,28,34,39,42,45,51,55,60]
print("리스트=",list)
print("34의 위치-->", binary_search(list, 34,0,len(list)-1))
print("33의 위치-->", binary_search(list, 33,0,len(list)-1))