# -*- coding: utf-8 -*-
# python 2
#  program napisal Miro - 20.4.2017 - naloga Jedilni list


print "Jedilni list"

jedilni_list = {}

while True:
    jed = raw_input("Vnesi jed za dnevni meni : ")
    jed_cena = raw_input("Vnesi ceno : ")
    status = raw_input("Želiš vnesti še kakšno jed ? (d/n) ").lower()
    jedilni_list[jed] = '%.2f' % (float(jed_cena))+" EUR"

    if status == "n":
        break

print "Vse jedi s cenami: %s" % jedilni_list
print "Podatki so zapisani v datoteki - meni.txt"
with open("meni.txt", 'w+') as text_file:
    text_file.write(str(jedilni_list))
