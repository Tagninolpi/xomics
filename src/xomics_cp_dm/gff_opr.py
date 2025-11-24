from .annotation_class import Annotation
from .gene_class import Gene
from .transcrit_class import Transcrit
from .exon_class import Exon

def gff_operation():

    g1= Gene("g1","first",0,100,".")

    t1= Transcrit("t1","firstT",0,50,".","g1")
    t2= Transcrit("t2","secondT",50,100,".","g1")

    g1.transcrit_list.append(t1)
    g1.transcrit_list.append(t2)
    

    g2= Gene("g2","first",0,100,".")

    t1= Transcrit("t1","firstT",0,50,".","g2")
    t3= Transcrit("t3","secondT",50,100,".","g2")

    g2.transcrit_list.append(t1)
    g2.transcrit_list.append(t3)

    g2b= Gene("g2","first",0,100,".")

    t2= Transcrit("t2","firstT",0,50,".","g2")
    t3= Transcrit("t3","secondT",50,100,".","g2")

    g2b.transcrit_list.append(t2)
    g2b.transcrit_list.append(t3)



    #print(g1)
    #print(g2)
    #print(g2+g2b)

    a1 = Annotation([g1])
    a2 = Annotation([g2])
    a2b = Annotation([g2b])
    print(a1)
    print(a2)
    print(a2b)
    print(a1+a2+a2b)



    print("operation") 
    print("branch opr test")