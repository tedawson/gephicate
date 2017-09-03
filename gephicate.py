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

print pairs
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

# next steps: replace names in pairs with node ids, create edges csv



