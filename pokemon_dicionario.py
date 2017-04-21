import json

class Pokemon:
	def __init__(self, nome, ataque, defesa, vida):
		self.nome = nome
		self.ataque = ataque
		self.defesa = defesa
		self.vida = vida

with open("pokemons.json") as json_data:
	pokemons = json.loads(json_data)

pokemonsDict = dict

for p in pokemons:
	pokemonsDict[p["pokemons"].nome] = Pokemon(p["pokemons"][p].nome, [p].ataque , [p].defesa , [p].vida) 
	print(p)