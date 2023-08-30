# Atm program

def paraçekme():
    
    global _bakiye
    çekilicekpara = int(input("Çekmek istediğiniz tutarı giriniz. "))

    if _bakiye < çekilicekpara:
        
        print("Hesabınızda bu kadar para bulunmuyor. Şaunki güncel baiyeniz",_bakiye,"TL'dir.")

    else:
        
        _bakiye = _bakiye - çekilicekpara
        print("Paranız verildi.(",çekilicekpara, "TL)\nGüncel bakiyeniz",_bakiye,"TL'dir.")
        

def parayatırma():

    global _bakiye
    yatırılacakpara = int(input("Yatırmak istediğiniz tutarı giriniz. "))

    _bakiye = _bakiye + yatırılacakpara
    print("Paranız yatırıldı.(",yatırılacakpara,"TL)\nGüncel bakiyeniz",_bakiye,"TL'dir.")
    


_kartsifresi = 1234
_bakiye = 500
sifre_sayac = 3
login = False
deneme = 1

print("Hoşgeldiniz")

for deneme in range(deneme,sifre_sayac+1):
    
    denemesayısı = (sifre_sayac - deneme)  
    sifre = int(input("Lütfen şifrenizi giriniz.\nŞifre:  "))

    if sifre == _kartsifresi:
        print("\n1. Para çekme")
        print("2. Para yatırma")
        print("3. Bakiye sogulama")
        print("4. Kart iade")

        seçim = int(input("Yapmak istediğiniz işlem nedir? \n"))

        if seçim == 1:
            
            paraçekme()
            break

        elif seçim == 2:

            parayatırma()
            break    
        
        elif seçim == 3:

            print("Şuan bankamizdaki güncel bakiyeniz:",_bakiye,"TL'dir." )

        elif seçim == 4:

            print("Kartınız iade edilior. İyi günler dileriz.")
            break
        
        else:
            print(seçim,"Numaralı bir işlem bulunmamaktadır. Lütfen geçerli olan bir işlem yapmak için şifrenizi tekrar girin.")
            break


    elif(denemesayısı == 0):
        print("\n3 kez hatalı deneme yaptınız. Hesabınız bloke oldu.\n")
        break
    else:
        print("\nŞifre yanlış!")
        print(denemesayısı,"deneme hakkınız kaldı.\n")

    deneme += 1

