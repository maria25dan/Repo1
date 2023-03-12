'''
1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
'''

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# for pare in alte_numere:
#     if pare % 2 == 0:
#         numere_pare.append(pare)
#         print(f"Numere pare sunt:", numere_pare)
# numere_impare = []
# for impare in alte_numere:
#     if impare % 2 != 0:
#         numere_impare.append(impare)
#         print(f"Numere impare sunt:", numere_impare)
# numere_pozitive = []
# for pozitive in alte_numere:
#     if pozitive > 0:
#         numere_pozitive.append(pozitive)
#         print(f"Numere pozitive sunt:", numere_pozitive)
# numere_negative = []
# for negative in alte_numere:
#     if negative < 0:
#         numere_negative.append(negative)
#         print(f"Numere negative sunt:", numere_negative)

'''
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4
'''
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#
# for i in range (len(alte_numere)):
#     for j in range (i+1, len(alte_numere)):
#         if alte_numere[i] > alte_numere [j]:
#             alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]
# print(alte_numere)
'''
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr
Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!
'''

# import random
# numar_secret = random.randint(1, 30)
# numar_ghicit = None
# while numar_secret:
#     numar_ghicit = int(input('Introduceti un nr intre 1 si 30'))
#     if numar_ghicit > numar_secret:
#        print(f"Numar {numar_ghicit} mai mare decat {numar_secret}")
#     if numar_ghicit < numar_secret:
#        print(f"Numar {numar_ghicit} mai mic decat {numar_secret}")
#     if numar_ghicit == numar_secret:
#        print(f"Felicitari ai ghicit {numar_secret}")
#
'''
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777
Ex:3
1
22
333
'''
# n = int(input("Introduceti inaltimea piramidei: "))
# for i in range (1, n+1):
#     for j in range (i):
#         print(f'{i}', end="")
#     print('')

'''
5.
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
'''

# tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
#
# for i in range(len(tastatura_telefon)):
#     for j in range(len(tastatura_telefon[i])):
#         print(f"Cifra curenta este:", tastatura_telefon[i][j])
