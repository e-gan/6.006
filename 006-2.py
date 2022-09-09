##################################################
# Problem Set 2 Coding Problem: Happy Accidents
##################################################

'''
Computes the number of happy accidents for an input array.
A happy accident is defined as a pair of values (i, j) in the 
array where i is positioned to the left of j and i > j.
You may assume all values are distinct.

param:arr: list[int] input array
returns:int: the number of happy accidents
'''
def count_happy_accidents(A, a=0, b=None, count=0):
    if b==None:
        b=len(A)
    if 1<b-a:
        mid=(a+b+1)//2
        count+=count_happy_accidents(A,a,mid)
        count+=count_happy_accidents(A,mid,b)
        left, right=A[a:mid], A[mid:b]
        i,j=0,0
        while a<b:
            if (j>=len(right)) or (i<len(left) and left[i]<right[j]):
                A[a]=left[i]
                i+=1
            else:
                count+=len(left)-i
                A[a]=right[j]
                j+=1
            a+=1
    return count
                