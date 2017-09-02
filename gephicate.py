# python module for yanking items from a film protocol into a gephi-ready csv

from sys import argv

script, source, target, action = argv

f = open(source, 'r')
whole_text = f.read()
read_start = whole_text.find('<begin>')
read_end = whole_text.find('<end>')
text = whole_text[read_start: read_end]

g = open(target, 'a')

text_list = text.split()

i = 0

for token in text_list:
    if token == action:
	   g.write('\n' + str(text_list[i-1: i+2]))
    i += 1

f.close()
g.close()


# retired idea for finding words in plain text (not list)

'''z = len(action) + 1
i = 0
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


