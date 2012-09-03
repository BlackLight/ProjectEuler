#!/usr/bin/python

import urllib

def crossDiff(a, b):
    return [a[0]-b[0], a[1]-b[1]]

def crossProduct(a, b):
    return [0, 0, a[0]*b[1] - a[1]*b[0]]

def dotProduct(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def sameSide(p1, p2, a, b):
    prod1 = crossProduct(crossDiff(b, a), crossDiff(p1, a))
    prod2 = crossProduct(crossDiff(b, a), crossDiff(p2, a))
    return True if dotProduct(prod1, prod2) >= 0 else False

def pointInTriangle(p, a, b, c):
    return True if (sameSide(p, a, b, c) and sameSide(p, b, a, c) and sameSide(p, c, a, b)) else False

def main():
    url = urllib.urlopen("http://projecteuler.net/project/triangles.txt")
    isInside = 0
    
    for triang in url.readlines():
        coords = str.split(triang.strip(), ',')
        
        if pointInTriangle([0,0], [int(coords[0]), int(coords[1])], [int(coords[2]), int(coords[3])], [int(coords[4]), int(coords[5])]):
            isInside += 1
            
    print(isInside)
    
if __name__ == "__main__":
    main()
