from colorama import Fore,init

class Parkovka:
    def __init__(self,filial_nomi,narxi,sigimi):
        self.filial_nomi = filial_nomi
        self.narxi = narxi
        self.sigimi = sigimi
        self.tushum = 0
        self.mashinalar = []
        

    def kirish(self,mashina:dict,vaqt: float | int):
        self.tushum += vaqt * self.narxi
        self.mashinalar.append(mashina)

        print(Fore.YELLOW + f"{mashina['mashina_nomi'].capitalize()}, parkovkaga qo'yildi.\nVaqti: {vaqt} soat\nNarxi: {int(vaqt * self.narxi)} so'm" + Fore.RESET)


    def chiqish(self,mashina_raqami: str):
        for mashina in self.mashinalar:
            if mashina["mashina_raqami"] == mashina_raqami:
                self.mashinalar.remove(mashina)
                print(Fore.YELLOW + f"{mashina['mashina_nomi']}, chiqib ketdi!" + Fore.RESET)
                break
    
    def mashinalarni_korish(self):
        if len(self.mashinalar) == 0:
            print(Fore.YELLOW + f"{self.filial_nomi} filialiga hali bironta ham mashina kirmadi." + Fore.RESET)
        elif len(self.mashinalar) == 1:
            print(Fore.YELLOW + f"Hozirda {self.filial_nomi}da faqatgina {self.mashinalar[0]['mashina_nomi']} parkovka qilingan!" + Fore.RESET)
        else:
            mashina_nomlari = []
            for mashina in self.mashinalar:
                mashina_nomlari.append(mashina['mashina_nomi'])

            text = Fore.YELLOW + f'{", ".join(mashina_nomlari[:-1]).capitalize()} va {mashina_nomlari[-1].capitalize()}' + Fore.RESET
            print(Fore.RED + f"Hozirda {self.filial_nomi}da quydagi mashinalar mavjud: {text}" + Fore.RESET)
        
    def tushumlarni_korish(self):
        print(Fore.YELLOW + f"{self.filial_nomi}da {int(self.tushum)} so'm tushum bo'lgan." + Fore.RESET)