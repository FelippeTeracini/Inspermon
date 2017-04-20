import pickle

inspermons_faceis= {
	"Pikaxu":{
		"ataque":3,"defesa":2,"vida":18
	},
	"Tatata":{
		"ataque":5,"defesa":2,"vida":12
	},
	"Pigey":{
		"ataque":2,"defesa":1,"vida":15
	},
	"Dogerpie":{
		"ataque":3,"defesa":4,"vida":10
	},
	"Magipark":{
		"ataque":1,"defesa":1,"vida":20
	},
	"Sharmander":{
		"ataque":5,"defesa":2,"vida":15
	},
	"Skuirtle":{
		"ataque":3,"defesa":5,"vida":10
	},
	"Bulbatauro":{
		"ataque":3,"defesa":3,"vida":20
	}	
}

with open("inspermons_faceis.pickle","wb") as arquivo_inspermons_faceis:
	pickle.dump(inspermons_faceis,arquivo_inspermons_faceis)