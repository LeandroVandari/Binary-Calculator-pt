#Importa os módulos necessários para o programa
from termcolor import colored, cprint
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askyesno
from tkinter.messagebox import *
import os
import sys

os.system("clear && printf '\e[3J'")
#Cria as variáveis que serão utilizadas.
texto_operacao = []
texto_resultado = []
texto_resultado_decimal = []
acabou = False

def passo():
	if passo_a_passo.get():
		input("\nPressione ENTER para continuar: ")
		print("\033[F" + "\033[K" + "\033[F" + "\033[K")
		cprint("---------------------------------------", "blue")
		
#"Regulariza" o número, isto é, deixa-o apropriado para lidar com o programa
def regularizar(primeiro_binario, segundo_binario):
	for step in range(len(primeiro_binario) - len(segundo_binario)):
		segundo_binario.append("0")
		
	segundo_binario = segundo_binario[::-1]
	return primeiro_binario, segundo_binario
	
#Soma dois números binários, contém a lógica necessária para a adição.
def somar_binarios(sobra_decimal, digito_decimal, primeiro_binario, segundo_binario, lista_digito_1, lista_digito_2, digito_1, digito_2, sobra, binario, ordem, texto_resultado, texto_operacao, decimal, acabou, texto_resultado_decimal, somando_1):

	#Se o programa não acabou, continua
	if not acabou:
		#Se é a primeira soma, utiliza um half-adder e cria a operação
		if sobra == "Primeira soma":
			cprint("   " + digito_1, "blue")
			texto_operacao.append("   " + digito_1)
			cprint("+  " + digito_2, "blue")
			texto_operacao.append("+  " + digito_2)
			cprint("---" + "-" * len(lista_digito_1), "blue")
			texto_operacao.append("---" + "-" * len(lista_digito_1))

			lista_digito_1 = lista_digito_1[::-1]
			lista_digito_2 = lista_digito_2[::-1]

			bit1 = lista_digito_1[0]
			bit2 = lista_digito_2[0]
			#Faz a adição e explica o passo a passo.
			print("A adição de números binários é parecida com a de decimais. Começamos pelo dígito à direita.\n\nNo caso dos binários, se o resultado for maior do que 1, gera um resto.\n\nComo este é o primeiro dígito (isto é, o primeiro \"bit\" do presente dígito) com o qual a operação será feita, podemos utilizar um half-adder, um programa que realiza somas de dois bits, sem incluir sobras anteriores.")
			passo()
			cprint("\nMAIS UMA ETAPA\n\nPrimeiro utilizamos o operador XOR para verificar, entre os bits somados, se APENAS UM DELES é igual a 1 (e não ambos).", "red")
			if (bit1 == "1" and not bit2 == "1") or (not bit1 == "1" and bit2 == "1"):
				resultado = "1"
				print("\nComo isto ocorreu, o resultado é 1.(Lembre-se que os bits somados eram {0} e {1})".format(bit1, bit2))
			else:
				resultado = "0"
				print("Já que isto é falso, o resultado é 0, e a sobra precisa ser determinada. (Ambos são {0})".format(bit1))
			passo()
			cprint("\nAgora, utilizamos o operador AND para verificar se ambos são 1, para determinar a sobra.", "red")
			if (bit1 == "1" and bit2 == "1"):
				sobra = "1"
				print("Já que isto é verdade, a sobra é de 1.")
			else:
				sobra = "0"
				print("Como isto não é verdade, a sobra é 0.\n".format(bit1, bit2))
			passo()
			texto_resultado.append(resultado)
			print("Temos, por enquanto, a seguinte soma:")
			for item in texto_operacao:
				cprint(item, "blue")
			cprint("   " + " " * (len(lista_digito_1) - 1) + resultado, "blue")
			passo()
			#Se há mais de um dígito e não há sobra anterior, chama a função somar para lidar com o próximo passo.
			if (len(lista_digito_1) > 1 or len(lista_digito_2) > 1) and sobra_decimal == False:
				texto_resultado_decimal, acabou, sobra_decimal = somar(primeiro_binario, segundo_binario, sobra, 1, texto_resultado, texto_operacao, digito_decimal, sobra_decimal, binario, texto_resultado_decimal, acabou)
			#Se há mais de um dígito no número mas há sobra anterior, chama a função somar_binários para lidar com o próximo passo.
			elif (len(lista_digito_1) > 1 or len(lista_digito_2) > 1) and sobra_decimal == True:
				lista_digito_1 = lista_digito_1[::-1]
				lista_digito_2 = lista_digito_2[::-1]
				sobra, texto_resultado, texto_operacao, texto_resultado_decimal, acabou, digito_1, digito_2, ordem = somar_binarios(True, digito_decimal,primeiro_binario, segundo_binario, lista_digito_1, lista_digito_2, "".join(lista_digito_1), "".join(lista_digito_2), sobra, binario, 1, texto_resultado, texto_operacao, decimal, acabou, texto_resultado_decimal, True)
		#Se não é a primeira soma, utiliza um full-adder para fazer o cálculo
		else:
			#Auxilia a regularizar as listas para facilitar o cálculo.
			lista_digito_1 = lista_digito_1[::-1]
			lista_digito_2 = lista_digito_2[::-1]
			if len(lista_digito_1) > len(lista_digito_2):
					for step in range(len(lista_digito_1) - len(lista_digito_2)):
						lista_digito_2.append("0")
			elif len(lista_digito_2) > len(lista_digito_1):
				for step in range(len(lista_digito_2) - len(lista_digito_1)):
						lista_digito_1.append("0")
			bit1 = lista_digito_1[ordem]
			bit2 = lista_digito_2[ordem]
			#Utiliza um half-adder para fazer a adição e explica o passo a passo
			cprint("\nMAIS UMA ETAPA\n", "red")
			if ordem == 1:
				cprint("\nAgora que chegamos à segunda parte, é necessário utilizar um full-adder, pois pode haver uma sobra da adição anterior","red")
			else:
				cprint("\nPrecisamos, novamente, utilizar um full-adder.", "red")
			
			print("\nAgora, somaremos os próximos bits.")
			passo()
			cprint("\nPrimeiro, utilizamos o operador XOR, para verificar se apenas um dos dois tem valor 1.", "red")
			XOR = ((bit1 == "1" and not bit2 == "1") or (not bit1 == "1" and bit2 == "1"))
			if XOR:
				print("Como isso é verdade, o operador 'devolve' o valor 1.")
			else:
				print("Como isso não é verdade, o operador 'devolve' o valor 0.")
			passo()
			cprint("\nAgora, utilizamos mais um operador XOR para verificar se a sobra anterior OU (apenas um dos dois números) tem o valor 1.", "red")
			print("\nSe sim, isto quer dizer que apenas um dos três ou os três valores são 1, o que implica um resultado de 1.")
			if (XOR == False and sobra == "1") or (XOR == True and sobra != "1"):
				print("Como isto é verdade, o resultado é 1.")
				resultado = "1"
			else:
				print("Como isto não é verdade, o resultado é 0.")
				resultado = "0"
			passo()
			cprint("\nAgora que temos o resultado, precisamos checar a sobra.", "yellow")
			cprint("\nPrimeiro, utilizamos o operador AND para verificar se a sobra anterior E o resultado do primeiro XOR são iguais a \"1\".", "red")
			passo()
			print("Se sim, isso quer dizer que exatamente dois dos números são 1, e portanto o resultado seria 0, e a sobra seria 1.")
			passo()
			cprint("\nDepois, utilizamos outro operador AND para verificar se ambos números iniciais são 1. Se este for o caso, a sobra deverá ser 1.", "red")
			if (XOR == True and sobra == "1") or (bit1 == "1" and bit2 == "1"):
				sobra = "1"
			else:
				sobra = "0"
			cprint("\nCombinamos ambas as checagens com um operador OR (ou XOR) para verificar se um dos dois (ou os dois, apesar de isso não ser possível) é verdadeiro. Portanto, a sobra é {}.".format(sobra), "red")        
			texto_resultado = texto_resultado[::-1]
			texto_resultado.append(resultado)
			texto_resultado = texto_resultado[::-1]
			
			passo()
			print("\nTemos, até agora, a seguinte operação:")
			for item in texto_operacao:
				cprint(item, "blue")
			txt = texto_resultado
			txt = "".join(txt)
			cprint("   " + " " * (len(lista_digito_1) - len(texto_resultado)) + txt, "blue")
			lista_digito_1 = lista_digito_1[::-1]
			lista_digito_2 = lista_digito_2[::-1]
		#Se está apenas adicionando 1 (Por haver sobra decimal), chama a função somar_binários novamente.
		if somando_1 and ordem + 1 < len(lista_digito_1):
			sobra, texto_resultado, texto_operacao, texto_resultado_decimal, acabou, digito_1, digito_2, ordem = somar_binarios(True, digito_decimal,primeiro_binario, segundo_binario, lista_digito_1, lista_digito_2, "".join(lista_digito_1), "".join(lista_digito_2), sobra, binario, ordem + 1, texto_resultado, texto_operacao, decimal, acabou, texto_resultado_decimal, True)
		
		txt = texto_resultado
		txt = "".join(txt)
    #Devolve os valores atualizados de diversas variáveis.
	return sobra, texto_resultado, texto_operacao, texto_resultado_decimal, acabou, digito_1, digito_2, ordem
#Converte um número para BCD.
def converter_bcd(numero):
    lista_resultado = []
    lista_numero = []
    lista_numero = list(numero)
	#Se o número tiver menos de 5 dígitos, adiciona zeros ao seu início para a conversão.
    if len(lista_numero) < 5:
        lista_numero = lista_numero[::-1]
        for step in range(5 - len(lista_numero)):
            lista_numero.append("0")
        lista_numero = lista_numero[::-1]
	#Faz a conversão e explica o passo a passo.
    cprint("Para converter o número binário em BCD utilizando portões de lógica, utilizam-se os mapas de Karnaugh para criar o circuito que fará a conversão.", "blue")
    cprint("(Se você quiser criar circuitos de lógica a partir de tabelas ou mapas de Karnaugh, acesse: https://electricalworkbook.com/binary-to-bcd-code-converter-circuit/")
    cprint("\nPara o primeiro dígito do BCD, o processo é o seguinte: (lembrando que o resultado em binário foi de {})".format(numero), "blue")
    passo()
	#1 digito
    print("\nUtilizamos um operador AND para verificar se o segundo dígito do binário ({1}) e o quarto dígito ({3}) são 1.\n\nUtilizamos outro operador AND para verificar se o segundo dígito ({1}) e o terceiro dígito ({2}) são 1.\n\n".format(lista_numero[0], lista_numero[1], lista_numero[2], lista_numero[3], lista_numero[4]))
    passo()
    print("Utilizamos um operador OR para verificar se um dos dois anteriores são 1.\n\nUtilizamos um operador OR para verificar se o resultado do operador OR anterior ou o primeiro dígito ({0}) são 1. Se sim, o primeiro dígito do BCD é 1.".format(lista_numero[0], lista_numero[1], lista_numero[2], lista_numero[3], lista_numero[4]))
    if lista_numero[0] == "1" or (lista_numero[1] == "1" and lista_numero[3] == "1") or (lista_numero[1] == "1" and lista_numero[2] == "1"):
        lista_resultado.append("1")
    else:
        lista_resultado.append("0")
    cprint("\nPortanto, o primeiro dígito é {}.".format(lista_resultado[0]), "red")
    passo()
	#2 digito
    cprint("\nPara o segundo dígito, o processo é o seguinte: (lembrando que o resultado em binário foi de {})".format(numero), "blue")
    print("\nPrimeiro, utilizamos um operador NOT para inverter o terceiro dígito do número a ser convertido ({2}).".format(lista_numero[0], lista_numero[1], lista_numero[2], lista_numero[3], lista_numero[4]))
    cprint("Depois, utilizamos um operador AND para verificar se o segundo dígito ({1}) e o oposto do terceiro dígito (fornecido pelo operador NOT anterior) são 1.\n\nAgora, utilizamos um operador NOT para inverter o quarto dígito ({3}).\n\nDepois, utilizamos um operador AND para verificar se o oposto do quarto dígito e o resultado obtido anteriormente (segundo dígito e oposto do terceiro dígito) são 1.".format(lista_numero[0], lista_numero[1], lista_numero[2], lista_numero[3], lista_numero[4]), "red")
    cprint("\nEsta é uma das possibilidades para que o segundo dígito seja um 1. Agora, calcularemos a outra.", "red")
    print("\nPara calcular a outra possibilidade, utilizamos um operador AND para verificar se o primeiro dígito ({0}) e o quarto dígito ({3}) são 1.\n\nPor fim, utilizamos um operador OR para verificar se pelo menos uma das possibilidades são verdadeiras.".format(lista_numero[0], lista_numero[1], lista_numero[2], lista_numero[3], lista_numero[4]))
    if (lista_numero[0] == "1" and lista_numero[3] == "1") or (lista_numero[1] == "1" and not lista_numero[2] == "1" and not lista_numero[3] == "1"):
        lista_resultado.append("1")
    else: 
        lista_resultado.append("0") 
    cprint("Portanto, o segundo dígito é {}.".format(lista_resultado[1]), "red")
    passo()
	#3 digito
    cprint("\nPara o terceiro dígito, o processo é o seguinte: (lembrando que o resultado em binário foi de {})".format(numero), "blue")
    cprint("\nPara este dígito, há 3 possibilidades de que seja um 1.\n\nA primeira, é a seguinte:", "red")
    print("Primeiro, utilizamos um operador NOT para inverter o segundo dígito ({1}).\n\nDepois, utilizamos um operador AND para verificar se o oposto do segundo dígito E o terceiro dígito ({3}) são 1.\n".format(lista_numero[0], lista_numero[1], lista_numero[2], lista_numero[3], lista_numero[4]))
    cprint("\nOutra possibilidade, é a seguinte:\n", "red")
    print("Utilizamos um operador AND para verificar se o terceiro número ({2}) e o quarto número ({3}) são 1.".format(lista_numero[0], lista_numero[1], lista_numero[2], lista_numero[3], lista_numero[4]))
    cprint("\nA última possibilidade, é:\n", "red")
    print("Utilizamos um operador NOT para inverter o quarto dígito ({3}).\n\nUtilizamos um operador and para verificar se o primeiro dígito ({0}) e o oposto do quarto dígito são 1.\n".format(lista_numero[0], lista_numero[1], lista_numero[2], lista_numero[3], lista_numero[4]))
    print("\nAgora utilizamos dois operadores OR, o primeiro para verificar se a primeira ou a segunda possibilidade são verdadeiras, e o segundo para verificar se o operador OR anterior ou a terceira possibilidade são verdadeiras.\n\nDesta forma, se pelo menos uma das possibilidades for verdadeira, o terceiro dígito será 1.")
    if (not lista_numero[1] == "1" and lista_numero[2] == "1") or (lista_numero[2] == "1" and lista_numero[3] == "1") or (lista_numero[0] == "1" and not lista_numero[3] == "1"):
        lista_resultado.append("1")
    else:
        lista_resultado.append("0")
    cprint("Portanto, o terceiro dígito é {}.".format(lista_resultado[2]), "red")
    passo()
	#4 digito
    cprint("\nPara o quarto dígito, o processo é o seguinte: (lembrando que o resultado em binário foi de {})".format(numero), "blue")
    cprint("\nPara este dígito, há 3 possibilidades de que seja um 1.\n\nA primeira, é a seguinte:", "red")
    print("Primeiro, utilizamos um operador NOT para inverter o quarto dígito ({3}).\n\nDepois, utilizamos o operador AND para verificar se o primeiro dígito ({0}) e o oposto do quarto dígito são 1.".format(lista_numero[0], lista_numero[1], lista_numero[2], lista_numero[3], lista_numero[4]))
    cprint("\nOutra possibilidade, é a seguinte:\n", "red")
    print("Utilizamos um operador AND para verificar se o primeiro dígito ({0}) e o segundo dígito ({1}) são 1.\n\nUtilizamos um operador NOT para inverter o resultado anterior.\n\nUtilizamos um operador and para verificar se o resultado anterior E o quarto dígito ({3}) são 1.".format(lista_numero[0], lista_numero[1], lista_numero[2], lista_numero[3], lista_numero[4]))
    cprint("\nA última possibilidade, é:\n", "red")
    print("Utilizamos um operador AND para verificar se o segundo dígito ({1}) e o terceiro dígito ({2}) são 1.\n\nUtilizamos um operador NOT para inverter o quarto dígito ({3}).\n\nUtilizamos um operador AND para verificar se o resultado do primeiro AND e o oposto do quarto dígito são 1.".format(lista_numero[0], lista_numero[1], lista_numero[2], lista_numero[3], lista_numero[4]))
    print("Agora utilizamos dois operadores OR, o primeiro para verificar se a primeira ou a segunda possibilidade são verdadeiras, e o segundo para verificar se o operador OR anterior ou a terceira possibilidade são verdadeiras.\n\nDesta forma, se pelo menos uma das possibilidades for verdadeira, o quarto dígito será 1.")
    if (lista_numero[0] == "1" and not lista_numero[3] == "1") or (not lista_numero[0] == "1" and not lista_numero[1] == "1" and lista_numero[3] == "1") or (lista_numero[1] == "1" and lista_numero[2] == "1" and not lista_numero[3] =="1"):
        lista_resultado.append("1")
    else:
        lista_resultado.append("0")
    cprint("Portanto, o quarto dígito é {}.".format(lista_resultado[3]), "red")
    passo()
	#5 digito
    cprint("\nPara o último dígito, o processo é o seguinte: (lembrando que o resultado em binário foi de {})".format(numero), "blue")
    print("\nSe o último dígito do número em binário com que começamos for 1, o resultado será 1.")
    if lista_numero[-1] == "1":
        lista_resultado.append("1")
    else:
        lista_resultado.append("0")
    cprint("\nPortanto, o último dígito é {0}, e o número binário ({1}) em BCD é ({2}).".format(lista_resultado[-1], numero, "".join(lista_resultado)), "red")
    passo()
	#Devolve o número convertido em BCD.
    return lista_resultado

#Converte um número BCD para o decimal, dizendo se é maior que 10 e qual seu dígito das unidades.
def converter_decimal(em_bcd):
	decimal = {
    "0000":"0",
	"0001":"1",
	"0010":"2",
	"0011":"3",
	"0100":"4",
	"0101":"5",
	"0110":"6",
	"0111":"7",
	"1000":"8",
	"1001":"9",
	}
	em_bcd = em_bcd[::-1]
	if em_bcd[-1] == "1":
		sobra_decimal = True
	else: sobra_decimal = False
	del(em_bcd[-1])
	em_bcd = em_bcd[::-1]
	em_decimal = decimal.get("".join(em_bcd))
	#Devolve o segundo dígito em decimal, e "diz" se o a casa das dezenas é um 1 ou um 0.
	return sobra_decimal, em_decimal

#Define a função somar, que faz a soma de dois números
def somar(primeiro_binario, segundo_binario, sobra, ordem, texto_resultado, texto_operacao, digito_decimal, sobra_decimal, binario, texto_resultado_decimal, acabou):
	if not acabou:
		#Regulariza os números, para facilitar a soma.
		if len(primeiro_binario) > len(segundo_binario):
			for step in range(len(primeiro_binario) - len(segundo_binario)):
				segundo_binario.append("0")
		elif len(segundo_binario) > len(primeiro_binario):
			for step in range(len(segundo_binario) - len(primeiro_binario)):
				primeiro_binario.append("0")
			
		#Define o "dicionário" para converter de binário para decimal
		decimal = {
			"0":"0",
			"1":"1",
			"10":"2",
			"11":"3",
			"100":"4",
			"101":"5",
			"110":"6",
			"111":"7",
			"1000":"8",
			"1001":"9",
			}
		#Define as variáveis que serão utilizadas no código
		digito_1 = primeiro_binario[digito_decimal]
		digito_2 = segundo_binario[digito_decimal]
		primeiro_maior = False
		lista_digito_1 = []
		lista_digito_2 = []
		#Transforma os dígitos em listas, para o cálculo, e adiciona zeros para igualar as casas.
		for numero in digito_1:
			lista_digito_1.append(numero)
		for numero in digito_2:
			lista_digito_2.append(numero)
		diferenca_tamanho = len(lista_digito_1) - len(lista_digito_2)
		if diferenca_tamanho > 0:
			lista_digito_2 = lista_digito_2[::-1]
			for step in range(diferenca_tamanho):
				lista_digito_2.append("0")
			lista_digito_2 = lista_digito_2[::-1]
			primeiro_maior = True
		elif diferenca_tamanho < 0:
			lista_digito_1 = lista_digito_1[::-1]
			for step in range(diferenca_tamanho * -1):
				lista_digito_1.append("0")
			lista_digito_1 = lista_digito_1[::-1]
		#Transforma as listas de volta em números
		digito_1 = "".join(lista_digito_1)
		digito_2 = "".join(lista_digito_2)
		if sobra == "Primeira soma":
			if (digito_decimal == 0):
				cprint("\nEXPLICAÇÃO INICIAL\n\nPara fazer uma adição, precisamos primeiro converter cada um dos dígitos do número decimal em um número binário.\n\nIsto é feito através de uma espécie de tabela armazenada na calculadora.", "red")
				print("\nA conversão já foi realizada. O primeiro número que você escolheu, convertido em binário, é {0}. O segundo, é {1}.\n".format(primeiro_binario[::-1], segundo_binario[::-1]))
				passo()
			cprint("\nSOMA\n\nAgora somaremos os números binários \"{0}\" e \"{1}\".\n\n(Lembrando que o primeiro número que você escolheu, já convertido em binário, é {2}, e o segundo, é {3})\n".format(primeiro_binario[digito_decimal], segundo_binario[digito_decimal], primeiro_binario[::-1], segundo_binario[::-1]), "red")
			if digito_decimal == 0:
				print("(Neste caso, estamos fazendo a primeira soma. Portanto, pegamos os *ÚLTIMOS* dígitos decimais de ambos os números, já convertidos.)\n")
		#Chama a função somar_binarios para começar o cálculo.
		sobra, texto_resultado, texto_operacao, texto_resultado_decimal, acabou, digito_1, digito_2, ordem = somar_binarios(sobra_decimal, digito_decimal, primeiro_binario, segundo_binario, lista_digito_1, lista_digito_2, digito_1, digito_2, sobra, binario, ordem, texto_resultado, texto_operacao, decimal, acabou, texto_resultado_decimal, False)
		#Se acabou a soma do dígito, e a sobra é 1, adiciona um 1 no início do resultado.
		if not ordem + 1 < len(lista_digito_1):
			if sobra == "1":
				texto_resultado = texto_resultado[::-1]
				texto_resultado.append("1")
				texto_resultado = texto_resultado[::-1]
				print("Como a sobra era de 1, e já acabamos este dígito, adicionamos um 1 ao início do número, ficando com {}.".format(texto_resultado))
				passo()
		if not acabou:
			#Verifica se há uma sobra do dígito decimal anterior e, se há, adiciona 1 ao número presente.
			if not ordem + 1 < len(lista_digito_1):
				print("Agora que fizemos a soma, precisamos verificar se há uma sobra do dígito decimal anterior, que já foi \"salva\" no primeiro dígito do BCD.")
				if sobra_decimal == True:
					cprint("Como há, adicionamos 1 ao resultado deste dígito.")
					lista_digito_1, lista_digito_2 = regularizar(texto_resultado, ["1"])
					sobra, texto_resultado, texto_operacao, texto_resultado_decimal, acabou, digito_1, digito_2, ordem = somar_binarios(True, digito_decimal,primeiro_binario, segundo_binario, lista_digito_1, lista_digito_2, "".join(lista_digito_1), "".join(lista_digito_2), "Primeira soma", binario, ordem, [], [], decimal, acabou, texto_resultado_decimal, True)
					if sobra == "1":
						texto_resultado = texto_resultado[::-1]
						texto_resultado.append("1")
						texto_resultado = texto_resultado[::-1]
				else: 
					print("Como não há, prosseguimos normalmente.")
				passo()
			#Se ainda não acabou o dígito, chama a função novamente para calcular.
			if ordem + 1 < len(lista_digito_1):
				try:
					texto_resultado_decimal, acabou, sobra_decimal = somar(primeiro_binario, segundo_binario, sobra, ordem + 1, texto_resultado, texto_operacao, digito_decimal, sobra_decimal, binario, texto_resultado_decimal, acabou)
				except TypeError:
					pass
			if not acabou:
				#Dá o resultado em binário.
				if not (ordem + 1 < len(lista_digito_1)):
						
					result = "".join(texto_resultado)
					print("\nO resultado da soma deste número é {}.".format(result))
					passo()
					cprint("\nAntes de converter o dígito de volta a decimal, é preciso convertê-lo a BCD (Binary Coded Decimal, ou, em tradução livre, Decimal Codificado em Binário), e então para decimal.\n", "red")
					#Converte o número para BCD e então para decimal
					em_bcd = converter_bcd(result)
					sobra_decimal, digito = converter_decimal(em_bcd)
					texto_resultado_decimal = texto_resultado_decimal[::-1]
					print("Podemos utilizar a tabela previamente mencionada para converter os quatro últimos dígitos do BCD em decimal.\n{0} em decimal é {1}.".format("".join(em_bcd), digito))
					texto_resultado_decimal.append(digito)
					texto_resultado_decimal = texto_resultado_decimal[::-1]
					passo()
					#Se o dígito em decimal já acabou, verifica se o número como um todo acabou. Se não, chama a soma novamente.
					if not (digito_decimal + 1 >= len(primeiro_binario) and digito_decimal + 1 >= len(segundo_binario)):
						em_bcd = em_bcd[::-1]
						del(em_bcd[-1])
						texto_resultado_decimal, acabou, sobra_decimal = somar(primeiro_binario, segundo_binario, "Primeira soma", 0, [], [], digito_decimal + 1, sobra_decimal, binario, texto_resultado_decimal, acabou)
					else:
						#Se o número como um todo já foi terminado, verifica se há uma sobra (se sim, adiciona 1 ao início do número) e dá o resultado da operação.
						if sobra_decimal == True:
							texto_resultado_decimal = texto_resultado_decimal[::-1]
							texto_resultado_decimal.append('1')
							texto_resultado_decimal = texto_resultado_decimal[::-1]
						cprint("\n\nAcabamos todos os dígitos, portanto, todo este processo nos dá um resultado de {}.".format("".join(texto_resultado_decimal)), "red")
						acabou = True
						input()
						sys.exit()
			else:
				#Se já acabou, devolve o resultado
				return texto_resultado_decimal, acabou, sobra_decimal
		#Devolve as variáveis necessárias;
		passo()
		return texto_resultado_decimal, acabou, sobra_decimal

            

        
#A função abaixo limpa as caixas de texto quando o usuário a seleciona
#Ou preenche-a com o seu devido texto, se o usuário clica em outra caixa
def clear_box(box):
    if (box == "caixa1"):
        if (caixa1.get() == "Número 1"):
            caixa1.delete('0', 'end')
        if (caixa2.get() == ""):
            caixa2.insert(0, 'Número 2')
    elif (box == "caixa2"):
        if (caixa2.get() == "Número 2"):
            caixa2.delete('0', 'end')
        if (caixa1.get() == ""):
            caixa1.insert(0, 'Número 1')

#Esta função converte o número recebido em uma lista de números binários, cada um correspondendo a um digito
def convert_to_binary(num):
    lista_num = []
    lista_num_binario = []

    #Cria uma lista com os dígitos do número recebido
    for digit in str(num):
        lista_num.append(digit)
    #É um "dicionário", tem uma definição para o que substituir pelo digito recebido,
    #Ou seja, qual o seu correspondente binário
    binary = {
    "0":"0",
    "1":"1",
    "2":"10",
    "3":"11",
    "4":"100",
    "5":"101",
    "6":"110",
    "7":"111",
    "8":"1000",
    "9":"1001",
    }
    #Insere o número binário correspondente na lista que será "devolvida"
    for item in lista_num:
        lista_num_binario.append(binary.get(lista_num[lista_num.index(item)], "Algo deu errado, tente novamente"))

    #Devolve a lista a quem chamou esta função
    return lista_num_binario

#Verifica se o que o usuário escreveu é válido (um número), e,
#Caso a opção "Entrada em binário" esteja selecionada,
#Verifica se o número inserido está em binário. Depois, "chama" a função para converter em binário.
#Dependendo do operador escolhido, chama uma das funções para calcular.
def check_valid(binario):
    #Verifica se o que foi escrito é um número
    tentar_2 = True
    try:
        primeiro_caixa = int(caixa1.get())
    except Exception:
        messagebox.showinfo("Erro!", "Entrada inválida para o primeiro número.")
        caixa1.focus_force()
        tentar_2 = False

    if (tentar_2 == True):
        try:
            segundo_caixa = int(caixa2.get())
        except Exception:
            messagebox.showinfo("Erro!", "Entrada inválida para o segundo número.")
            caixa2.focus_force()
            tentar_2 = False

    #Se a opção "Entrada em binário" não estiver selecionada, converte os números para o binário.
    if (tentar_2 == True):
        if (binario== False):
            primeiro_decimal = primeiro_caixa
            segundo_decimal = segundo_caixa
            primeiro_binario = convert_to_binary(primeiro_caixa)
            segundo_binario = convert_to_binary(segundo_caixa)
        #Se a opção "Entrada em binário" estiver selecionada, verifica se o que foi digitado está em binário.
        else:
            primeiro_decimal = ""
            segundo_decimal = ""
            primeiro_binario = str(primeiro_caixa)
            segundo_binario = str(segundo_caixa)
            for letter in primeiro_binario:
                if (tentar_2 == True):
                    if letter != "0" and letter != "1":
                        messagebox.showinfo("Erro!", "Entrada inválida para o primeiro número. (Não está em binário)")
                        tentar_2 = False
            if tentar_2 == True:
                for letter in segundo_binario:
                    if (tentar_2 == True):
                        if letter != "0" and letter != "1":
                            messagebox.showinfo("Erro!", "Entrada inválida para o segundo número. (Não está em binário)")
                            tentar_2 = False
            primeiro_binario = [primeiro_binario]
            segundo_binario = [segundo_binario]
        #Dependendo do operador selecionado, chama a opção correspondente para calcular.
        if tentar_2 == True:
            os.system("clear && printf '\e[3J'")
            if choice.get() == "+":
                primeiro_binario = primeiro_binario[::-1]
                segundo_binario = segundo_binario[::-1]
                root.destroy()
                somar(primeiro_binario, segundo_binario, "Primeira soma", 0, texto_resultado, texto_operacao, 0, False, binario, texto_resultado_decimal, acabou)
            elif choice.get() == "−":
                pass
            elif choice.get() == "×":
                pass
            elif choice.get() == "÷":
                pass

#Cria a janela de interação com o usuário e define alguns parâmetros, como tamanho, título, posição na tela etc.
root = Tk()
width = int(root.winfo_screenwidth() / 2)
height = int(root.winfo_screenheight() / 2)
win_width = root.winfo_width()
win_height = root.winfo_height()
root.geometry('500x200+'+ str(width - win_width) +'+'+ str(height - win_height//2))
root.minsize(width = 500, height = 200)
root.title("Calculadora em binário!")

input_text = StringVar()

#Cria a caixa de texto onde "Número 1" está.
caixa1 = ttk.Entry(root, justify=CENTER)
caixa1.place(anchor='center', relx=0.2, rely=0.2)
caixa1.insert(0, 'Número 1')
caixa1.bind("<FocusIn>", lambda args : clear_box("caixa1"))

#Cria a caixa de texto onde "Número 2" está.
caixa2 = ttk.Entry(root, justify=CENTER)
caixa2.place(anchor='center', relx=0.8, rely=0.2)
caixa2.insert(0, 'Número 2')
caixa2.bind("<FocusIn>", lambda args : clear_box("caixa2"))

#Cria a opção de apresentar o processo passo a passo.
passo_a_passo = BooleanVar(value=True)
check1 = ttk.Checkbutton(root, text='Cálculo passo a passo (com pausas)', variable=passo_a_passo, onvalue=True, offvalue=False)
check1.place(anchor='w', relx = 0.02, rely = 0.5)


#Cria a caixa de seleção de operações.
operations = ['+', '−', '×', '÷']
choice = ttk.Combobox(root, values = operations)
choice.place(anchor = 'center', relx = 0.5, rely = 0.2)
choice.configure(width = 2)
choice.set('+')

#Cria o botão "Calcular".
calculate = ttk.Button(root, text = 'Calcular', command = lambda : check_valid(False))
calculate.place(anchor='center', relx=0.5, rely=0.9)
root.mainloop()

