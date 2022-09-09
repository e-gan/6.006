import math

def ez_money(D):
    """Find a sequence of commodities to exchange to get more of that
    commodity.

    Args:
        D: A list of deals, each deal is of the form (A, x, B, y)
           which means someone will give you y of B for x of A.

    Returns:
        None if no such opputunity is found, otherwise a List of
        commodities to exchange.
    """
    mapper=[None]
    Adj={}
    rev={}
    Adj[0]={}
    atomicCounter=1
    
    for deal in D:
        A,x,B,y=deal
        
        if deal[0] in mapper:
            A=mapper.index(deal[0])
        else:
            mapper.append(A)
            A=atomicCounter
            atomicCounter+=1
        
        if deal[2] in mapper:
            B=mapper.index(B)
        else:
            mapper.append(B)
            B=atomicCounter
            atomicCounter+=1
            
        Adj.setdefault(A,{})
        Adj.setdefault(B,{})
        Adj[A][B]=math.log2(x)-math.log2(y)
        
        rev.setdefault(A,[])
        rev.setdefault(B,[])
        rev[B].append(A)
        
        Adj[0][A]=0
        Adj[0][B]=0
    try:    
        return [mapper[x] for x in bellman_ford(Adj,Adj,0)]
    except:
        return None
    
def bellman_ford(Adj, w, s): # Adj: adjacency list, w: weights, s: start
    # initialization
    infinity = float('inf') # number greater than sum of all + weights
    d = [infinity for _ in Adj] # shortest path estimates d(s, v)
    parent = [None for _ in Adj] # initialize parent pointers
    d[s], parent[s] = 0, s # initialize source
    # construct shortest paths in rounds
    V = len(Adj) # number of vertices
    for i in range(V - 1): # relax all edges in (V - 1) rounds
        for u in range(V): # loop over all edges (u, v)
            for v in Adj[u]: # relax edge from u to v
                relax(Adj, w, d, parent, u, v)
    # check for negative weight cycles accessible from s
    for u in range(V): # Loop over all edges (u, v)
        for v in Adj[u]:
            if d[v] > d[u] + w[u][v]:
                return neg(v, parent,Adj)

def relax(Adj, w, d, parent, u, v):
    if d[v]>d[u] + w[u][v]:
        d[v]=d[u] + w[u][v]
        parent[v]=u

def neg(v, parent, Adj):
    store=[v]
    while parent[store[-1]] not in store:
        store.append(parent[store[-1]])
    order=(store[store.index(parent[store[-1]]):]+[parent[store[-1]]])[::-1]
    
    summer=0
    for u,v in zip(order[:-1],order[1:]):
        summer+=Adj[u][v]
    if summer<0:
        return order[:-1]
    return neg(order[1],parent,Adj)