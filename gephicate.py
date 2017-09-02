# python module for yanking items from a film protocol into a gephi-ready csv

from sys import argv

script, source, target, action = argv

f = open(source, 'r')
whole_text = f.read()
read_start = whole_text.find('<begin>')
read_end = whole_text.find('<end>')
text = whole_text[read_start: read_end]

z = len(action) + 1

g = open(target, 'a')

text_list = text.split()

for token in text_list:
    if token == action:
	    g.write('\n' + token)

f.close()
g.close()


# retired idea for finding words in plain text (not list)

'''i = 0
j = len(text)
while i < j:
    wordspot = text.find(action)
    if wordspot == -1:
        break
    else:
        print text[wordspot + z]
        texto = text[wordspot + z: ]
        i = i + (len(text) - len(texto))
        text = texto'''
	
# print text


