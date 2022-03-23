import random
from secrets import choice

#variaveis


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*"

#criar o gerador
tamanho = int(input("Quantos caracteres tera sua senha?: "))
senha = ""

for e in range(0,tamanho):
    caracteres_senha = random.choice(chars)
    senha += caracteres_senha

#Colocar a senha na tela

print("gerando senha...")
print("Sua senha é: ", senha)

#Funcao para gerar o nome senha 

#Codigo criado por Vinicius Aguilar Lopes
#Esse codigo cria uma senha trocando as vogais de uma palavra por caracteres especiais e numeros

def gerar_nome(nome):
    crypted = ""
    nome.lower()
    letra_a = "4@"
   
    for e in nome:
        for i in e:
            if i == "a":
                crypted += random.choice(letra_a)
            elif i == "e":
                crypted += "3"
            elif i == "i":
                crypted += "1"
            elif i == "o":
                crypted += "0"
            else:
                crypted += i
    randomizar_letras(crypted)
      


def randomizar_letras(letras):

    lista = ""
    b = "12"

    for o in letras:
        escolher = random.choice(b)
        if escolher == "1":
            lista += o.upper()
        else:
            lista += o.lower()
    
    print('gerando senha...')
    print('senha: ', lista)


senha = input('Escreva uma palavra ou nome que deseja criar como senha: ')
gerar_nome(senha)


        
    

