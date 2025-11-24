class Exon:
    def __init__(self,id:str,start:int,end:int,strand:str,gene_id:str,transcrit_id:str):
        self.id = id
        self.start = start
        self.end = end
        self.strand = strand
        
        self.gene_id = gene_id
<<<<<<< HEAD
        self.transcrit_id = transcrit_id 
    
    def __repr__(self):
        return f"id:{self.id}"

    def __str__(self):
        msg = f"id:{self.id} name:{self.name} start:{self.start} end:{self.end} strand:{self.strand} gene id:{self.gene_id} transcrit id:{self.transcrit_id}"
        return msg
        
=======
        self.transcrit_id = transcrit_id
>>>>>>> b92b6c71dbdec54f511e5c14d45da86de6211615
