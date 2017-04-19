import random
import time
import pickle
def batalha(x,y,z):
	return x-y+z

with open("inspermons_noobs.pickle","rb") as arquivo_inspermons_noobs:
		dicionario_inspermons=pickle.load(arquivo_inspermons_noobs)

with open("inspermons_iniciais.pickle","rb") as arquivo_inspermons_iniciais:
		dicionario_inspermons_iniciais=pickle.load(arquivo_inspermons_iniciais)

xp = 0

while True:
	print("Bem vindo ao Inspermón")  # Início do jogo
	time.sleep(0.5)
	while True:


#    ==============================    Inspermon Inicial    ====================================


		print("Com qual Inspermón você deseja iniciar?")     # apresentação dos inspermons
		time.sleep(0.5)
		print("- Sharmander: Ataque = {} , Defesa = {} , Vida = {}".format(dicionario_inspermons_iniciais["Sharmander"]["ataque"],dicionario_inspermons_iniciais["Sharmander"]["defesa"],dicionario_inspermons_iniciais["Sharmander"]["vida"]))
		time.sleep(0.5)		
		print("- Skuirtle: Ataque = {} , Defesa = {} , Vida = {}".format(dicionario_inspermons_iniciais["Skuirtle"]["ataque"],dicionario_inspermons_iniciais["Skuirtle"]["defesa"],dicionario_inspermons_iniciais["Skuirtle"]["vida"]))
		time.sleep(0.5)		
		print("- Bulbatauro: Ataque = {} , Defesa = {} , Vida = {}".format(dicionario_inspermons_iniciais["Bubatauro"]["ataque"],dicionario_inspermons_iniciais["Bubatauro"]["defesa"],dicionario_inspermons_iniciais["Bubatauro"]["vida"]))
		time.sleep(0.5)	


		inspermon_inicial = input("->")   		# definição de qual inspermon sera o escolhido
		inspermon_inicial = inspermon_inicial.lower()

		'''def pokemon_inicial(pokemon):
			ataque1=dicionario_inspermons_iniciais["pokemon"]["ataque"]
			defesa=dicionario_inspermons_iniciais["pokemon"]["defesa"]
			vida=dicionario_inspermons_iniciais["pokemon"]["vida"]
			nome=pokemon.title()


		if inspermon_inicial == "sharmander":
			pokemon_inicial(sharmander)'''

		if inspermon_inicial == "sharmander":   			# definição dos atributos do inspermon
			ataque1=dicionario_inspermons_iniciais["Sharmander"]["ataque"]
			defesa=dicionario_inspermons_iniciais["Sharmander"]["defesa"]
			vida=dicionario_inspermons_iniciais["Sharmander"]["vida"]
			nome="Sharmander"
			break
		if inspermon_inicial == "skuirtle":
			ataque1=dicionario_inspermons_iniciais["Skuirtle"]["ataque"]
			defesa=dicionario_inspermons_iniciais["Skuirtle"]["defesa"]
			vida=dicionario_inspermons_iniciais["Skuirtle"]["vida"]
			nome="Skuirtle"
			break
		elif inspermon_inicial == "bulbatauro":
			ataque1=dicionario_inspermons_iniciais["Bubatauro"]["ataque"]
			defesa=dicionario_inspermons_iniciais["Bubatauro"]["defesa"]
			vida=dicionario_inspermons_iniciais["Bubatauro"]["vida"]
			nome="Bulbatauro"
			break
		else:
			print("Digite um Inspermón válido")
			time.sleep(0.5)
			continue


	while True:
		time.sleep(0.5)							# Mudança de nome do inspermon
		namechange = input("Deseja mudar o nome do seu Inspermón? ")  # Caracterização do próprio personagem
		namechange = namechange.lower()


		time.sleep(0.5)
		if namechange == "sim" or namechange == "s":
			nome=input("Qual será o nome do seu Inspermón? ")
			print("Agora o nome do seu Inspermón é {}".format(nome))
			break

		elif namechange == "nao" or namechange == "n" or namechange == "não":

			print("O nome do seu Inspermón ainda é {}".format(nome))
			break
		else:
			print("Digite um comando válido (Sim ou Não)")
			continue
	time.sleep(0.5)
	print("Seu Inspermón tem os seguintes atributos: Ataque:{}, Defesa:{}, Vida:{}".format(ataque1,defesa,vida))   # Apresentação do Inspermon
	time.sleep(0.5)

#    ==========================================     Início do jogo      ================================================
	while True:  # Jogo

		comando = input("O que você deseja fazer? (Passear ou Dormir): ")  # Pergunta sobre o que o usuário deseja fazer
		comando = comando.lower()

		if comando == "dormir":   # Dormir: para o jogo e salva os dados
			break

# Inspermon adversário:
		elif comando == "passear":   # Passear em busca de novos inspermons
			print("Passeando...")
			time.sleep(1) 

			print("Você encontrou um Inspermón")  # Encontro com um inspermon
			time.sleep(1)			
			nome_oponente=random.choice(list(dicionario_inspermons.keys()))   # Escolha aleatória do inspermon adversário


			print("Voce esta batalhando contra {}".format(nome_oponente))  
			time.sleep(1)
			ataque_oponente=dicionario_inspermons[nome_oponente]["ataque"] # Definição aleatória do atributos do Inspermon adversário
			defesa_oponente=dicionario_inspermons[nome_oponente]["defesa"]
			vida_oponente=dicionario_inspermons[nome_oponente]["vida"]


			print("Este Inspermón possui os seguintes atributos: Ataque: {}, Defesa: {} e Vida: {}".format(ataque_oponente,defesa_oponente,vida_oponente))
			time.sleep(1)


#       =================================================    Batalha    ===============================================
			while True:

				while True:
					x=2
					xp_ganho=10
					def funcaoxp(xp,xp_ganho):
						xp=xp+xp_ganho
						return xp

					ação=input("O que você deseja fazer? (Atacar ou Fugir): ")   # Pergunta se deseja atacar ou fugir

					if ação == "fugir":
						chancefugir=random.randint(1,2)  # Sorte de fuga

						if chancefugir==2:
							print("Você conseguiu fugir!")  # Fuga com sucesso
							time.sleep(0.5)
							x=1 # X
							break

						else:
							print("Você não conseguiu fugir!")  # Fuga sem sucesso
							time.sleep(0.5)
							x=2
							break

					if ação == "atacar": # Ataque
						print("1- Ataque normal, 2- Ataque de sorte ")
						time.sleep(0.5)
						ataque_ativo=int(input("Qual ataque deseja usar? 1 ou 2: "))  # Escolha do ataque a ser utilizado


						critico=random.randint(1,5)  # Chance de ataque critico

						if ataque_ativo==1:

							if critico==1:
								ataque1=ataque1*2
								print("ATAQUE CRÍTICO".format(nome))
								time.sleep(0.5)

								if vida_oponente>0:  # Realização do ataque e atualização da vida restante
									vida_oponente= batalha(vida_oponente,ataque1,defesa_oponente)

									if vida_oponente>0:
										print("{} deu {} de dano em {}, agora ele tem {} de vida".format(nome,ataque1-defesa_oponente,nome_oponente,vida_oponente))  # Cálculo da vida restante
										time.sleep(0.5)
										ataque1=ataque1/2
										break 

									else:			# Fim da batalha, vitória
										print("{} deu {} de dano em {}, ele desmaiou".format(nome,ataque1-defesa_oponente,nome_oponente))  # Cálculo da vida restante
										time.sleep(0.5)
										print("Voce derrotou {}!" .format(nome_oponente))
										time.sleep(0.5)
										xp=funcaoxp(xp,xp_ganho)   # Atualização da experiência										
										print("Voce recebeu {} de experiencia, agora você tem {}".format(xp_ganho,xp))
										time.sleep(0.5)
										ataque1=ataque1/2
										x=3
										break

							if critico!=1:
								if vida_oponente>0:  # Realização do ataque e atualização da vida restante
									vida_oponente= batalha(vida_oponente,ataque1,defesa_oponente)

									if vida_oponente>0:
										print("{} deu {} de dano em {}, agora ele tem {} de vida".format(nome,ataque1-defesa_oponente,nome_oponente,vida_oponente))  # Cálculo da vida restante
										time.sleep(0.5)
										break 

									else:			# Fim da batalha, vitória
										print("{} deu {} de dano em {}, ele desmaiou".format(nome,ataque1-defesa_oponente,nome_oponente))  # Cálculo da vida restante
										time.sleep(0.5)
										print("Voce derrotou {}!" .format(nome_oponente))

										time.sleep(0.5)
										xp=funcaoxp(xp,xp_ganho)   # Atualização da experiência										
										print("Voce recebeu {} de experiencia, agora você tem {}".format(xp_ganho,xp))
										time.sleep(0.5)
										x=3
										break



						if ataque_ativo == 2:  # Ataque 2 valor de ataque aleatório
							ataque2=random.randint(1,10)

							if critico==1:
								ataque2=ataque2*2
								print("ATAQUE CRÍTICO" .format(nome))
								time.sleep(0.5)

								if vida_oponente>0:  # Realização do ataque e atualização da vida restante
									vida_oponente= batalha(vida_oponente,ataque2,defesa_oponente)

									if vida_oponente>0:
										print("{} deu {} de dano em {}, agora ele tem {} de vida".format(nome,ataque2-defesa_oponente,nome_oponente,vida_oponente))  # Cálculo da vida restante
										time.sleep(0.5)
										ataque2=ataque2/2
										break 

									else:			# Fim da batalha, vitória
										print("{} deu {} de dano em {}, ele desmaiou".format(nome,ataque2-defesa_oponente,nome_oponente))  # Cálculo da vida restante
										time.sleep(0.5)
										print("Voce derrotou {}!" .format(nome_oponente))
										time.sleep(0.5)
										xp=funcaoxp(xp,xp_ganho)   # Atualização da experiência										
										print("Voce recebeu {} de experiencia, agora você tem {}".format(xp_ganho,xp))
										time.sleep(0.5)
										ataque2=ataque2/2
										x=3
										break

							if critico!=1:
								if vida_oponente>0 and ataque2-defesa_oponente>0 :  # Realização do ataque e atualização da vida restante
									vida_oponente= batalha(vida_oponente,ataque2,defesa_oponente)

									if vida_oponente>0:
										print("{} deu {} de dano em {}, agora ele tem {} de vida".format(nome,ataque2-defesa_oponente,nome_oponente,vida_oponente))  # Cálculo da vida restante
										time.sleep(0.5)
										break 

									else:			# Fim da batalha, vitória
										print("{} deu {} de dano em {}, ele desmaiou".format(nome,ataque2-defesa_oponente,nome_oponente))  # Cálculo da vida restante
										time.sleep(0.5)
										print("Voce derrotou {}!" .format(nome_oponente))

										time.sleep(0.5)
										xp=funcaoxp(xp,xp_ganho)   # Atualização da experiência										
										print("Voce recebeu {} de experiencia, agora você tem {}".format(xp_ganho,xp))
										time.sleep(0.5)
										x=3
										break


							if critico==1:      # Caso seja um ataque crítico
								ataque2=ataque2*2

							if ataque2-defesa_oponente>0:  # Verifica se o inspermon causou dano no adverário
								vida_oponente= batalha(vida_oponente,ataque2,defesa_oponente)

								if vida_oponente>0:  # Realização do ataque e atualização da vida restante
									print("{} deu {} de dano em {}, agora ele tem {} de vida".format(nome,ataque2-defesa_oponente,nome_oponente,vida_oponente))  # Cálculo da vida restante
									time.sleep(0.5)
									break

							if ataque2-defesa_oponente<=0: # Notificação de não ter dado dano algum
								print("{} não deu dano em {}, ele continua com {} de vida".format(nome,nome_oponente,vida_oponente))
								time.sleep(0.5)
								break

							if vida_oponente<=0:  # Derrota do oponente
								print("{} deu {} de dano em {}, agora ele tem 0 de vida".format(nome,ataque1-defesa_oponente,nome_oponente))  # Cálculo da vida restante
								time.sleep(0.5)
								print("Voce derrotou {}!" .format(nome_oponente))
								time.sleep(0.5)
								xp=funcaoxp(xp,xp_ganho)   # Atualização da experiência										
								print("Voce recebeu {} de experiencia, agora você tem {}".format(xp_ganho,xp))
								time.sleep(0.5)
								x=3
								break

						else: # Erro de digitação

							print("Digite um ataque válido!")
							time.sleep(0.5)
							continue
					else:
						print("Digite um comando válido!")
						time.sleep(0.5)
						continue

				if x==2:  # X para fuga sem sucesso
					if vida_oponente>0:
						time.sleep(0.5)
						print("É a vez do seu oponente!")
						time.sleep(0.5)

						critico_oponente = random.randint(0,5)

						if critico_oponente==1:   #Ataque crítico do oponente
							print("ATAQUE CRÍTICO")
							time.sleep(0.5)
							ataque_oponente=ataque_oponente*2

							if  ataque_oponente-defesa >0:   #Ataque crítico do oponente
								vida= batalha(vida, ataque_oponente, defesa)
								print("{} deu {} de dano em {}! Agora ele tem {} de vida".format(nome_oponente,ataque_oponente-defesa,nome,vida))
								time.sleep(0.5)
								ataque_oponente=ataque_oponente/2
								continue

							else:
								ataque_oponente=ataque_oponente/2   #Ataque crítico sem dano do oponente
								print("Seu Inspermón não levou dano")
								time.sleep(0.5)
								continue

						if critico_oponente!=1:
							if ataque_oponente- defesa>0:   #Ataque do oponente
								vida=batalha(vida, ataque_oponente, defesa)
								print("{} deu {} de dano em {}! Agora ele tem {} de vida".format(nome_oponente,ataque_oponente-defesa,nome,vida))		
								time.sleep(0.5)
								continue						
						
							else:   #Ataque do oponente sem dano
								print("Seu Inspermón não levou dano")
								time.sleep(0.5)
								continue

						if vida<=0:  # Derrota do seu inspermon
							print("Seu Inspermón desmaiou e foi levado para o InsperCenter")
							time.sleep(0.5)
							vida=20
							break

				elif x==1 or x==3:  # X para fuga com sucesso/parada do loop de batalha
					x=2
					break

			continue
			
		else:
			print("Digite um comando válido.")
			time.sleep(0.5)

	print("Até a proxima!")       # Fim do jogo

	break

