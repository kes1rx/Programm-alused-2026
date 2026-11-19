
print("Vali programm:") #lisasin valikud 1-3 
print("1 - Arvu kontroll") #see valik teeb arvu kontroll
print("2 - Kehamassiindeks")#see valik leiab kehamassiindeks
print("3 - Ostu allahindlus")#see valik leiab allahindlus

valik = input("Sisesta valik (1-3) => ") #inimene teeb valik 1 2 või kolmas variant

if valik == "1": #kui inimene valib 1 variant teeb arvukontroll
    print("Arvu kontroll")
    arv = int(input("Sisesta täisarv => "))  #inimene kirjutab täisarv

    if arv > 0: #kui arv on rohkem kui 0 see arv on positiivne arv
        print("Arv on positiivne")
    elif arv == 0: 
        print("Arv on null")
    else:
        print("Arv on negatiivne")

    if arv % 2 == 0:
        print("Arv on paarisarv")
    else:
        print("Arv on paaritu")

    if arv % 3 == 0: #see tähendab et selline arv jagub 3-ga
        print("Arv jagub 3-ga")
    else:
        print("Arv ei jagu 3-ga")
         #see tähendab et selline arv ei saa jaga 3-ga
elif valik == "2": #kui valik on teine alustas leida kehamassiindeks
    print("Kehamassiindeks")
    mass = float(input("Sisesta kaal (kg) => ")) #inimene sisestab kaal (kg)
    pikkus = float(input("Sisesta pikkus (m) => ")) #ja inimenee kirjutab inimese pikkus

    if mass > 0 and pikkus > 0:
        kmi = mass / (pikkus * pikkus) #kirjutan et bmi sain leida kui mass jagab (pikkus korrutab pikkus)
        print("KMI:", round(kmi, 1))

        if kmi < 16:
            print("Alakaal")#kui keha mass indeks on < 16 see on alakaal
        elif kmi < 21:
            print("Normaalkaal") #kui kmi on < 21 see on normaalkaal
        elif kmi < 26:
            print("Ülekaal")#kui inimene < 26 see oli ülekaal
        else:
            print("Rasvumine")
    else:
        print("Vigane kaal või pikkus")#kui inimene kirjutab vale arvu
        #teen kolmas valik allagindlus
elif valik == "3": #kui on valik 3 sest ta teen print Ostu allahindlus
    print("Ostu allahindlus") #teen kolmas valik
    summa = float(input("Sisesta ostusumma => "))#inimene kirjutab arvu

    if summa <= 0: #kui on summa <= 0 see on vigane summa
        print("Vigane summa")
    elif summa > 500: 
        print("Allahindlus 10%, maksta:", round(summa * 0.9, 2)) #teen korrata
    elif summa > 100:
        print("Allahindlus 5%, maksta:", round(summa * 0.95, 2))
    else:
        print("Allahindlust pole, maksta:", summa)

else:
    print("Vigane valik")
