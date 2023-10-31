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
    if andar >= 0:
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
                    #break
                if fantasma[f] == 'X':
                    fantasmas_capturados += 1
                    #break       
print(f"fantasmas capturados: {fantasmas_capturados}")
print(f"caçadores capturados: {caçadores_capturados}")

       