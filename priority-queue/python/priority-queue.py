# Priority Queue implementation with max-Heap (priority for largest number)

def max_heapify(A, n, i):
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < n and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)

def build_max_heap(A):
    global n
    idx = int((n // 2) - 1)
    for i in range(idx, -1, -1):
        max_heapify(A, n, i)

def deleteRoot(A):
    global n
    lastElement = A[n - 1]
    A[0] = lastElement
    n = n - 1
    max_heapify(A, n, 0)

def printArray(A, n):
 
    for i in range(n):
        print(A[i],end=" ")
    print()