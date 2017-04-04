# -*- coding: utf-8 -*-
# python 2
# program napisal Miro - 4.4.2017 - naloga 8.2
# FIZZBUZZ

print ""
print "IGRA FIZZBUZZ"
print ""
izbor = raw_input("Vnesi vrednost med 1 in 100 : ") # vnesemo vrednost med 1 in 100
if int(izbor) < 1 or int(izbor) > 100:
    print "Števila ni med 1 in 100 !!!"
    pass
elif int(izbor) > 0 or int(izbor) < 101:
    krog = 1
    while krog < (int(izbor)+1):
        if krog%3==0 and krog%5==0:
            print "FIZZBUZZ"
            krog+=1
        elif krog%3==0:
            print "FIZZ"
            krog+=1
        elif krog%5==0:
            print "BUZZ"
            krog+=1
        elif krog%3!=0 and krog%5!=0:
            print str(krog)
            krog += 1