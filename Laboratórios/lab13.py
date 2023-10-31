###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Amigos do 495
# Nome: Pedro Henrique
# RA: 267809
###################################################

# Leitura da sequência
numeros = [int(i) for i in input().split()]

# Ordenação dos amigos do 495
n_crescente = []
for num in numeros:
    n = str(num)
    n = ''.join(sorted(n))
    n = int(n)
    n_crescente.append(n)
print(n_crescente)


# Impressão da resposta