###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Gráfico de Recorrência
# Nome: Pedro Henrique Martins Belo
# RA: 267809
###################################################

#Seu chefe pediu para que você analisasse as vendas mensais da empresa na qual você está trabalhando. Durante seus estudos, você descubriu que este tipo de dado, que possui valores registrados ao longo do tempo, é considerado uma série temporal e que existe uma forma de representar esta informação como um gráfico de recorrência.
#O gráfico de recorrência transforma séries temporais em imagens binárias (com cada ponto da imagem tendo valor 0 ou 1). Para isto, para cada valor da série temporal, é verificada a diferença em relação a todos os valores da série, e, se a diferença (absoluta) for menor ou igual a um determinado limiar, o valor de recorrência entre os dois pontos é indicado como 0, caso contrário, como 1.
#O exemplo a seguir mostra uma série temporal com 4 valores:

#5 10 3 8

#Considere um limiar igual a 3. Para o primeiro valor da série (5), as diferenças (absolutas) entre o valor avaliado (5) e todos os elementos da série são os seguintes:

#0 5 2 3

#Logo, a recorrência para esse primeiro valor avaliado (5) será igual a:

#0 1 0 0

#Como a diferença (absoluta) entre o valor avaliado (5) para primeiro valor da série (5), para o terceiro valor da série (3) e para o quarto valor da série (8) são menores ou igual ao limiar (3), esses pontos receberão o valor 0. Já para o segundo valor da série (10), a diferença (absoluta) é maior do que o limiar (3), portanto, esse ponto receberá o valor 1.
#O mesmo processo pode ser feito para todos os outros valores da série, considerando como valores avaliados. Ao final, teremos o seguinte gráfico de recorrência, sendo a primeira linha correspondente a avaliação para o valor 5, a segunda linha correspondente a avaliação para o valor 10, e assim por diante:

#0 1 0 0
#1 0 1 0
#0 1 0 1
#0 0 1 0

#Devido ao seu conhecimento de programação, você decidiu criar um programa que leia as vendas da empresa e um valor de limiar e transforme esta informação em um gráfico de recorrência. Seu programa deverá ler um valor N, representando o tamanho da série temporal, seguida por N valores, correspondentes aos valores de venda mensal. 
#Depois, seu código receberá um valor L, representando o valor do limiar analisado. Como saída, seu código deverá imprimir o gráfico de recorrência. Note que deve existir um espaço entre cada valor (0 ou 1), mas não deve existir nenhum espaço após o último valor.

#Resolução:

# Leitura de dados

lista = []
linha = []
pos = 0
n = int(input())
for i in range(n):
    v = int(input())
    lista.append(v)
l = int(input())

# Impressão do gráfico de recorrência

for c in range(n):
    if c < n:
        for i in range(n):
            if i < n - 1:
                if lista[pos] - lista[i] >= 0:
                    if lista[pos] - lista[i] <= l:
                        print(0, end = ' ')
                    elif lista[pos] - lista[i] > l:
                        print(1, end = ' ')
                else:
                    if lista[i] - lista[pos] <= l:
                        print(0, end = ' ')
                    elif lista[i] - lista[pos] > l:
                        print(1, end = ' ')
            else:
                if lista[pos] - lista[i] >= 0:
                    if lista[pos] - lista[i] <= l:
                        print(0)
                    elif lista[pos] - lista[i] > l:
                        print(1)
                else:
                    if lista[i] - lista[pos] <= l:
                        print(0)
                    elif lista[i] - lista[pos] > l:
                        print(1)
        pos += 1
    else:
        break
    
    