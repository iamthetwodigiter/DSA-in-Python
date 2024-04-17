def maximum(A, n):
    max = A[0]
    for i in range(n):
        if A[i] > max:
            max = A[i]

    return max+1

def countsort(A, max):
    B = [0 for i in range(max)]

    for items in A:
        B[items] += 1

    C = []

    for i in range(max):
        while(B[i] > 0):
            C.append(i)
            B[i] -= 1

    return C

def main():
    A = list(map(int, input("Enter space separated list elements: ").split()))

    n = len(A)

    print("Array before sorting: ",*A)
    res = countsort(A, maximum(A, n))
    print("Array after sorting: ",*res)

if __name__ == "__main__":
    main()