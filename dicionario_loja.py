import pickle

loja= {
	"vida1":{
		"preço":10, "ganho":1
	},
	"vida5":{
		"preço":50, "ganho":5
	},
	"vida10":{
		"preço":100, "ganho":10
	},
	"ataque1":{
		"preço":10, "ganho":1
	},
	"ataque5":{
		"preço":50, "ganho":5
	},
	"ataque10":{
		"preço":100, "ganho":10
	},
	"defesa1":{
		"preço":10, "ganho":1
	},
	"defesa5":{
		"preço":50, "ganho":5
	},
	"defesa10":{
		"preço":100, "ganho":10
	}
}	

with open("loja.pickle","wb") as arquivo_loja:
	pickle.dump(loja,arquivo_loja)