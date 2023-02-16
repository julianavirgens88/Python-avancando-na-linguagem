def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "morango"
    letras_acertadas = ["_","_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    #enquanto(true e true)
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip() #tirar espaços

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()): #letra maiuscula
                letras_acertadas[index] = letra 
                #print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1  #posição ou index


        print(letras_acertadas)

    print("GAME OVER")

if(__name__ == "__main__"):
    jogar()

