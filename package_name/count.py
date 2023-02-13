## Description: "Count number of ACGT"
## Author: Huan Chen
## May-2021

import matplotlib.pylab as plt
import numpy as np

def count_sequence(res):
    """Return the plot information of target gene."""
    #Getting count of each type of nucleotide
    countnum = []
    labels = ['A','C','G','T']
    for i in labels:
        countnum.append(res.count(i))
    #using plt to draw the nucleotide distribution figure
    ind = [1,2,3,4]
    n_num = countnum
    _, ax_x = plt.subplots()
    ax_x.scatter(ind, countnum,color=['red','green','gold','deepskyblue'],s=90)
    #adding number for each nucleotide
    for i, txt in enumerate(n_num):
        ax_x.annotate(txt, (ind[i], countnum[i]))    
    plt.xticks(ind,labels)
    plt.ylabel('Count')
    plt.title('Nucleotide Distribution')
    plt.xlim(0.5,4.5)
    plt.ylim(0,np.max(countnum)+50)
    
    return countnum
