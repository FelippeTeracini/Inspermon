import pickle

inspermons_dificeis= {
	"Nidorrei":{
		"ataque":35,"defesa":32,"vida":42
	},
	"Esnorlacs":{
		"ataque":30,"defesa":30,"vida":55
	},
	"Vaporneon":{
		"ataque":33,"defesa":35,"vida":44
	},
	"Dragoday":{
		"ataque":35,"defesa":34,"vida":48
	},
	"Arcanove":{
		"ataque":30,"defesa":38,"vida":45
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

with open("inspermons_dificeis.pickle","rb") as arquivo_inspermons_dificeis:
		dicionario_inspermons_dificeis=pickle.load(arquivo_inspermons_dificeis)