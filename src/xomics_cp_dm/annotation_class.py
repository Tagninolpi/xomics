from .gene_class import Gene
from .transcrit_class import Transcrit
from .exon_class import Exon
from matplotlib import figure


class Annotation:
    def __init__(self,genes_list):
        self.gene_list:list[Gene[Transcrit[Exon]]] = genes_list

    def get_gene(self,gene_id:str):
        for gene in self.gene_list:
            if gene.id == gene_id:
                return gene
        raise ValueError(f"Le gène '{gene_id}' est introuvable dans cette annotation.")
    
    def to_gff(self,filename:str):
        with open(filename, "w") as f:
            for gene in self.gene_list:
                f.write(gene.line + "\n")
                for transcrit in gene.transcrit_list:
                    f.write(transcrit.line + "\n")
                    for exon in transcrit.exon_list:
                        f.write(exon.line + "\n")

    def rna_len(self,filename:str):
        fig = figure.Figure(figsize=(max(6, len(self.gene_list) * 0.8), 6))
        ax   = fig.subplots(1, 1)
        RNAlens = []
        gene_names = []
        for gene in self.gene_list:
            transcrit_len = []
            for transcrit in gene.transcrit_list:
                lenght = 0
                for exon in transcrit.exon_list:
                    lenght += exon.end - exon.start
                transcrit_len.append(lenght)
            RNAlens.append(transcrit_len)
            gene_names.append(gene.name)
        print(RNAlens)
        print(gene_names)
        
        ax.boxplot(RNAlens, tick_labels=gene_names)
        fig.savefig(filename)



    def __add__(self,annot2):
        new_genes = []
        for gene2 in annot2.gene_list:
            for gene in self.gene_list:
                if gene2.id == gene.id:
                    new_genes.append(gene+gene2)
                else:
                    new_genes.append(gene)
            if not gene2 in self.gene_list:
                new_genes.append(gene2)
        self.gene_list = new_genes
        return self
    
    

    def __str__(self):
        return f"Genes:{self.gene_list}"
    
    def __repr__(self):
        return self.gene_list
