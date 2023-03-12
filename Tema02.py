# 1 eu il vad asa, exista un drum - care indeplineste anumite conditii? DA, atunci te duci pe el => if
# daca nu le indeplineste, treci mai departe pe urmatorul => else

#2:
# nota = int(input('Va rugam sa scrieti un numar mai mare decat 0: '))
# if nota < 0 :
#     print(f'Ati introdus un numar negativ')
# else:
#     print(f'Felicitari, ai introdus corect!')

#3 -  aici am incheiat cu else
# nota = int(input('Numarul introdus este numar pozitiv, negativ sau neutru?: '))
# if nota < 0 :
#   print(f'Ati introdus un numar negativ {nota}')
# elif nota == 0 :
#     print(f'Ati introdus un numar neutru {nota}')
# else:
#     print("Ai introdus un numar pozitiv")

#4
# nota = int(input('Va rugam sa scrieti un numar intre -2 si 13: '))
# if nota < 14 and nota > -3:
#     print(f'bravo')
# else:
#     print(f'n-ai introdus corect')

#5
# x = 7
# y = 1
# if abs(x - y) < 5:
#     print (f'Numarul absolut este: {x - y} ')
# else :
#     print (f'Diferenta este mai mare decat 5')

#6
# nr = int(input('Va rugam sa scrieti un numar care sa NU fie intre 5 si 27: '))
# if not (5 <= nr <= 27):
#     print(f'bravo')
# else:
#     print(f'n-ai introdus corect')

#7 - aici nu am mai incheiat cu else, e ok daca am lasat elif ca si ultima conditie?
# (cred ca nu, probabil trebuie else: si fara sa o conditionez, practic ia ultima posibilitate)
# x = int(input('Introdu valoare X: '))
# y = int(input('Introdu valoare Y: '))
# if x == y :
#     print(f'Valorile sunt egale {x==y}')
# elif x > y:
#     print(f"X mai mare decat Y")
# elif y > x:
#     print(f"Y mai mare decat X")

#8
# a = int(input('Introdu valoare a: '))
# b = int(input('Introdu valoare b: '))
# c = int(input('Introdu valoare c: '))
#
# if a == b == c:
#     print(f'Tr echilateral')
# elif a == b != c or a == c != b or b == c != a:
#     print(f'Tr isoscel')
# else :
#     print(f"Nici o latura nu este egala")

#9
#aeiouAEIOU
'''
litera = input('Introdu o vocala: ')
v1 = 'A'
v2 = 'a'
v3 = 'E'
v4 = 'e'
v5 = 'I'
v6 = 'i'
v7 = 'O'
v8 = 'o'
v9 = 'U'
v10 = 'u'
if litera == v1:
    print(f'Ai introdus {litera}')
elif litera == v2:
    print(f'Ai introdus {litera}')
elif litera == v3:
    print(f'Ai introdus {litera}')
elif litera == v4:
    print(f'Ai introdus {litera}')
elif litera == v5:
    print(f'Ai introdus {litera}')
elif litera == v6:
    print(f'Ai introdus {litera}')
elif litera == v7:
    print(f'Ai introdus {litera}')
elif litera == v8:
    print(f'Ai introdus {litera}')
elif litera == v9:
    print(f'Ai introdus {litera}')
elif litera == v10:
    print(f'Ai introdus {litera}')
else:
    print(f'Ai introdus o consoana (sau mai multe litere.')
'''

#10
'''
nota = int(input('Introdu o nota intre 1 si 10: '))
if 10 >= 9 < nota < 11:
    print('Nota in sistem american este A')
elif 9 >= 8 < nota < 10:
    print('Nota in sistem american este B')
elif 8 >= 7 < nota < 9:
    print('Nota in sistem american este C')
elif 7 >= 6 < nota < 8:
    print('Nota in sistem american este D')
elif 6 >= 4 < nota < 7:
    print('Nota in sistem american este E')
elif nota >= 1 < 5:
    print('Nota in sistem american este F')
else:
    print(f'Nota introdusa e gresita')
'''













