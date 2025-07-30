# pip install matplotlib
import matplotlib.pyplot as plt

# langas, grafikas = plt.subplots()
# plt.show()

# langas, grafikas = plt.subplots(2,2)
# pirmas_ktv = grafikas[0][0]
# antras_ktv = grafikas[0][1]
# trecias_ktv = grafikas[1][0]
# ketvirtas_ktv = grafikas[1][1]
# plt.show()

vid_temp = [4,-2, 5, 8, 12, 20, 23, 27, 20, 18, 10, 6]
vid_temp_kitais_metais = [3, -1, 6, 9, 13, 19, 24, 26, 19, 17, 9, 5]
menesiai = [
    "Sausis", "Vasaris", "Kovas", "Balandis", "Gegužė", "Birželis",
    "Liepa", "Rugpjūtis", "Rugsėjis", "Spalis", "Lapkritis", "Gruodis"
]

# langas, grafikas = plt.subplots()
# grafikas.plot(menesiai, vid_temp, color='green')
# grafikas.plot(menesiai, vid_temp_kitais_metais, color='blue')
#
# grafikas.set_title("metines oro temp palyginimas")
# grafikas.set_ylabel("temp")
# grafikas.set_xlabel("menesiai")
# grafikas.tick_params(axis='x', labelsize=8)
# grafikas.tick_params(axis='y', labelsize=12)
# plt.xticks(rotation=70)
# plt.show()

# langas, grafikas = plt.subplots()
# grafikas.scatter(menesiai,vid_temp)
# grafikas.scatter(menesiai,vid_temp_kitais_metais)
# grafikas.plot(menesiai,vid_temp)
# grafikas.plot(menesiai,vid_temp_kitais_metais)
# grafikas.bar(menesiai,vid_temp)
# grafikas.bar(menesiai,vid_temp_kitais_metais)
# plt.show()
# x = [1,2,5,3,8,10,7]
# # y = [0, 0.1, 0.2, 0, 0, 0.2, 0]
# y = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
# labels = [
#     "Pirmadienis", "Antradienis", "Trečiadienis",
#     "Ketvirtadienis", "Penktadienis", "Šeštadienis", "Sekmadienis"
# ]
# colors = ['#FF69B4', '#FFD700', '#8A2BE2', '#00CED1', '#FF4500']
# langas, grafikas = plt.subplots()
# grafikas.pie(x, explode=y,  labels=labels, colors=colors, autopct='%1.2f%%')
# plt.show()

saules_indeksas = [1,2,5,3,8,10,7,10,10,10,14,12]
langas, grafikas = plt.subplots()
twix = grafikas.twinx()
grafikas.plot(menesiai,vid_temp,color="red")
grafikas.set_ylabel("temperatura")
twix.plot(menesiai,saules_indeksas, color="blue")
twix.set_ylabel("saules indeksas")

plt.show()

