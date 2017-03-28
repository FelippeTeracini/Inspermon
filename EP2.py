import random
while True:
	lista_de_inspermons=["Hsumon","Diegomon","Hsumon","Teramon"]
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
			while True:
				ataque_ativo=int(input("Qual ataque deseja usar? "))
				if ataque_ativo == 1:
						vida_oponente=vida_oponente-(ataque1-defesa_oponente)
						if vida_oponente>0:
							print("{} deu {} de dano no seu oponente, agora ele tem {} de vida".format(nome,ataque1-defesa_oponente,vida_oponente))
							continue
						else:
							print("Voce derrotou esse Inspermon!")
							break
				elif ataque_ativo == 2:
					ataque2=random.randint(1,10)
					vida_oponente=vida_oponente-(ataque2-defesa_oponente)
					if vida_oponente>0:
						print("{} deu {} de dano no seu oponente, agora ele tem {} de vida".format(nome,ataque2-defesa_oponente,vida_oponente))
						continue
					else:
						print("Voce derrotou esse Inspermon!")
						break
				else:
					print("Digite um ataque valido!")
					continue
			continue
		else:
			print("Digite um comando válido.")
	print("Ate a proxima!")
	continue
