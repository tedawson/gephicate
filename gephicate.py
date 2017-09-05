# python script for yanking items from a film protocol into a gephi-ready csv

from sys import argv
import csv

script, source, action = argv

f = open(source, 'r')
whole_text = f.read()
read_start = whole_text.find('<begin>')
read_end = whole_text.find('<end>')
text = whole_text[read_start: read_end]

# create a file to show which items have been taken from protocol
g = open('list-of-relations.txt', 'a')
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

# split list of pairs into a list of sources and targets
print pairs

i = 1
source = []
target = []
for item in pairs:
    if i % 2 == 0:
	    target.append(item)
    else:
	    source.append(item)
    i += 1

print source
print target
print numbered_nodes

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

print source
print source_column
print target_column
edges = zip(source_column, target_column)
print edges
# weight edges


# create edges csv
with open('edges.csv', 'w') as csvfile:
    fieldnames = ['source', 'target', 'type']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for x,y in edges:
        writer.writerow({'source': x,'target': y, 'type': 'directed'})
