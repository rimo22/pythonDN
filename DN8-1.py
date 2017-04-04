# -*- coding: utf-8 -*-
# python 2
#  program napisal Miro - 3.4.2017 - naloga 8.1
# program pretvarja med enotami

while True:
    print ""
    print "PRETVORNIK"
    print "Izberi možnost pretvarjanja med naslednjimi možnostmi :"
    print "1 - pretvori med kilometri in miljami"
    print "2 - pretvori med miljami in kilometri"
    print "3 - pretvori med temperaturo v °C (Celsius) in °F (Fahreheit)"  # C=5/9*(F–32)
    print "4 - pretvori med temperaturo v °F (Fahreheit) in °C (Celsius)"  # C=5/9*(F–32)
    print "5 - konec"
    print ""
    izbor = raw_input("Vpiši vrednost za željeno pretvorbo : ")     #vnesemo število - "izbor"
    if izbor == "1":                                                # pretvarja km v milje
        print ""
        print "Pretvarjaš kilometre v milje"
        print ""
        vnos_km = raw_input("Vpiši kilometre, ki jih želiš pretvoriti v milje : ")
        milje = round(int(vnos_km)*0.6214,2)
        print vnos_km + " km = " + str(milje) + " milj"
        preveri = raw_input("Želiš nadaljevati ? (d/n)").lower()
        if preveri == "d":
            pass
        elif preveri !="d":
            break
    elif izbor == "2":                                              # pretvarja milje v km
        print ""
        print "Pretvarjaš milje v kilometre"
        print ""
        vnos_milje = raw_input("Vpiši milje, ki jih želiš pretvoriti v kilometre : ")
        km = round(int(vnos_milje)/0.6214,2)
        print vnos_milje + " milj = " + str(km) + " km"
        preveri = raw_input("Želiš nadaljevati ? (d/n)").lower()
        if preveri == "d":
            pass
        elif preveri != "d":
            break
    elif izbor == "3":                                              # pretvarja C v F
        print ""
        print "Pretvarjaš °C v °F"
        print ""
        vnos_stopinjeC = raw_input("Vpiši temperaturo v stopinjah Celzija(°C) : ")
        stopinjeF = round(((9*int(vnos_stopinjeC)+160)/5), 2)
        print vnos_stopinjeC + " C = " + str(stopinjeF) + " F"
        preveri = raw_input("Želiš nadaljevati ? (d/n)").lower()
        if preveri == "d":
            pass
        elif preveri != "d":
            break
    elif izbor == "4":                                              # pretvarja F v C
        print ""
        print "Pretvarjaš °F v °C"
        print ""
        vnos_stopinjeF = raw_input("Vpiši temperaturo v stopinjah Farenheit(°F) : ")
        stopinjeC = round((5*(int(vnos_stopinjeF)-32)/9), 2)
        print vnos_stopinjeF + " F = " + str(stopinjeC) + " C"
        preveri = raw_input("Želiš nadaljevati ? (d/n)").lower()
        if preveri == "d":
            pass
        elif preveri != "d":
            break
    elif izbor == "5":                                              #zaključek dela
        break
print ""
print "Hvala za sodelovanje in lep dan še naprej !!!"
print ""