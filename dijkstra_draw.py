import networkx as nx
import matplotlib.pyplot as plt

# WS network (small-world graph)
# generate a WS network which has 1000 nodes,
# each node has 2 neighbour nodes,
# random reconnection probability was 0.
WS = nx.random_graphs.watts_strogatz_graph(1000, 2, 0)

import random
x = 100
y = random.randint(0, 999)
for a in range(0, x):
    WS.add_edge(random.randint(0, 999), random.randint(0, 999), length = y)

# circular layout
pos = nx.circular_layout(WS)
nx.draw(WS, pos, with_labels = False, node_size = 30)
plt.show()
