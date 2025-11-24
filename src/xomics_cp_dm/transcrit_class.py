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

    