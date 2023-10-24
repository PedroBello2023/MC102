###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Loteamento
# Nome: 
# RA: 
###################################################

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