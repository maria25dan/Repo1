# 1.Funcție care să calculeze și să returneze suma a două numere
# def suma(a, b):
#     return (a+b)
# print(f"Suma este:", suma(5,10)) # 15
# print(f"Suma este:", suma(3,11)) # 14

#2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
# def numar(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
# print(numar(16)) # returneaza True
# print(numar(17)) # returneaza False

# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)
# def numarTotal (nume, prenume, nume_mijlociu):
#     total_caractere = nume + prenume + nume_mijlociu
#     return len(total_caractere)
#
# nume = input("introdu numele:  ")
# prenumele = input("introdu prenumele:  ")
# nume_mijloc = input("introdu numele din mijloc:  ")
#
# print(f"Numarul total de caractere este: ", numarTotal('Dan', 'Ana', 'M'))
# print(f"Numarul total de caractere este: ", numarTotal('Dan', 'Ana', 'Maria'))
# print(f"Numarul total de caractere este: ", numarTotal(nume, prenumele, nume_mijloc))

# 4. Funcție care returnează aria dreptunghiului
# def arie(a,b):
#     aria = a*b
#     print(f"Aria dreptunghilui este: {aria}")
#
# arie(2,5)
# arie(10,8)

# 5. Funcție care returnează aria cercului
# def arie_cerc():
#     pi = 3.14
#     r = int(input('Raza este: '))
#     arie_final = pi * r ** 2
#     return arie_final
# print(f"Aria este: {arie_cerc()}")

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și False dacă nu găsește.
# def caracter(cuvant):
#     if 'x' in cuvant:
#         return True
#     else:
#         return False
# cuvant_x = input("Introduce-ti un cuvant:  ")
# print(f"se gaseste x in cuvantu: {caracter(cuvant_x)} ?")

# Introduce-ti un cuvant:  ana
# se gaseste x in cuvantu: False ?
# Introduce-ti un cuvant:  axa
# se gaseste x in cuvantu: True ?

# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case este y

# def caractere2(cuvant2):
#     litere_mici = 0
#     litere_mari = 0
#     for i in cuvant2:
#         if i.isupper():
#             litere_mari +=1
#         else:
#             litere_mici +=1
#     print(f"litere mici sunt: {litere_mici}")
#     print(f"litere mari sunt: {litere_mari}")
# caractere2('TesTu')
# # litere mici sunt: 3
# # litere mari sunt: 2

# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive

# def nr_pozitive(numere):
#     lista =[]
#     for numar in numere:
#         if numar > 0:
#             lista.append(numar)
#     return lista
# print(f"Lista cu nr pozitive este: {nr_pozitive([8, -11, 5, -3, 4])}")

# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

# def doua_numere (x, y):
#     if x > y:
#         print(f'Primul numar x este mai mare decat al doilea nr y ')
#     elif y > x:
#         print(f'Al doilea nr y este mai mare decat primul nr x')
#     else:
#         print(f"Numerele sunt egale")
#
# doua_numere (15, 0)
# doua_numere (5, 10)
# doua_numere (5, 5)

# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
nr = int(input(f"Introduceti nr de adaugat in set: "))
set = {7, 8, 9, 4, 5, 6, -1}

def mixt (nr, set):
    if nr in set:
        print(f"nu am adaugat numărul în set. Acesta există deja")
        return False
    else:
        set.add(nr)
        print(f"am adaugat numărul nou {nr} în set, setul este {set}")
        return True
print(mixt(nr, set))

