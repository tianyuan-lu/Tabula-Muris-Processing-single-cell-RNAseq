library(scRNAseq)
library(SingleCellExperiment)
library(scDD)
library(BiocParallel)
BiocParallel::register(BiocParallel::SerialParam())

info <- read.table("celltype_annot.tsv", header = T, row.names = 1)
reads <- read.table("tissue_normalized.csv",header=T,row.names=1)
reads <- reads[,intersect(rownames(info),colnames(reads))]

scDD_obj <- SingleCellExperiment(assays=list(normcounts=as.matrix(reads)))
condition <- as.data.frame(info[,2])
rownames(condition)<-rownames(info)
colnames(condition)<-"condition"
condition$condition <- ifelse(condition$condition=="M",1,2)
colData(scDD_obj) <- DataFrame(condition)

scDD_res <- scDD(scDD_obj, testZeroes = TRUE, permutations = 0, param = MulticoreParam(workers=1))
write.table(results(scDD_res),"celltype_scDD.tsv",sep = "\t",quote = FALSE,row.names = FALSE)
