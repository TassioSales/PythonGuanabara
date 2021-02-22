from datetime import date 
ano = int(input("Digite que ano deseja analisar: ou digite 0 para o ano atual "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} e BISSEXTO')
elif ano == 0:
    ano = date.today().year
else:
    print(f'O ano {ano} NÃO e BISSEXTO')

