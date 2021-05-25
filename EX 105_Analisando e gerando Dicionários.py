def notas(*n, sit=False):
    """
    ->Função para analisar uma o mais notas de alunos
    :param n: uma o mais notas de alunos
    :param sit: valor opcional se deve ou nao adicionar
    :return:retorna uma dicinario com as informaçoes
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(8.0, 5.0, 9.0, 6.0, 8.4, sit=True)
print(resp)
