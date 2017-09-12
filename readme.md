# Gephicate

Gephicate is a program which takes human-made protocols of interactions and parses the information into CSVs that are suitable for importing into Gephi. Thus, it eliminates the mindless middle stage in creating network visualizations of relationships in literary works. This program functions, but is still in-progress. Quite inelegant, and a panoply of errors would be thoroughly unsurprising.

## How to Gephicate

Begin with a protocol. This can contain whatever information you want, but the portion to be graphed should be marked off with a `<begin>` and `<end>` tag, and it should be plaintext. All relationships should be indicated with three words, a name on either side of a one word action. For instance "Bob KISSES Sue" or "Joe TALKSTO Mike". It is recommended to use all caps for actions, but not required (this reduces the risk of accidentally using the key action term in some other context). Anything placed within angle brackets ("<>") is "commented out" and will be skipped when the protocol is parsed. A protocol may include a variety of different actions. See "sample.txt" above for one possible example of what the final thing might look like.

Once you have the protocol, it is time to Gephicate. Gephicate is a Python script (thus you must have Python installed on your computer and have at least some idea of how to run scripts. Someday there will be a handy link here for those that are just getting started with Python, in the meantime, please consult your trusted search engine). From the commandline, run Gephicate with the path of your protocol as an argument. Thus, if using sample.txt as a protocol you would enter this (assuming everything is in the same directory):

```
python gephicate.py sample.txt
```

Gephicate will then prompt you to name a directory for the results and a relationship keyword. In entering the keyword, be sure to use a word exactly as in your protocol. Thus, to investigate touches in sample.txt, you would enter "TOUCHES".

Whatever directory you've created will contain three files. "list-of-relations.txt" is just an easy check to see that Gephicate pulled out the items you are interested in. It should contain a series of three item sets that reflect the relationships you were looking for. The other items are "nodes.csv" and "edges.csv". These we will import into Gephi.

Open a new project on Gephi. Under the File menu, select "Import Spreadsheet." Select "nodes.csv," check that it is being imported as "nodes" and click "next" then "finish." Then do the same, but importing "edges.csv" as "edges." And voila. The rest is up to Gephi.

## Things as yet left undone
- wrap chunks in functions for modularity
- make style consistent and pythonic
- addressing language in readme... don't push too hard here though. Don't want to get a hernia.