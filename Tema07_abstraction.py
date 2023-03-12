'''
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’
'''

from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14
    culoare = "invizibil"

    @abstractmethod
    def aria(self):
        pass

    def descriere(self):
        print(f"Cel mai probabil am colturi")


class Patrat(FormaGeometrica):
    __latura = None

    # def __init__(self, latura_din_ext):
    #     self.__latura = latura_din_ext

    def aria(self):
        return self.__latura * self.__latura

    def set_latura(self, latura_din_text):
        if latura_din_text <= 0:
            print(f"Latura nu poate fi negativa")
        else:
            self.__latura = latura_din_text

    def get_latura(self):
        return self.__latura

    def delete_latura(self):
        del self.__latura


patratel = Patrat()
patratel.set_latura(-5)
patratel.set_latura(5)

arie_patratel = patratel.aria()
print(f" Aria patratului este: {arie_patratel}")

latura_patratel = patratel.get_latura()
print(f"Latura patratului patratel: {latura_patratel}")
patratel.delete_latura()
print(f"Latura patratului patratel: {patratel.get_latura()}")
patratel.descriere()


class Cerc(FormaGeometrica):
    __raza = None
    culoare = "verde"

    def __init__(self, raza_cercului):
        self.__raza = raza_cercului

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza_din_ext):
        if raza_din_ext <= 0:
            print(f"Raza e prea mica")
        else:
            self.__raza = raza_din_ext

    def delete_raza(self):
        del self.__raza

    def aria(self):
        return self.PI * self.__raza * self.__raza

    def descriere(self):
        super().descriere()
        print(f"Eu nu am colturi")
        print(f"Initial am fost {super().culoare} iar acum sunt {self.culoare}.")


cerculet = Cerc(4)
cerculet.descriere()
print(f"Aria cercului este {cerculet.aria()}")