#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 20:43:44 2021

@author: emilygan
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
    if len(A)==1:
        return A
    
    parent=A[0]
    
    search=L[0]+1
    
    start=1
    
    if search in L:
        start=L.index(search)
    else:
        return [parent]
    
    if search in L[start+1:]:
        i=L[start+1:].index(search)+start+1
        
        return tree_rescue(A[start:i],L[start:i]) + [parent] + tree_rescue(A[i:],L[i:])
    
    return tree_rescue(A[start:],L[start:]) + [parent]
    