from .gene_class import Gene
from .transcrit_class import Transcrit
from .exon_class import Exon

class Annotation:
    def __init__(self,genes_list):
        self.gene_list:list[Gene[Transcrit[Exon]]] = genes_list

    def __add__(self,annot2):
        new_genes = []
        for gene2 in annot2.gene_list:
            for gene in self.gene_list:
                if gene2 == gene:
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
