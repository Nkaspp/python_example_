def Merge(A,p,q,r):
    n1 = q - p + 1
    n2 = r - q

    L = A[p:q+1]
    R = A[q+1:r+1]

    i = 0
    j = 0

    for k in range(r - p + 1 ):

        if i > n1-1:
            A[p+k] = R[j]
            j = j + 1

        elif j > n2-1:
            A[p+k] = L[i]
            i = i + 1

        elif L[i] < R[j]:
            A[p+k] = L[i]
            i = i + 1

        else:
            A[p+k] = R[j]
            j = j + 1

    return A
