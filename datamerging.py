import csv
import pandas as pd

data1 = []
data2 = []

with open("bright_stars.csv","r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data1.append(i)

with open("dwarf_stars.csv","r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data2.append(i)

header1 = data1[0]
header2 = data2[0]

final_data1 = data1[1:]
final_data2 = data2[1:]

headers = header1 + header2

final_data = []

for index, data_row in enumerate(final_data1):
    final_data.append(final_data1[index]+final_data2[index])

with open("final.csv","a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(final_data)