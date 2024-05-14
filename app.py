import random

#Criando uma lista de possíveis palavras a serem sorteadas:
palavras = ['python','programacao','futebol','desenvolvedor','morango','futebol']

#escolha da palavra:
palavra_sorteada = random.choice(palavras)

#Criando uma string com traços para representar a quantidade de letras da palavra:
palavra_escondida = '*' * len(palavra_sorteada)

#criando uma lista vazia para armazenar as letras que já foram faladas:
letras_adivinhadas = []

max_tentativas = 6

while True:
    #mostrar na tela a palavra escondida:
    print(palavra_escondida)

    #pedimos ao jogador para digitar uma letra:
    letra = input('Digite uma letra> ')

    #verificar se a letra digitada já foi chutada:
    if letra in letras_adivinhadas:
        print('Você já digitou essa letra. Tente outra por favor!')
        continue

    #adicionar a letra a lista de letras digitadas:
    letras_adivinhadas.append(letra)

    #verificar se a letra digitada está presente na palavra sorteada:
    if letra in palavra_sorteada:
        lista = []
        for indice in range(len(palavra_sorteada)):
            if letra == palavra_sorteada[indice]:
                lista.append(letra)
            else:
                lista.append(palavra_escondida[indice])
        palavra_escondida = ''.join(lista) 

    else: #letra não estiver na palavra sorteada:
        max_tentativas -= 1
        print(f'Letra não encontrada! Você tem mais {max_tentativas} tentativas.')

    #verificamos se o jogador ganhou ou perdeu
    if palavra_escondida == palavra_sorteada:
        print('Parabéns! Você ganhou.')
        break
    elif max_tentativas == 0:
        print(f'Suas tentativas acabaram :( Você perdeu. A palavra sorteada era {palavra_sorteada}.)')
        break