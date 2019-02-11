# Tabula_Muris_Processing_single_cell_RNAseq
Pipeline for processing and analyzing single cell RNAseq data

Key steps of our analysis are presented below. Please also refer to our manuscript regarding other analyses not online. For technical inquiries please contact Tianyuan Lu (tianyuan.lu@mail.mcgill.ca) or Dr. Jessica C. Mar (j.mar@uq.edu.au).

### Preprocessing
---
Raw counts data can be retrived from the Tabula Muris study at https://github.com/czbiohub/tabula-muris.

These data can be preprocessed by

		Rscript preprocessing.R celltype_annot.tsv

where **celltype_annot.tsv** can be found in the "CellTypeAnnotation" folder. Change "tissue" in line 5 of the script to "Brain"/"Heart" or any other desired tissue.

### Imputation
---
Imputation of the filtered data can be performed by scImpute.

		scimpute(count_path = "/path/to/filteredfile" 
         	         infile = "csv",           
         		 outfile = "csv",          
         		 out_dir = "/path/to/output/directory",         
         		 drop_thre = 0.5,          # threshold set on dropout probability
         		 Kcluster = number_of_clusters,             # number of cell populations; in our study, 4 for brain cells and 6 for heart cells
         		 ncores = 10)              

Please refer to https://github.com/Vivianstats/scImpute for more instructions. Imputed data have been provided in rds format.

### Normalization
---
Normalization of imputed data can be performed using the following code in R:

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
---
GSVA can be performed using the R package "GSVA"

		exp <- as.matrix(read.table("expression_matrix", header=T, row.names=1))
		gset <- getGmt("Mus.gmt")
		GSVAresult <- gsva(exp,gset)

where the "Mus.gmt" describing gene sets has been provided.

### PANDA network
