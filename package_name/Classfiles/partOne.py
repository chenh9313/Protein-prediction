"""Genome sequence to protein sequence."""

import requests
import matplotlib.pylab as plt
import numpy as np
from bs4 import BeautifulSoup
import pandas as pd


class GenomeProtein:
    #Return the sequence of genome and protein

    def __init__(self, Genename, Locus, Link):
        # Define default input
        self.name = Genename
        self.locus = Locus
        self.link = Link
        self.seq = ' '

    #This is Part0: Showing basic info of input

    def basic_info(self):
        # show basic infomation
        print("The gene name is:" + self.name)
        print("The gene locus is: " + self.locus)
        print("The link address is: " + self.link)

    #This is Part1: Download information of target gene from website

    def download_sequence(self):
        """Return the genome sequence information of target gene from website"""
        # The following library downloads the data and stores it in a page variable
        page = requests.get(self.link)
        soup = BeautifulSoup(page.content, 'html.parser')
        # getting the raw target genome sequence and stores it in a rawseq variable
        rawseq = soup.find_all('p', style="font-family: monospace")
        rawseq2 = rawseq[0].get_text().replace(
            "\xa0", "").replace("\n", "").replace(" ", "")
        # using join and isdigit to remove numeric digits from string
        self.seq = ''.join([i for i in rawseq2 if not i.isdigit()])
        print("Length is:", len(self.seq), "pb")
        print(self.name, "genome sequence is:\n", self.seq)

    #This is Part2: Get the information of nucleotide distribution from part1

    def count_sequence(self):
        """Return the plot information of target gene"""
        # Getting count of each type of nucleotide
        count = []
        labels = ['A', 'C', 'G', 'T']
        for i in labels:
            count.append(self.seq.count(i))

        # using plt to draw the nucleotide distribution figure
        ind = [1, 2, 3, 4]
        n_num = count
        _, ax_x = plt.subplots()
        ax_x.scatter(ind, count, color=[
                   'red', 'green', 'gold', 'deepskyblue'], s=90)
        # adding number for each nucleotide
        for i, txt in enumerate(n_num):
            ax_x.annotate(txt, (ind[i], count[i]))
        plt.xticks(ind, labels)
        plt.ylabel('Count')
        plt.title('Nucleotide Distribution')
        plt.xlim(0.5, 4.5)
        plt.ylim(0, np.max(count)+50)

    #This is Part3: Get the information of gene structure from genome annotation files

    def structure_gene(self):
        """Return the gene structure information of target gene"""
        # Using pandas to read data

        # Finding gene locus and return the structure information
        # read in the files hosted on the datadoubleconfirm repository, get the link to the raw file
        url = 'https://gitlab.msu.edu/chenhua9/protein-prediction/-/raw/master/docs/files/Annotation_info.csv'
        df_file = pd.read_csv(url, error_bad_lines=False, sep='\t')
        res_s = df_file[df_file['Genename'].str.match(self.locus)]
        exon = len(res_s[res_s['Type'].str.match("exon")])
        print(self.locus, "has", exon, "exon")
        print(res_s)
        print(exon)

    #This is Part4: Get the information of protein sequence of the gene

    def protein_sequence(self):
        """Return the information of protein sequence of target gene"""
        # get the seq from part1 Download function
        # Providing the amino acid background information
        aa_dic = {
            "A": ["GCT", "GCC", "GCA", "GCG"],
            "L": ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"],
            "R": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
            "K": ["AAA", "AAG"], "N": ["AAT", "AAC"],
            "M": ["ATG"], "D": ["GAT", "GAC"],
            "F": ["TTT", "TTC"], "C": ["TGT", "TGC"],
            "P": ["CCT", "CCC", "CCA", "CCG"],
            "Q": ["CAA", "CAG"],
            "S": ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
            "E": ["GAA", "GAG"],
            "T": ["ACT", "ACC", "ACA", "ACG"],
            "G": ["GGT", "GGC", "GGA", "GGG"],
            "W": ["TGG"], "H": ["CAT", "CAC"],
            "Y": ["TAT", "TAC"],
            "I": ["ATT", "ATC", "ATA"],
            "V": ["GTT", "GTC", "GTA", "GTG"]}
        name = ["A", "L", "R", "K", "N", "M", "D", "F", "C", "P",
                "Q", "S", "E", "T", "G", "W", "H", "Y", "I", "V"]

        # getting the protein sequence
        res_p = []
        start = self.seq.index("ATG")+3
        for i in range(start, len(self.seq), 3):
            sed = self.seq[i:i+3]
            for j in name:
                if sed in aa_dic[j]:
                    posit = name.index(j)
            res_p.append([key for key in aa_dic.keys()][posit])
            proteinseq = ''.join(res_p)
        print(proteinseq)

        # count the amino acid number
        count = []
        for i in name:
            count.append(proteinseq.count(i))
        # using plt to draw the  distribution figure

        ind = list(range(1, 21))
        n_num = count
        _, ax_x = plt.subplots()
        ax_x.scatter(ind, count)
        for i, txt in enumerate(n_num):
            ax_x.annotate(txt, (ind[i], count[i]))
        plt.xticks(ind, name)
        plt.ylabel('Count')
        plt.title('Amino Acid Distribution')
        plt.xlim()
        plt.ylim(-1, np.max(count)+5)
        plt.plot(ind, count, color="green")
