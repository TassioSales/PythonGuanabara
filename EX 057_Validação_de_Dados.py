sexo = str(input('Informe seu sexo [M/F]')).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input('Dados invalidos por favor Informe seu sexo [M/F]')).strip().upper()[0]
print(f'Sexo {sexo} Registrado com sucessor')
  
        