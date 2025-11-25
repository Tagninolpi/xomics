from xomics_cp_dm.annotation_class import Annotation
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="gff_parse",
        description="test parser writer image generation"
    )

    parser.add_argument(
        "gff_path",
        help="Chemin vers le fichier GFF à parser"
    )

    parser.add_argument(
            "gene_id",
            help="id du gène"
        )

    parser.add_argument(
            "graph_name",
            help="nom de l'image"
        )

    parser.add_argument(
            "new_gff_name",
            help="nom de nouveau gff"
        )

    args = parser.parse_args()
        
    annot1 = Annotation.parse_gff(args.gff_path)

    print(f"annot1 = {annot1}")

    gene1 = annot1.get_gene(args.gene_id)

    print(f"gene1 = {gene1}")
    
    annot1.rna_len(args.graph_name)

    annot1.to_gff(args.new_gff_name)