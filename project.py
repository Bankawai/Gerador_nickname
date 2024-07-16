import random

def sortearLetra():
    LetraSorteada=alfabeto[random.randint(0,len(alfabeto)-1)]

    for letra in vogais:
        if LetraSorteada==letra:
            tipo="vogal"
            break
        
    for letra in consoante:
        if LetraSorteada==letra:
           tipo="consoante"
           break

    
    return LetraSorteada, tipo


def FormarPalavra(tipo):
    if tipo == "consoante":
        letra=vogais[random.randint(0,len(vogais)-1)]
        tipo="vogal"
    else:
          
         letra=consoante[random.randint(0,len(consoante)-1)] 
         tipo="consoante"
    return letra, tipo


    



alfabeto = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
alfabeto = alfabeto.replace(" ","")
alfabeto = alfabeto.split(",")




vogais=list()
consoante=list()
palavra=list()

for letra in alfabeto:
    if letra== "A" or letra=="E" or letra=="I" or letra=="O" or letra=="U":
        vogais.append(letra)
    else:
        consoante.append(letra)


tamanho = int(input("Quantas letras terá o nick?"))


PrimeiraLetra=sortearLetra()
Aux=PrimeiraLetra

for i in range(tamanho):
    Aux=FormarPalavra(Aux[1])
    palavra.append(Aux[0])


PalavraFinal= "".join(palavra)




print(PalavraFinal)

