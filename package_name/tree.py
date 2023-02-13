## Description: "Return the gene structure information of target gene"
## Author: Huan Chen
## May-2021

"""This is Part6: Get the information of protein sequence of the gene """
import matplotlib.pylab as plt
import networkx as nx

def tree_builder(num_ber,input_info):
    """Return the information of evolution tree."""
    g_graph = nx.Graph()
    a_num = []
    for i in range(1,num_ber):
       a_num.append("ADF"+str(i))
    g_graph.add_nodes_from(a_num)
    g_graph.add_edges_from(input_info)
    nx.draw(g_graph,with_labels=True, font_weight='bold',pos=nx.spring_layout(g_graph))
    plt.show()
    print(nx.info(g_graph))
    return nx.info(g_graph).split("\n")[4].split(":")[1].replace('   ','')
