# Gephicate

Gephicate is a program which takes human-made protocols of interactions and parses the information into CSVs that are suitable for importing into Gephi. Thus, it eliminates the mindless middle stage in creating network visualizations of relationships in literary works. This program functions, but is still in-progress. Quite inelegant, and a panoply of errors would be thoroughly unsurprising.

## How to Gephicate

Begin with a protocol. This can contain whatever information you want, but the portion to be graphed should be marked off with a `<begin>` and `<end>` tag, and it should be plaintext. All relationships should be indicated with three words, a name on either side of a one word action. For instance "Bob KISSES Sue" or "Joe TALKSTO Mike". It is recommended to use all caps for actions, but not required (this reduces the risk of accidentally using the key action term in some other context. A protocol may include a variety of different actions. See "sample.txt" above for one possible example of what the final thing might look like.

Once you have the protocol, it is time to Gephicate. Gephicate is a Python script (thus you must have Python installed on your computer and have at least some idea of how to run scripts. Someday there will be a handy link here for those that are just getting started with Python, in the meantime, please consult your trusted search engine). From the commandline, run Gephy with two arguments, first the path of the protocol, then the action you are interested in graphing. Thus, if using sample.txt as a protocol and wishing to create a graph of who touches whom, you would enter this (assuming everything is in the same directory):

```
python gephicate.py sample.txt "TOUCHES"
```

This will produce three files. "list-of-relations.txt" is just an easy check to see that Gephicate pulled out the items you are interested in. It should contain a series of three item sets that reflect the relationships you were looking for. The other items are "nodes.csv" and "edges.csv". These we will import into Gephy.

Open a new project on Gephi. Click on the data laboratory tab, and then on the button that says "Import Spreadsheet." Select "nodes.csv," check that it is being imported as "nodes" and click OK twice. Then do the same, but importing "edges.csv" as "edges." And voila. The rest is up to Gephi.

## Things as yet left undone
- wrap chunks in functions for modularity
- make style consistent and pythonic
- addressing language in readme... don't push too hard here though. Don't want to get a hernia.