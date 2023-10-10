import math
from Merge import Merge

def Merge_Sort(A,p,r):

    if p == r:
        return A

    if p < r:
        q = math.floor((p+r)/2)
        Merge_Sort(A,p,q)
        Merge_Sort(A,q+1,r)
        Merged_List = Merge(A,p,q,r)

    return Merged_List



def test1():
    A = [5, 2, 4, 6, 1, 3, 2, 6]
    assert Merge_Sort(A,0,len(A)-1) == [1, 2, 2, 3, 4, 5, 6, 6], "Should be [1, 2, 2, 3, 4, 5, 6, 6]"

def test2():
    A = [12,4,5,1,2,8,90,45,22]
    assert Merge_Sort(A, 0, len(A) - 1) == [1, 2, 4, 5, 8, 12, 22, 45, 90], "Should be [1, 2, 4, 5, 8, 12, 22, 45, 90]"

# test1()
# test2()
