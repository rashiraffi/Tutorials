#Modelling road network of India's cities

import networkx as nx
import matplotlib.pyplot as plt
import random
G=nx.Graph()

#G=nx.DiGraph()

city_set=['Dehli','Bangalore','Hyd','Ahmedabad','Chennai','Kolkata','Surat','Pune','Jaipur']

for _ in city_set:
    G.add_node(_)

#nx.draw(G,with_labels=1)
#plt.show()

costs=[]
value=100
while(value<=2000):
    costs.append(value)
    value+=100

#print (costs)

#we are going to add 16 edges to this network
a=list(G.nodes())
while(G.number_of_edges()<16):
    c1=a[random.randint(0,8)]
    c2=a[random.randint(0,8)]
    if c1 != c2 and G.has_edge(c1,c2)==0:
        w=random.choice(costs)
        G.add_edge(c1,c2,weight=w)
pos=nx.circular_layout(G)
nx.draw(G,pos,with_labels=1)
plt.show()