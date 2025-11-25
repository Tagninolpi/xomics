# xomics_cp_dm

xomics_cp_dm est une librairie Python permettant de lire, manipuler et exporter des annotations génomiques au format GFF.
Elle fournit un modèle orienté objet clair (Gene → Transcrit → Exon) ainsi qu’une classe Annotation permettant d’effectuer des opérations avancées sur des collections de gènes.

## Installation

Dans un projet uv, utlisez la commande suivante pour installer le package `xomics_cp_dm`
```sh
uv add  --index https://gitlab-pedago.univ-lyon1.fr/api/v4/projects/706/packages/pypi/simple --allow-insecure-host gitlab-pedago.univ-lyon1.fr xomics_cp_dm
```

## Utilisation

Pour utiliser la librairie `xomics_cp_dm` dans un script python, et créer une nouvelle `annotation` à partir d'un fichier gff:

```python 
from xomics_cp_dm.annotation_class import Annotation
annot1 = Annotation.parse_gff('data/Human_sample1.gff')
```

Où `Human_sample1.gff` est un fichier au format [GFF](https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md)


## La collection "Annotation"

La classe `Annotation` est définie par une liste de gènes `self.gene_list`. 

### Récupération d'un gène par son id

```python
gene1 = annot1.get_gene('GLP2R')
```
Où `GLP2R` est l'id du gène.

### Visualisation des longueurs de transcrits

la fonction `rna_len` permet de visualiser la longueur des transcrit de tous les gènes d'un collection et génère un graphique format **.png**

```python
annot1.rna_len('graphique_boxplot.png')
```

Où `graphique_boxplot.png` est le nom du fichier image générée.

### Export au format GFF

La fonction `to_gff` permet de générer un fichier au format **.gff** des gènes de la collection, ainsi que les transcrits et exons associés.

```python
annot1.to_gff('New_Human_sample1.gff')
```

Où `New_Human_sample1.gff` est le nom du nouveau fichier **gff** généré.

## L'objet Gene 

L'objet `Gene` est défini par les attribus suivants :
* id
* name
* start
* end
* strand

* line (ligne **gff** issue du parsage)

* transcrit_list (list des objets `Transcrit` du gène)

## L'objet Transcrit 

L'objet `Transcrit` est défini par les attribus suivants :

* id
* name
* start
* end
* strand

* line

* gene_id (l'id du `Gene` contenant ce `Transcrit`)
* exon_list (list des objets `Exon` du gène)

## L'objet Exon 
L'objet `Exon` est défini par les attribus suivants :
* id
* name
* start
* end
* strand

* line

* gene_id (l'id du `Gene` contenant ce `Transcrit`)
* transcrit_id (l'id du `Transcrit` contenant cet `Exon`)

