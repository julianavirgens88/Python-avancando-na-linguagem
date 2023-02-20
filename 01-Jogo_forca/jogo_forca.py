import random # Agora que já temos todas as palavras na lista devemos acessá-las aleatoriamente. Para isso, vamos importar a biblioteca random.

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palaras.txt", "r") # De início devemos abrir o arquivo, e como já sabemos é uma boa prática fechá-lo ao final(arquivo.close()).
    palavras = []

    for linha in arquivo: # Depois temos que criar uma lista e percorrer o arquivo. Cada linha do arquivo deve ser guardada nessa lista.
        linha = linha.strip() # Precisamos remover o \n ao final da linha, fazendo um strip nela.
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras)) # Com a biblioteca já disponível temos que acessar uma das palavras incluídas na nossa lista. Para isso será necessário gerar um número com a posição aleatória. O número gerado deveria ser apenas de índices válidos na lista: 0 até o tamanho da lista.

    palavra_secreta = palavras[numero].upper() # Com o número gerado basta agora pegarmos a palavra secreta correspondente a essa posição.

    letras_acertadas = ["_" for letra in palavra_secreta] # vai criar um traço para cada letra

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
