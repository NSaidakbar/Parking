from colorama import Fore,init
from parking import Parkovka


filial1_narxi = 10_000
filial2_narxi = 15_000

filial1 = Parkovka(filial_nomi="Chilonzor",narxi=filial1_narxi,sigimi=20)
filial2 = Parkovka(filial_nomi="Yakkasaroy",narxi=filial2_narxi,sigimi=50)

while True:
    kirit = input(Fore.GREEN + "\n1. Haydovchi sifatida kirish.\n2. Admin sifatida kirish.\n3. Dasturdan chiqish\n\n >>> " + Fore.RESET)
    if kirit == "1":

        while True:
            filial = input(Fore.GREEN + "Qaysi filialdasiz?\n1. Chilonzor\n2. Yakkasaroy\n3. Asosiy menyuga qaytish\n >>> " + Fore.RESET)

            if filial == "1":
                print(Fore.YELLOW + f"{'-' * 20} CH I L O N Z O R | P A R K O V K A {'-' * 20}\n\n" + Fore.RESET)
                haydovchi = input(Fore.GREEN + "1. Mashina qo'yish\n2. Mashina olib chiqish\n>>> " + Fore.RESET)
                
                if haydovchi == "1":
                    mashina_nomi = input(Fore.YELLOW + "Mashina nomini kiriting: " + Fore.RESET)
                    mashina_raqami = input(Fore.YELLOW + "Mashina raqamini kiriting: " + Fore.RESET)
                    vaqti = float(input(Fore.YELLOW + "Qancha vaqt qo'ymoqchisiz: " + Fore.RESET))
                    filial1.kirish(mashina={"mashina_nomi":mashina_nomi,"mashina_raqami":mashina_raqami},vaqt=vaqti)
                    break
                    
                elif haydovchi == "2":
                    raqam = input(Fore.YELLOW + "Mashinangiz raqamini kiriting: " + Fore.RESET)
                    filial1.chiqish(mashina_raqami=raqam)
                    break
            
            elif filial == "2":
                print(Fore.YELLOW + f"{'-' * 20} Y A K K A S A R O Y | P A R K O V K A {'-' * 20}\n\n" + Fore.RESET)
                haydovchi = input(Fore.GREEN + "1. Mashina qo'yish\n2. Mashina olib chiqish\n>>> " + Fore.RESET)
                
                if haydovchi == "1":
                    mashina_nomi = input(Fore.YELLOW + "Mashina nomini kiriting: " + Fore.RESET)
                    mashina_raqami = input(Fore.YELLOW +"Mashina raqamini kiriting: " + Fore.RESET)
                    vaqti = float(input(Fore.YELLOW + "Qancha vaqt qo'ymoqchisiz: " + Fore.RESET))
                    filial2.kirish(mashina={"mashina_nomi":mashina_nomi,"mashina_raqami":mashina_raqami},vaqt=vaqti)
                    break
                    
                elif haydovchi == "2":
                    raqam = input(Fore.YELLOW + "Mashinangiz raqamini kiriting: " + Fore.RESET)
                    filial2.chiqish(mashina_raqami=raqam)
                    break

            elif filial in ['exit','3']:
                break

            else:
                print(Fore.RED + "Notug'ri buyruq kiritdingiz, 1, 2 yoki 3 dan foydalaning." + Fore.RESET)

    elif kirit == "2":
        qiymat = True

        while qiymat:
            parol = input(Fore.GREEN + "Parolni kiriting: " + Fore.RESET)

            if parol == "1111":
                print(Fore.YELLOW + "Xush kelibsiz ADMIN." + Fore.RESET)
                
                while True:
                    filiallar = input(Fore.GREEN + "Qaysi filial malumotlarini ko'rmoqchisiz:\n\n1. Chilonzor\n2. Yakkasaroy\n3. Asosiy menyuga qaytish \n >>> " + Fore.RESET)
                    
                    if filiallar == "1":
                        kirit = input(Fore.GREEN + "1. Mashinalarni ko'rish \n2. Tushumlarni ko'rish \n >>> " + Fore.RESET)
                        
                        if kirit == "1":
                            filial1.mashinalarni_korish()
                            
                        elif kirit == "2":
                            filial1.tushumlarni_korish()
                        
                        else:
                            print(Fore.RED + "Xato buyruq kiritdingiz. 1 yoki 2 dan foydalaning." + Fore.RESET)
                        
                            
                    elif filiallar == "2":
                        kirit = input(Fore.GREEN + "1. Mashinalarni ko'rish \n2. Tushumlarni ko'rish \n >>> " + Fore.RESET)
                        
                        if kirit == "1":
                            filial2.mashinalarni_korish()
                            
                        elif kirit == "2":
                            filial2.tushumlarni_korish()

                        else:
                            print(Fore.RED + "Xato buyruq kiritdingiz. 1 yoki 2 dan foydalaning." + Fore.RESET)
                    
                    elif filiallar == "3":
                        print(Fore.YELLOW + "Asosiy menyuga qaytdingiz." + Fore.RESET)
                        qiymat = False
                        break

                    else:
                        print(Fore.RED + "Notug'ri buyruq kiritdingiz." + Fore.RESET)
            elif parol == 'exit':
                break

            else:
                print(Fore.RED + "Notug'ri parol kiritdingiz. Qayta urinib ko'ring. Chiqish uchun exit yozing." + Fore.RESET)


    elif kirit in ["exit","3"]:
        print(Fore.YELLOW + "Dastur yakunlandi.Tashrifingiz uchun rahmat!" + Fore.RESET)
        break
    
    else:
        print(Fore.RED + "Notug'ri buyuruq kiritdingiz. 1, 2 yoki 3 dan foydalaning." + Fore.RESET)