# python script for yanking items from a film protocol into a gephi-ready csv

from sys import argv
import csv
import os
import gephifun

script, source = argv

action = raw_input('Please enter a relationship keyword: ')
print "Weighting key: 1 is normal; numbers larger than 1 will exaggerate weight, numbers smaller than 1 diminish it. If you don't know what to put, try .5"
heavyness = float(raw_input('Enter a weighting factor: '))
# get the protocol ready
f = open(source, 'r')
whole_text = f.read()
read_start = whole_text.find('<begin>')
read_end = whole_text.find('<end>')
main_text = whole_text[read_start: read_end]

# skip stuff in angle brackets
text = ''
for char in main_text:
	if char == '<':
		inside = 1
	elif inside == 1 and char == '>':
		inside = 0
	elif inside == 1:
		continue
	else:
		text += char

# create a directory for files
dirname = raw_input('Name of directory for results: ')
os.makedirs(dirname)
pairs = gephifun.getPairs(text, dirname, action)

# close protocol source file, as all necessary info is removed
f.close()

nodes, nodes_dict = gephifun.getNodes(pairs)
edges = gephifun.getEdges(pairs, nodes_dict)
weighted_edges = gephifun.weightEdges(edges, heavyness)
final_edges = gephifun.removeDuplicates(weighted_edges)

# create nodes.csv and populate with numbered_nodes values
with open(os.path.join(dirname,'nodes.csv'), 'w') as csvfile:
    fieldnames = ['id', 'label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for x,y in nodes:
        writer.writerow({'id': x,'label': y})

# create edges.csv
with open(os.path.join(dirname,'edges.csv'), 'w') as csvfile:
    fieldnames = ['source', 'target', 'type', 'weight']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for (x,y),z in final_edges:
        writer.writerow({'source': x,'target': y, 'type': 'directed', 'weight': z})