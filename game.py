import os, random, funcoes
from symtable import Function



funcoes.limpar()
desafiante = input("Informe o nome do desafiante: ")
competidor = input("Informe o nome do competidor: ")
funcoes.limpar()

palavra_chave = input("Informe a palavra chave: ")
funcoes.limpar()

dicas = [input("Informe a dica 01:"), input("Informe a dica 02:"), input("Informe a dica 03: ")]
funcoes.limpar()

palavra = (palavra_chave)

tentativas = 0
chances = 5

letras_escolhidas=[]

space = ["_"] *len(palavra)
print("Bem vindo ao jogo da forca!")


while tentativas < chances and "".join(space) != palavra:
    funcoes.start()
    letra = input("Informe uma letra: ")
    while letra in letras_escolhidas:
        print("Essa letra já foi esolhida!")
        letra = input("Informe uma letra: ")
    letras_escolhidas.append(letra)
    funcoes.start()
    if letra in palavra:
        print("A letra está correta!")
        for i in range(len(palavra)):
            if letra == palavra[i]:
                space[i] = letra
    else:
        print("A letra está incorreta!")
        tentativas = tentativas + 1
        if tentativas == 1:
            print(funcoes.erro1())
        elif tentativas == 2:
            print(funcoes.erro2())
        elif tentativas == 3:
            print(funcoes.erro3())
        elif tentativas == 4:
            print(funcoes.erro4())
        else:
            print(funcoes.perdeu())

    print("Tentativas", tentativas, "erros", chances-tentativas,)

    print("A palavra está assim: ")
    print(space)

if tentativas == chances:
    print("Você perdeu!")
    open('histórico.txt', 'a').write(f'Competidor perdedor foi: {competidor}  -   Desafiante Ganhador foi: {desafiante}   -   A palavra foi: {palavra_chave} \n ')
    print("A palavra era", palavra)

elif tentativas != chances:
    print("Você ganhou!")
    open('histórico.txt', 'a').write(f'Ganhador foi Competidor: {competidor}  -  Perdedor foi Desafiante: {desafiante}   -   A palavra foi: {palavra_chave} \n')

print (open('histórico.txt','r').read())

try:
    avaliar = int(input("Dê uma nota para o jogo: "))
    print("A nota dada foi:",avaliar)
except:
    print("Valor informado é inválido!")

obrigado = int(input("Agradecemos pela sua avaliação, Augusto e Diogo!"))
















   
    