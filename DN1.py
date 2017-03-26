# -*- coding: utf-8 -*-
# python 2
#  program napisal Miro - 26.3.2017 - nalogi 7.2 in 7.3 dopolnil 26.3.2017 popoldan
# program naključno izbere število med 1 in 100, poskušamo ugotoviti število s pomočjo komentarja
# ob tem šteje tudi število poskusov

# import os, sys  # določimo encoding = utf-8
import random   # omogočimo, da računalnik izbere naključno število v danem obsegu

comp_value = random.randint(1, 100)                                 #računalnik izbere število med 1 in 100
print "IGRA - UGANI SKRITO ŠTEVILO !!!!"
print "Poskusi ugotoviti število med 1 in 100, ki si jo naključno izbral računalnik."
stevec_poskusov = 1                                                 #števec poskusov damo na 1
while True:
    moja_vrednost = raw_input("Vpiši številko med 1 in 100 : ")     #vnesemo število
    if int(moja_vrednost) == comp_value:                            #preverimo pravilnost in izpišemo če je pogoj izpolnjen
        print "Čestitam, pravilno si ugotovil/a, da gre za število " + str(comp_value) + "."
        print "Uspelo ti je v " + str(stevec_poskusov) + ". poskusu."
        print "**********************************"
        odgovor = raw_input("Si želiš še eno igro ? (1=Da/2=Ne)")   #vprašamo, po novi igri
        if odgovor == "1":                                          # odgovor DA - pripravimo vse za začetek nove igre
            comp_value = random.randint(1, 100)
            stevec_poskusov = 1
            print "NOVA IGRA - UGANI SKRITO ŠTEVILO !!!!"
            print "Poskusi ugotoviti številko med 1 in 100, ki si jo naključno izbral računalnik."
        elif odgovor != "1":                                        # odgovor NE - skočimo ven iz zanke
            print ""
            print "Hvala za sodelovanje in lep dan še naprej :-)"
            break
    elif int(moja_vrednost) < comp_value:                           # preverimo če je vnešeno število manjše od računalikove izbire
        stevec_poskusov+=1                                          # povečamo števec poskusov za 1
        print "Pravilno število je večje !!!"                       # igralcu napišemo komentar, da lažje nadaljuje z igro
    elif int(moja_vrednost) > comp_value:                           # preverimo če je vnešeno število večje od računalikove izbire
        stevec_poskusov+=1                                          # povečamo števec poskusov za 1
        print "Pravilno število je manjše !!!"                      # igralcu napišemo komentar, da lažje nadaljuje z igro

print ""
print "DODATEK - izpis šumnikov"
# primer izpisa šumnikov
znak = "čćšđž"
znak1 = "ČĆŠĐŽ"
print znak + " " + znak1
