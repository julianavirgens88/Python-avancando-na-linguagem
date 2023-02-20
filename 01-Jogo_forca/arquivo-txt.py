# Para criar um arquivo que pegue as palavras e a máquina escolha qual vai utilizar para o jogador:

# No prompt de comando, criar o arquivo:
# open("nomedoarquivo.txt","w") {w-write; r-read; a-append (acrescentar)} sempre nessa ordem, o nome do arquivo e o modificador de acesso.
# Importante é que não precisamos passar o modificador de acesso, pois o segundo parâmetro é opcional:
# arquivo = open("entrada.txt")
#Nesse caso será utilizado o modo de leitura (r) por padrão.


# abrimos um arquivo de texto
# escreve o que quer no arquivo: arquivo.write("banana\n") fazer dessa forma vai criar uma lista, com uma palavra abaixo da outra.
# arquivo.write("maça\n")...
# arquivo.close() - para fechar o arquivo
# no gitbash encontra o arquivo pelo comando ls
# para abrir esse arquivo: cat nomedoarquivo.txt - vai aparecer todas as palavras que foram colocadas. Não usamos o cd como de costume.
# mv palaras.txt PycharmProjects/pythonProject - movemos o arquivo para para o Pycharm para seguir usando o código.