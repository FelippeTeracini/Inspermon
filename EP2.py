import random

while True:

	lista_de_inspermons:["Hsumon","Diegomon","Hsumon","Teramon"] #nomes dos Inspermóns existentes

	print("Bem vindo ao Inspermón")  #início do jogo
	nome = input("Qual o nome do seu Inspermón? ")  #caracterização do próprio personagem 
	ataque1=5
	ataque2=1
	defesa=5
	vida=20

	while True:  #jogo
		comando = input("O que você deseja fazer? ")  #pergunta do que vai ser realizado entre as opções 

		if comando == "dormir":  #sair do jogo
			break

		elif comando == "passear":  #passear, procurar um inspermon pra batalha
			x=random.randint(0,len(lista_de_inspermons)) #randomização das caracteristicas do oponente
			print("Voce esta batalhando contra {}".format(x))
			ataque_oponente=2
			defesa_oponente=2
			vida_oponente=10
			continue
			
		else:
			print("Digite um comando válido.")