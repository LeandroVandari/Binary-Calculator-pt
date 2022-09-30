#Importa os módulos necessários para o programa
from termcolor import colored, cprint
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askyesno

texto_operacao = []
texto_resultado = []
    
#Define a função somar, que faz a soma de dois números
def somar(primeiro_binario, segundo_binario, sobra, ordem, texto_resultado, texto_operacao, digito_decimal):
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
    #Transforma os dígitos em listas, para o cálculo
    for numero in digito_1:
        lista_digito_1.append(numero)
    for numero in digito_2:
        lista_digito_2.append(numero)
    diferenca_tamanho = len(lista_digito_1) - len(lista_digito_2)
    if diferenca_tamanho > 0:
        lista_digito_2 = lista_digito_2[::-1]
        for step in range(diferenca_tamanho):
            cprint(lista_digito_dois, "yellow")
            lista_digito_2.append("0")
            cprint(lista_digito_dois, "yellow")
        primeiro_maior = True
        lista_digito_2 = lista_digito_2[::-1]
    elif diferenca_tamanho < 0:
        lista_digito_1 = lista_digito_1[::-1]
        for step in range(diferenca_tamanho * -1):
            lista_digito_1.append("0")
        lista_digito_1 = lista_digito_1[::-1]

    if sobra == "Primeira soma":
        if (binary.get() == False):
            cprint("Para fazer uma adição, precisamos primeiro converter cada um dos dígitos em binário. Isto é feito através de uma espécie de tabela armazenada na calculadora.", "red")
            
            cprint("O primeiro número, em binário, é {0}. O segundo, é {1}.\n".format(primeiro_binario[::-1], segundo_binario[::-1]), "red")
        print("Pegamos o último dígito de cada número para somar:\n")
        if (primeiro_maior):
            cprint("   " + digito_1, "blue")
            texto_operacao.append("   " + digito_1)
            
            if (diferenca_tamanho != 0):
                cprint("+  " + (" " * diferenca_tamanho) + "" + digito_2, "blue")
                cprint(("-" * 3) + ("-" * diferenca_tamanho) + ("-" * len(digito_2)), "blue")
                texto_operacao.append("+  " + (" " * diferenca_tamanho) + "" + digito_2)
                texto_operacao.append(("-" * 3) + ("-" * diferenca_tamanho) + ("-" * len(digito_2)))
            else:
                cprint("+  " + "" + digito_2, "blue")
                cprint(("-" * 3) + ("-" * len(digito_2)), "blue")
                texto_operacao.append("+  " + "" + digito_2)
                texto_operacao.append(("-" * 3) + ("-" * len(digito_2)))
        else:
            if (diferenca_tamanho != 0):
                cprint("   " + (" " * (diferenca_tamanho * -1)) + "" + digito_1, "blue")
                cprint("+  " + digito_2, "blue")
                cprint(("-" * 3) + ("-" * (diferenca_tamanho * -1)) + ("-" * len(digito_1)), "blue")
                texto_operacao.append("   " + (" " * (diferenca_tamanho * -1)) + "" + digito_1)
                texto_operacao.append("+  " + digito_2)
                texto_operacao.append(("-" * 3) + ("-" * (diferenca_tamanho * -1)) + ("-" * len(digito_1)))
            else:
                cprint("   " + "" + digito_1, "blue")
                cprint("+  " + digito_2, "blue")
                cprint(("-" * 3) + ("-" * len(digito_1)), "blue")
                texto_operacao.append("   " + "" + digito_1)
                texto_operacao.append("+  " + digito_2)
                texto_operacao.append(("-" * 3) + ("-" * len(digito_1)))
        lista_digito_1 = lista_digito_1[::-1]
        lista_digito_2 = lista_digito_2[::-1]
        
        bit1 = lista_digito_1[0]
        bit2 = lista_digito_2[0]
        print("Fazemos uma adição normal, apenas em binário. Como este é o primeiro dígito com o qual a operação será feita, podemos utilizar um half-adder: \n")
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
        cprint("   " + (" " * (len(lista_digito_1) - 1) if primeiro_maior else " " * (len(lista_digito_2) - 1)) + resultado, "blue")
        if len(lista_digito_1) > 1 or len(lista_digito_2) > 1:
            somar(primeiro_binario, segundo_binario, sobra, 1, texto_resultado, texto_operacao, digito_decimal)
        else:
            if sobra == "1":
                texto_resultado = texto_resultado[::-1]
                texto_resultado.append("1")
                texto_resultado = texto_resultado[::-1]
            txt = "".join(texto_resultado)
            cprint("Como não há mais nenhum 'bit' para somar, o resultado deste dígito é {0}, que, em decimal, é {1}.".format(txt, decimal.get(txt)), "red")
        
    else:
        try:
            bit1 = lista_digito_1[ordem]
        except:
            bit1 = "0"
        try:
            bit2 = lista_digito_2[ordem]
        except:
            bit2 = "0"
        if ordem == 1:
            print("\nAgora que chegamos à segunda parte, é necessário utilizar um full-adder, pois pode haver uma sobra da adição anterior")
        else:
            print("\nPrecisamos, novamente, utilizar um full-adder")
        print("Agora, somaremos os próximos números.")
        print("\nPrimeiro, utilizamos o operador XOR, para verificar se apenas um dos dois tem valor 1.")
        XOR = ((bit1 == "1" and not bit2 == "1") or (not bit1 == "1" and bit2 == "1"))
        if XOR:
            print("Como isso é verdade, o operador 'devolve' o valor 1.")
        else:
            print("Como isso não é verdade, o operador 'devolve' o valor 0.")
        print("\nAgora, utilizamos mais um operador XOR para verificar se a sobra OU (apenas um dos dois números) tem o valor 1.\nSe sim, isto quer dizer que apenas um dos três ou os três valores são 1, o que implica um resultado de 1.")
        if (XOR == False and sobra == 1) or (XOR == True and sobra != 1):
            print("Como isto é verdade, o resultado é 1.")
            resultado = "1"
        else:
            print("Como isto não é verdade, o resultado é 0.")
            resultado = "0"
        print("\nAgora que temos o resultado, precisamos checar a sobra.")
        print("\nPrimeiro, utilizamos o operador AND para verificar se a sobra anterior E o resultado do primeiro XOR são verdadeiros.")
        print("Se sim, isso quer dizer que exatamente dois dos números são 1, e portanto o resultado seria 0, e a sobra seria 1.")
        print("\nDepois, utilizamos outro operador AND para verificar se ambos números iniciais são 1. Se este for o caso, a sobra deverá ser 1.")
        if (XOR == True and sobra == 1) or (bit1 == 1 and bit2 == 1):
            sobra = "1"
        else:
            sobra = "0"
        print("\nCombinamos ambas as checagens com um operador OR (ou XOR) para verificar se um dos dois (ou os dois, apesar de isso não ser possível) é verdadeiro. Portanto, a sobra é {}.".format(sobra))
        print(texto_resultado)
        texto_resultado = texto_resultado[::-1]
        texto_resultado.append(resultado)
        texto_resultado = texto_resultado[::-1]
        print("\nTemos, até agora, a seguinte operação:")
        for item in texto_operacao:
            print(item)
        txt = texto_resultado
        txt = "".join(txt)
        print("   " + (" " * ((len(lista_digito_1) - len(txt)) + 1) if primeiro_maior else " " * ((len(lista_digito_2) - len(txt)) + 1)) + txt)
        if len(lista_digito_1) >= ordem or len(lista_digito_2) >= ordem:
            somar(primeiro_binario, segundo_binario, sobra, ordem + 1, texto_resultado, texto_operacao, digito_decimal)
        else:
            if sobra == "1":
                texto_resultado = texto_resultado[::-1]
                texto_resultado.append("1")
                texto_resultado = texto_resultado[::-1]
            result = "".join(texto_resultado)
            print("O resultado da soma deste número é {}.".format(result))
            print("Agora convertemos este resultado de volta ao decimal. {0} em decimal, é {1}.".format(result, decimal.get(result)))
            #CONTINUAR AQUI
                
            

        
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
def check_valid():
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
        if (binary.get() == False):
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
            if choice.get() == "+":
                primeiro_binario = primeiro_binario[::-1]
                segundo_binario = segundo_binario[::-1]
                somar(primeiro_binario, segundo_binario, "Primeira soma", 0, texto_resultado, texto_operacao, 0)
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
check1.place(anchor='center', relx = 0.15, rely = 0.5)

#Cria a caixa de seleção de operações.
operations = ['+', '−', '×', '÷']
choice = ttk.Combobox(root, values = operations)
choice.place(anchor = 'center', relx = 0.5, rely = 0.2)
choice.configure(width = 2)

#Cria o botão "Calcular".
calculate = ttk.Button(root, text = 'Calcular', command = lambda : check_valid())
calculate.place(anchor='center', relx=0.5, rely=0.9)
root.mainloop()
