"""Build evolution tree."""

import matplotlib.pylab as plt
import networkx as nx

class BuildTree:
    """Return the informtion of evolution pressure selection."""

    def __init__(self, Number, Inputinfo):
        self.num = Number
        self.info = Inputinfo

    def tree_builder(self):
        """Return the information of evolution tree."""
        #using network to draw the tree

        g_graph = nx.Graph()
        a_num = []
        for i in range(1,self.num):
            a_num.append("ADF"+str(i))
        g_graph.add_nodes_from(a_num)
        g_graph.add_edges_from(self.info)
        nx.draw(g_graph,with_labels=True, font_weight='bold',pos=nx.spring_layout(g_graph))
        plt.show()
        print(nx.info(g_graph))
