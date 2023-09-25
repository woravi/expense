# writecsv.py
import csv

def writecsv(data):
    with open('data.csv', 'a', newline='', encoding='utf8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

writecsv()
