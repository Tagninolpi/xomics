from .exon_class import Exon
class Transcrit:
    def __init__(self,id:str,name:str,start:int,end:int,strand:str,gff_line:str,gene_id:str):
        self.id = id
        self.name = name
        self.start = start
        self.end = end
        self.strand = strand

        self.line = gff_line
        
        self.exon_list:list[Exon] = []
        
        self.gene_id = gene_id

    def __eq__(self, transcrit_2):
        return transcrit_2.id == self.id and self.gene_id == transcrit_2.gene_id 
    
    def __repr__(self):
        msg =f"id:{self.id}"
        #msg +=f"\nexon list:{self.exon_list}"
        return msg
    def __str__(self):
        msg = f"id:{self.id} name:{self.name} start:{self.start} end:{self.end} strand:{self.strand} gene_id:{self.gene_id}"
        msg += f"\nexon list:{self.exon_list}"
        return msg
