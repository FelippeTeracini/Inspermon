import json

class Pokemon:
	def __init__(self, pkname, attack, defence, live):
		self.pkname = pkname
		self.attack = attack

json_data=open("pokemons.json").read()
poke = json.loads(json_data)

pokeDict = dict

for p in poke:
	#pokeDict[p["pokemons"].pkname] = Pokemon(p["pokemons"][p].name, .attack , defense , live) 
	print(p[""])