import json
from pprint import pprint
filename = 'vklads.json'

with open(filename, 'r') as f_obj:
	vklads = json.load(f_obj)

pprint(vklads)
	

