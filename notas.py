# gestor de notas

alumnos = { 
    'Ana' : 8.5,
    'Luís' : 7.0,
    'Alba' : 9.2,
    'Héctor' : 4.7
}

def calcular_media (lista_alumnos):
    if lista_alumnos:
        return sum(lista_alumnos.values()) / len(lista_alumnos)

print('Listado de alumnos y notas: ')
for nombre, nota in alumnos.items():
    print(f'{nombre}: {nota}')

print(f'La nota media del grupo es de: {calcular_media(alumnos):.2f}')
