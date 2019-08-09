# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(100) #例如这里设置为一百万 


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1,a,c,b)
        print(a, '-->', c)
        move(n-1,b,a,c)
    


move(3, 'A', 'B', 'C')