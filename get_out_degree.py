#!/path/to/python3

import csv
import argparse
import numpy

parser = argparse.ArgumentParser(description = "get out degree scores")
parser.add_argument('-m', type = argparse.FileType('r'), help = "PANDA output matrix")
args = parser.parse_args()

TFDict = {}
expMat = csv.reader(args.m,delimiter="\t")
for line in expMat:
    if line[0] not in TFDict:
        TFDict[line[0]] = list(numpy.repeat(0,100))
    count = list(map(float,line[2:]))
    if numpy.mean(count)>=0:
        TFDict[line[0]] = list(numpy.add(TFDict[line[0]],count))

for TF in TFDict:
    print(TF,"\t".join(list(map(str,TFDict[TF]))),sep="\t")
