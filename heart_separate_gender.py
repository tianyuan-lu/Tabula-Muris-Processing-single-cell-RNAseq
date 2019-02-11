#!/path/to/python3

import pandas
import csv

com = pandas.read_csv(open("Heart_normalized_sex_removed_with_TSS.tsv"),delimiter="\t",index_col=0,low_memory=False)

annot1 = csv.reader(open("All_heart_annot_filtered_outlier.tsv"),delimiter="\t")

male = []
female = []

for line in annot1:
    if line[1]=="cardiac_muscle_cell" or line[1]=="endocardial_cell" or line[1]=="endothelial_cell" or line[1]=="fibroblast" or line[1]=="leukocyte" or line[1]=="smooth_muscle_cell":
        if line[2]=="M":
            male.append(line[0])
            continue
        female.append(line[0])

com[male].to_csv('male_all_heart.tsv',sep='\t')
com[female].to_csv('female_all_heart.tsv',sep='\t')
