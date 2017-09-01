# python module for yanking items from a film protocol into a gephi-ready csv

from sys import argv

script, source, target, action = argv

f = open(source, 'r')
whole_text = f.read()
read_start = whole_text.find('<begin>')
read_end = whole_text.find('<end>')
text = whole_text[read_start: read_end]

z = len(action) + 1
i = 0
j = len(text)

while i < j:
    word = text.find(action)
    if word == -1:
        break
    else:
        print text[word + z]
        texto = text[word + z: ]
        i = i + (len(text) - len(texto))
        text = texto
	
# print text


