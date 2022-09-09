#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tree Rescue
"""

def tree_rescue(A, L):
    """Rescue the tree from the a list of keys in a specific order and a list of levels
    for each corresponding keys.

    The provided list `A` has a special order as follows,

        ```
        A = []
        def collect_nodes(node):5
            if node is None:
                return

            A.append(node)
            collect_nodes(node.left)
            collect_nodes(node.right)
        ```

    Args:
        A (List[int]): List of keys in the order specified above.
        L (List[int]): Level of each of the keys in the same order.

    Returns: (List[int])
        A list of keys in the 'in-order' traversal of the constructed binary-tree.
    """
    L1,L2=subtrees(A,L)
    return order(L1,L2)
    
    
def subtrees(A,L):
    A2=[[A[0]]]
    L2=[[0]]
    for i in range(1,len(L)):
        if L[i]>L[i-1]:
            A2[-1].append(A[i])
            L2[-1].append(L[i])
        else:
            A2.append([A[i]])
            L2.append([L[i]])
    return A2[::-1],L2[::-1]
    

def order(A2,L2):
    if len(L2)==0:
        return []
    current=L2.pop()
    values=A2.pop()
    if len(current)==1 or len(L2)==0 or min(current)>=L2[-1][0]:
        return values[::-1]
    search=L2[-1][0]-1
    ordered=[]
    x=len(current)-1
    while True:
        while current[x]>=search and x>=0:
            ordered.append(values[x])
            x-=1
        ordered.extend(order(A2,L2))
        if len(L2)>0:
            search=L2[-1][0]-1
        else:
            break
    while x>=0:
        ordered.append(values[x])
        x-=1
    return ordered