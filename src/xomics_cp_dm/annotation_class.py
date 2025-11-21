from .gene_class import Gene
from .transcrit_class import Transcrit
from .exon_class import Exon

class Annotation:
    def __init__(self):
        self.gene_list:list[Gene|Transcrit|Exon] = []
        