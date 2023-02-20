import random # Agora que já temos todas as palavras na lista devemos acessá-las aleatoriamente. Para isso, vamos importar a biblioteca random.

def jogar():

    imprime_mensagem_abertura

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta) #["_" for letra in palavra_secreta] # vai criar um traço para cada letra

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta): #aqui fazemos a marcação das letras, o jogador da o chute e se o chute tiver na palavra, vai encaixando onde a letra fica.
           marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if(acertou):
        imprime_mensagem_vencedor()
        
    else:
        imprime_mensagem_perdedor()
     
    print("Fim do jogo")


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palaras.txt", "r") # De início devemos abrir o arquivo, e como já sabemos é uma boa prática fechá-lo ao final(arquivo.close()).
    palavras = []

    for linha in arquivo: # Depois temos que criar uma lista e percorrer o arquivo. Cada linha do arquivo deve ser guardada nessa lista.
        linha = linha.strip() # Precisamos remover o \n ao final da linha, fazendo um strip nela.
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras)) # Com a biblioteca já disponível temos que acessar uma das palavras incluídas na nossa lista. Para isso será necessário gerar um número com a posição aleatória. O número gerado deveria ser apenas de índices válidos na lista: 0 até o tamanho da lista.

    palavra_secreta = palavras[numero].upper() # Com o número gerado basta agora pegarmos a palavra secreta correspondente a essa posição.
    return palavra_secreta #como não existe fora do código usamos o return.

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]  

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
     index = 0
     for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if(__name__ == "__main__"):
    jogar()
