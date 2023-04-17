from owlready2 import *



onto = get_ontology("climate-change.owl").load()

print(onto.Countries)