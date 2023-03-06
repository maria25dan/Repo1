#  1. o variabila este o casuta (goala) careia noi ii dam o valoare / o identitate
# 2:
string = "haine"
numar = 89
float = 3.53
bool = True

# 3:
    # print(type(string))
    # print(type(numar))
    # print(type(float))
    # print(type(bool))

# 4: Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
# - Verifică tipul acesteia.
    # float=round(float)
    # print(float)
    # print(type(float)) # => <clasa 'int'>

#5 Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești. -  nu sunt
    # print("Variaba de tip strig este:",string)
    # print("Variaba de tip int este:",int)
    # print("Variaba de tip float este:",float)
    # print(f'Variaba de tip bool este: {bool}')

# 6. Citește de la tastatură:# - numele; # - prenumele. Afișează: 'Numele complet are x caractere'.
    # numele = input("Va rugam sa scrieti numele: ")
    # prenumele = input("Va rugam sa scrieti prenumele: ")
    # nume_complet = (len(numele)+len(prenumele))
    # print(f'Numele complet are {nume_complet} caractere')

# 7. Citește de la tastatură: - lungimea; - lățimea. Afișează: 'Aria dreptunghiului este x'.
    # lungime = int(input('Va rugam introduceti lungimea: '))
    # latime = int(input("Va rugam introduceti latimea (numere): "))
    # aria = lungime*latime
    # print(aria)
    # print(f'Aria dreptunghiului este {aria} ')

# 8
    # text = 'Coral is either the stupidest animal or the smartest rock'
    #  cuvant_the=text.split()
    # print(cuvant_the.count('the'))

# 9. inlocuieste cu THE
    # print(text.replace("the","THE"))

# 10. Folosiți un assert ca să verificați dacă acest string conține doar numere.
    # text_1 = 'Coral is either the stupidest animal or the smartest rock'
    # text_2 = text_1.isdigit()
    # print(type(text_2))
    # assert text_2 == False, "Eroare - eacest text nu contine numere"
    # print('Am trecut de asert, textul contine doar litere ')

