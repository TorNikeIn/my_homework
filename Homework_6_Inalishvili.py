# 1. შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს და დაბეჭდავს შემდეგნაირად:
# input: “ablabdabdab”
# Output: „Tripled: ablabdabdabablabdabdabablabdabdab“

def tripled():
    user_input = input("Enter text: ")
    print(user_input*3)


tripled()



# 2. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას მთვარეზე.
# (მთვარის გრავიტაცია 6_ჯერ ნაკლებია დედამიწისაზე)

def moon_gravity():
    weight = int(input("Enter your weight in whole kgs: "))
    return weight/6


moon_gravity()



# 3. შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას მომხმარებლისგან input()   ფუნქციის
# დახმარებით (სამ მონაცემს _ პირველ რიცხვს, მოქმედებას (+ - * / ^), მეორე რიცხვს)
# მაგ. „2 * 6“.  ფუნქცია დაშლის სტრიქონს split() ფუნქციის გამოყენებით. დათვლის და დააბრუნებს შედეგს.
# გაითვალისწინე რომ რიცხვის შეყვანის მაგიერ სიმბოლოების შეყვანის შემთხვევაში უნდა დააბრუნოს ფუნქციამ შესაბამისი მესიჯი.
# ასევე ნულზე გაყოფა არ შეიძ₾ება, ამ შემთხვევაშიც უნდა დააბრუნოს შესაბამისი მესიჯი. (დააბრუნოს და დაპრინტოს)

import math
def simple_calc():

    expression = input("Enter expression with two numbers and one math operator(for example: 3 + 5 ) : ")
    inputs = expression.split()
    first_num = int(inputs[0])
    second_num = int(inputs[2])

    if len(inputs) != 3:
        print("Enter only two numbers and one operator with spaces between.")
        return
    elif not inputs[0].isnumeric() and not inputs[2].isnumeric():
        print("Enter only numbers as first and last parameters.")
        return
    elif inputs[1] not in ["+", "-", "/", "*", "^"]:
        print("use only +, -, *, /, or ^ for operator. ")
        return
    elif inputs[1] == "/" and inputs[2] == 0:
        print("Can't divide by 0.")
        return
    else:
        if inputs[1] == "+":
            answer = first_num + second_num
            print(answer)
            return answer
        if inputs[1] == "-":
            answer = first_num - second_num
            print(answer)
            return answer
        if inputs[1] == "*":
            answer = first_num * second_num
            print(answer)
            return answer
        if inputs[1] == "/":
            answer = first_num / second_num
            print(answer)
            return answer
        if inputs[1] == "^":
            answer = first_num ** second_num
            print(answer)
            return answer


simple_calc()




# არასავალდებულო:
# გავლილი მასალის გამოყენებით შექმენი ფუნქცია, რომელიც მიიღებს ლათინური სიმბოლოებით
# დაწერილ სიტყვას, დაშიფრავს მორზეს ანბანით და დააბრუნებს შედეგს.

def convert_to_morse():
    word_to_convert = input("Type a word to convert into a Morse code: ")
    list_of_letters = list(word_to_convert.strip().upper())

    abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..','--',
             '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',]

    morse_code = ""
    for i in list_of_letters:
        if i in abc:
            index_of_alpha = abc.index(i)
            morse_code += morse[index_of_alpha]
        else:
            print("Enter a valid Latin word. Use only letters from A to Z.")
            return
    print(morse_code)
    return morse_code


convert_to_morse()


