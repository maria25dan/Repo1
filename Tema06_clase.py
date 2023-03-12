'''
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
'''

# definire clasa
#
# class Cerc:
#
#     raza = None
#     pi = 3.14
#     culoare = None
#
#     # definire constructor:
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     # definire metoda:
#     def descrie_cerc(self):
#         print(f"Raza este {self.raza} de culoare {self.culoare} .")
#
#     # definire metoda:
#     def aria(self):
#         aria = self.pi * self.raza ** 2
#         return aria
#
#     # definire metoda:
#     def diametru(self):
#         diametru = 2 * self.raza
#         return diametru
#
#     # definire metoda:
#     def circumferinta(self):
#         circumferinta = 2 * self.pi * self.raza
#         return circumferinta
#
# #definire obiecte:
# cerc1 = Cerc(3, "verde")
# cerc2 = Cerc(5, "galben")
#
# #apelare metode pentru obiectele definite
# cerc1.descrie_cerc()
# print(f"Aria cercului este {cerc1.aria()}.")
# print(f"Diametrul este : {cerc1.diametru()} . ")
# print(f"Circumferinta este {cerc1.circumferinta()} . ")
#
# print("------------------------------------------------")
#
# cerc2.descrie_cerc()
# print(f"Aria cercului este {cerc2.aria()} . ")
# print(f"Diametrul este : {cerc2.diametru()} . ")
# print(f"Circumferinta este {cerc2.circumferinta()} . ")


''' 
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
 '''
#
# class Dreptunghi:
#     lungime = None
#     latime = None
#     culoare = None
#
#     # constructor
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     #metode
#     def descrie(self):
#         print(f"Dreptunghiu are lungimea de {self.lungime} , latimea de {self.latime} si culoarea - {self.culoare} - .")
#
#     def aria(self):
#         aria = self.lungime * self.latime
#         return aria
#
#     def perimetru(self):
#         perimetru = 2 * self.aria()
#         return perimetru
#
#     def schimba_culoare(self, culoare_noua):
#         self.culoare = culoare_noua
#         self.descrie()  # asa apelam o metoda descriere in alta metoda schimb_culoare
#
# # obiecte
# obiect1 = Dreptunghi(4, 2, "verde")
# obiect2 = Dreptunghi(8, 4, "galben")
#
# #apelare metode pentru fiecare obiect
# obiect1.descrie()
# print(f"Aria este : {obiect1.aria()}  .")
# print(f"Perimetrul este : {obiect1.perimetru()}  .")
# obiect1.schimba_culoare('negru')
#
# print(f"---------------------------------------------------------------")
#
# obiect2.descrie()
# print(f"Aria este : {obiect2.aria()}  .")
# print(f"Perimetrul este : {obiect2.perimetru()}  .")
# obiect2.schimba_culoare('negru')

'''
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
'''

# class Angajat:
#     nume = None
#     prenume = None
#     salariu = None
#
#     #constructor
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#     #metode
#     def descriere(self):
#         print(f"Angajatul {self.nume} are vechimea in firma de 10 ani :) .")
#
#     def nume_complet(self):
#         print(f"Numele complet este: {self.nume} {self.prenume} .")
#
#     def salariu_lunar(self):
#         print(f"Salariu este : {self.salariu}  .")
#
#     def salariu_anual(self):
#         salariu_anual = self.salariu * 12
#         print(f'Salariu anual este : {salariu_anual}')
#
#     def marire_salariu(self, marire_salariu):  # pentru procente impartim la 100
#         salariu_marit = self.salariu + (self.salariu * marire_salariu/100 )
#         print(f"Angajatul {self.nume} {self.prenume}, are noul salariu marit de {salariu_marit}")
#
# #obiecte
# angajat1 = Angajat('Popa', 'Marius', 1000)
# angajat2 = Angajat('Cosma', 'Ion', 2000)
#
# #apelare metode
# angajat1.descriere()
# angajat1.nume_complet()
# angajat1.salariu_lunar()
# angajat1.salariu_anual()
# angajat1.marire_salariu(20)
# print(f"----------------------------------------------------------")
# angajat2.descriere()
# angajat2.nume_complet()
# angajat2.salariu_lunar()
# angajat2.salariu_anual()
# angajat2.marire_salariu(20)

'''
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
'''

# class Cont:
#     iban = None
#     titular_cont = None
#     sold = None
#     #constructor
#     def __init__(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#     #metode
#     def afisare_sold(self):
#         print(f"Titularul {self.titular_cont} are in cont {self.iban} suma de {self.sold} lei .")
#
#     def debitare_cont(self, suma):
#         if suma <= self.sold:
#             self.sold = self.sold - suma
#             print(f"A fost debitata suma: {suma}, mai aveti {self.sold} lei")
#         else:
#             print(f'Fonduri insuficiente, suma e prea mare')
#
#     def creditare_cont(self, suma2):
#         self.sold +=suma2
#         print(f'S-a incasat suma de {suma2}, noua valoare a contrului este de {self.sold}')
#
# #obiecte
# cont1 = Cont('RO000 AAAA 1234', 'Popa', 1000)
#
# #apelare metode
# cont1.afisare_sold()
# cont1.debitare_cont(1200)
# cont1.creditare_cont(250)
#
# print(f"-------------------------------------------------------------")
#
# #obiecte
# cont2 = Cont('RO000 BBBB 1256 000', 'Cosma', 2000)
#
# #apelare metode
# cont2.afisare_sold()
# cont2.debitare_cont(700)
# cont2.creditare_cont(130)