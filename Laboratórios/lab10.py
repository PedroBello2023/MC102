#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caçadores de Tesouros
# Nome: Pedro Henrique Martins Belo
# RA: 267809
#####################################################

def seguinte(l,c,letra, mapa):
    if letra == 'N':
        l -= 1
    if letra == 'S':
        l += 1
    if letra == 'L':
        c += 1
    if letra == 'O':
        c -= 1
    return mapa[l][c], l, c

def faztroca(l,c,mapa, valor_atual, valor_seguinte, indice):
    aux = valor_atual
    valor_atual = valor_seguinte
    mapa[l][c] = aux
    return valor_atual, mapa
   







# Leitura do mapa
n, m = [int(i) for i in input().split()]
list = []
mapa = []
for _ in range(n):
  linha = [int(i) for i in input().split()]
  mapa.append(linha)
q = int(input())
for i in range(q):
    l, c = [int(i) for i in input().split()]
    caminho = str(input()).upper()
    valor_atual = mapa[l][c]
    for indice in range(len(caminho)):
        letra = caminho[indice]
        valor_seguinte, x, y = seguinte(l,c,letra, mapa)
        

        if valor_atual < valor_seguinte:
            valor_atual, mapa = faztroca(x,y, mapa, valor_atual, valor_seguinte, indice)
        if indice == 0:
            mapa[l][c] = 0
        l=x
        c=y
        if indice == len(caminho) - 1:
            print(f"Caçador {i+1}: {valor_atual}")
            
            
                
       



