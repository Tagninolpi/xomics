class Exon:
    def __init__(self,id:str,start:int,end:int,strand:str,gene_id:str,transcrit_id:str):
        self.id = id
        self.start = start
        self.end = end
        self.strand = strand
        
        self.gene_id = gene_id
        self.transcrit_id = transcrit_id