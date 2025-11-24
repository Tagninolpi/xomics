from .gene_class import Gene
from .transcrit_class import Transcrit
from .exon_class import Exon

class Annotation:
    def __init__(self,genes_list):
        self.gene_list:list[Gene[Transcrit[Exon]]] = genes_list
        