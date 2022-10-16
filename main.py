#Importa os módulos necessários para o programa
from termcolor import colored, cprint
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askyesno
from tkinter.messagebox import *
import os
        
texto_operacao = []
texto_resultado = []
texto_resultado_decimal = []

def somar_binarios(lista_digito_1, lista_digito_2, digito_1, digito_2, sobra, binario, ordem):
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
        print("Fazemos uma adição normal, apenas em binário. Como este é o primeiro dígito com o qual a operação será feita, podemos utilizar um half-adder:")
        cprint("\nPrimeiro utilizamos o operador XOR para verificar se o último dígito de APENAS UM dos números é 1.", "red")
        if (bit1 == "1" and not bit2 == "1") or (not bit1 == "1" and bit2 == "1"):
                resultado = "1"
                print("Como isto ocorreu, o resultado é 1.({0} e {1}, respectivamente)".format(bit1, bit2))
        else:
                resultado = "0"
                print("Já que isto é falso, o resultado é 0, e a sobra precisa ser determinado. (Ambos são {0})".format(bit1))
        cprint("\nAgora, utilizamos o operador AND para verificar se ambos são 1, para determinar a sobra.", "red")
        if (bit1 == "1" and bit2 == "1"):
                sobra = "1"
                print("Já que isto é verdade, a sobra é de 1.")
        else:
                sobra = "0"
                print("Como isto não é verdade, a sobra é 0. ({0} e {1}, respectivamente)\n".format(bit1, bit2))
        texto_resultado.append(resultado)
        print("Temos, por enquanto, a seguinte soma:")
        for item in texto_operacao:
                cprint(item, "blue")
        cprint("   " + " " * (len(lista_digito_1) - 1) + resultado, "blue")
        if len(lista_digito_1) > 1 or len(lista_digito_2) > 1:
                somar(primeiro_binario, segundo_binario, sobra, 1, texto_resultado, texto_operacao, digito_decimal, sobra_decimal, binario, metodo)
        else:
                if sobra == "1":
                        texto_resultado = texto_resultado[::-1]
                        texto_resultado.append("1")
                        texto_resultado = texto_resultado[::-1]
                        txt = "".join(texto_resultado)
                        cprint("Como não há mais nenhum 'bit' para somar, o resultado deste dígito é {0}, que, em decimal, é {1}.".format(txt, decimal.get(txt)), "red")

        else:
        lista_digito_1 = lista_digito_1[::-1]
        lista_digito_2 = lista_digito_2[::-1]
        bit1 = lista_digito_1[ordem]
        bit2 = lista_digito_2[ordem]
        if ordem == 1:
                cprint("\nAgora que chegamos à segunda parte, é necessário utilizar um full-adder, pois pode haver uma sobra da adição anterior","yellow")
        else:
                print("\nPrecisamos, novamente, utilizar um full-adder")
        print("Agora, somaremos os próximos números.")
        cprint("\nPrimeiro, utilizamos o operador XOR, para verificar se apenas um dos dois tem valor 1.", "red")
        XOR = ((bit1 == "1" and not bit2 == "1") or (not bit1 == "1" and bit2 == "1"))
        if XOR:
                print("Como isso é verdade, o operador 'devolve' o valor 1.")
        else:
                print("Como isso não é verdade, o operador 'devolve' o valor 0.")
        cprint("\nAgora, utilizamos mais um operador XOR para verificar se a sobra OU (apenas um dos dois números) tem o valor 1.", "red")
        print("Se sim, isto quer dizer que apenas um dos três ou os três valores são 1, o que implica um resultado de 1.")
        if (XOR == False and sobra == "1") or (XOR == True and sobra != "1"):
                print("Como isto é verdade, o resultado é 1.")
                resultado = "1"
        else:
                print("Como isto não é verdade, o resultado é 0.")
                resultado = "0"
        cprint("\nAgora que temos o resultado, precisamos checar a sobra.", "yellow")
        cprint("\nPrimeiro, utilizamos o operador AND para verificar se a sobra anterior E o resultado do primeiro XOR são verdadeiros.", "red")
        print("Se sim, isso quer dizer que exatamente dois dos números são 1, e portanto o resultado seria 0, e a sobra seria 1.")
        print("\nDepois, utilizamos outro operador AND para verificar se ambos números iniciais são 1. Se este for o caso, a sobra deverá ser 1.")
        if (XOR == True and sobra == "1") or (bit1 == "1" and bit2 == "1"):
                sobra = "1"
        else:
                sobra = "0"
        cprint("\nCombinamos ambas as checagens com um operador OR (ou XOR) para verificar se um dos dois (ou os dois, apesar de isso não ser possível) é verdadeiro. Portanto, a sobra é {}.".format(sobra), "red")		
        texto_resultado = texto_resultado[::-1]
        texto_resultado.append(resultado)
        texto_resultado = texto_resultado[::-1]
        print("\nTemos, até agora, a seguinte operação:")
        for item in texto_operacao:
                cprint(item, "blue")
        txt = texto_resultado
        txt = "".join(txt)
        cprint("   " + " " * (len(lista_digito_1) - len(texto_resultado)) + txt, "blue")
        return sobra, resultado, texto_resultado, texto_operacao, txt

def converter_bcd(numero, metodo):
	lista_resultado = []
	lista_numero = []
	lista_numero = list(numero)
	if len(lista_numero) < 5:
		lista_numero = lista_numero[::-1]
		for step in range(5 - len(lista_numero)):
			lista_numero.append("0")
		lista_numero = lista_numero[::-1]
	if metodo == "ambos":
		metodo = ["double dabble", "portoes"]
	else:
		metodo = [metodo]
	if "portoes" in metodo:
		cprint("Para converter o número binário em BCD utilizando portões de lógica, utilizam-se os mapas de Karnaugh para criar o circuito que fará a conversão.", "blue")
		cprint("(Se você quiser criar circuitos de lógica a partir de tabelas ou mapas de Karnaugh, acesse: https://electricalworkbook.com/binary-to-bcd-code-converter-circuit/")
		cprint("\nPara o primeiro dígito do BCD, o processo é o seguinte: (lembrando que o resultado em binário foi de {})".format(numero), "blue")
		#1 digito
		print("\nUtilizamos um operador AND para verificar se o segundo dígito do binário ({1}) e o quarto dígito ({3}) são 1.\n\nUtilizamos outro operador AND para verificar se o segundo dígito ({1}) e o terceiro dígito ({2}) são 1.\n\nUtilizamos um operador OR para verificar se um dos dois anteriores são 1.\n\nUtilizamos um operador OR para verificar se o resultado do operador OR anterior ou o primeiro dígito ({0}) são 1. Se sim, o primeiro dígito do BCD é 1.".format(lista_numero[0], lista_numero[1], lista_numero[2], lista_numero[3], lista_numero[4]))
		if lista_numero[0] == "1" or (lista_numero[1] == "1" and lista_numero[3] == "1") or (lista_numero[1] == "1" and lista_numero[2] == "1"):
			lista_resultado.append("1")
		else:
			lista_resultado.append("0")
		cprint("\nPortanto, o primeiro dígito é {}.".format(lista_resultado[0]), "red")
		#2 digito
		cprint("\nPara o segundo dígito, o processo é o seguinte: (lembrando que o resultado em binário foi de {})".format(numero), "blue")
		print("\nPrimeiro, utilizamos um operador NOT para inverter o terceiro dígito do número a ser convertido ({2}).\n\nDepois, utilizamos um operador AND para verificar se o segundo dígito ({1}) e o oposto do terceiro dígito (fornecido pelo operador NOT anterior) são 1.\n\nAgora, utilizamos um operador NOT para inverter o quarto dígito ({3}).\n\nDepois, utilizamos um operador AND para verificar se o oposto do quarto dígito e o resultado obtido anteriormente (segundo dígito e oposto do terceiro dígito) são 1.".format(lista_numero[0], lista_numero[1], lista_numero[2], lista_numero[3], lista_numero[4]))
		cprint("\nEsta é uma das possibilidades para que o segundo dígito seja um 1. Agora, calcularemos a outra.", "red")
		print("\nPara calcular a outra possibilidade, utilizamos um operador AND para verificar se o primeiro dígito ({0}) e o quarto dígito ({3}) são 1.\n\nPor fim, utilizamos um operador OR para verificar se pelo menos uma das possibilidades são verdadeiras.".format(lista_numero[0], lista_numero[1], lista_numero[2], lista_numero[3], lista_numero[4]))
		if (lista_numero[0] == "1" and lista_numero[3] == "1") or (lista_numero[1] == "1" and not lista_numero[2] == "1" and not lista_numero[3] == "1"):
			lista_resultado.append("1")
		else: 
			lista_resultado.append("0") 
		cprint("Portanto, o segundo dígito é {}.".format(lista_resultado[1]), "red")
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
		#5 digito
		cprint("\nPara o último dígito, o processo é o seguinte: (lembrando que o resultado em binário foi de {})".format(numero), "blue")
		print("\nSe o último dígito do número em binário com que começamos for 1, o resultado será 1.")
		if lista_numero[-1] == "1":
			lista_resultado.append("1")
		else:
			lista_resultado.append("0")
		cprint("\nPortanto, o último dígito é {0}, e o número binário ({1}) em BCD é ({2}).".format(lista_resultado[-1], numero, "".join(lista_resultado)), "red")
		
	if "double dabble" in metodo:
		pass
	return lista_resultado

def converter_decimal(em_bcd):
	decimal = {
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
	return sobra_decimal, em_decimal

#Define a função somar, que faz a soma de dois números
def somar(primeiro_binario, segundo_binario, sobra, ordem, texto_resultado, texto_operacao, digito_decimal, sobra_decimal, binario, metodo):
	#Define o "dicionário" para converter de binário para decimal
	decimal = {
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
        if (binario == False):
			cprint("Para fazer uma adição, precisamos primeiro converter cada um dos dígitos em binário. Isto é feito através de uma espécie de tabela armazenada na calculadora.", "red")
			
			cprint("O primeiro número, em binário, é {0}. O segundo, é {1}.\n".format(primeiro_binario[::-1], segundo_binario[::-1]), "red")
		print("Pegamos o último dígito de cada número para somar:\n")
	sobra, resultado, texto_resultado, texto_operacao, txt = somar_binarios(lista_digito_1, lista_digito_2, digito_1, digito_2, sobra, binario, ordem)
        if not (sobra== "Primeira soma"):
        print("Agora que fizemos a soma, precisamos verificar se há uma sobra do dígito decimal anterior, que já foi \"salva\" no primeiro dígito do BCD.")
        if sobra_decimal == True:
                sobra, resultado, texto_resultado, texto_operacao, txt = somar_binarios(texto_resultado, ["1"], txt, "1", "0", binario, ordem)
		if ordem + 1 < len(lista_digito_1):
			somar(primeiro_binario, segundo_binario, sobra, ordem + 1, texto_resultado, texto_operacao, digito_decimal, sobra_decimal, binario, metodo)
		else:
			if sobra == "1":
				texto_resultado = texto_resultado[::-1]
				texto_resultado.append("1")
				texto_resultado = texto_resultado[::-1]
			result = "".join(texto_resultado)
			print("\nO resultado da soma deste número é {}.".format(result))
			cprint("\nAntes de converter o dígito de volta a decimal, é preciso convertê-lo a BCD (Binary Coded Decimal, ou, em tradução livre, Decimal Codificado em Binário), e então para decimal.\n", "red")

			em_bcd = converter_bcd(result, metodo)
			# if em_bcd[0] == "1":
			# 	sobra_decimal = True
			# else:
			# 	sobra_decimal = False
			sobra_decimal, digito = converter_decimal(em_bcd)
			texto_resultado_decimal = texto_resultado_decimal[::-1]
			texto_resultado_decimal.append(digito)
			texto_resultado_decimal = texto_resultado_decimal[::-1]
			if not (digito_decimal + 1 > len(primeiro_binario) and digito_decimal + 1 > len(segundo_binario)):
				em_bcd = em_bcd[::-1]
				del(em_bcd[-1])
				somar(primeiro_binario, segundo_binario, 0, 0, texto_resultado, texto_operacao, digito_decimal + 1, sobra_decimal, binario, metodo)
			else:
                if sobra_decimal == True:
                        texto_resultado_decimal = texto_resultado_decimal[::-1]
                        texto_resultado_decimal.append('1')
                        texto_resultado_decimal = texto_resultado_decimal[::-1]
                cprint("Acabamos todos os dígitos, portanto, o resultado da operação requisitada é {}.".format("".join(texto_resultado_decimal)), "red")


			#CONTINUAR AQUI: CONVERSÃO PARA DCB - DOUBLE DABBLE: https://www.realdigital.org/doc/6dae6583570fd816d1d675b93578203d#binary-to-bcd
			#OUTRO METODO: KMAPS: https://electricalworkbook.com/binary-to-bcd-code-converter-circuit/
				
			

		
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
def check_valid(binario, metodo):
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
				somar(primeiro_binario, segundo_binario, "Primeira soma", 0, texto_resultado, texto_operacao, 0, False, binario, metodo)
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

#Cria a opção "Entrada em binário", que pode ser selecionada.
binary = BooleanVar(value=False)
check1 = ttk.Checkbutton(root, text='Entrada em binário', variable=binary, onvalue=True, offvalue=False)
check1.place(anchor='w', relx = 0.01, rely=0.77)

#Cria o texto da escolha de método de conversão de binário para DCB. https://electricalworkbook.com/binary-to-bcd-code-converter-circuit/
texto = ttk.Label(root, text = "Método de conversão de binário para BCD:", font='Helvetica 14 bold')
texto.place(anchor='w', relx = 0.01, rely = 0.38)

#Cria a opção do método double dabble para converter de binário em BCD.
metodo = StringVar()
double_dabble = ttk.Radiobutton(root, text='Double dabble', variable=metodo, value="double dabble")
double_dabble.place(anchor='w', relx = 0.01, rely = 0.5)

#Cria a opção do método por portões de lógica para a conversão de binário em BCD.
portoes = ttk.Radiobutton(root, text='Portões de lógica', variable=metodo, value='portoes')
portoes.place(anchor='w', relx=0.25, rely=0.5)
metodo.set('portoes')


#Cria a opção de utilizar ambos métodos
ambos = ttk.Radiobutton(root, text='Ambos', variable=metodo, value='ambos')
ambos.place(anchor='w', relx=0.55, rely=0.5)

#Cria o texto de outras opções
outras_opcoes = ttk.Label(root, text = "Outras opções:", font='Helvetica 14 bold')
outras_opcoes.place(anchor='w', relx = 0.01, rely = 0.65)

#Cria a caixa de seleção de operações.
operations = ['+', '−', '×', '÷']
choice = ttk.Combobox(root, values = operations)
choice.place(anchor = 'center', relx = 0.5, rely = 0.2)
choice.configure(width = 2)
choice.set('+')

#Cria o botão "Calcular".
calculate = ttk.Button(root, text = 'Calcular', command = lambda : check_valid(binary.get(), metodo.get()))
calculate.place(anchor='center', relx=0.5, rely=0.9)
root.mainloop()

