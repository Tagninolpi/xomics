# Plan du fichier gff_parse.py : 
# Transforme la colonne 9 en dictionnaire (savoir si la ligne est un gène, un exon, etc)
# Lire le fichier ligne par ligne
# Créer mes objets en fonction des lignes

from .gene_class import Gene
from .transcrit_class import Transcrit
from .exon_class import Exon

def parse_attributes(attr_str):
    attrs = {}
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

    return attrs


def parse_gff(gff_path):
    genes = []
    current_gene = None
    current_transcrit = None

    with open(gff_path) as f:
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
            attrs = parse_attributes(fields[8])

            if feature == "gene":
                gene_id = attrs.get("ID")
                gene_name = attrs.get("Name", gene_id)

                current_gene = Gene(
                    id=gene_id,
                    name=gene_name,
                    start=start,
                    end=end,
                    strand=strand
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
                    gene_id=parent_gene
                )

                current_gene.transcrit_list.append(current_transcrit)
                continue


            if feature == "exon":
                exon_id = attrs.get("ID", f"exon_{start}_{end}")
                parent_transcrit = attrs.get("Parent")
                parent_gene = current_gene.id  # toujours associé au gene courant

                exon = Exon(
                    id=exon_id,
                    start=start,
                    end=end,
                    strand=strand,
                    gene_id=parent_gene,
                    transcrit_id=parent_transcrit
                )

                current_transcrit.exon_list.append(exon)
                continue

    return genes
 