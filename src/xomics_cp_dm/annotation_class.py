from .gene_class import Gene
from .transcrit_class import Transcrit
from .exon_class import Exon
from matplotlib import figure


class Annotation:
    def __init__(self,genes_list):
        self.gene_list:list[Gene[Transcrit[Exon]]] = genes_list

    def get_gene(self,gene_id:str):
        for gene in self.gene_list:
            if gene.id == gene_id:
                return gene
        raise ValueError(f"Le gène '{gene_id}' est introuvable dans cette annotation.")
    
    def to_gff(self,filename:str):
        with open(filename, "w") as f:
            for gene in self.gene_list:
                f.write(gene.line + "\n")
                for transcrit in gene.transcrit_list:
                    f.write(transcrit.line + "\n")
                    for exon in transcrit.exon_list:
                        f.write(exon.line + "\n")

    def rna_len(self,filename:str):
        fig = figure.Figure(figsize=(max(6, len(self.gene_list) * 0.8), 6))
        ax   = fig.subplots(1, 1)
        RNAlens = []
        gene_names = []
        for gene in self.gene_list:
            transcrit_len = []
            for transcrit in gene.transcrit_list:
                lenght = 0
                for exon in transcrit.exon_list:
                    lenght += exon.end - exon.start
                transcrit_len.append(lenght)
            RNAlens.append(transcrit_len)
            gene_names.append(gene.name)
        print(RNAlens)
        print(gene_names)
        
        ax.boxplot(RNAlens, tick_labels=gene_names)
        fig.savefig(filename)



    def __add__(self,annot2):
        new_genes = []
        for gene2 in annot2.gene_list:
            for gene in self.gene_list:
                if gene2.id == gene.id:
                    new_genes.append(gene+gene2)
                else:
                    new_genes.append(gene)
            if not gene2 in self.gene_list:
                new_genes.append(gene2)
        self.gene_list = new_genes
        return self
    
    @staticmethod
    def parse_gff(file_path:str):

        genes = []
        current_gene = None
        current_transcrit = None

        with open(file_path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                fields = line.split("\t")
                chrom = fields[0]
                feature = fields[2]
                start = int(fields[3])
                end = int(fields[4])
                strand = fields[6]
                attrs = {}
                attr_str = fields[8]
                for item in attr_str.split(";"):
                    item = item.strip()
                    if not item:
                        continue

                    if "=" in item:
                        key, value = item.split("=", 1)
                    else:
                        parts = item.split(" ", 1)
                        if len(parts) == 2:
                            key, value = parts
                        else:
                            continue

                    attrs[key] = value

                if feature == "gene":
                    gene_id = attrs.get("ID")
                    gene_name = attrs.get("Name", gene_id)

                    current_gene = Gene(
                        id=gene_id,
                        name=gene_name,
                        start=start,
                        end=end,
                        strand=strand,
                        gff_line=line
                    )

                    genes.append(current_gene)
                    current_transcrit = None
                    continue


                if feature == "mRNA":
                    transcrit_id = attrs.get("ID")
                    transcrit_name = attrs.get("Name", transcrit_id)
                    parent_gene = attrs.get("Parent")

                    current_transcrit = Transcrit(
                        id=transcrit_id,
                        name=transcrit_name,
                        start=start,
                        end=end,
                        strand=strand,
                        gff_line=line,
                        gene_id=parent_gene
                    )

                    current_gene.transcrit_list.append(current_transcrit)
                    continue


                if feature == "exon":
                    exon_id = attrs.get("ID", f"exon_{start}_{end}")
                    parent_transcrit = attrs.get("Parent")
                    parent_gene = current_gene.id

                    exon = Exon(
                        id=exon_id,
                        start=start,
                        end=end,
                        strand=strand,
                        gff_line=line,
                        gene_id=parent_gene,
                        transcrit_id=parent_transcrit
                    )

                    current_transcrit.exon_list.append(exon)
                    continue

        return Annotation(genes)


    def __str__(self):
        return f"Genes:{self.gene_list}"
    
    def __repr__(self):
        return self.gene_list
