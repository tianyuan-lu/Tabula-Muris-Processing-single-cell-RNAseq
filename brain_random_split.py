#!/path/to/python3

import csv
import pandas
import random
import numpy

astro=[]
endo=[]
micro=[]
oligo=[]

counts = pandas.read_csv(open("female_all_brain.tsv"),delimiter="\t",index_col=0)
annot = csv.reader(open("sample_tissue_female.txt"),delimiter="\t")

for line in annot:
    if line[1]=="astrocyte_of_the_cerebral_cortex": astro.append(line[0])
    if line[1]=="endothelial_cell": endo.append(line[0])
    if line[1]=="microglial_cell": micro.append(line[0])
    if line[1]=="oligodendrocyte": oligo.append(line[0])

random.seed(20180509)
random.shuffle(astro)
random.shuffle(endo)
random.shuffle(micro)
random.shuffle(oligo)

for tmp in range(1,101):
    ls = list(numpy.random.choice(endo,10))
    counts[ls].to_csv('split_endothelial_male_%s'%tmp,sep="\t")

for tmp in range(1,101):
    ls = list(numpy.random.choice(astro,10))
    counts[ls].to_csv('split_astrocyte_male_%s'%tmp,sep="\t")

for tmp in range(1,101):
    ls = list(numpy.random.choice(micro,10))
    counts[ls].to_csv('split_microglial_male_%s'%tmp,sep="\t")

for tmp in range(1,101):
    ls = list(numpy.random.choice(oligo,10))
    counts[ls].to_csv('split_oligodendrocyte_male_%s'%tmp,sep="\t")
