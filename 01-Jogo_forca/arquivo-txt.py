# Para criar um arquivo que pegue as palavras e a máquina escolha qual vai utilizar para o jogador:

# No prompt de comando, criar o arquivo:
# open("nomedoarquivo.txt","w") {w-write; r-read; a-append; r+ - significa leitura e escrita} (acrescentar)} sempre nessa ordem, o nome do arquivo e o modificador de acesso.
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

#Por exemplo, o código abaixo cria uma cópia de uma imagem:
##arquivo copia.py
#logo = open('python-logo.png', 'rb')
#data = logo.read()
#logo.close()

#logo2 = open('python-logo2.png', 'wb')
#logo2.write(data)
#logo2.close()


# Vamos então abrir o arquivo no modo de leitura, basta passar o nome do arquivo e a letra r para a função open, como já vimos no vídeo anterior:

# >>> arquivo = open("palavras.txt", "r")
# Como abrimos o arquivo no modo de leitura, a função write não funciona. Para ler o arquivo inteiro, utilizamos a função read:

# >>> arquivo.read()
# 'banana\nmelancia\nmorango\nmanga\n'
# Mas se executarmos a função novamente:

# >>> arquivo.read()
# Nos é retornado uma string vazia. Por quê?

# O arquivo é como um fluxo de linhas, que começa no início do arquivo, como se fosse o ponteiro. Ele vai descendo e lendo arquivo, após ler tudo, ele fica posicionado no final do arquivo, então quando chamamos a função read() novamente, não há mais conteúdo, pois ele todo já foi lido.

# Ou seja, para ler o arquivo novamente, devemos fechá-lo e abri-lo novamente.

# Lendo linha por linha do arquivo
# Mas não queremos ler todo o conteúdo do arquivo, e sim ler linha por linha. Como já foi visto, um arquivo é um fluxo de linhas, uma sequência de linhas, então como é uma sequência, podemos fazer um for nela:

# >>> arquivo = open("palavras.txt", "r")
# >>> for linha in arquivo:
# ...     print(linha)
# ... 
# banana

# melancia

# morango

# manga
# Mas podemos reparar que existe uma linha entre cada fruta. Por que isso acontece? Para ver melhor, vamos ler somente uma linha do arquivo, com a função readLine():

# >>> arquivo = open("palavras.txt", "r")
# >>> linha = arquivo.readline() aqui vai ler apenas a primeira linha do arquivo.
# >>> linha
# 'banana\n'

# Há um \n ao final da linha, porque a linha sabe que ao seu final deve ser ser feita uma nova linha. Mas anteriormente havíamos feito um print, que também quebra uma linha ao final da impressão, colocando também um \n! Assim, são criadas duas novas linhas, por isso havia uma linha em branco entre as frutas.

# Limpando a linha
# Como vimos, há um \n ao final de cada linha, de cada palavra, mas queremos somente a palavra. Já vimos como tirar espaços em branco no início e no fim da string, basta utilizar a função strip(), que também remove caracteres especiais, como o \n.

# Sabendo disso tudo, podemos implementar a funcionalidade de leitura de arquivo no nosso jogo. Faremos isso no próximo vídeo.