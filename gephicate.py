# python script for yanking items from a film protocol into a gephi-ready csv

from sys import argv
import csv
import os

# possibly rework to get source and action via prompt?
script, source, action = argv

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
dirname = raw_input('Name of directory for results:')

os.makedirs(dirname)

# create a file to show which items have been taken from protocol
filename = 'list-of-relations.txt'
g = open(os.path.join(dirname,filename), 'a')
g.write('This list shows the relations from ' + source + ' that Gephicate used to construct the nodes and edges CSVs.')
text_list = text.split()

# move through text and extract words on either side of action, putting these both in g and in a list for further use
i = 0
pairs = []
for token in text_list:
    if token == action:
	   g.write('\n' + str(text_list[i-1: i+2]))
	   pairs += [text_list[i-1], text_list[i+1]]
    i += 1

# close protocol source file, as all necessary info is removed
f.close()
g.close()

# extract nodes from pairs
nodes = []
for item in pairs:
    if item in nodes:
	    pass
    else:
	    nodes.append(item)

# associate nodes with numbers
numbered_nodes = list(enumerate(nodes, 1))

# create nodes.csv and populate with numbered_nodes values
with open('nodes.csv', 'w') as csvfile:
    fieldnames = ['id', 'label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for x,y in numbered_nodes:
        writer.writerow({'id': x,'label': y})

# what is the purpose of this step?
# split list of pairs into a list of sources and targets
i = 1
source = []
target = []
for item in pairs:
    if i % 2 == 0:
	    target.append(item)
    else:
	    source.append(item)
    i += 1

# replace names in source and targets list with node numbers, zip
reverse_nodes = [(y,x) for x, y in numbered_nodes]
nodes_dict = dict(reverse_nodes)

source_column = []
for item in source:
    zork = nodes_dict.get(item)
    source_column.append(zork)

target_column = []
for item in target:
    zork = nodes_dict.get(item)
    target_column.append(zork)

edges = zip(source_column, target_column)

# weight edges
# get weights and zip together with edges
weights = [edges.count(x) for x in edges]
weighted_edges = zip(edges, weights)

# remove duplicates
final_edges = []
for tuple in weighted_edges:
    if tuple not in final_edges:
        final_edges.append(tuple)
	
	
# create edges csv
with open('edges.csv', 'w') as csvfile:
    fieldnames = ['source', 'target', 'type', 'weight']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for (x,y),z in final_edges:
        writer.writerow({'source': x,'target': y, 'type': 'directed', 'weight': z})
