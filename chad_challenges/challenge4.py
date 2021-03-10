#!/usr/bin/env python3

#Method 1
def PrintPattern(pattern):
    for stars in pattern:
        while stars > 0:
            print("*", end="")
            stars -= 1
        print("")

size = 5
pattern1 = list(range(1,size)) + list(range(size,0,-1)) #Cool and educational way to do it.
pattern2 = [1,2,3,4,5,4,3,2,1] #But, simple and readable code is better code.

PrintPattern(pattern1)
PrintPattern(pattern2)

#Method 2
def PrintStarList(sList):
    for stars in sList:
        print(stars)

starList = ["*", "**","***","****","*****","****","***","**","*"]

PrintStarList(starList)
