# -*- coding: utf-8 -*-
# python 2
#  program napisal Miro - 20.4.2017 - naloga 10.2
# program naključno izbere število med 1 in 100, poskušamo ugotoviti število s pomočjo komentarja
# ob tem šteje tudi število poskusov - uporaba funkcij

import random   # omogočimo, da računalnik izbere naključno število v danem obsegu

def preveri_stevilo():
    comp_value = random.randint(1, 100)  # računalnik izbere število med 1 in 100
    stevec_poskusov = 1  # števec poskusov damo na 1
    print "IGRA - UGANI SKRITO ŠTEVILO !!!!"
    print "Poskusi ugotoviti število med 1 in 100, ki si jo naključno izbral računalnik."

    while True:
        moja_vrednost = int(raw_input("Vpiši številko med 1 in 100 : "))

        if comp_value == moja_vrednost:
            print "Čestitam, pravilno si ugotovil/a, da gre za število " + str(comp_value) + "."
            print "Uspelo ti je v " + str(stevec_poskusov) + ". poskusu."
            break

        elif moja_vrednost < comp_value:
            stevec_poskusov += 1
            print "Pravilno število je večje !!!"
        elif moja_vrednost > comp_value:
            stevec_poskusov += 1
            print "Pravilno število je manjše !!!"


if __name__ == "__main__":
    preveri_stevilo()