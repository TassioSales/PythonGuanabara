def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade  = anoatual - ano
    if idade < 16:
        return f'Com {idade} anos: Não vota: '
    elif 16 <= idade  < 18  or idade > 65:
        return f'Com {idade} anos: Não Opcional: '
    else:
        return f'Com {idade} anos: Voto Obrigatorio'

nasc = int(input('Em que ano voce nasceu: '))
print(voto(nasc))
