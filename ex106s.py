c = ('\033[m',        #0 - sem cores
     '\033[0;30;41m',  #1 - vermelho
     '\033[0;30;42m',  #2 - verde
     '\033[0;30;43m',  #3 - amarelo
     '\033[0;30;44m',  #4 - azul
     '\033[0;30;45m',  #5 - roxo
     '\033[47;30m'     #6 - branco
     )


def help_system():
    from time import sleep
    print("Système d'Aide Python")

    while True:
        print(c[5], end='')
        help_usuario = input('Fonction ou Bibliothèque: ',)
        print(c[4],end='')
        sleep(0.5)
        print(f'Accéder au manuel {help_usuario}: ')
        print(c[0], end='')
        sleep(1)
        help(help_usuario)
        print(c[3], end='')
        cont = str(input('Souhaitez-vous continuer (Oui ou Non): '))[0]
        print(c[0], end='')
        if cont.upper() == 'N':
            print(c[2], end='')
            print('Déconnexion...appel refusé')
            sleep(1)
            print('La Fin, Au revoir!')
            print(c[0], end='')
            break


help_system()



