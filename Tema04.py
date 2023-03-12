'''
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# for i in range (len(masini)):
#     print(f'Masina mea preferata este: {masini[i]}')
# for masini2 in masini:
#     print(f'Masina mea preferata este: {masini2}')
# i = 0
# while i < len(masini):
#     print(f'Masina mea preferata este: {masini[i]}')
#     i +=1

'''
2. Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrie cu majuscule,exceptând primul și ultimul.
În else:
- Printează lista.
'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# for i in range(1, len(masini) -1):
#         masini[i] = masini[i].upper()
# else:
#     print(f"Elemenete cu majuscule: {masini}")

'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# for masinax in masini:
#     if masinax == "Mercedes":
#         print(f"Masina dorita de dumneavoastra este: {masinax}")
#         break
# else:
#     print(f'Am gasit masina {masinax}. Mai cautam')

'''
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
- Printează S-ar putea să vă placă mașina x.
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# for masina4 in masini:
#     if masina4 == "Trabant" or masina4 == "Lăstun":
#         continue
#     print(f"S-ar putea sa va placa masina: {masina4}")
#
'''
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
    - Salvează aceste mașini în masini_vechi.
    - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x.
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# for i in range(len(masini)):
#     if masini[i] == "Trabant" or masini[i] == "Lăstun":
#         masini_vechi.append(masini[i])
#         masini[i] = 'Tesla'
# print(f"Modele vehci: {masini_vechi}")
# print(f"Modele noi:  {masini}")

'''
6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașina X 
iterated prin lista cheilor dictionarului
● Iterează prin listă.
'''
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# buget = 15000
# print(pret_masini.items())
# for masina, pret in pret_masini.items():
#     if pret <= buget:
#         print(f" Pentru un buget de sub 15000 euro puteți alege mașina {masina}")
'''
7. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# numara3 = 0
# for numar in numere:
#     if numar == 3:
#         numara3 +=1
#         print(f"Cifra 3 apare de : {numara3} ori")
'''
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''
# suma = 0
# for suma1 in numere:
#     suma += suma1
#     print(f"Suma listei este: {suma}")
''' 
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
 '''
# numere = [5, 7, 3, 45, 3, 3, 1, 0, -4, 3]
# nr_maxim = 0
# for i in range (len(numere)):
#     if numere[i] > nr_maxim:
#         nr_maxim = numere[i]
# print(f"Numarul maxim este: {nr_maxim}")

'''
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(len(numere)):
    if numere[i] >= 0:
        numere[i] = - numere[i]
        print(f"Lista noua: {numere[i]}")
