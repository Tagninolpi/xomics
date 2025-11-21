class Exon:
    def __init__(self,id:str,start:int,end:int,strand:str,gene_ids:dict,transcrit_ids:dict):
        self.id = id
        self.start = start
        self.end = end
        self.strand = strand
        
        self.gene_ids = gene_ids
        self.transcrit_ids = transcrit_ids
        