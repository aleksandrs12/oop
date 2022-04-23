from datetime import date
from datetime import datetime

print('Instrukcija: \n  1. Uz jautajumu "Vai aizvert programmu? (y/n)" jaatbild ar y(ja) vai n(ne), ja bus cita vertiba ta skaitisies ka ne.\n  2. Izmerus jaievada ar cipariem.\n  3. Rekins saglabajas faila "valdis.txt"')

class Rekins:
    darba_samaksa = 15
    PVN = 21
    def __init__(self, vards: str, veltijums: str, izmeri: list, mat_cena: int):
        self.vards = vards
        self.veltijums = veltijums
        self.izmeri = izmeri
        self.mat_cena = mat_cena

    def izrekinat_cenu(self):
        self.veltijums = self.veltijums.strip()
        cena = len(self.veltijums) * 1.2 + (self.izmeri[0] / 100 * self.izmeri[1] / 100 * self.izmeri[2] / 100) / 3 * self.mat_cena
        p = (cena + self.darba_samaksa) * self.PVN / 100
        rekina_summa = (cena + self.darba_samaksa) + p
        rekina_summa = round(rekina_summa * 100) / 100
        return rekina_summa

    def izvadit(self):
        print('\nklienta vards: ' + self.vards + '\nveltijums: ' + self.veltijums + '\nplatums, garums, augstums (mm): ' + str(self.izmeri) + '\nmateriala cena EUR : ' + str(self.mat_cena) + '\ndatums: ' + str(date.today()) + '\nlaiks: ' + datetime.now().strftime("%H:%M:%S") + '\nrekina summa: ' + str(self.izrekinat_cenu()))

    def ierakstit(self):
        f = open('valdis.txt', 'w')
        f.write('klienta vards: ' + self.vards + '\nveltijums: ' + self.veltijums + '\nplatums, garums, augstums (mm): ' + str(self.izmeri) + '\nmateriala cena EUR : ' + str(self.mat_cena) + '\ndatums: ' + str(date.today()) + '\nlaiks: ' + datetime.now().strftime("%H:%M:%S") + '\nrekina summa: ' + str(self.izrekinat_cenu()))

while input('Vai aizvert programmu? (y/n): ') != 'y':
    try:
        a = Rekins(input('Ierakstiet klienta vardu: '), input('Ierakstiet veltijumu: '), [int(input('Ierakstiet platumu (mm): ')), int(input('Ierakstiet garumu (mm): ')), int(input('Ierakstiet augstumu (mm): '))], int(input('Ierakstiet materiala cenu EUR : ')))
        a.izvadit()
        a.ierakstit()
        print('Rekins tika ierakstits')
    except:
        print('Nepareizi ievaditi dati')
    
