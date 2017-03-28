import random
while True:
	lista_de_inspermons:["Hsumon","Diegomon","Hsumon","Teramon"]
	print("Bem vindo ao Inspermón")
	nome = input("Qual o nome do seu Inspermón? ")
	ataque1=5
	ataque2=1
	defesa=5
	vida=20
	while True:
		comando = input("Oque você deseja fazer? ")
		if comando == "dormir":
			break
		elif comando == "passear":
			x=random.randint(0,len(lista_de_inspermons))
			print("Voce esta batalhando contra {}".format(x))
			ataque_oponente=2
			defesa_oponente=2
			vida_oponente=10
			

			continue
		else:
			print("Digite um comando válido.")