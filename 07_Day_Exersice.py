# Ejercicio 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Ejercicio 2
print(len(it_companies))

# Ejercicio 3
it_companies.add('Twitter')
print(it_companies)

# Ejercicio 4
it_companies.update(['X', 'Steam', 'Instagram'])
print(it_companies)

# Ejercicio 5
it_companies.remove('Twitter')
print(it_companies)

# Ejercicio 6 
it_companies.discard('OLA')
print(it_companies)

# Ejercicio 1
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Ejercicio 2
c = B.union(A)
print(c)

# Ejercicio 3
print(A.intersection(B))

# Ejercicio 4
print(A.issubset(B))

# Ejercicio 5
print(A.isdisjoint(B))

# Ejercicio 6
print(B.union(A))
print(A.union(B))

# Ejercicio 7
print(A.symmetric_difference(B))

# Ejercicio 8
del A
del B