#!/bin/bash -l
#SBATCH -A sens2017106
#SBATCH -p node
#SBATCH -n 1
#SBATCH -t 7-00:00:00
#SBATCH -J repmask
#SBATCH -C mem512GB

#runs repeatmasker on gr38, outputs gff file

# /sw/data/uppnex/ToolBox/hg38bundle/Homo_sapiens_assembly38.fasta
module load bioinfo-tools RepeatMasker

RepeatMasker -pa 16 -qq -species human /proj/nobackup/sens2017106/wharf/kbilgrav/kbilgrav-sens2017106/Repeatmasker/Homo_sapiens_assembly38.fasta  -dir grch38_r -gff




