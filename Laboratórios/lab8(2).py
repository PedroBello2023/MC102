n = int(input())
palavras = []
for i in range(n):
    palavras.append(str(input()))
anagramas = {}   
for p in palavras:
    classPalavras = "".join(sorted(p))
    if classPalavras not in anagramas:
        anagramas[classPalavras] = [p] 
    else:
        anagramas[classPalavras].append(p)
lista = list(anagramas.values())
for indice in lista:
    for i in indice:
        if i == indice[-1]: 
            print(i) 
        else:
            print(i, end = '-')
            
            
