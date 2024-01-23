# 1. მომხმარებელს შემოაყვანინე ინფორმაცია და დათვალე რამდენი რიცხვი,
# ანბანის ასო და სხვა სიმბოლოა მოცემული წინადადებაში. შედეგი დაბეჭდე.
# გამოიყენე for ციკლი, isalpha და isdigit ფუნქციები.


user_text = input("Please enter some text: ")

num_of_alphas = 0
num_of_digits = 0
num_of_rest = 0

for char in user_text:
    if char.isalpha():
        num_of_alphas +=1
    elif char.isdigit():
        num_of_digits +=1
    else:
        num_of_rest +=1
print(f"There are {num_of_alphas} letters, {num_of_digits} digits, and {num_of_rest} other symbols in this text.")




# 2. მომხმარებელს შეაყვანინე ორი წინადადება და მათგან შეადგინე მესამე
# შემდეგ წესებზე დაყრდნობით. შექმნილი წინადადება უნდა იწყებოდეს
# პირველი წინადადების პირველი სიმბოლოთი, რომელსაც ჯერ მოჰყვება
# მეორე წინადადების ბოლო სიმბოლო, შემდეგ კი პირველი წინადადების
# მეორე სიმბოლო და მეორე წინადადების ბოლოდან მეორე სიმბოლო.


sentence_1 = input("Please type in the first sentence: ")
sentence_2 = input("Please type in the second sentence: ")

char_list_3 = []
counter = 2
sentence_1_counter = 0
sentence_2_counter = len(sentence_2)-1

while True:
    if counter % 2 == 0:
        char_list_3 += sentence_1[sentence_1_counter]
        sentence_1_counter += 1
    else:
        char_list_3 += sentence_2[sentence_2_counter]
        sentence_2_counter -= 1
    counter +=1
    if (sentence_1_counter > len(sentence_1)) or (sentence_2_counter < 0):
        break
final_string = "".join(char_list_3)
print(final_string)




# 3. მომხმარებელს შეაყვანინე ორი წინადადება და შეამოწმე, პირველ
# წინადადებაში არსებული ყველა სიმბოლო თუ შედის მეორე წინადადებაში
# და პირიქით, მეორე წინადადებაში შემავალი ყველა სიმბოლო თუ შედის
# პირველ წინადადებაში.
# თუ ეს ორი პირობა დაკმაყოფილდა, დაბეჭდე:
# „Strings are balanced!“
# თუ რომელიმე პირობა დაირღვა, დაბეჭდე:
# „Strings are not balanced!“


input_1 = input("Please enter the first string: ")
input_2 = input("Please enter the second string: ")

balanced = True

for i in input_1:
    if input_2.find(i) <0:
        balanced = False
if balanced:
    for j in input_2:
        if input_1.find(j) < 0:
            balanced = False
if balanced:
    print("\"Strings are balanced!\"")
else:
    print("\"Strings are not balanced!\"")