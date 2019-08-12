# -*- coding: utf-8 -*-
# Felipe Ribeiro Barros
# O Dicionário está na seguite forma:
# agenda = {"nome": ["endereço", "telefones", "data de nascimento"]}
# Sempre ao entrar em uma função, a tela é limpa!

import os
import math
agenda = {}
arq = open("Agenda.txt", "r")
for i in arq.readlines():                        # Pega o arquivo e transforma em um dicionário
	agenda[i.split(":")[0]] = [i.split(":")[1], i.split(":")[2], i.split(":")[3][0:-1]]

def menu(agenda):       # Menu principal onde aparecem na tela as opções de escolha de atividades
	os.system(['clear','cls'][os.name == 'nt'])
	arquivo = open("menu.txt", "w")
	arquivo.write("=========================== MENU PRINCIPAL ===========================\n\n\n 1 - Cadastro\n\n 2 - Remover Contato\n\n 3 - Alterar Contato\n\n 4 - Consultar Contato\n\n 5 - Consultar Aniversariantes\n\n 0 - Salvar Dados e Sair\n\n\n                                                   Por Felipe Ribeiro")
	arquivo = open("menu.txt", "r")
	print arquivo.read()
	print
	print
	escolha = int(raw_input("Qual das opções acima deseja executar? "))
	if escolha == 1:
		cadastrar(agenda)
	elif escolha == 2:
		remover(agenda)
	elif escolha == 3:
		altera(agenda)
	elif escolha == 4:
		menu_consulta(agenda)
	elif escolha == 5:
		menu_niver(agenda)
	elif escolha == 0:
		sair(agenda)
			
		
def cadastrar(agenda):             # Pede-se os dados e vai adicionando-os no dicionário, se confirmar "SIM"
	os.system(['clear','cls'][os.name == 'nt'])
	print "                            - ADICIONE UM CONTATO -"
	print
	nome = raw_input("Digite seu nome completo:\n")
	print
	endereco = raw_input("Digite seu endereço completo (no máximo 35 espaços):\n")
	print
	telefone = raw_input("Digite o(s) telefone(s) (xxxx-xxxx xxxx-xxxx):\n")
	print
	niver = raw_input("Digite a sua data de nascimento (xx/xx/xxxx):\n")
	print
	confirma = int(raw_input("Confirma Cadastro (1-SIM, 2-NÃO)? "))
	print
	if confirma == 1:
		agenda[nome] = [endereco, telefone, niver]
		outro = int(raw_input("Inserir Outro (1-SIM, 2-NÃO)? "))
		if outro == 1:
			cadastrar(agenda)
		elif outro == 2:
			menu(agenda)
	elif confirma == 2:
		menu(agenda)
		

def remover(agenda):        # Pede-se o Nome da Pessoa Registrada e remove todos os dados sobre ela (remove a chave)
	os.system(['clear','cls'][os.name == 'nt'])
	print "                            - REMOVA UM CONTATO -"
	print
	nome = raw_input("Digite o nome do contato a ser removido:\n")
	print
	if agenda.has_key(nome):
		print nome, agenda[nome][0], agenda[nome][1], agenda[nome][2]
		print
		confirma = int(raw_input("Confirma Remoção (1-SIM, 2-NÃO)? "))
		if confirma == 1:
			del agenda[nome]
			print "Contato excluído com sucesso!"
		elif confirma == 2:
			menu(agenda)
	else:
		print "Este nome não está nos contatos ou você digitou errado!"
	print
	outro = int(raw_input("Remover Outro (1-SIM, 2-NÃO)? "))
	if outro == 1:
		remover(agenda)
	elif outro == 2:
		menu(agenda)


def altera(agenda):    # Pede-se o Nome do contato que deseja alterar e vai pedindo novos dados, excluindo o antigo
	os.system(['clear','cls'][os.name == 'nt'])
	print "                       - ALTERE OS DADOS DE UM CONTATO -"
	print
	nome = raw_input("Digite o nome de quem quer alterar os dados: ")
	print
	if agenda.has_key(nome):
		print nome, agenda[nome][0], agenda[nome][1], agenda[nome][2]
		print
		certeza = int(raw_input("Alterar Contato (1-SIM, 2-NÃO)? "))
		print
		if certeza == 1:
			novo_nome = raw_input("Corrija o Nome do contato:\n")
			print
			novo_endereco = raw_input("Digite o novo endereço (no máximo 35 espaços):\n")
			print
			novo_tel = raw_input("Digite o(s) novo(s) telefone(s) (xxxx-xxxx xxxx-xxxx):\n")
			print
			novo_niver = raw_input("Digite nova data de nascimento (xx/xx/xxxx):\n")
			print
			confirma = int(raw_input("Confirma Alteração (1-SIM, 2-NÃO)? "))
			print
			if confirma == 1:
				del agenda[nome]     # Exclui o antigo e adiciona os novos dados
				agenda[novo_nome] = [novo_endereco, novo_tel, novo_niver]
			elif confirma == 2:
				menu(agenda)
		elif certeza == 2:
			menu(agenda)
	else:
		print "Digite o nome corretamente!"
		print
	outro = int(raw_input("Alterar Outro Contato (1-SIM, 2-NÃO)? "))
	if outro == 1:
		altera(agenda)
	elif outro == 2:
		menu(agenda)


def menu_consulta(agenda):      # Menu para escolha "consulta"; com 3 opções, consultar por nome, telefone ou voltar
	os.system(['clear','cls'][os.name == 'nt'])
	arquivo = open("consultas.txt", "w")
	arquivo.write("=========================== MENU DE CONSULTA ===========================\n\n\n 1 - Por Nome\n\n 2 - Por Telefone\n\n 3 - Voltar\n")
	arquivo = open("consultas.txt", "r")
	print arquivo.read()
	print
	print
	escolha = int(raw_input("Qual das opções acima deseja executar? "))
	if escolha == 1:
		por_nome(agenda)
	elif escolha == 2:
		por_telefone(agenda)
	elif escolha == 3:
		menu(agenda)


def por_nome(agenda):     # Caso tenha escolhido a opção de consulta seja "por nome", entra nesta função.
	os.system(['clear','cls'][os.name == 'nt'])
	print "                            - CONSULTA POR NOME -"
	print
	procurador = 0
	nome = raw_input("Nome: ")       # Pede-se nome
	print
	for cada in range(len(agenda.keys())):
		if nome.lower() in agenda.keys()[cada].lower():    # verifica se o nome existe no dicionário.
			procurador += 1
			if procurador == 1:
				print "%-18s %-37s %-10s %-10s" % ("Nome", "Endereço", "Telefones", "Aniversário")
				print
			print "%-18s %-37s %-10s %-10s" % (agenda.keys()[cada].split()[0] + " " + agenda.keys()[cada].split()[-1], agenda[agenda.keys()[cada]][0], agenda[agenda.keys()[cada]][1].split()[0], agenda[agenda.keys()[cada]][2])   # Imprime Primeiro Nome + Último nome + endereço + 1ºtelefone + aniversário
			if len(agenda[agenda.keys()[cada]][1].split()) > 1:
				for tel in range(1, len(agenda[agenda.keys()[cada]][1].split())):
					print "%66s" % (agenda[agenda.keys()[cada]][1].split()[tel]) # Imprime de forma organizada os dados (os telefones verticais ficaram muito show!) xD
		print                                                                    # Caso existam mais telefones, serão imprimidos um abaixo do outro. (para sobrar espaço na linha para o endereço)
	if procurador == 0:
		print "Este contato não está registrado!"    # Caso o contato não exista.
	print
	outro = int(raw_input("Consultar Outro (1-SIM, 2-NÃO)? "))
	print
	if outro == 1:
		menu_consulta(agenda)
	elif outro == 2:
		menu(agenda)


def por_telefone(agenda):     #  Caso tenha escolhido a opção de consulta seja "por telefone", entra nesta função.
	os.system(['clear','cls'][os.name == 'nt'])
	print "                           - CONSULTA POR TELEFONE -"
	print
	telefone = raw_input("Telefone (xxxx-xxxx): ")   # Mesmo processo da função "por_nome", mas prioriza os telefones, e não os nomes
	procurador = 0
	print
	for dados in range(len(agenda.items())):    # Ao invés de percorrer por chave, como na função anterior...percorre por (chave,valor), pois precisarei de ambos.
		if telefone in agenda.items()[dados][1][1].split():
			procurador += 1
			if procurador == 1:
				print "%-18s %-10s %-37s %-10s" % ("Nome", "Telefones", "Endereço", "Aniversário")
				print
			print "%-18s %-10s %-37s %-10s" % ((agenda.items()[dados][0]).split()[0] + " " + (agenda.items()[dados][0]).split()[-1], agenda.items()[dados][1][1].split()[0], agenda.items()[dados][1][0], agenda.items()[dados][1][2])
			if len(agenda.items()[dados][1][1].split()) > 1:
				for tel in range(1, len(agenda.items()[dados][1][1].split())):
					print "%28s" % (agenda.items()[dados][1][1].split()[tel])
			print		
	if procurador == 0:
		print "Telefone não registrado!"       # Caso não exista o telefone nos contatos
	print
	outro = int(raw_input("Consultar Outro (1-SIM, 2-NÃO)? "))
	if outro == 1:
		menu_consulta(agenda)
	elif outro == 2:
		menu(agenda)


def menu_niver(agenda):    # Menu de aniversários, caso entre na opção "5" do Menu Principal.
	os.system(['clear','cls'][os.name == 'nt'])
	arquivo = open("aniversario.txt", "w")
	arquivo.write("====================== CONSULTA DE ANIVERSÁRIOS ======================\n\n\n 1 - Dia\n\n 2 - Mês\n\n 3 - Semana\n\n 4 - Voltar\n")
	arquivo = open("aniversario.txt", "r")
	print arquivo.read()
	print
	print
	escolha = int(raw_input("Escolha uma opção: "))        # Novo Menu que fornece 3 opções: consultar por dia, por mes, ou voltar ao menu principal.
	if escolha == 1:
		por_dia(agenda)
	elif escolha == 2:
		por_mes(agenda)
	elif escolha == 3:
		por_semana(agenda)
	elif escolha == 4:
		menu(agenda)
		

def por_dia(agenda):     # Caso tenha escolhido a opção "por dia", entra nesta função.
	os.system(['clear','cls'][os.name == 'nt'])
	print "                     - CONSULTANDO ANIVERSARIANTE POR DIA -"
	print
	procurador = 0
	dia = int(raw_input("Dia: "))    # Pede-se dia e mês, e imprime todos os contatos que nasceram neste dia e mês.
	print
	mes = int(raw_input("Mês: "))
	print
	for dados in range(len(agenda.items())):
		if (dia == int(agenda.items()[dados][1][2].split("/")[0])) and (mes == int(agenda.items()[dados][1][2].split("/")[1])):
			procurador += 1
			if procurador == 1:
				print "%-18s %-10s %-37s %-10s" % ("Nome", "Telefones", "Endereço", "Aniversário")
				print
			print "%-18s %-10s %-37s %-10s" % (agenda.items()[dados][0].split()[0] + " " + agenda.items()[dados][0].split()[-1], agenda.items()[dados][1][1].split()[0], agenda.items()[dados][1][0], agenda.items()[dados][1][2])
			if len(agenda[agenda.keys()[dados]][1].split()) > 1:
				for tel in range(1, len(agenda[agenda.keys()[dados]][1].split())):
					print "%28s" % (agenda[agenda.keys()[dados]][1].split()[tel])
			print
	if procurador == 0:
		print "Não há aniversariante(s) nesta data!"    # Caso não haja aniversariantes no dia/mês escolhido.
		
	print
	outro = int(raw_input("Consultar Outro (1-SIM, 2-NÃO)? "))
	if outro == 1:
		menu_niver(agenda)
	elif outro == 2:
		menu(agenda)
		
		
def por_mes(agenda):        # Caso tenha escolhido a opção "por mês", entra nesta função.
	os.system(['clear','cls'][os.name == 'nt'])
	print "                     - CONSULTANDO ANIVERSARIANTE POR MÊS -"
	print
	procurador = 0
	mes = int(raw_input("Mês: "))   # Mesmo processo da função anterior, diferenciando apenas que não se pede dia, mas apresenta todos os aniversariantes do mês escolhido.
	print
	for dados in range(len(agenda.items())):
		if mes == int(agenda.items()[dados][1][2].split("/")[1]):
			procurador += 1
			if procurador == 1:
				print "%-18s %-10s %-37s %-10s" % ("Nome", "Telefones", "Endereço", "Aniversário")
			print "%-18s %-10s %-37s %-10s" % (agenda.items()[dados][0].split()[0] + " " + agenda.items()[dados][0].split()[-1], agenda.items()[dados][1][1].split()[0], agenda.items()[dados][1][0], agenda.items()[dados][1][2])  # Mesmo processo das impressões em consultas!
			if len(agenda[agenda.keys()[dados]][1].split()) > 1:
				for tel in range(1, len(agenda[agenda.keys()[dados]][1].split())):
					print "%28s" % (agenda[agenda.keys()[dados]][1].split()[tel])     # Telefones verticais!
			print
	if procurador == 0:
		print "Não há aniversariante nos registros!"    # Novamente a mensagem caso não haja ninguém.
	
	print
	outro = int(raw_input("Consultar Outro (1-SIM, 2-NÃO)? "))
	if outro == 1:
		menu_niver(agenda)
	elif outro == 2:
		menu(agenda)
		

def por_semana(agenda):  # Nova função que indica quantos dias ou semanas faltam pro aniversário da pessoa escolhida!
	os.system(['clear','cls'][os.name == 'nt'])
	print "                   - CONSULTANDO ANIVERSARIANTE POR SEMANA -"
	print
	data_atual = raw_input("Digite a data de hoje (xx/xx/xxxx): ").split("/")
	dia_hoje = int(data_atual[0])
	mes_hoje = int(data_atual[1])
	ano = int(data_atual[2])
	print
	nome = raw_input("Digite o nome correto do aniversariante: ")
	print
	if agenda.has_key(nome):
		dia_niver = int(agenda[nome][2].split("/")[0])
		mes_niver = int(agenda[nome][2].split("/")[1])
		
		ano_inteiro = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}  # Todos os meses com quantidade de dias cada.
		
		if ano % 400 == 0 or (ano % 4 == 0 and not (ano % 100 == 0)):     # Se é bissexto
			ano_inteiro[2] = 29
		else:
			ano_inteiro[2] = 28
		print
		
		cont = 0
		if mes_hoje > mes_niver:           # Abaixo, todos os meios de verificar e mostrar; tanto se o aniversario ja passou, como quanto falta pra chegar (em semanas e dias apenas... portanto se faltar mais de 1 ano, exibi-se a mensagem "Só ano que vem!")
			print nome + ", Seu Aniversário já passou... até o próximo ano!"
			
		elif mes_hoje == mes_niver:
			if dia_hoje < dia_niver:
				cont = dia_niver - dia_hoje
			elif dia_hoje == dia_niver:
				print nome + ", Hoje é seu Aniversário! PARABÉNS!"
			else:
				print nome + ", Seu Aniversário já passou... até o próximo ano!"
		else:
			while mes_niver >= mes_hoje:
				dia_niver -= 1
				cont += 1
				if dia_niver == 0:
					mes_niver -= 1
					if mes_niver >= mes_hoje:
						dia_niver = ano_inteiro[mes_niver]
				elif dia_niver == dia_hoje and mes_niver == mes_hoje:
					break
		semana = math.trunc(cont / 7)
		dias = cont % 7

		if cont == 1:
			print nome + ", Amanhã é o seu aniversário!"
		elif 1 < cont < 7:
			print "Ainda Faltam", cont, "Dias!"
		elif semana == 1 and dias > 1:
			print "Ainda Falta 1 Semana e", dias, "Dias!"
		elif semana == 1 and dias == 0:
			print "Só Falta 1 Semana!"
		elif semana > 1 and dias == 1:
			print "Faltam", semana, "Semanas e 1 Dia!"
		elif semana > 1 and dias == 0:
			print "Faltam", semana, "Semanas!"
		elif semana > 1 and dias > 1:
			print "Faltam", semana, "semanas e", dias ,"Dias!"
			
		print
		outro = int(raw_input("Consultar Outro (1-SIM, 2-NÃO)? "))
		if outro == 1:
			menu_niver(agenda)
		elif outro == 2:
			menu(agenda)
	else:
		ent = raw_input("Este contato não está registrado, digite o nome corretamente! (tecle ENTER)")
		if ent == "":
			menu_niver(agenda)
		
		
def sair(agenda):     # Função mais importante, pois salva todos os dados do dicionário "agenda" e a transforma em arquivo... Mas que seja capaz de ser re-lida ao iniciar o programa, transformando-a novamente em dicionário
	os.system(['clear','cls'][os.name == 'nt'])  # É um processo combinado de ficar transformando dicionário e arquivo e visse versa (no começo)
	salvando = open("Agenda.txt", "w")           # para que um seja entendido pelo outro!
	for j in agenda.items():
		salvando.write(j[0] + ":" + j[1][0] + ":" + j[1][1] +":" + j[1][2] + "\n")
		
	arquivo = open("Fim.txt", "r")
	print arquivo.read()                 # Mensagem "FIM" ao sair
	
	
menu(agenda)




