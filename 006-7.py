#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 19:54:50 2021

@author: emilygan
"""

def trade_turkey(prices, k):
    """"Find the optimal way to buy and sell turkeys to maximize 
    the total profit.

    Args:
        prices: a list of turkey prices, where prices[i] is the price
        of a turkey on day i.
        k: the maximum number of turkeys you can buy

    Returns:
        a list of up to k non-overlapping trades that gives you the
        max total profit, where each trade is of format (buy_index, sell_index)
    """
    n=len(prices)
    
    if n==0 or k==0:
        return []
    
    x=[[[0,[]] for i in range(n+1)] for k2 in range(k+1)]
            
    for k2 in range(1,k+1):
        for i in range(1,n):
            prof,trade=x[k2][i-1]
            for j in range(i):
                if x[k2-1][j-1][0]+prices[i]-prices[j] > prof:
                    prof=x[k2-1][j-1][0]+prices[i]-prices[j]
                    trade=x[k2-1][j-1][1]+[(j,i)]
            x[k2][i]=prof, trade
                    
    return x[k][n-1][1]
    
            
        
    
    
                
        
                
        