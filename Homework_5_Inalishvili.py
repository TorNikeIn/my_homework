# 1. ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე ინფორმაცია
# საკუთარი სახელის, გვარის და ასაკის შესახებ. თითოეული
# მომხმარებლის ინფორმაცია შეინახე ინდივიდუალურ სიაში.
# შემდეგ კი სამივე სია დაამატე საერთო ცალრიელ სიას სახელად
# consumer_info. Input_ის მეშვეობით მომხმარებლის ინდექსის
# შეყვანის შემთხვევაში პროგრამამ უნდა დაბრუნოს არჩეულ
# მომხმარებელზე ინფორმაცია შემდეგნაირად:
# Name: Elene
# Lastname: Khardava
# Age: 21

consumer_info = [[], [], []]
for i in range(0,3):
    firstname = input("Please enter your firstname: ")
    lastname = input("Please enter your lastname: ")
    age = input("Please enter your age: ")
    consumer_info[i] += [firstname, lastname, age]

consumer_id = int(input("Choose consumer id to display data (0, 1, or 2) : "))
print(f"""Name: {consumer_info[consumer_id][0]}
Lastname: {consumer_info[consumer_id][1]}
Age: {consumer_info[consumer_id][2]}""")




# 2. მომხმარებელი დაარეგისტრირე ონლაინ პლატფორმაზე თუ
# სახელის ველი არ იქნება ცარიელი, ხოლო პაროლი 8 სიმბოლოზე
# მეტი ან ტოლია. მისი მონაცემები შეინახე ლისთში. შემდეგ მიეცი
# საშუალება სცადოს პლატფორმაზე შესვლა და შეადარე მის მიერ
# შემოყვანილი ინფორმაცია სიაში შენახულ ინფორმაციას.
# დაბეჭდე შესაბამისი მესიჯი.


username = input("Create an username: ")
password = input("Create a password(must contain at least 8 symbols): ")

if username and len(password) >= 8:
    user_data = [username, password]
    log_username = input("Please enter your username: ")
    log_password = input("Please enter your password: ")
    if log_username == username and log_password == password:
        print("You are logged in.")
    else:
        print("Username or password is not correct!")
else:
    print("Username can't be empty or password is shorter than 8 symbols.")




# 3. შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული ცნობილი
# მსახიობების შესახებ ინფორმაცია. მომხმარებელს შემოჰყავს
# მსახიობის სახელი ან გვარი. თუ სიაში მოიძებნა მსახიობი,
# დაბეჭდა მის შესახებ არსებული ინფორმაცია რეზუმის სახით.


actors_list = [
    ["Jack Nicholson", ["Age: 86", "Nationality: USA", "Top movies: 'Chinatown', 'One Flew Over the Cuckoo's Nest', 'The Shining'", "Awards: 3 Academy Awards, 6 Golden Globes"]],
    ["Tom Hanks", ["Age: 67", "Nationality: USA", "Top movies: 'Splash', 'Big', 'Forrest Gump'", "Awards: 2 Academy Awards, 4 Golden Globes"]],
    ["Dustin Hoffman", ["Age: 86", "Nationality: USA", "Top movies: 'Kramer vs Kramer', 'Tootsie', 'Rain Man'", "Awards: 2 Academy Awards, 6 Golden Globes"]],
    ["Joaquin Phoenix", ["Age: 49", "Nationality: Puerto Rico", "Top movies: 'Her', 'The Master', 'Gladiator'", "Awards: 1 Academy Awards, 2 Golden Globes"]],
    ["Anthony Hopkins", ["Age: 85", "Nationality: Wales", "Top movies: 'Legends of the Fall', 'The Father', 'The Silence of the Lambs'", "Awards: 2 Academy Awards, 4 BAFTA Awards"]]
]

user_choice = input("Please enter the name of actor: ").lower().strip()

not_in_the_list = 1
for i in actors_list:
    if user_choice in i[0].lower():
        print("\n", i[0], "\n", i[1][0], "\n", i[1][1], "\n", i[1][2], "\n", i[1][3])
        not_in_the_list -= 1

if not_in_the_list == 1:
    print("Sorry, your actor isn't in the list.")