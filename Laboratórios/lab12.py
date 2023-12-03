
# Leitura da matriz representando a mansão
A, L = [int(v) for v in input().split()]
mansao = [[] for _ in range(A)]

for andar in range(A-1,-1,-1):
    for _ in range(L):
      mansao[andar].append(list(input()))
    if andar > 0:
        input()
fantasmas = []
caçadores = []
# Leitura das posições de cada fantasma e de cada caçador
n = int(input())
for i in range(0, n):
   a, l, c = [int(v) for v in (input().split())]
   fantasmas.append([a,l,c])
   
m = int(input())
for i in range(0, m):
   a, l, c = [int(v) for v in (input().split())]
   caçadores.append([a,l,c])
# Simulação do movimento dos fantasmas
fantasmasCapturados = 0
caçadoresCapturados = 0

for fantasma in fantasmas:
    contador = 0
    limite = 150
    fa = fantasma[0]
    fl = fantasma[1]
    fc = fantasma[2]
    while True:
        contador +=1
        if contador > limite:
            break
        try:
            if fa < 0 or fl < 0 or fc < 0:
                break
            else:
                posiçãoDoFantasma = mansao[fa][fl][fc]
        except:
            break
        else:
            for caçador in caçadores:
                ca = caçador[0]
                cl = caçador[1]
                cc = caçador[2]
                if fa == ca and fl == cl and fc == cc:
                    caçadoresCapturados += 1
                    caçadores.remove(caçador)
                    break
            if posiçãoDoFantasma == "N":
                fl -= 1
            elif posiçãoDoFantasma == "S":
                fl += 1
            elif posiçãoDoFantasma == "O":
                fc -= 1
            elif posiçãoDoFantasma == "L":
                fc += 1
            elif posiçãoDoFantasma == "C":
                fa += 1
            elif posiçãoDoFantasma == "B":
                fa -= 1
            elif posiçãoDoFantasma == "X":
                fantasmasCapturados += 1
                break
# Impressão da saída
print(f'fantasmas capturados: {fantasmasCapturados}')
print(f'caçadores capturados: {caçadoresCapturados}')


