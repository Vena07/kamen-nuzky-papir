import random
import time

vybrano = False
print("Kamen nuzky papir")
print("")

def VyberPredmetu():
    print(" ")
    print("1.📜")
    print("2.🪨")
    print("3.✂️")
    
    vybrano = False
    
    while vybrano == False:
        print(" ")
        predmet = int(input(" Vyberte si předmět ( 1/2/3 ): "))
        print(" ")
        if 0 < predmet <4:
            vybrano = True
            return vybrano
        else:
            print("Zdananý špatný výběr")

def Vyhodonoceni():
    if hrac1 == 1:
        if hrac2 == 1:
            print("Remíza! Byl zvolen Papír")
        elif hrac2 == 2:
            print("Hráč 1 vyhrál! Papír balí kámen")
        elif hrac2 == 3 :
            print("Hráč 2 vítězí! Nůžky roztříhají papír")
    
    if hrac1 == 2:
        if hrac2 == 1:
            print("Hráč 2 vyhrál! Papír balí kámen")
        elif hrac2 == 2:
            print("Remíza! Byl zvolen Kámen")
        elif hrac2 == 3 :
            print("Hráč 1 vyhrál! Kámen zničí nůžky")
    
    if hrac1 == 3:
        if hrac2 == 1:
            print("Hráč 1 vítězí! Nůžky roztříhají papír")
        elif hrac2 == 2:
            print("Hráč 2 vyhrál! Kámen zničí nůžky")
        elif hrac2 == 3 :
            print("Remíza! Byl zvoleny Nůžky")

while True:    
    while vybrano == False:
        vyber = int(input("Vyberet si zdali chte hrát porti hráči(1) nebo prosti počítači(2): "))
        if 0 < vyber <3:
            vybrano = True
        else:
            print("Zdananý špatný výběr")    

    vybrano = False

    if vyber == 1 :
        print("Hráči 1 vyberte si předmět:")
        hrac1 = VyberPredmetu()
        
        for i in range(100):
            print(" ")
        
        print("Hráči 2 vyberte si předmět:")
        hrac2 = VyberPredmetu()
        
        Vyhodonoceni()

    if vyber == 2 :

        print("Hráči 1 vyberte si předmět:")
        hrac1 = VyberPredmetu()        

        print("Hráč 2 si vybírá předmět")
        print(" ")
        time.sleep(3)
        
        hrac2 = random.randint(1,3)

        Vyhodonoceni() 
    
    while vybrano == False:
        print(" ")
        vyber = int(input("Chete pokračovat? (1. Ano / 2.Ne): "))
        if 0 < vyber <3:
            break

