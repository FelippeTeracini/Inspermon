import pickle

Inspermons_iniciais={"Sharmander":{"ataque":5,"defesa":2,"vida":15},"Skuirtle":{"ataque":3,"defesa":5,"vida":10},"Bubatauro":{"ataque":3,"defesa":3,"vida":20}}

with open("inspermons_iniciais.pickle","wb") as arquivo_inspermons_iniciais:
	pickle.dump(Inspermons_iniciais,arquivo_inspermons_iniciais)