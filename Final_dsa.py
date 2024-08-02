import networkx as nx
import matplotlib.pyplot as plt
import itertools
import pandas as pd
import json

def add_edge(graph, node1, node2):
    if node1 not in graph:
        graph.add_node(node1)
    if node2 not in graph:
        graph.add_node(node2)
    graph.add_edge(node1, node2)

def graph_representation(G,text,L=[],V=[]):
    graph = nx.Graph()
    for i in G:
        for j in G[i]:
            node1,node2=(i),(j)
            add_edge(graph,node1,node2)
    
    node_colors = ['red' if node in L else 'skyblue' for node in graph.nodes]

    # Draw the graph
    nx.draw(graph, pos=nx.spring_layout(graph), with_labels=True, node_size=500, node_color=node_colors, font_size=10, font_weight='bold', edge_color='black', linewidths=1, alpha=0.7)
    plt.title('Graph Plot')
    plt.show()


def is_independent_set(graph, vertices):

    for vertex1 in vertices:
        for vertex2 in vertices:
            # Check if there is an edge between any pair of vertices in the set
            if vertex1 != vertex2 and vertex2 in graph[vertex1]:
                return False
    return True
def is_clique_set(graph, vertices):

    for vertex1 in vertices:
        for vertex2 in vertices:
            # Check if there is an edge between any pair of vertices in the set
            if vertex1 != vertex2 and vertex2 not in graph[vertex1]:
                return False
    return True

def complement_graph(graph, vertices):
    # Create a copy of the original graph
    complemented_graph = {vertex: [] for vertex in graph}

    # Add edges between vertices not in the independent set
    for vertex1 in vertices:
        for vertex2 in vertices:
            if vertex1!=vertex2:
                if vertex2 not in graph[vertex1]:
                    complemented_graph[vertex1].append(vertex2)
                    complemented_graph[vertex2].append(vertex1)
    for vertex in complemented_graph:
        complemented_graph[vertex]=list(set(complemented_graph[vertex]))

    return complemented_graph

def find_independent_sets(graph, k):
    vertices = list(graph.keys())
    independent_sets = []
    for combination in itertools.combinations(vertices, k):
        if is_independent_set(graph, combination):
            independent_sets.append(list(combination))
    return independent_sets

def find_cliques(graph, k):
    vertices = list(graph.keys())
    clique_sets = []
    for combination in itertools.combinations(vertices, k):
        if is_clique_set(graph, combination):
            clique_sets.append(list(combination))
    return clique_sets


def read_csv_to_list(filename):
    df = pd.read_csv(filename)
    data_list = df.values.tolist()
    return data_list

filename = 'input_data.csv'
edges = read_csv_to_list(filename)
graph={}
for edge in edges:
    if edge[0] in graph:
        graph[edge[0]].append(edge[1])
    else:
        graph[edge[0]]=[edge[1]]
    if edge[1] in graph:
        graph[edge[1]].append(edge[0])
    else:
        graph[edge[1]]=[edge[0]]

for vertex in graph:
    graph[vertex]=list(set(graph[vertex]))


vertices=[]
for vertex in graph:
    vertices.append(vertex)


complemented_graph = complement_graph(graph, vertices)

# Find independent sets of size k
k = int(input("Enter the size k: "))  # Define the size of the independent set


independent_sets = find_independent_sets(graph, k)
sho=0
if independent_sets:
    print(f"The independent sets of size {k} are:")
    for ind_set in independent_sets:
        print(ind_set)
    sho+=1
    #print(independent_sets[0])
else:
    print(f"No independent set of size {k} found.")


clique_sets = find_cliques(complemented_graph, k)

if clique_sets:
    print(f"The clique sets of size {k} are:")
    for ind_set in clique_sets:
        print(ind_set)
    #print(graph,complemented_graph)
    sho+=1
else:
    print(f"No clique set of size {k} found.")
if sho==2:
    e1=[]
    for i in vertices:
        d={}
        d["id"]=i
        if i in independent_sets[0]:
            d["group"]=2
        else:
            d["group"]=1
        e1.append(d)
    for i in vertices:
        d={}
        d["id"]=str(i)
        if i in clique_sets[0]:
            d["group"]=3
        else:
            d["group"]=4
        e1.append(d)
    dict1=[]
    for i in graph:
        for j in graph[i]:

            das={}
            das["source"]=i
            das["target"]=j
            co=0
            if i not in independent_sets[0]:
                das["value"]=1
            elif j not in independent_sets[0]:
                das["value"]=1
            else:
                das["value"]=2

            dict1.append(das)
    for i in complemented_graph:
        for j in complemented_graph[i]:

            das={}
            das["source"]=str(i)
            das["target"]=str(j)
            co=0
            if i in clique_sets[0]:
                if j in clique_sets[0]:
                    das["value"]=3
                else:
                    das["value"]=4
            else:
                das["value"]=4

            dict1.append(das)
    datas={}
    datas["nodes"]=e1
    datas["links"]=dict1

    #Creating starwars.json
    jsonFilePath = r'edges1.json'
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(datas, indent=4))
            



