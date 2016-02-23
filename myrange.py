#-*- coding:utf-8 -*-
import sys

def myrange(N):
    i = 0
    while i<N:
        yield i
        i += 1

if __name__ == "__main__":
    N = 10
    a = [0,1,2,3]
    #print(next(a))
    r = myrange(N)
    print(next(r))
    print(next(r))
    print(next(r))

    for n in myrange(N):
        
        print(n)
