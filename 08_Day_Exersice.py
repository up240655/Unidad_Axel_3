perro = {}

perro['nombre'] = 'Rocky'
perro['color'] = 'Cafe'
perro['raza'] = 'Golden Retriver'
perro['patas'] = 4
perro['edad'] = 1

print("Diccionario perro:", perro)

estudiante = {
    'nombre': 'Axel',
    'apellido': 'Montes',
    'género': 'Masculino',
    'edad': 18,
    'estado_civil': 'Soltero',
    'habilidades': ['Python', 'Futbol', 'Ingles'],
    'país': 'Mexico',
    'ciudad': 'Aguacalientes',
    'dirección': 'Prolongacion Primavera #210'
}
longitud_estudiante = len(estudiante)
print("Longitud del diccionario estudiante:", longitud_estudiante)

tipo_habilidades = type(estudiante['habilidades'])
print("Tipo de dato de habilidades:", tipo_habilidades)

estudiante['habilidades'].append('Análisis de Datos')
estudiante['habilidades'].append('Machine Learning')
print("Habilidades actualizadas:", estudiante['habilidades'])

claves_estudiante = list(estudiante.keys())
print("Claves del diccionario estudiante:", claves_estudiante)

valores_estudiante = list(estudiante.values())
print("Valores del diccionario estudiante:", valores_estudiante)

tuplas_estudiante = list(estudiante.items())
print("Diccionario como lista de tuplas:", tuplas_estudiante)

estudiante.pop('estado_civil')
print("Diccionario estudiante después de eliminar estado civil:", estudiante)

del perro
print("Diccionario perro eliminado.")
