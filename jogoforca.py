import os, 

def clear ():
    os.system('cls')

def campeao():
    print("YOU WIN!!!")
    return(campeao)

def jogo(erros):
    if erros == 0:
        jogo()
    elif erros == 1:
        erro1()
    elif erros == 2:
        erro2()
    elif erros == 3:
        erro3()
    elif erros == 4:
        erro4()
    elif erros == 5:
        erro5()

def historico():
    print()
    try: 
        arquivo = open("historico.txt","r")
        conteudo = arquivo.read()
        arquivo.close()
        return conteudo
    except:
        arquivo = open("historico.txt","w")
        arquivo.close()
        return ""
def historico02():
    try: 
        arquivo = open("historico.txt","r")
        conteudo = arquivo.readlines()
        arquivo.close()
        return conteudo
    except:
        arquivo = open("historico.txt","w")
        arquivo.close()
        return []

def competidor():
    print()

def madeira ():
    print('''  
     ____
    |
    |
    |
    |
   _|_  ''')

def erro1():
    print('''
     ____
    |    |
    |   ( )
    |
    |
   _|_ ''')

def erro2():
    print('''
     ____
    |    |
        ( )
    |    |
    |    |
    |
   _|_ ''')

def erro3():
    print('''
     ____
    |    |    
    |   ( )
    |    |\
    |    |
    |
    |    
   _|_ ''')

def erro4():
    print('''
     ____
    |    |    
    |   ( )
    |   /|\
    |    |
    |   / 
    |    
   _|_
    ''')

def ganhou():
    clear()
    campeao()
    print('''
     ____
    |    |    
    |   ( )
    |   /|\
    |    |
    |   / \
    |    
   _|_ 
        
   ''')

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
options = ['1', '2', '3']




   






    
