import random
import time

while True:

	lista_de_inspermons=open("Inspermons", "r")  # Criação dos Inspermons

	print("Bem vindo ao Inspermón")  # Início do jogo

	nome = input("Qual o nome do seu Inspermón? ")  # Caracterização do próprio personagem
	ataque1=5
	defesa=5
	vida=20

# Início do jogo:
	while True:  # Jogo

		comando = input("O que você deseja fazer? (Passear ou Dormir): ")  # Pergunta sobre o que o usuário deseja fazer
		comando = comando.lower()

		if comando == "dormir":   # Dormir: para o jogo e salva os dados
			break

# Inspermon adversário:
		elif comando == "passear":   # Passear em busca de novos inspermons
			print("Passeando...")

			time.sleep(1) 

			'''print("Você encontrou um Inspermon")  # Encontro com um inspermon			
			n_oponente=random.randint(0,len(lista_de_inspermons))   # Escolha aleatória do inspermon adversário
			nome_oponente=lista_de_inspermons[n_oponente-1]
			time.sleep(1)

			print("Voce esta batalhando contra {}".format(nome_oponente))  

			ataque_oponente=random.randint(defesa+1,defesa+5)  # Definição aleatória do atributos do Inspermon adversário
			defesa_oponente=random.randint(0,ataque1-1)
			vida_oponente=random.randint(10,20)
			time.sleep(1)'''

			print("Você encontrou um Inspermon")
			oponente=randon.randit(0,len(lista_de_inspermons))
			

			print("Este Inspermón possui os seguintes atributos: {} de ataque, {} de defesa e {} de vida" .format (ataque_oponente, defesa_oponente, vida_oponente))
			time.sleep(1)

			def batalha(x,y,z):
				return x-y+z


# Batalha:
			while True:

				while True:
					ataque1=5
					x=2

					ação=input("O que você deseja fazer? (Atacar ou Fugir): ")   # Pergunta se deseja atacar ou fugir

					if ação == "fugir":
						chancefugir=random.randit(1,2)  # Sorte de fuga

						if chancefugir==3:
							time.sleep(0.5)
							print("Você conseguiu fugir!")  # Fuga com sucesso
							x=1 # X
							break

						else:
							time.sleep(0.5)
							print("Você não conseguiu fugir!")  # Fuga sem sucesso
							x=2
							break

					if ação == "atacar": # Ataque
						print("1- Ataque do seu Inspermon, 2- Ataque de sorte ")
						time.sleep(0.5)
						ataque_ativo=int(input("Qual ataque deseja usar? 1 ou 2: "))  # Escolha do ataque a ser utilizado


						critico=random.randint(1,5)  # Chance de ataque critico

						if ataque_ativo==1:

							if critico==1:
								ataque1=ataque1*2

							if vida_oponente>0:  # Realização do ataque e atualizaçãovida_oponente= batalha_ataque1(vida_oponente,ataque1,defesa_oponente) da vida restante
								vida_oponente= batalha(vida_oponente,ataque1,defesa_oponente)
								print("{} deu {} de dano em seu oponente, agora ele tem {} de vida".format(nome,ataque1-defesa_oponente,vida_oponente))  # Cálculo da vida restante
								time.sleep(0.5)
								break 

							if vida_oponente<=0:    # Fim da batalha, vitória
								print("Voce derrotou esse Inspermon!")
								time.sleep(0.5)
								x=3
								break

						elif ataque_ativo == 2:  # Ataque 2 valor de ataque aleatório
							ataque2=random.randint(1,10)

							if critico==1:
								ataque2=ataque2*2

							if ataque2-defesa_oponente>0:  # Verifica se o inspermon causou dano no adverário
								vida_oponente= batalha(vida_oponente,ataque2,defesa_oponente)

								if vida_oponente>0:  # Realização do ataque e atualização da vida restante
									print("{} deu {} de dano em seu oponente, agora ele tem {} de vida".format(nome,ataque2-defesa_oponente,vida_oponente))  # Cálculo da vida restante
									time.sleep(0.5)
									break

							if ataque2-defesa_oponente<=0: # Notificação de não ter dado dano algum
								print("{} não deu dano em seu oponente, ele continua com {} de vida".format(nome,vida_oponente))
								time.sleep(0.5)
								break

							if vida_oponente<=0:  # Derrota do oponente
								print("Voce derrotou esse Inspermon!")
								time.sleep(0.5)
								x=3
								break

						else: # Erro de digitação
							print("Digite um ataque valido!")
							continue

				if x==2:  # X para fuga sem sucesso
					time.sleep(0.5)
					print("É a vez do seu oponente!")
					time.sleep(0.5)

					if ataque_oponente-defesa>0:  # Ataque do oponente após tentativa de fuga
						#if critico==1
						#ataque_oponente=ataque_oponente*2
						vida=vida-(ataque_oponente-defesa)
						if vida>0:
							print("O oponente deu {} de dano em {}! Agora ele tem {} de vida".format(ataque_oponente-defesa,nome,vida))
							time.sleep(0.5)
							continue

					if vida<=0:  # Derrota do seu inspermon
						print("Seu Inspermon desmaiou e foi levado para o InsperCenter")
						time.sleep(0.5)
						vida=20
						break

				elif x==1 or x==3:  # X para fuga com sucesso/parada do loop de batalha
					x=2
					break

			continue
			
		else:
			print("Digite um comando válido.")

	print("Até a proxima!")

	break

