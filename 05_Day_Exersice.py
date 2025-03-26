# Ejercicio 1

lista_vacia = []

# Ejercicio 2

mi_lista = [1, 2, 3, 4, 5, 6, 7]

# Ejercicio 3

longitud_lista = len(mi_lista)
print("Longitud de la lista:", longitud_lista)

# Ejercicio 4

primer_elemento = mi_lista[0]
elemento_medio = mi_lista[len(mi_lista) // 2]
ultimo_elemento = mi_lista[-1]
print("Primer elemento:", primer_elemento, "Elemento del medio:", elemento_medio, "Último elemento:", ultimo_elemento)

#  Ejercicio 5

tipos_de_datos_mixtos = ["Juan", 30, 1.75, "Soltero", "Calle Falsa 123"]

# Ejercicio 6

empresas_it = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Ejercicio 7

print("Empresas de IT:", empresas_it)

# Ejercicio 8

print("Número de empresas:", len(empresas_it))

# Ejercicio 9

print("Primera empresa:", empresas_it[0])
print("Empresa del medio:", empresas_it[len(empresas_it) // 2])
print("Última empresa:", empresas_it[-1])

# Ejercicio 10

empresas_it[1] = "Alphabet"
print("Empresas de IT modificadas:", empresas_it)

# Ejercicio 11

empresas_it.append("Tesla")
print("Empresas de IT después de agregar:", empresas_it)

# Ejercicio 12

empresas_it.insert(len(empresas_it) // 2, "Netflix")
print("Empresas de IT después de insertar:", empresas_it)

# Ejercicio 13

empresas_it[3] = empresas_it[3].upper()
print("Empresas de IT después de cambiar a mayúsculas:", empresas_it)

# Ejercicio 14

empresas_unidas = '#;  '.join(empresas_it)
print("Empresas unidas:", empresas_unidas)

# Ejercicio 15

empresa_a_verificar = "Google"
print(f"¿{empresa_a_verificar} está en la lista? {empresa_a_verificar in empresas_it}")

# Ejercicio 16 

empresas_it.sort()
print("Empresas de IT ordenadas:", empresas_it)

# Ejercicio 17

empresas_it.reverse()
print("Empresas de IT en orden descendente:", empresas_it)

# Ejercicio 18 

primeras_tres = empresas_it[:3]
print("Primeras tres empresas:", primeras_tres)

# Ejercicio 19 

ultimas_tres = empresas_it[-3:]
print("Últimas tres empresas:", ultimas_tres)

# Ejercicio 20 

indice_medio = len(empresas_it) // 2
empresa_medio = empresas_it[indice_medio] if len(empresas_it) % 2 != 0 else empresas_it[indice_medio-1:indice_medio+1]
print("Empresa(s) del medio:", empresa_medio)

# Ejercicio 21 

empresas_it.pop(0)
print("Empresas de IT después de eliminar la primera:", empresas_it)

# Ejercicio 22

indice_medio = len(empresas_it) // 2
if len(empresas_it) % 2 != 0:
    empresas_it.pop(indice_medio)
else:
    empresas_it.pop(indice_medio - 1)
    empresas_it.pop(indice_medio - 1)
print("Empresas de IT después de eliminar la(s) del medio:", empresas_it)

# Ejercicio 23

empresas_it.pop(-1)
print("Empresas de IT después de eliminar la última:", empresas_it)

# Ejercicio 24

empresas_it.clear()
print("Empresas de IT después de eliminar todas:", empresas_it)

# Ejercicio 25

del empresas_it
# print(empresas_it)  # Esto dará un error porque la lista ya no existe

# Ejercicio 26

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end

# Ejercicio 27

full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Python") + 1, "SQL")
print("Full Stack después de insertar Python y SQL:", full_stack)


# Ejercicio 1
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ejercicio 2

edades.sort()
edad_minima = min(edades)
edad_maxima = max(edades)
print("Edades ordenadas:", edades)
print("Edad mínima:", edad_minima)
print("Edad máxima:", edad_maxima)

# Ejercicio 3

edades.append(edad_minima)
edades.append(edad_maxima)
print("Edades después de agregar mínima y máxima:", edades)

# Ejercicio 4

longitud_edades = len(edades)
if longitud_edades % 2 == 0:
    mediana = (edades[longitud_edades // 2 - 1] + edades[longitud_edades // 2]) / 2
else:
    mediana = edades[longitud_edades // 2]
print("Mediana de las edades:", mediana)

# Ejercicio 5

promedio_edades = sum(edades) / len(edades)
print("Edad promedio:", promedio_edades)

# Ejercicio 6

rango_edades = edad_maxima - edad_minima
print("Rango de las edades:", rango_edades)

# Ejercicio 7

diferencia_min = abs(edad_minima - promedio_edades)
diferencia_max = abs(edad_maxima - promedio_edades)
print("Diferencia entre mínima y promedio:", diferencia_min)
print("Diferencia entre máxima y promedio:", diferencia_max)

# Ejercicio 8

paises = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
longitud_paises = len(paises)
if longitud_paises % 2 == 0:
    paises_medios = paises[longitud_paises // 2 - 1:longitud_paises // 2 + 1]
else:
    paises_medios = [paises[longitud_paises // 2]]
print("País(es) del medio:", paises_medios)

# Ejercicio 9

mitad = (longitud_paises + 1) // 2 
primera_mitad = paises[:mitad]
segunda_mitad = paises[mitad:]
print("Primera mitad de países:", primera_mitad)
print("Segunda mitad de países:", segunda_mitad)

# Ejercicio 10

primeros_tres, *paises_escandinavos = paises
print("Primeros tres países:", primeros_tres)
print("Países escandinavos:", paises_escandinavos)