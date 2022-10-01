secreto = "protocolo"
digitadas = []
chances = 5

print ('-=' * 20)
print ('        JOGO DA FORCA')
print ('-=' * 20)

while True:

    letra = str(input('Digite uma letra: '))
    if len(letra)>1:

        print('Errou, não vale digitar a mesma a mesma letra')
        continue
    digitadas.append(letra)
    secreto_temporário = ' '
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporário += letra_secreta
        else:
            secreto_temporário += '*'
    
    if secreto_temporário == secreto:
        print('você venceu e escapou da forca!')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporário}')

    if letra not in secreto:
        chances -= 1

    if chances <=0:
        print('Você perdeu! FORCA!')
        break

    print(f'Você tem {chances} chances.')
    print()