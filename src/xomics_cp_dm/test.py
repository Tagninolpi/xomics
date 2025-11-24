from xomics_cp_dm.gff_parse import parse_gff

genes = parse_gff("data/Human_sample1.gff")

print(f"Nombre de gènes trouvés : {len(genes)}")

for g in genes:
    print(f"\nGène : {g.id}  ({g.name})  [{g.start}-{g.end}]")
    print(f"  -> {len(g.transcrit_list)} transcrits")

    for t in g.transcrit_list:
        print(f"      Transcrit : {t.id}  ({t.name})  [{t.start}-{t.end}]")
        print(f"         -> {len(t.exon_list)} exons")
