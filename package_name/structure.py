## Description: "Return the gene structure information of target gene"
## Author: Huan Chen
## May-2021

"""This is Part3: Get the information of gene structure from genome annotation files """
import pandas as pd

def structure_gene(locus):
    """Return the gene structure information of target gene."""
    #Finding gene locus and return the structure information
    url = 'https://gitlab.msu.edu/chenhua9/protein-prediction/-/raw/master/docs/files/Annotation_info.csv'
    df_file = pd.read_csv(url, error_bad_lines=False, sep='\t')
    res_s = df_file[df_file['Genename'].str.match(locus)]
    exon = len(res_s[res_s['Type'].str.match("exon")])
    print(locus,"has",exon,"exon")
    print(res_s)
    return exon
