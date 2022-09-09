#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 00:43:19 2021

@author: emilygan
"""

def num_opt_even_weight_paths(graph, s):
    '''
    The num_opt_even_weight_paths function should return a dictionary mapping node v to the number of optimal
    paths of even weight from s to v.

    graph - an adjacency list of a DAG in the form {u: {v:w(u,v)} mapping nodes to a dictionary 
            where the keys are their adjacencies and the values are the edge weights
            graph[u][v] would be equal to the weight of the edge u to v.
            you may assume that graph.keys() represents all nodes present
    s - start node

    return: a dictionary mapping node v to the number of optimal paths of even weight from s to v. 
            optimal[s] should be 1.
    '''
    ans={}
    for i in graph:
        #track shortest path, # of shortest paths, and shortest even path, # of shortest even paths
        ans[i]=[float('inf'),0,float('inf'),0]
        
    _,topo=dfs(graph,s)
    topo.reverse()
    
    ans[s]=[0,1,0,1]
    
    for i in topo:
        for x in graph[i]:
            n=ans[i][0] + graph[i][x]
            
            if n < ans[x][0]:
                ans[x][0]=n
                ans[x][1]=ans[i][1]
            elif n == ans[x][0]:
                ans[x][1]+=ans[i][1]
                
            if n%2==0 and n<ans[x][2]:
                ans[x][2]=n
                ans[x][3]=ans[i][1]
            elif n == ans[x][2]:
                ans[x][3]+=ans[i][1]
                
            if ans[i][2] + graph[i][x]!=n:
                m=ans[i][2] + graph[i][x]
                
                if m%2==0 and m<ans[x][2]:
                    ans[x][2]=m
                    ans[x][3]=ans[i][3]
                elif m == ans[x][2]:
                    ans[x][3]+=ans[i][3]
            
    for i in ans:
        ans[i]=ans[i][3]
    
    return ans
    
    

def dfs(Adj, s, parent = None, order = None):
    if parent is None:
        parent = {s : s}
        order = []
    for v in Adj[s]:
        if v not in parent:
            parent[v] = s
            dfs(Adj, v, parent, order)
    order.append(s)
    return parent, order


# if __name__ == "__main__":
#     print(num_opt_even_weight_paths({"a":{"b":3, "c":5}, "b":{"c":3}, "c":{}}, "a"))
#     # should return {"a":1, "b":0, "c":1}

#     print(num_opt_even_weight_paths({"a":{"b":3, "c":5, "d":2}, "b":{"c":3}, "d":{"c":4}, "c":{}}, "a"))
#     # should return {"a":1, "b":0, "c":2}