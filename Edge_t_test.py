#!/path/to/python3

import csv
import numpy
from scipy import stats
import argparse

parser = argparse.ArgumentParser(description="""Given tab-separated files""")
parser.add_argument('edges',
                    type=argparse.FileType('r'),
                    help="List of annotated edges.")
parser.add_argument('cov_files1',
                    type=argparse.FileType('r'),         
                    help="List of tab-separated files. Male")
parser.add_argument('cov_files2',
                    type=argparse.FileType('r'),
                    help="List of tab-separated files. Female")
args = parser.parse_args()

file1 = csv.reader(args.cov_files1, delimiter="\t")
file2 = csv.reader(args.cov_files2, delimiter="\t")
Edges = csv.reader(args.edges, delimiter="\t")

print("TF","Gene","Male_mean","Female_mean","Trend","Tstatistic","p-value",sep="\t")

lst1 = []
for line in file1:
    lst1.append([float(line[i]) for i in range(0,len(line))])

lst2 = []
for line in file2:
    lst2.append([float(line[j]) for j in range(0,len(line))])

k = 0
for row in Edges:
    stat, p = stats.ttest_ind(lst1[k],lst2[k],equal_var=False)
    if numpy.mean(lst1[k]) < numpy.mean(lst2[k]):
        print(row[0],row[1],numpy.mean(lst1[k]),numpy.mean(lst2[k]),"Up",stat,p,sep="\t")
        k = k+1
        continue
    print(row[0],row[1],numpy.mean(lst1[k]),numpy.mean(lst2[k]),"Down",stat,p,sep="\t")
    k = k+1
