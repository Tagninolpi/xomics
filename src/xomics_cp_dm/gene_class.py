from .transcrit_class import Transcrit
class Gene:
    def __init__(self,id:str,name:str,start:int,end:int,strand:str):
        self.id = id
        self.name = name
        self.start = start
        self.end = end
        self.strand = strand

        self.transcrit_list:list[Transcrit] = []



