
import pickle 

inspermons_lendarios= {

	"Articuno":{
		"ataque":80,"defesa":70,"vida":100
	},
	"Zapdos":{
		"ataque":70,"defesa":80,"vida":100
	},
	"Moltres":{
		"ataque":75,"defesa":75,"vida":100
	}
}

with open("inspermons_lendarios.pickle","wb") as arquivo_inspermons_lendarios:
	pickle.dump(inspermons_lendarios,arquivo_inspermons_lendarios)