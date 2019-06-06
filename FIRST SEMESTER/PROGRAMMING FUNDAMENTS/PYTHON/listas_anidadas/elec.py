#-*- coding: utf-8 -*-
import csv
import codecs


a = ""
with codecs.open(f'electrodomesticos.csv', "r", encoding='utf-8', errors='ignore') as File:
    reader = csv.reader(File)
    for row in reader:
        a += '"'+row[6]+'", '




print(a)




