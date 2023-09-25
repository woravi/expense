import csv


def readcsv():
    with open('data.csv', 'r', newline='', encoding='utf8') as file:
        fr = list(csv.reader(file))
        print(fr)


readcsv()
