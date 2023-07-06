# Implementation of a min-heap from an unordered array

def min_heapify(A,i):
    l = 2 * i + 1
    r = 2 * i + 2
    if l < len(A) and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)


def build_min_heap(A):
    n = int((len(A)//2)-1)
    for i in range(n, -1, -1):
        min_heapify(A,i)

    return A