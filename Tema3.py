"""
# 1
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
#a
print(f'Lista muzica este : {note_muzicale}')
#b
note_inversate = note_muzicale[::-1]
print((f'Lista inversata este: {note_inversate}'))
#c
note_inversate.reverse()
print (f'Note initile: {note_inversate}')

#2
print(f'Nota DO apare de: {note_muzicale.count("do")}')
 """

'''3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], 
gaseste 2 variante sa le unesti intr-o singura lista.'''
# declarare si initializare liste
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
#
# #lista imbricata - folosind functia append()
# # lista1.append(lista2)
# # print(f'Lista imbricata este: {lista1}')
#
# #lista prin comasare  - folosind functia extend() => arata mai bine, mai uniform :)
# lista1.extend(lista2)
# print(f'Lista comasata este: {lista1}')
#
# #4
# lista1.sort()  #=> sorteaza lista alfabetic / crescator in cazul nostru
# print(f"Lista sortata este: {lista1}")
# lista1.pop(0) # sterge elementul de pe pozitia 0
# print(f"Lista sortata fara 0: {lista1}")
#
# #5
# if lista1 == ():
#     print(f' Lista este goala: {lista1}')
# else :
#     print(f'Lista nu este goala: {lista1}')
#
# #6
# lista1.clear()
# print(lista1)
#
# #7
# if lista1 == []:
#     print(f' Lista este goala: {lista1}')
# else :
#     print(f'Lista nu este goala: {lista1}')
#8
dict1 = {'Ana': 8,
         'Gigel': 10,
         'Dorel': 5}
#print(f'Afisare elevi: {dict1.keys()}') # afiseaza cheile

#9
'''
Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
Ex: ‘Ana a luat nota {x}’.
Doar nota o vei lua folosindu-te de cheie
'''
# print(f" Ana a luat nota {dict1 ['Ana']}")
# print(f" Gigel a luat nota {dict1 ['Gigel']}")
# print(f" Dorel a luat nota {dict1 ['Dorel']}")
#
# #10
# dict1.update({"Dorel":"6"}) # schimba valoarea pentru cheia Dorel
# print(f" Dorel a luat nota {dict1 ['Dorel']}")
#
# #11
# dict1.pop("Gigel") # il sterge pe Gigel
# dict1["Ionica"] = 9  #adauga un element nou (format din: cheie:valoare)
# print(f"Afisare elevi: {dict1}")

#12
'''
- Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
- Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.
'''
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
# zile_sapt.add('luni') #daca exista o dublura, apare doar o singura data
# print(zile_sapt) #setul este afisat intr-o ordine aleatorie

#13
'''
13. Foloseste un if si verifica daca:
- Weekend este un subset al zilelor din sapt (adica daca elementele din 
setul weekend se regasesc intre elementele din setul zile_sapt)
- Weekend nu este un subset al zilelor din sapt
Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. 
Rezultatul fiecarui punct de mai sus va fi un boolean
'''
# if weekend >= zile_sapt:
#     print('weekend este un subset al setului zile_sapt? (T):', weekend.issubset(zile_sapt)) # daca <= sau != => True
# else:
#     print('weekend este un subset al setului zile_sapt? (F):', zile_sapt.issubset(weekend)) #daca >= => False

'''
 14. Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu
sunt in weekend si invers)
'''
print(f'zile_sapt - weekend:', zile_sapt.difference(weekend))  # arata elementele care raman in zile saptamana, fara weekend
print(weekend-zile_sapt) # afiseaza un set gol, pentru ca zile sapt contine toale elementele setului weekend si daca le-am scazut, nu mai are ce afisa
'''
15. Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in
ambele seturi). Hint: Va puteti folosi de o functie
'''
print(f'Intersectia elementelor este:', zile_sapt.intersection(weekend))