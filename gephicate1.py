# python script for yanking items from a film protocol into a gephi-ready csv

from sys import argv
import csv
import os
import gephifun

script, source = argv

action = raw_input('Please enter a relationship keyword: ')
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

gephifun.getPairs(text, dirname, action)

