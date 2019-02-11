#!/path/to/python3

import csv
import pandas
import random
import numpy

card=[]
endocar=[]
endothe=[]
fibro=[]
leuko=[]
smoom=[]

counts = pandas.read_csv(open("female_all_heart.tsv"),delimiter="\t",index_col=0)
annot = csv.reader(open("heart_sample_tissue_female.txt"),delimiter="\t")

for line in annot:
    if line[1]=="cardiac_muscle_cell": card.append(line[0])
    if line[1]=="endocardial_cell": endocar.append(line[0])
    if line[1]=="endothelial_cell": endothe.append(line[0])
    if line[1]=="fibroblast": fibro.append(line[0])
    if line[1]=="leukocyte": leuko.append(line[0])
    if line[1]=="smooth_muscle_cell": smoom.append(line[0])

random.seed(19970819)
random.shuffle(card)
random.shuffle(endocar)
random.shuffle(endothe)
random.shuffle(fibro)
random.shuffle(leuko)
random.shuffle(smoom)

for tmp in range(1,101):
    ls = list(numpy.random.choice(card,10))
    counts[ls].to_csv('split_cardiac_female_%s'%tmp,sep="\t")

for tmp in range(1,101):
    ls = list(numpy.random.choice(endocar,10))
    counts[ls].to_csv('split_endocardial_female_%s'%tmp,sep="\t")

for tmp in range(1,101):
    ls = list(numpy.random.choice(endothe,10))
    counts[ls].to_csv('split_endothelial_female_%s'%tmp,sep="\t")

for tmp in range(1,101):
    ls = list(numpy.random.choice(fibro,10))
    counts[ls].to_csv('split_fibroblast_female_%s'%tmp,sep="\t")

for tmp in range(1,101):
    ls = list(numpy.random.choice(leuko,10))
    counts[ls].to_csv('split_leukocyte_female_%s'%tmp,sep="\t")

for tmp in range(1,101):
    ls = list(numpy.random.choice(smoom,10)) 
    counts[ls].to_csv('split_smoothmuscle_female_%s'%tmp,sep="\t")
