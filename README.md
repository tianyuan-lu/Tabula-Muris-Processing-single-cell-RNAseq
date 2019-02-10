# Tabula_Muris_Processing_single_cell_RNAseq
Pipeline for processing and analyzing single cell RNAseq data
### Preprocessing

### Imputation

### Normalization
---
Normalization of imputed data was performed using the following code:

		brain <- readRDS("BrainImputed.rds")
		heart <- readRDS("HeartImputed.rds")
		Seuseth <- NormalizeData(object=seuseth, normalization.method="LogNormalize")
		Seusetb <- NormalizeData(object=seusetb, normalization.method="LogNormalize")
		SEUSETB <- FindVariableGenes(object=Seusetb, mean.function=ExpMean, dispersion.function=LogVMR, x.low.cutoff=0.0125, x.high.cutoff=3, y.cutoff=0.5)
		SEUSETH <- FindVariableGenes(object=Seuseth, mean.function=ExpMean, dispersion.function=LogVMR, x.low.cutoff=0.0125, x.high.cutoff=3, y.cutoff=0.5)
		heartHVG <- heart[SEUSETH@var.genes,]
		brainHVG <- brain[SEUSETB@var.genes,]

Loading the "Seurat" R package is necessary. Normalized data are stored in the **Seuseth** and **Seusetb** objects.

### Identification of differential distribution

### Gene set variation analysis

### PANDA network
