#!/path/to/python3

import csv
import argparse
import numpy

parser = argparse.ArgumentParser(description = "get in degree scores")
parser.add_argument('-m', type = argparse.FileType('r'), help = "PANDA output matrix")
args = parser.parse_args()

GeneDict = {}
expMat = csv.reader(args.m,delimiter="\t")
for line in expMat:
    if line[1] not in GeneDict:
        GeneDict[line[1]] = list(numpy.repeat(0,100))
    count = list(map(float,line[2:]))
    if numpy.mean(count)>=0:
        GeneDict[line[1]] = list(numpy.add(GeneDict[line[1]],count))

for Gene in GeneDict:
    print(Gene,"\t".join(list(map(str,GeneDict[Gene]))),sep="\t")
