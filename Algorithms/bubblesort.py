def bubblesort(A, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

    return A

def main():
    A = list(map(int, input("Enter space separated list elements: ").split()))

    n = len(A)

    print("Array before sorting: ",*A)
    res = bubblesort(A, n)
    print("Array after sorting: ",*res)

if __name__ == "__main__":
    main()