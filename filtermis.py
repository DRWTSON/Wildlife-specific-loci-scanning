#!/usr/bin/python3.6
Usage="""
convertphasetounphase.py - version1
Read vcf file, and culculate the eachline freq allel

Usage:
         python convertphasetounphase.py input output"""

from sys import argv
import os
import operator
if len(argv) < 3:
    print (Usage)

else:
    f1 = open(argv[1],'r')
    f2 = open(argv[2],'w')
    for eachline in f1:
        if eachline[0] == '#':
            f2.write(eachline)
        else:
            a = eachline.strip().split('\t')
            feq=0
            total=0
            for c in a[9:]:
                if c[0:3] == '1/1':
                    feq+=2
                    total+=2
                elif c[0:3] == '0/1':
                    feq+=1
                    total+=2
                elif c[0:3] == '0/0':
                    total+=2
                elif c[0:3] == './.':
                    total+=2
        else:
                    print(c)
            total+=0.0000001
            feq1 = float(feq)/float(total)
           # print ("%.2f"%feq1)
            if feq1 >= 1:       ####gaizheli
                f2.write('\t'.join(a)+'\n')
    f1.close()
    f2.close()
