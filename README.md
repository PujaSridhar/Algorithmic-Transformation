#### Algorithmic-Transformation (Independent Set to Clique) 
This Python script is designed to transform Independent sets to Clique sets. It utilizes the NetworkX library for graph operations and 3D force graph for visualization.

## Prerequisites
Python 3.x
NetworkX library
Pandas library
Installation

Copy code
pip install networkx pandas
Usage
Prepare your graph data in a CSV file. Each row should represent an edge between two nodes.

Make sure you clear the edges1.json before running the script
Run the script:

Copy code
python Final_dsa.py
Enter the size k of the independent sets you want to find when prompted.

The script will display the independent sets and clique sets of size k found in the graph, if any.

Additionally, the script generates a JSON file containing the graph data and analysis results for visualization purposes.

Input Data Format
The input data should be provided in a CSV file with two columns representing the source and target nodes of each edge.

Output
The script prints the independent sets and clique sets of the specified size, if found.
It generates a JSON file containing the graph data and analysis results for visualization. The JSON file is named edges1.json.
Visualization
The script visualizes the 3D force graph. Nodes belonging to one clique set is colored red, while nodes belonging to another clique set is colored blue.
