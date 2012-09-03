#!/usr/bin/python

fibo_cache = {}

def fibo(n):
    if n in fibo_cache:
        return fibo_cache[n]
    
    if n == 0:
        fibo_cache[0] = 0
        return 0
    
    if n == 1:
        fibo_cache[1] = 1
        return 1
    
    if n%2 != 0:
        m = int((n+1)/2)
        f = int(fibo(m-1))
#        F = int(round(f*1.61803398874989484820458683436563811772030917980576)) if f > 1 else 1
        F = fibo(m)
        fibo_cache[n] = f*f + F*F
        return fibo_cache[n]
    else:
        m = int(n/2)
        f = int(fibo(m-1))
#        F = int(round(f*1.61803398874989484820458683436563811772030917980576)) if f > 1 else 1
        F = fibo(m)
        fibo_cache[n] = (2*f + F)*F
        return fibo_cache[n]

def isPandigital(n):
    s = str(n)
    for i in range(1,10):
        if not str(i) in s:
            return False
    return True

def main():
    n = 1
    
    while True:
        f = fibo(n)
        l = len(str(f))
        
        if isPandigital(int(str(f)[l-9:l])):
            print(n)
            break

if __name__ == "__main__":
    main()
