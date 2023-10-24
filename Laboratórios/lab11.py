###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Loteamento
# Nome: Pedro Henrique Martins Belo
# RA: 267809
###################################################

#Seu amigo possui um grande terreno e planeja realizar um loteamento, vendendo parcelas menores para cada comprador. Como a tarefa de gerenciar os lotes não é trivial, ele pediu para você criar um programa para auxiliar no gerenciamento das vendas.

#O terreno original possui 15 unidades de largura e 15 unidades de comprimento. Como a área será habitada, seu amigo irá criar ruas que irão atravessar a área na vertical e na horizontal. Além disso, ele venderá o restante da terra para compradores, que indicarão a porção de terra que cada um deles tem interesse.

#Seu programa deverá ler duas linhas, com as informações das ruas. A primeira linha possuirá um ou mais valores inteiros indicando os índices na matriz em que as ruas horizontais serão criadas e a segunda linha possuirá um ou mais valores inteiros representando os índices na matriz em que as ruas verticais serão criadas. Na próxima linha, seu código receberá um valor inteiro n, indicando a quantidade de compradores, sendo que n será menor ou igual a 9. Nas próximas n linhas, você deverá ler quatro inteiros, sendo os dois primeiros representando a linha e a coluna do canto superior esquerdo do lote, enquanto os dois últimos representam a linha e a coluna do canto inferior direito do lote de interesse do comprador, sendo que o lote sempre terá formato retangular. O canto superior esquerdo do loteamento é indicado como linha 0 e coluna 0. Caso a proposta de compra conflite com um lote já vendido ou com uma rua, aquela compra não será realizada.

#Como saída, seu código deverá imprimir o mapa do terreno, sendo as ruas representadas pelo caracter ., e os terrenos vendidos representados pelo número do comprador (começando de 1 e indo até 9). Pedaços do terreno não vendidos deverão ser representadas por x.

#Exemplos de entradas e saídas esperadas pelo seu programa:

#Resolução:

loteamento = []
for i in range(0, 15):
  linha = []
  for j in range(0, 15):
    linha.append('x')
  loteamento.append(linha)
# Leitura de dados
n = [int(k) for k in input().split()]
o = [int(a) for a in input().split()]
compradores = int(input())
# Processamento
for q in range(len(n)):
  for i in range(0, 15):
      loteamento[n[q]][i] = loteamento[n[q]][i].replace('x','.')
  for j in range(0, 15):
      loteamento[n[q]][j] = loteamento[n[q]][j].replace('x', '.')
for s in range(len(o)):
  for y in range(0, 15):
      loteamento[y][o[s]] = loteamento[y][o[s]].replace('x', '.')
for comprador in range(1, compradores + 1):
    a, b, c, d = [int(v) for v in input().split()]
    if all(loteamento[x][w] == 'x' for x in range(a, c + 1) for w in range(b, d + 1)):
       for i in range(a, c + 1):
          for j in range(b, d + 1):
             loteamento[i][j] = f'{comprador}'
# Impressão da saída
for linha in loteamento:
  print(" ".join(linha))