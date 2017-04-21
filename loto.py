# -*- coding: utf-8 -*-
# python 2
#  program napisal Miro - 21.4.2017 - naloga 10.3 LOTO
# program naključno izbere LOTO števila (6 + 1) število med 1 in 39



import random   # omogočimo, da računalnik izbere naključno število v danem obsegu

def preveri_loto_stevilo():
    print ""
    print "IGRA - LOTO"
    print "Računalnik - žrebanje LOTO številk (7+1)."
    print ""
    lista_loto_stevil = []
    lista_loto_stevil_dodatna = []
    stevec_poskusov = 0                                                 #števec poskusov damo na 1
    while True:
        loto_stevilo = random.randint(1, 39)            # računalnik izbere število med 1 in 39
        if loto_stevilo in lista_loto_stevil:
            print "Številka " + str(loto_stevilo) + " je bila že izžrebana"
            pass
        elif loto_stevilo != lista_loto_stevil:
            print "Tvoje "+str(stevec_poskusov+1)+". število je : " + str(loto_stevilo)
            lista_loto_stevil.append(loto_stevilo)
            stevec_poskusov += 1


            if stevec_poskusov == 7:
                loto_stevilo_dodatno = random.randint(1, 39)  # računalnik izbere dodatno število med 1 in 39

                if loto_stevilo_dodatno in lista_loto_stevil:
                    print "Dodatna številka " + str(loto_stevilo_dodatno) + " je bila že izžrebana"
                    loto_stevilo_dodatno = random.randint(1, 39)
                    pass
                elif loto_stevilo_dodatno != lista_loto_stevil:
                    lista_loto_stevil_dodatna.append(loto_stevilo_dodatno)
                    print "V današnjem krogu smo izžrebali naslednjih 7 števil: " + str(sorted(lista_loto_stevil))
                    print "in dodatno številko: " + str(lista_loto_stevil_dodatna)
                    break

if __name__ == "__main__":
    preveri_loto_stevilo()