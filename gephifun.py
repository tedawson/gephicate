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