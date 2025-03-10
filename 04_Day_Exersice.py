#Exercise 1

No1 = "Thirty"
No2 = "Days"
No3 = "Of"
No4 = "Python"
Space = " "
Full = No1 +Space +No2 +Space +No3 +Space +No4
print(Full)
print(len(Full))

#Exersice 2

no1 = "Coding"
no2 = "For"
no3 = "All"
space =" "
full = no1 +space +no2 +space +no3 
print(full)
print(len(full))

#Exersice 3

company = 'Coding For All'

#Excersice 4

print(company)

#Exersice 5

print(len(company))

#Exersice 6

print(company.upper())

#Exersice 7

print(company.lower())

#Exersice 8

string = "Coding Foe All"
print(string.capitalize())
print(string.title())
print(string.swapcase())

#Exersice 9

print(company[0:6])

#Exersice 10

oracion = 'Python For Everyone'
print(oracion.replace('Everyone', 'All'))

#Exersice 11

print(company.split())

#Exersice 12

empresas = "Facebook, Google, Microsoft, IBM, Apple, Oracle, Amazon"
print(empresas.split(', '))

#Exersice 13

print(company[0])

#Exersice 14

print(len(company) - 1)

#Exersice 15

print(company[10])

#Exersice 16

acronimo1 = ''.join([palabra[0]for palabra in 'Python For Everyone'.split()])
print(acronimo1)

#Exersice 17

acronimo2 = ''.join([palabra[0] for palabra in 'Coding For All'.split()])
print(acronimo2)

#Exersice 18

print(company.index('C'))

#Exersice 19

print(company.index('F'))

#Exersice 20

print(company.rfind('1'))

#Exersice 21

oracion = 'You cannot end a sentence with because because because is a conjuction'
print(oracion.find('because'))

#Exersice 22

print(oracion.rindex('because'))

#Exersice 23

print(oracion[34:57])

#Exersice 24

print(company.startswith('Coding'))

#Exersice 25

print(company.endswith('Coding'))

#Exersice 26

print('    Coding For All    '.strip())

#Exersice 27

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

#Exersice 28

bibliotecas_python = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(bibliotecas_python))

#Exersice 29

print("I am enjoy this challenge.\nI just wonder what is next")

#Exerisice 30

print("Name\tAge\tCountry\tCity\tAsabeneh\t250\tFinland\tHelsinki")

#Exersice 31

radio = 10
area = 3.14 * radio **2

#Exersice 32

print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")