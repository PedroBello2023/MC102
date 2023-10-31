
if fantasma[f] == 'L':
    fantasma[f] = mansao[a][l][c+1]
if fantasma[f] == 'C':
    fantasma[f] = mansao[a+1][l][c]
if fantasma[f] == 'O':
    fantasma[f] = mansao[a-1][l][c]
if fantasma[f] == caçador[c]:
    caçadores_capturados += 1