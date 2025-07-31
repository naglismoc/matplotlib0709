import csv
import copy

import matplotlib.pyplot as plt

from helper import print_table

data = []

with open("imunizacija.csv",mode='r',encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(dict(row))

# print(data)
print_table(data,5)
cleared_data = copy.deepcopy(data)

for row in cleared_data:
    row.pop("\ufeffESRI_OID")
    row.pop("workplace_code")
    row.pop("workplace_name")
    row.pop("percentile_1")
    row.pop("percentile_2")
    row.pop("as_of_date")
    row.pop("activity_evrk2")

print_table(cleared_data,5)

formatted_data = copy.deepcopy(cleared_data)

for row in formatted_data:
    row['employees'] = int(row['employees'])
    pts = row['immunised_percent'].replace("%","").split("-")
    row['immunised_percent'] = (int(pts[0]) + int(pts[1])) / 2
print_table(formatted_data,5)

municipalities = {}
counties = {}

for row in formatted_data:
    key_m = row['municipality']
    key_c = row['county']
    value = row['employees']

    if key_m in municipalities:
        municipalities[key_m] += value
    else:
        municipalities[key_m] = value

    if key_c in counties:
        counties[key_c] += value
    else:
        counties[key_c] = value

print(municipalities)
print(counties)

# langas, grafikas = plt.subplots()
# grafikas.bar(counties.keys(),counties.values())
# plt.xticks(rotation=60)
# plt.tight_layout()
# plt.show()

# langas, grafikas = plt.subplots()
# grafikas.bar(municipalities.keys(),municipalities.values())
# plt.xticks(rotation=60)
# plt.tight_layout()
# plt.show()

keys = list(municipalities.keys())
values = list(municipalities.values())
for i in range(len(values)):
    for j in range(i + 1, len(values)):
        if values[i] < values[j]:
            values[i], values[j] = values[j], values[i]
            keys[i], keys[j] = keys[j], keys[i]

langas, grafikas = plt.subplots()
plt.bar(keys,values)
plt.xticks(rotation=60)
plt.tight_layout()
plt.show()

#Užduotis
# grafiškai atvaizduokite procentinį pasiskiepijima regionuose ir savivaldybese
# grafiškai atvaizduokite ką nors protingo ir logiško


