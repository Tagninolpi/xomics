from .transcrit_class import Transcrit
class Gene:
    def __init__(self,id:str,name:str,start:int,end:int,strand:str,gff_line:str,):
        self.id = id
        self.name = name
        self.start = start
        self.end = end
        self.strand = strand

        self.line = gff_line

        self.transcrit_list:list[Transcrit] = [] 

    def __add__ (self,gene2):
        if not self.id == gene2.id:
            raise ValueError("Impossible de fusionner deux gènes différents.")
        for transcrit in gene2.transcrit_list:
            if not transcrit in self.transcrit_list:
                self.transcrit_list.append(transcrit)
        return self

    def __repr__(self):
        msg = f"\nid:{self.id} transcrit list:{self.transcrit_list}\n"
        return msg

    def __str__(self):
        msg = f"id:{self.id} name:{self.name} start:{self.start} end:{self.end} strand:{self.strand}"
        msg +=f"\ntranscrit list:{self.transcrit_list}"
        return msg

    #Implémentez la méthode __add__ pour la classe gène qui lèvera une exeptions si 
    #les deux gènes (self et l'autre) n'ont pas le même "GeneID" et retournera un 
    #nouvel objet Gene qui contiendra les transcrits présents dans les deux gènes initiaux.




