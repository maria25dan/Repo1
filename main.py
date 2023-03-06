print("Hello World")

#comenariu

'''
comment
 multi 
 line
'''

#camelCase
#snake_case
#PascalCase - folosit la clase

numePrenume = "Andrei Pop"
print(numePrenume)

nume, prenume = 'Pop', 'Andrei'
print(nume, prenume)

### TIPURI DE DATE (PRIMITIVE) ###

# string -> text
# int -> numere intregi
# boolean -> True si False
# float -> numere cu zecimale, cu PUNCT intre ele

variabila_string = 'text'
variabila_int = 25
variabila_boolean_true = True
variabila_boolean_false = False
variabila_float = 25.75

print(type(variabila_string))
print(type(variabila_int))

text_numar = '3'
text_numar_secund= '5'
numar = int(text_numar)
numar2 = int(text_numar_secund)
suma = numar + numar2
print(suma)

suma2 =  text_numar + text_numar_secund
print(suma2)

#text_neconvertibil = '4j'
#variabila_intreaga = int (text_neconvertibil)  => nu se poate converti pentru ca int nu are voie sa aiba litere

print("Hello \n Anto")
print('Hello \'Anto\'')
print("Hello \"Anto\"")
print("Hello 'Anto'")

#Concatenare
text_1 = "Afara ploua"
text_2 = "imi place"
text_3 = "nu vreau sa ninga"

string_concatenat = text_1 + text_2 + text_3
print(string_concatenat)
print(text_1 + text_2 + text_3)
print(string_concatenat)

ziua_curenta = 24
print(string_concatenat + str(ziua_curenta))

imi_place_programarea = True
assert imi_place_programarea == True, "Eroare! nu imi place programarea"
print("Am trecut de assert!")

# user =  "abcUser"
# expected_pass = "pass123"
# inserted_pass = input ("Va rugam introduceti parola")
# print(expected_pass==inserted_pass)
# assert expected_pass == inserted_pass, "Eroare, ati introdus gresit parola"

# user = "abcUser"
# expected_password ="pass123"
# inserted_password = input("Va rugam sa inserati parola: ")
# print(expected_password==inserted_password) # printeaza rezultatul evaluarii
# assert expected_password==inserted_password,"Eroare: parola gresita, mai aveti doua incercari"


# a =  int(input("va rugam ..."))
# b = int(input("va rugam introduceti alt nr")
# print (type(a))

# functia input returneaza valori de tip string.
# Ca sa putem sa le procesam ca int trebuie sa facem type casting
a = int(input("Va rugam sa introduceti primul numar: "))
b = int(input("Va rugam sa introduceti al doilea numar: "))
suma = a + b
print(suma)

### STRING SLICING ###

'''
Index :      0 1 2 3 4
Caracter:    A f a r a
'''
text = "Afara ninge linistit"
# print(text[0:4])
# print(text[0:5:1])
# print(text[0:5:2])
print(text[::2])
print(text[::])
print(text[-3:])
print(text[::-1])
print(len(text))





















