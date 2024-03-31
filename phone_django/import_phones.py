import csv

with open('C:\\Users\\zlunn\\PycharmProjects\\phone_django\\phone_dj\\phones.csv', 'r') as csvfile:
    data = {}
    reader = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(reader, 1):
        for w in range(len(row[0])):
            if i == 1:
                data['1'] = row[0].replace(' ', '').split(';')
                continue
            else:
                for n, el in enumerate(data['1']):
                    if n == w and el not in data:
                        data[el] = []
                        data[el].append(row[0].split(';')[w])
                        break
                    elif n == w:
                        data[el].append(row[0].split(';')[w])
                        break

del data['1']
