"""This is Part4: Get the information of protein sequence of the gene """
import matplotlib.pylab as plt
import numpy as np

def protein_sequence(seq):
    """Return the information of protein sequence of target gene."""
    #get the seq from part1 Download function
    #Providing the amino acid background information by using dictory
    aa_dic = {"A" : ["GCT","GCC","GCA","GCG"],
        "L" : ["TTA","TTG","CTT","CTC","CTA","CTG"],
        "R" : ["CGT","CGC","CGA","CGG","AGA","AGG"],
        "K" : ["AAA","AAG"],"N" : ["AAT","AAC"],
        "M" : ["ATG"],"D" : ["GAT","GAC"],
        "F" : ["TTT","TTC"],"C" : ["TGT","TGC"],
        "P" : ["CCT","CCC","CCA","CCG"],
        "Q" : ["CAA","CAG"],
        "S" : ["TCT","TCC","TCA","TCG","AGT","AGC"],
        "E" : ["GAA","GAG"],
        "T" : ["ACT","ACC","ACA","ACG"],
        "G" : ["GGT","GGC","GGA","GGG"],
        "W" : ["TGG"],"H" : ["CAT","CAC"],
        "Y" : ["TAT","TAC"],
        "I" : ["ATT","ATC","ATA"],
        "V" : ["GTT","GTC","GTA","GTG"]}
    name = ["A","L","R","K","N","M","D","F","C","P","Q","S","E","T","G","W","H","Y","I","V"]
    #getting the protein sequence
    res_p = []
    start = seq.index("ATG")+3
    for i in range(start,len(seq),3):
        sed = seq[i:i+3]
        for j in name:
            if sed in aa_dic[j]:
                posit = name.index(j)
        res_p.append([key for key in aa_dic.keys()][posit])
        proteinseq = ''.join(res_p)
#    return proteinseq
    #count the amino acid number
    count = []
    for i in name:
        count.append(proteinseq.count(i))
    ind = list(range(1, 21))
    n_num = count
    _, ax_x = plt.subplots()
    ax_x.scatter(ind, count)
    for i, txt in enumerate(n_num):
        ax_x.annotate(txt, (ind[i], count[i]))
    plt.xticks(ind,name)
    plt.ylabel('Count')
    plt.title('Amino Acid Distribution')
    plt.xlim()
    plt.ylim(-1,np.max(count)+5)
    plt.plot(ind, count,color="green")
    return proteinseq
