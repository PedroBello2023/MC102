# Leitura da matriz representando a mansão
A, L = [int(v) for v in input().split()]
mansao = [[] for _ in range(A)]
fantasmas_capturados = 0
caçadores_capturados = 0
caçador = []
fantasma = []
for andar in range(A-1,-1,-1):
    for _ in range(L):
      mansao[andar].append(list(input()))
    if andar > 0:
        input()
if A == 1:
    N = int(input())
    for _ in range(0, N):
        a, l, c = [int(i) for i in input().split()]
        x = mansao[a][l][c]
        fantasma.append(x)
    M = int(input())
    for _ in range(0, M):
        i, j, k = [int(i) for i in input().split()]
        y = mansao[i][j][k]
        caçador.append(y)
    for p in range(len(caçador)):
        for f in range(len(fantasma)):
            if fantasma[f] == 'N':
                l -= 1
                fantasma[f] = mansao[a][l][c]
            if fantasma[f] == 'S':
                l += 1
                fantasma[f] = mansao[a][l][c]
            if fantasma[f] == 'O':
                c -= 1
                fantasma[f] = mansao[a][l][c]
            if fantasma[f] == 'L':
                c += 1
                fantasma[f] = mansao[a][l][c]
            if fantasma[f] == 'C':
                a += 1
                fantasma[f] = mansao[a][l][c]
            if fantasma[f] == 'B':
                a -= 1
                fantasma[f] = mansao[a][l][c]
            if fantasma[f] == f'{caçador[p]}':
                caçadores_capturados += 1
                break
            if fantasma[f] == 'X':
                fantasmas_capturados += 1
                break 
else:
    caminho = []
    fantasma = ''
    cam = []
    N = int(input())
    for _ in range(0, N):
        cam.clear()
        a, l, c = [int(i) for i in input().split()]
        fantasma = mansao[a][l][c]
        caminho.append(fantasma)
        cam.append(fantasma)
        while True:
            if 0 <= a < A and 0 <= l < L and 0 <= c < len(mansao[a][0]):
                if fantasma == 'X':
                    fantasmas_capturados += 1
                    break
                if fantasma == 'N':
                    l -= 1
                    fantasma = mansao[a][l][c]
                    caminho.append(fantasma)
                    cam.append(fantasma)
                if fantasma == 'S':
                    l += 1
                    fantasma = mansao[a][l][c]
                    caminho.append(fantasma)
                    cam.append(fantasma)
                if fantasma == 'L':
                    c += 1
                    fantasma = mansao[a][l][c]
                    caminho.append(fantasma)
                    cam.append(fantasma)
                if fantasma == 'O' :
                    c -= 1
                    fantasma = mansao[a][l][c]
                    caminho.append(fantasma)
                    cam.append(fantasma)
                if fantasma == 'C':
                    a += 1
                    fantasma == mansao[a][l][c]
                    caminho.append(fantasma)
                    cam.append(fantasma)
                if fantasma == 'B':
                    a -= 1
                    fantasma = mansao[a][l][c]
                    caminho.append(fantasma)
                    cam.append(fantasma)
            else:
                if  a < 0 or l < 0 or c < 0 or c > len(mansao[a][0]) or a >= A:
                    break
        #print(caminho)
        #print(cam)
    M = int(input())
    for _ in range(0, M):
        a, l, c = [int(i) for i in input().split()]
        caçador.append(mansao[a][l][c])
        #print(caçador)
        for posição in caçador:
            if posição in caminho:
                caçadores_capturados += 1
                caçador.clear() 

print(f"fantasmas capturados: {fantasmas_capturados}")
print(f"caçadores capturados: {caçadores_capturados}")
      
