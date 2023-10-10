###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Criptografia Cíclica
# Nome: Pedro Henrique Martins Belo
# RA: 267809
###################################################

#Na sua infância, você e seus primos adoravam brincar mandando mensagens secretas uns para os outros. Para isso, vocês criaram um sistema para reescrever as mensagens (hoje em dia você sabe que vocês estavam usando uma forma simples de criptografia). Você achou algumas dessas mensagens e gostaria de escrever um programa para decodificá-las.

#Dada uma palavra secreta P, que só vocês conheciam, uma mensagem era codificada da seguinte forma: todas as letras da mensagem que são iguais a letra na posição i de P são substituídas pela letra na posição i+1 de P. Ou seja, toda ocorrência da primeira letra de P na mensagem é substituída pela segunda letra de P na mensagem; toda ocorrência da segunda letra de P é substituída pela terceira letra de P; e assim por diante. Além disso, todas as ocorrências da última letra de P na mensagem são substituídas pela primeira letra de P. Por exemplo, dada a palavra secreta hora, a mensagem Hoje esta chovendo é codificada como Orje esth corvendh. Note que letras maiúsculas continuam maiúsculas e letras minúsculas continuam minúsculas.

#A entrada do seu programa é composta por duas linhas, a primeira com a palavra P e a segunda com a mensagem que deve ser decodificada. A saída do seu programa deve ser composta pela mensagem decodificada. Você pode assumir que a palavra P não possui letras repetidas e é formada apenas por letras minúsculas, e que a mensagem não possui acentuação.

#Note que sabendo como uma mensagem foi codificada (de acordo com processo descrito acima) é fácil decodificar a mensagem, como solicitado nesta tarefa.

#Resolução:

p = str(input())
P1 = list(p)
P2 = list(p.upper())
mensagem = str(input())
chave = -1
decifrada = ""
for letra in mensagem:
    if letra in P1:
        indice = P1.index(letra)
        nova_letra = P1[(indice + chave)%len(P1)]
        decifrada += nova_letra
    else:
        if letra.isupper() and letra in P2:
            decifrada += ''
        else:
            decifrada += letra
    if letra in P2:
        indice = P2.index(letra)
        nova_letra = P2[(indice + chave)%len(P2)]
        decifrada += nova_letra

print(decifrada)

