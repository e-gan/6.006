#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Node(object):
    """Even though we are not asking for a tree in return,
    feel free to use this Node class to help you build the tree.
    """

    def __init__(self, index, r) -> None:
        self.parent = None
        self.left = None
        self.right = None
        self.index = index
        self.h = None
        self.r = r

    def traverse(self):
        left = self.left.traverse() if self.left else []
        right = self.right.traverse() if self.right else []
        return left + [self.h] + right
    
        

'''
Represents an array data structure which allows incrementing over
a range of indices. For example, if we started with an array:

A = [5, 1, 7, 2, 11]

Here are some example queries:
    get(0) --> 5
    get(1) --> 1
    get(2) --> 7
    get(3) --> 2
    get(4) --> 11

However, if we then called:
    increment(2, 4, 6) --> A = [5, 1, 13, 8, 17]
    increment(0, 3, 2) --> A = [7, 3, 15, 10, 17]

So the previous queries would now yield:
    get(0) --> 7
    get(1) --> 3
    get(2) --> 15
    get(3) --> 10
    get(4) --> 17
'''
class KresgeGrass(object):

    def __init__(self, A) -> None:
        '''Initializing the Data Structure from array/list A'''
        def updateH(node, A):
            if node.parent:
                node.h=A[node.index]-node.parent.h
            else:
                node.h=A[node.index]
                
        def subtree(A,i,j):
            c = (i+j)//2
            root=Node(index=c,r=(i,j))
            updateH(root,A)
            if i<c:
                root.left=subtree(A,i,c-1)
                root.left.parent=root
                updateH(root.left,A)
            if c<j:
                root.right=subtree(A,c+1,j)
                root.right.parent=root
                updateH(root.right,A)
            return root
        
        self.root=subtree(A,0,len(A)-1)
        self.index=self.root.index
        
    def get(self, i) -> int:
        '''Return the i-th element in your data structure'''
        def find(root, i):
            if i<root.index:
                return root.h + find(root.left, i)
            elif i>root.index:
                return root.h + find(root.right,i)
            else:
                return root.h
        return find(self.root, i)

    def increment(self, a, b, k) -> None:
        '''Increment elements from indices a to b by k'''
        def inc(root, a, b, k):
            if a<=root.index<=b:
                root.h+=k
                if root.r[0]<a:
                    inc(root.left, root.r[0], a-1, -k)
                if b<root.r[1]:
                    inc(root.right, b+1, root.r[1], -k)
            elif b<root.index:
                inc(root.left,a,b,k)
            elif root.index<a:
                inc(root.right,a,b,k)
                
        inc(self.root,a,b,k)
                    
                    
            
    