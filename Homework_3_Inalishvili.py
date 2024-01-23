# 1. ჯეირანის პროგრამა
# დაასრულე ჯეირანის თამაშის პროგრამა ციკლის გამოყენებით. თამაშის დასასრულებლად
# რომელიმე მოთამაშემ უნდა დააგროვოს 3 ქულა.


import random

options = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:

    computer_guess = random.choice(options)
    player_guess = input("Choose rock, paper, or scissors : ").lower().strip()
    if player_guess not in options:
        print("Enter option correctly! Type only rock, paper or scissors.")
        continue
    draw_combination = player_guess == computer_guess
    winning_combination_1 = player_guess == "rock" and computer_guess == "scissors"
    winning_combination_2 = player_guess == "paper" and computer_guess == "rock"
    winning_combination_3 = player_guess == "scissors" and computer_guess == "paper"
    if winning_combination_1 or winning_combination_2 or winning_combination_3:
        print("Player won this round!")
        player_score += 1
    elif draw_combination:
        print("Draw!")
    else:
        print("Computer won this round!")
        computer_score += 1
if player_score == 3:
    print(f'''Game Over
Player won
Score: {player_score} : {computer_score}''')
else:
    print(f'''Game Over
Computer won
Score: {computer_score} : {player_score}''')




# 2. გამრავლების ტაბულა
# ორმაგი for ციკლის_ის დახმარებით დაბეჭდე გამრავლების ტაბულა 1_დან მომხმარებლის
# მიერ შეყვანილი მთელი რიცხვის ჩათვლით.


max_number = int(input("Please enter a number: "))
if max_number <= 0:
    print("Enter greater than 0")
else:
    for i in range(1, max_number+1):
        for j in range(1, max_number+1):
            print(i*j, end="\t")
        print("\n")




# 3. საბანკო ანგარიში
# შეადგინე პროგრამა რომელიც განასახიერებს საბანკო ანგარიშს. მასზე განთავსებულია
# თანხა 3000 ლარის ოდენობით. პროგრამა გეკითხება გაწეულ ხარჯს და აკლებს ანგარიშს
# მანამ, სანამ არ შეიყვან 0_ს. შემდეგ გიბეჭდავს ანგარიშზე დარჩენილ თანხას და წყვეტს
# ფუნქციონირებას. თუ ანგარიშზე არსებული თანხა ნაკლებია დანახარჯის თანხაზე,
# პროგრამამ უნდა დაბეჭდოს, რომ ანგარიშზე არ არის საკმარისი თანხა და გააგრძელოს ფუნქციონირება.


total_amount = 3000

while True:
    expense_amount = int(input("Please enter expense amount: "))
    if expense_amount == 0:
        print(f"$usd {total_amount} is left on your bank account.")
        break
    elif expense_amount > total_amount:
        print("Sorry, there is not enough money on your account.")
        continue
    else:
        total_amount -= expense_amount




# 4. თუთიყუშის პროგრამა
# დაწერე პროგრამა _ თუთიყუში. პროგრამამ უნდა გაიმეოროს რასაც ეტყვი მანამ სანამ არ
# შეიყვან სიტყვას quit, თუმცა წინ დაურთოს კითხვა „User Said Whaaat!?”
# თუ შევიყვანეთ სიტყვა Hello დაიბეჭდება
# „User Said Whaaat!?”
# “User Said Hello”


while True:
    text_to_repeat = input("I'm all ears! tell me some sh... : ").lower().strip()
    if text_to_repeat == "quit":
        break
    else:
        print(f"""\"User Said Whaaat!?"
"User Said {text_to_repeat}\"""")
