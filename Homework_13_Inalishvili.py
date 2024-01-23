# დაწერე ფუნქცია, რომელიც მომხმარებელს ჩააწერინებს ტექსტურ ფაილში ინფორმაციას Input ფუნქციის დახმარებით
# მანამ, სანამ მომხმარებელი არ შეიყვანს სიტყვას _ “enough”.


def text_editor():
    with open("new_file", "a") as file:
        while True:
            user_input = input("Enter text to add. (to exit, enter 'enough'): ")
            if user_input.strip().lower() == "enough" :
                break
            else:
                file.write(f"{user_input} \n")




# დაწერე ფუნქცია, რომელიც input ფუნქციის დახმარებით მომხმარებლისგან მიიღებს საქაღალდის ლოკაციას
# და შესაქმნელი ფაილის სახელს, შემდეგ მიღებულ ლოკაციაზე შექმნის შესაბამის ფაილს
# და ამოპრინტავს საქაღალდეში არსებულ ყველა ფაილის სიას.

import os


def dir_lister():
    folder_location = input("Please enter folder location: ")
    file_name = input("Please enter file name: ")
    if not os.path.exists(folder_location):
        print("Please Enter valid folder path.")
    else:
        with open(f"{folder_location}/{file_name}.txt", "x"):
            files = os.listdir(folder_location)
        for element in files:
            print(element)

