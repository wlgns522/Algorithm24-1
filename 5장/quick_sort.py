def quick_sort(A, left, right):
    if left<right :
        mid = partition(A, left, right)
        quick_sort(A, left, mid-1)
        quick_sort(A, mid+1, right)

def partition(A, left, right):
    pivot = A[right]
    i = left -1
    for j in range(left, right):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[right] = A[right], A[i+1]
    return i+1

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Original : ", data)
quick_sort(data, 0, len(data)-1)
print("QuickSort : ", data)
