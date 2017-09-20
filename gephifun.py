# functions for gephicate

import os

def getPairs(text, dirname, action):
	'''Extracts nodes and edges from your protocol, putting them in a file and a list called "pairs"'''
	filename = 'list-of-relations.txt'
	g = open(os.path.join(dirname,filename), 'a')
	g.write('This list shows the relations that Gephicate used to construct the nodes and edges CSVs.')
	text_list = text.split()

	# move through text and extract words on either side of action, putting these both in g and in a list for further use
	i = 0
	pairs = []
	for token in text_list:
		if token == action:
		   g.write('\n' + str(text_list[i-1: i+2]))
		   pairs += [text_list[i-1], text_list[i+1]]
		i += 1

	# close list of relations
	g.close()
	return pairs
	
def getNodes(pairs):
	'''Extracts node names from "pairs" and numbers them, returning a list of tuples'''
	node_names = []
	for item in pairs:
		if item in node_names:
			pass
		else:
			node_names.append(item)
	# associate nodes with numbers
	nodes = list(enumerate(node_names, 1))
	reverse_nodes = [(y,x) for x, y in nodes]
	nodes_dict = dict(reverse_nodes)
	return nodes, nodes_dict
	
def getEdges(pairs, nodes_dict):
	'''gets edges'''
	# need to do this with two lists like in gephicate?
	sources = []
	targets = []
	i = 1
	for item in pairs:
		if i % 2 == 0:
			target = nodes_dict.get(item)
			targets.append(target)
		else:
			source = nodes_dict.get(item)
			sources.append(source)
		i += 1
	edges = zip(sources, targets)
	return edges
	
def weightEdges(edges):
	'''assigns weights to edges'''
	weights = [edges.count(x) for x in edges]
	weighted_edges = zip(edges, weights)
	return weighted_edges


#def writeCSVs():

