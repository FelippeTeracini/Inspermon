import pickle

inspermons_iniciais= {
	"Sharmander":{
		"ataque":5,"defesa":2,"vida":15
	},
	"Skuirtle":{
		"ataque":3,"defesa":5,"vida":10
	},
	"Bulbatauro":{
		"ataque":3,"defesa":3,"vida":20
	},
	"Sharmilion":{
		"ataque":12,"defesa":10,"vida":31
	},
	"Ivitauro":{
		"ataque":10,"defesa":15,"vida":35
	},
	"Uarturtle":{
		"ataque":15,"defesa":12,"vida":29
	},
	"Cheirazard":{
		"ataque":37,"defesa":30,"vida":45
	},
	"Venustauro":{
		"ataque":33,"defesa":38,"vida":47
	},
	"Blastoide":{
		"ataque":40,"defesa":35,"vida":40
	}
}

with open("inspermons_iniciais.pickle","wb") as arquivo_inspermons_iniciais:
	pickle.dump(inspermons_iniciais,arquivo_inspermons_iniciais)