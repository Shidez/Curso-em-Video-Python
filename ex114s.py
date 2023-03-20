
def sitePudim():
    import requests
    from time import sleep
    while True:
        try:
            site = requests.get('http://www.pudim.com.br/')
            if site.status_code == 200:
                site_ok = (str(input('Site pudim sem problema nenhum! Deseja ver o pudim? [S/N]: '))).strip().upper()[0]
                if site_ok == 'S':
                    sleep(0.5)
                    print('Clique aqui: http://www.pudim.com.br/')
                    sleep(0.5)
                    print('Programa encerrado!')
                    break
                elif site_ok == 'N':
                    print('xatu, não quer ver o pudim!')
                    sleep(0.5)
                    print('Programa encerrado!')
                    break

                else:
                    print('Opção invalida!')

        except IndexError:
            print('Usuário não digitou nada!')

        except requests.exceptions.ConnectionError:
            print('Site pudim com problemas, não acessivel!')
            break


n = input(sitePudim())
print(n)



