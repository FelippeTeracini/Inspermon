import random
import time
import pickle
import os 

sim=["sim", "s"]
nao=["nao","n","não"]
def batalha(x,y,z):
	return x-y+z

def funcaoxp(xp,xp_ganho):
	xp=xp+xp_ganho
	return xp

def MudaNome(nome):
	while True:

		x = input("Deseja mudar o nome do seu Inspermón?\n ")
		x = x.lower()

		if x in sim:
			nome = input("Qual será o nome do seu Inspermón?\n ")
			print("Agora o nome do seu Inspermón é {}".format(nome))
			break

		elif x in nao:
			print("O nome do seu Inspermón ainda é {}".format(nome))
			break

		else:
			print("Digite um comando válido (Sim ou Não)")
			continue
		nome = nome
	return nome



with open("inspermons_faceis.pickle","rb") as arquivo_inspermons_faceis:
		dicionario_inspermons_faceis=pickle.load(arquivo_inspermons_faceis)

with open("inspermons_iniciais.pickle","rb") as arquivo_inspermons_iniciais:
		dicionario_inspermons_iniciais=pickle.load(arquivo_inspermons_iniciais)

with open("inspermons_medios.pickle","rb") as arquivo_inspermons_medios:
		dicionario_inspermons_medios=pickle.load(arquivo_inspermons_medios)

with open("inspermons_dificeis.pickle","rb") as arquivo_inspermons_dificeis:
		dicionario_inspermons_dificeis=pickle.load(arquivo_inspermons_dificeis)

with open("inspermons_lendarios.pickle","rb") as arquivo_inspermons_lendarios:
		dicionario_inspermons_lendarios=pickle.load(arquivo_inspermons_lendarios)


xp = 190

while True:
	print("Bem vindo ao Inspermón")  # Início do jogo

	'''abrir_salvo=input("Deseja abrir jogo salvo? \n ")

	if abrir_salvo in sim:
		with open("jogo_salvo","rb") as arquivo_jogo_salvo:
			dados_salvos=pickle.load(arquivo_jogo_salvo)
			
		nome=dados_salvos["nome"]
		ataque1=dados_salvos["ataque"]
		defesa=dados_salvos["defesa"]
		vida_inicial=dados_salvos["vida"]
		xp=dados_salvos["xp"]

	time.sleep(0.5)'''
	while True:



#    ==============================    Inspermon Inicial    ====================================

		def pokemon_inicial(lista,pokemon,Nindex):
			ataque1=lista[pokemon]["ataque"]
			defesa=lista[pokemon]["defesa"]
			vida_inicial=lista[pokemon]["vida"]
			index=Nindex
			evolucao=1
			return(ataque1,defesa,vida_inicial,index,evolucao)

		print("Com qual Inspermón você deseja iniciar?")     # apresentação dos inspermons
		time.sleep(0.5)
		print("- Sharmander: Ataque = {} , Defesa = {} , Vida = {}".format(dicionario_inspermons_iniciais["Sharmander"]["ataque"],dicionario_inspermons_iniciais["Sharmander"]["defesa"],dicionario_inspermons_iniciais["Sharmander"]["vida"]))
		time.sleep(0.5)		
		print("- Skuirtle: Ataque = {} , Defesa = {} , Vida = {}".format(dicionario_inspermons_iniciais["Skuirtle"]["ataque"],dicionario_inspermons_iniciais["Skuirtle"]["defesa"],dicionario_inspermons_iniciais["Skuirtle"]["vida"]))
		time.sleep(0.5)		
		print("- Bulbatauro: Ataque = {} , Defesa = {} , Vida = {}".format(dicionario_inspermons_iniciais["Bulbatauro"]["ataque"],dicionario_inspermons_iniciais["Bulbatauro"]["defesa"],dicionario_inspermons_iniciais["Bulbatauro"]["vida"]))
		time.sleep(0.5)	


		inspermon_inicial = input("->")   		# definição de qual inspermon sera o escolhido
		inspermon_inicial = inspermon_inicial.lower()


		if inspermon_inicial == "sharmander":
			ataque1,defesa,vida_inicial,index,evolucao=pokemon_inicial(dicionario_inspermons_iniciais,"Sharmander",1)
			nome="Sharmander"
			break

		if inspermon_inicial == "skuirtle":
			ataque1,defesa,vida_inicial,index,evolucao=pokemon_inicial(dicionario_inspermons_iniciais,"Skuirtle",2)
			nome="Skuirtle"

			break
		elif inspermon_inicial == "bulbatauro":
			ataque1,defesa,vida_inicial,index,evolucao=pokemon_inicial(dicionario_inspermons_iniciais,"Bulbatauro",3)
			nome="Bulbatauro"
			break

		else:
			print("Digite um Inspermón válido")
			time.sleep(0.5)
			continue

	nome=MudaNome(nome)


	vida = vida_inicial
	time.sleep(0.5)
	print("Seu Inspermón tem os seguintes atributos: Ataque:{}, Defesa:{}, Vida:{}".format(ataque1,defesa,vida))   # Apresentação do Inspermon
	time.sleep(0.5)
	dinheiro=100000
#    ==========================================     Início do jogo      ================================================
	while True:  # Jogo
		vida = vida_inicial
		comando = input("O que você deseja fazer? (Passear, Loja ou Dormir):\n ")  # Pergunta sobre o que o usuário deseja fazer
		comando = comando.lower()

		def escolha_adversário(lista):

			nome_oponente=random.choice(list(lista.keys()))   # Escolha aleatória do inspermon adversário
			ataque_oponente=lista[nome_oponente]["ataque"] 
			defesa_oponente=lista[nome_oponente]["defesa"]
			vida_oponente=lista[nome_oponente]["vida"]
			return (nome_oponente,ataque_oponente,defesa_oponente,vida_oponente)

		if comando == "dormir":   # Dormir: para o jogo e salva os dados
			break

		elif comando == "loja":
			while True:
				time.sleep(0.5)
				compra=input("Você está na loja, o que quer comprar: ataque, defesa ou vida? Você também pode sair digitando: sair\n ")

			
				if compra=="ataque":
					time.sleep(1)
					print("Você pode aumentar seu ataque em 1 por 10 inpermoedas, 5 por 50 inpermoedas ou 10 por 100 inpermoedas")
					compra_ataque=input("Quanto deseja comprar?\n ")
					time.sleep(1)

					while True:
						if compra_ataque==1 and dinheiro>=10:
							print("Seu ataque aumentou 1 ponto")
							ataque1=ataque1+1
							dinheiro=dinheiro-10
							break

						elif compra_ataque==5 and dinheiro>=50:
							print("Seu ataque aumentou 5 pontos")
							ataque1=ataque1+5
							dinheiro=dinheiro-50
							break

						if compra_ataque==1 and dinheiro>=100:
							print("Seu ataque aumentou 10 pontos")
							ataque1=ataque1+10
							dinheiro=dinheiro-100
							break

						if compra_ataque!=1 or compra_ataque!=5 or compra_ataque!=10:
							print("Digite um comando válido")
							continue
						else:
							print("Infelizmente você não tem inspermoedas suficientes para comprar este item")
							break

				elif compra=="defesa":
					time.sleep(1)
					print("Você pode aumentar sua defesa em 1 por 10 inpermoedas, 5 por 50 inpermoedas ou 10 por 100 inpermoedas")
					compra_defesa=input("Quanto deseja comprar?\n ")
					time.sleep(1)

					while True:
						if compra_defesa==1 and dinheiro>=10:
							print("Sua defesa aumentou 1 ponto")
							defesa=defesa+1
							dinheiro=dinheiro-10
							break

						if compra_defesa==5 and dinheiro>=50:
							print("Sua defesa aumentou 5 pontos")
							defesa=defesa+5
							dinheiro=dinheiro-50
							break

						if compra_defesa==1 and dinheiro>=100:
							print("Sua defesa aumentou 10 pontos")
							defesa=defesa+10
							dinheiro=dinheiro-100
							break

						if compra_defesa!=1 or compra_defesa!=5 or compra_defesa!=10:
							print("Digite um comando válido")
							continue

						else:
							print("Infelizmente você não tem inspermoedas suficientes para comprar este item")
							break

				elif compra=="vida":
					time.sleep(1)
					print("Você pode aumentar sua vida em 1 por 10 inpermoedas, 5 por 50 inpermoedas ou 10 por 100 inpermoedas")
					compra_vida=input("Quanto deseja comprar?\n ")
					time.sleep(1)

					while True:
						if compra_vida==1 and dinheiro>=10:
							print("Sua vida aumentou 1 ponto")
							vida_inicial=vida_inicial+1
							dinheiro=dinheiro-10
							break

						if compra_vida==5 and dinheiro>=50:
							print("Sua vida aumentou 5 pontos")
							vida_inicial=vida_inicial+5
							dinheiro=dinheiro-50
							break

						if compra_vida==1 and dinheiro>=100:
							print("Sua vida aumentou 1 ponto")
							vida_inicial=vida_inicial+10
							dinheiro=dinheiro-100
							break

						if compra_vida!=1 or compra_vida!=5 or compra_vida!=10:
							print("Digite um comando válido")
							continue

						else:
							print("Infelizmente você não tem inspermoedas suficientes para comprar esta item")
							break

				elif compra=="sair":
					time.sleep(0.5)
					print("Volte sempre")
					break
				
				else:
					print("Digite um comando válido")
					continue

# Inspermon adversário:

		elif comando == "passear":   # Passear em busca de novos inspermons
			print("Passeando...")
			time.sleep(1) 

			print("Você encontrou um Inspermón")  # Encontro com um inspermon
			time.sleep(1)

			if evolucao == 1:
				nome_oponente,ataque_oponente,defesa_oponente,vida_oponente=escolha_adversário(dicionario_inspermons_faceis)

			elif evolucao == 2:

				chance_2 = random.randint(1,5)

				if chance_2 == 1:
					nome_oponente,ataque_oponente,defesa_oponente,vida_oponente=escolha_adversário(dicionario_inspermons_faceis)

				else:
					nome_oponente,ataque_oponente,defesa_oponente,vida_oponente=escolha_adversário(dicionario_inspermons_medios)


			elif evolucao == 3:
				chance_3_facil=[2,3,4]
				chance_3_medio=[5,6,7,8,9,10]

				chance_3 = random.randint(1,20)

				if chance_3 == 1:
					nome_oponente,ataque_oponente,defesa_oponente,vida_oponente=escolha_adversário(dicionario_inspermons_lendarios)

				elif chance_3 in chance_3_facil:
					nome_oponente,ataque_oponente,defesa_oponente,vida_oponente=escolha_adversário(dicionario_inspermons_faceis)

				elif chance_3 in chance_3_medio:
					nome_oponente,ataque_oponente,defesa_oponente,vida_oponente=escolha_adversário(dicionario_inspermons_medios)
				
				else:
					nome_oponente,ataque_oponente,defesa_oponente,vida_oponente=escolha_adversário(dicionario_inspermons_dificeis)

			print("Voce esta batalhando contra {}".format(nome_oponente))  
			time.sleep(1)

			print("Este Inspermón possui os seguintes atributos: Ataque: {}, Defesa: {} e Vida: {}".format(ataque_oponente,defesa_oponente,vida_oponente))
			time.sleep(1)


#       =================================================    Batalha    ===============================================
			while True:

				while True:
					x=2
					if evolucao == 1:
						xp_ganho=10

					elif evolucao == 2:
						if chance_2 == 1:
							xp_ganho = 10
						else:
							xp_ganho = 20

					elif evolucao == 3:
						if chance_3 == 1:
							xp_ganho = 100
						elif chance_3 in chance_3_facil:
							xp_ganho = 10
						elif chance_3 in chance_3_medio:
							xp_ganho = 20
						else:
							xp_ganho = 30 


					ação=input("O que você deseja fazer? (Atacar ou Fugir):\n ")   # Pergunta se deseja atacar ou fugir

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
						ataque_ativo=int(input("Qual ataque deseja usar? 1 ou 2: \n "))  # Escolha do ataque a ser utilizado


						critico=random.randint(1,5)  # Chance de ataque critico

						if ataque_ativo==1:

							if critico==1:
								if evolucao==1:
									ataque1=ataque1*1.5
									print("ATAQUE CRÍTICO".format(nome))
									time.sleep(0.5)
									critico=random.randint(1,5)

								if vida_oponente>0 and ataque1-defesa_oponente>=0:  # Realização do ataque e atualização da vida restante
									vida_oponente= batalha(vida_oponente,ataque1,defesa_oponente)

									if vida_oponente>0:
										print("{} deu {} de dano em {}, agora ele tem {} de vida".format(nome,ataque1-defesa_oponente,nome_oponente,vida_oponente))  # Cálculo da vida restante
										time.sleep(0.5)
										ataque1=ataque1/1.5
										break 

									else:			# Fim da batalha, vitória
										print("{} deu {} de dano em {}, ele desmaiou".format(nome,ataque1-defesa_oponente,nome_oponente))  # Cálculo da vida restante
										time.sleep(0.5)
										print("Voce derrotou {}!" .format(nome_oponente))
										time.sleep(0.5)
										xp=funcaoxp(xp,xp_ganho)   # Atualização da experiência										
										print("Voce recebeu {} de experiencia, agora você tem {}".format(xp_ganho,xp))
										time.sleep(0.5)
										ataque1=ataque1/1.5
										x=3
										break

							if critico!=1 and ataque1-defesa_oponente>0:
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
							else:
								print("{} não deu dano em {}, ele continua com {} de vida".format(nome,nome_oponente,vida_oponente))
								break


						if ataque_ativo == 2:  # Ataque 2 valor de ataque aleatório
							ataque2=random.randint(1,10)

							if critico==1:
								ataque2=ataque2*1.5
								print("ATAQUE CRÍTICO" .format(nome))
								time.sleep(0.5)
								critico=random.randint(1,5)

								if ataque2-defesa_oponente>0:  # Realização do ataque e atualização da vida restante
									vida_oponente= batalha(vida_oponente,ataque2,defesa_oponente)

									if vida_oponente>0:
										if ataque2-defesa_oponente>0:
											print("{} deu {} de dano em {}, agora ele tem {} de vida".format(nome,ataque2-defesa_oponente,nome_oponente,vida_oponente))  # Cálculo da vida restante
											time.sleep(0.5)
											ataque2=ataque2/1.5
											break 
										if ataque2-defesa_oponente<=0:
											print("{} não deu dano em {}, ele continua com {} de vida".format(nome,ataque2-defesa_oponente,nome_oponente,vida_oponente))  # Cálculo da vida restante
											time.sleep(0.5)
											ataque2=ataque2/1.5
											break 

									else:			# Fim da batalha, vitória
										print("{} deu {} de dano em {}, ele desmaiou".format(nome,ataque2-defesa_oponente,nome_oponente))  # Cálculo da vida restante
										time.sleep(0.5)
										print("Voce derrotou {}!" .format(nome_oponente))
										time.sleep(0.5)
										xp=funcaoxp(xp,xp_ganho)   # Atualização da experiência										
										print("Voce recebeu {} de experiencia, agora você tem {}".format(xp_ganho,xp))
										time.sleep(0.5)
										ataque2=ataque2/1.5
										x=3
										break

							if critico!=1:
								if ataque2-defesa_oponente>0 :  # Realização do ataque e atualização da vida restante
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
								ataque2=ataque2*1.5
								critico=random.randint(1,5)

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
								print("{} deu {} de dano em {}, ele desmaiou".format(nome,ataque1-defesa_oponente,nome_oponente))  # Cálculo da vida restante
								time.sleep(0.5)
								print("Voce derrotou {}!" .format(nome_oponente))
								time.sleep(0.8)
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
							ataque_oponente=ataque_oponente*1.5

							if ataque_oponente-defesa>0:
								vida= batalha(vida, ataque_oponente, defesa)
								
								if vida>0:
									print("{} deu {} de dano em {}! Agora ele tem {} de vida".format(nome_oponente,ataque_oponente-defesa,nome,vida))
									time.sleep(0.5)
									ataque_oponente=ataque_oponente/1.5
									continue

								if vida<=0:
									print("Seu Inspermón levou {} de dano, desmaiou e foi levado para o InsperCenter".format(ataque_oponente-defesa))
									time.sleep(0.5)
									vida=vida_inicial
									ataque_oponente=ataque_oponente/1.5
									break	

							if ataque_oponente-defesa<=0:
								print("Seu Inspermón não levou dano")
								ataque_oponente=ataque_oponente/1.5
								continue

						if critico_oponente!=1:
							if ataque_oponente-defesa>0:
								vida= batalha(vida, ataque_oponente, defesa)
								
								if vida>0:
									print("{} deu {} de dano em {}! Agora ele tem {} de vida".format(nome_oponente,ataque_oponente-defesa,nome,vida))
									time.sleep(0.5)
									continue

								if vida<=0:
									print("Seu Inspermón levou {} de dano, desmaiou e foi levado para o InsperCenter".format(ataque_oponente-defesa))
									time.sleep(0.5)
									vida=vida_inicial
									break	

							if ataque_oponente-defesa<=0:
								print("Seu Inspermón não levou dano")
								continue

						if vida<=0:  # Derrota do seu inspermon
							print("Seu Inspermón desmaiou e foi levado para o InsperCenter")
							time.sleep(0.5)
							vida=vida_inicial
							break

				elif x==1 or x==3:  # X para fuga com sucesso/parada do loop de batalha
					x=2
					break

#    =================================    Evolução    ===================================

			def funcao_evolucao(nome,pokemon,evolucao):

				print("{} está se preparando para evoluir".format(nome))
				time.sleep(1)
				print(".")
				time.sleep(1)
				print(".")
				time.sleep(1)
				print(".")
				time.sleep(1)
				print("{} evoluiu para {}!".format(nome, evolucao))

				ataque1=dicionario_inspermons_iniciais[evolucao]["ataque"]
				defesa=dicionario_inspermons_iniciais[evolucao]["defesa"]
				vida_inicial=dicionario_inspermons_iniciais[evolucao]["vida"]

				nome = evolucao

				vida = vida_inicial

				time.sleep(1)
				print("Seu Inspermón tem os seguintes atributos: Ataque:{}, Defesa:{}, Vida:{}".format(ataque1,defesa,vida))

				return(ataque1,defesa,vida_inicial,nome)

				time.sleep(0.5)
				print("Seu Inspermón tem os seguintes atributos: Ataque:{}, Defesa:{}, Vida:{}".format(ataque1,defesa,vida))


			if evolucao == 1 and xp >= 200:

				evolucao = 2

				if index == 1:
					ataque1,defesa,vida_inicial,nome=funcao_evolucao(nome,"Sharmander","Sharmilion")
					nome = MudaNome(nome)

				if index == 2:
					ataque1,defesa,vida_inicial,nome=funcao_evolucao(nome,"Skuirtle","Uarturtle")
					nome = MudaNome(nome)

				if index == 3:
					ataque1,defesa,vida_inicial,nome=funcao_evolucao(nome,"Bulbatauro","Ivitauro")
					nome = MudaNome(nome)

			elif evolucao == 2 and xp >= 500:
				
				evolucao = 3

				if index == 1:
					ataque1,defesa,vida_inicial,nome=funcao_evolucao(nome,"Sharmilion","Cheirazard")
					nome = MudaNome(nome)
				if index == 2:
					ataque1,defesa,vida_inicial,nome=funcao_evolucao(nome,"Uarturtle","Blastoide")
					nome = MudaNome(nome)
				if index == 3:
					ataque1,defesa,vida_inicial,nome=funcao_evolucao(nome,"Bulbatauro","Venustauro")
					nome = MudaNome(nome)

			continue
			
		else:
			print("Digite um comando válido.")
			time.sleep(0.5)

	while True:
		time.sleep(0.5)
		salvar_jogo=input("Deseja salvar o jogo? \n ")
		salvar_jogo=salvar_jogo.lower()

		if salvar_jogo in sim:
			salvo=open("jogo_salvo.py","w")
			salvo.write("import pickle\n")
			salvo.write("jogo_salvo= {\n")
			salvo.write("inspermon= {}\n".format(nome))
			salvo.write("ataque= {}\n".format(ataque1))
			salvo.write("defesa= {}\n" .format(defesa))
			salvo.write("vida= {}\n".format(vida))
			salvo.write("xp= {}\n" .format(xp))
			#salvo.write("dinheiro: {}".format(dinheiro))
			salvo.close()
			time.sleep(0.5)
			print("Jogo salvo com sucesso")
			break

		if salvar_jogo in nao:
			break

		else:
			print("Digite um comando válido (Sim ou Não)")
			continue

	print("Até a proxima!")       # Fim do jogo

	break

