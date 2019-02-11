library(dplyr)
library(scRNAseq)

file <- commandArgs(trailingOnly = TRUE)
reads <- read.csv("tissue-counts.csv", header = T, row.names = 1)
info <- read.table(file, header = T, row.names = 1)
genome <- read.table("TM_gene_genomic_info.tsv", header = F)

info$Individual <- NA
info$Individual <- sapply(strsplit(rownames(info),"[.]"), "[", 2)

Rn <- as.data.frame(t(reads["Rn45s",]))

comp_info<-cbind(as.data.frame(info[intersect(rownames(info),rownames(Rn)),]),Rn[intersect(rownames(info),rownames(Rn)),])
colnames(comp_info)[4]<-"Rn45s"

reads <- reads[,intersect(rownames(comp_info),colnames(reads))]

genome <- na.omit(genome)
colnames(genome)<-c("Chromosome","Start","End","Strand","Gene","Gene_Type")
rownames(genome)<-genome$Gene
genome$Length <- genome$End - genome$Start
genome %>%
  select(-Gene) -> genome
genome <- genome[intersect(rownames(reads),rownames(genome)),]
reads <- reads[intersect(rownames(reads),rownames(genome)),]

scRNA_obj <- SummarizedExperiment(assays = list(counts=as.matrix(reads)))
colData(scRNA_obj) <- DataFrame(comp_info)
rowData(scRNA_obj) <- DataFrame(genome)

filter1 <- rowSums(assay(scRNA_obj)>5)>5
table(filter1)
filter2 <- colSums(assay(scRNA_obj)>500)>5 & colSums(assay(scRNA_obj))>50000
table(filter2)
scRNA_obj <- scRNA_obj[filter1,filter2]

write.table(assay(scRNA_obj),paste0("Filtered_",file,sep=""),sep="\t",quote=FALSE)
