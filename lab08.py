###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Anagramas
# Nome: Pedro Henrique Martins Belo
# RA: 267809
###################################################

#Um anagrama é uma palavra formada ao rearranjar as letras de uma outra palavra. Um anagrama tem o mesmo tamanho e a mesma ocorrência de letras da palavra original. 
# Por exemplo, a palavra ROMA é um anagrama da palavra AMOR e a palavra AMORA é um anagrama da palavra AROMA.

#João está criando um jogo de anagramas. Nesse jogo, cada pessoa tem que organizar uma lista de palavras em conjuntos distintos, sendo que cada conjunto possui palavras que são anagramas umas das outras. 
# Se uma palavra não possui nenhum anagrama na lista de palavras do jogo, então ela ficará isolada em um dos conjuntos. Você pode assumir que não existem palavras repetidas na lista.

#Como entrada, você receberá um inteiro n, que indica a quantidade de palavras da lista, seguido por n linhas, cada uma contendo uma palavra do jogo. 
# As palavras estão ordenadas em ordem alfabética.

#Como saída, você deve imprimir os conjuntos de anagramas. Cada conjunto deve ser impresso em uma linha, com as palavras em ordem alfabética, separadas por um -. 
# Além disso, na impressão da saída, os conjuntos (linhas) também devem estar em ordem alfabética, considerando a primeira palavra de cada conjunto.

#Resolução:

# Leitura das palavras

n = int(input())

palavras = []

for c in range(n):
    p = str(input())
    palavras.append(p)


# Agrupamento dos anagramas

def grupoanagrama(palavras):
    
    anagramagrupo = {}
    
    for palavra in palavras:
        sortedpalavras = "".join(sorted(palavra))
        
        if sortedpalavras in anagramagrupo:
            anagramagrupo[sortedpalavras].append(palavra)
        else:
            anagramagrupo[sortedpalavras] = [palavra]
    
    return list(anagramagrupo.values())
    

# Impressão da saída

for x in grupoanagrama(palavras):
    for i in x:
        if i != x[-1]: 
            print(i, end = '-')
        else:
            print(i)