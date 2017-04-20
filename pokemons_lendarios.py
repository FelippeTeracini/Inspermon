<<<<<<< HEAD
import pickle 

inspermons_lendarios= {
=======
qpokemons_lendarios= {
>>>>>>> 19bfa680506867c6030dd18e486227e16e7a46d0
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