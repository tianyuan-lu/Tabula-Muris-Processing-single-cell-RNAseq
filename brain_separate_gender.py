#!/path/to/python3

import pandas
import csv

com = pandas.read_csv(open("Brain_normalized_sex_removed_with_TSS.tsv"),delimiter="\t",index_col=0,low_memory=False)

annot1 = csv.reader(open("All_brain_annot_filtered_outlier.tsv"),delimiter="\t")

male = []
female = []

for line in annot1:
    if line[1]=="astrocyte_of_the_cerebral_cortex" or line[1]=="endothelial_cell" or line[1]=="oligodendrocyte" or line[1]=="microglial_cell":
        if line[2]=="M":
            male.append(line[0])
            continue
        female.append(line[0])

com[male].to_csv('male_all_brain.tsv',sep='\t')
com[female].to_csv('female_all_brain.tsv',sep='\t')
