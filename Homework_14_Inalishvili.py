# დაწერე კოდი რომელიც article.txt _დოკუმენტში იპოვის რიგით მეორე ყველაზე ხშირად განმეორებად სიტყვას.

def second_most_finder():
    with open("article.txt", "r") as file:
        text_file = file.readlines()
    words = "".join(text_file).lower().split()
    alphas = [word for word in words if word.isalpha()]
    words_set = set(alphas)
    elements_dict = {}
    for element in words_set:
        elements_dict[element] = alphas.count(element)
    sorted_dict = dict(sorted(elements_dict.items(), key=lambda item: item[1]))
    second_word = list(sorted_dict.keys())[1]
    print(f"""Second most occurred word in the article is {second_word}.
            it occurred {sorted_dict[second_word]} times.""")
    return second_word


second_most_finder()




# names.csv ფაილში არსებული ინფორმაცია გადმოაკოპირე names.txt ფაილში.


import csv

csv_data = []
with open("names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for element in csv_reader:
        csv_data += element

csv_data_str = str(csv_data)

with open("names.txt", "w") as text_file:
    text_file.write(csv_data_str)

