def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "morango"

    enforcou = False
    acertou = False

    #enquanto(true e true)
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip() #tirar espaços

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()): #letra maiuscula
                print("Encontrei a letra {} na posição {}".format(letra, index))
                index = index + 1  #posição ou index


        print("jogando")

    print("GAME OVER")

if(__name__ == "__main__"):
    jogar()

