# gestor de notas

alumnos = { 
    'Ana' : 8.5,
    'Luís' : 7.0,
    'Alba' : 9.2,
    'Héctor' : 4.7
}

print('Listado de alumnos y notas: ')
for nombre, nota in alumnos.items():
    print(f'{nombre}: {nota}')
