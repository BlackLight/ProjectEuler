#!/usr/bin/python

factTable = {}

def fact(n):
    f = 1
    
    for i in range(1,n+1):
        f *= i
    return f

def generateFactTable(limit):
    for i in range(0, limit):
        factTable[i] = fact(i)
        
def sumFact(n):
    s = 0
    
    for digit in str(n):
        s += factTable[int(digit)]
    return s

def factChain(n):
    chain = [n]
    
    while True:
        k = sumFact(chain[len(chain)-1])
        
        if not k in chain:
            chain.append(k)
        else:
            break
        
    return chain

def main():
    generateFactTable(10)
    num = 0
    
    for i in range(1, 1000000):
        if len(factChain(i)) == 60:
            num += 1
            
    print(num)

if __name__ == "__main__":
    main()
    