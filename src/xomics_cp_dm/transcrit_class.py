from .exon_class import Exon
class Transcrit:
    def __init__(self,id:str,name:str,start:int,end:int,strand:str,gene_id:str):
        self.id = id
        self.name = name
        self.start = start
        self.end = end
        self.strand = strand
        
        self.exon_list:list[Exon] = []
        
        self.gene_id = gene_id

    def __eq__(self, transcrit_2):
        same_id = True if transcrit_2.id == self.id else False
        same_gene_id = True if any(gene_id in self.gene_ids for gene_id in transcrit_2.gene_ids) else False
        if same_gene_id and same_id:
            return True
        else:
            return False