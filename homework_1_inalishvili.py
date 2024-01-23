# დავალება 1
# დაწერე პროგრამა, რომელიც გეკითხება ჯერ სახელს, შემდეგ გვარს და
# ინფორმაციის მიღების შემდეგ ტერმინალში ბეჭდავს ერთმანეთის გვერდით.

first_name = input('Enter your firstname:')
last_name = input('Enter your lastname:')

print(first_name, last_name)


# დავალება 2
# დაწერე პროგრამა, რომელიც ითხოვს ორ რიცხვს, პირველი რიცხვი აჰყავს მეორის
# ხარისხში და შედეგი იბეჭდება ტერმინალში.

base_num = input('Enter a base number:')
exponent_num = input('Enter an exponent number:')

print(int(base_num) ** int(exponent_num))


# დავალება 3
# დაწერე პროგრამა, რომელიც გეკითხება სახელს, გვარს, ასაკს და
# ქალაქს და ბეჭდავს ინფორმაციას ტერმინალში.

name = input('Enter your name:')
surname = input('Enter your surname:')
age = input('Enter your age:')
city = input('Enter your city:')

print(f'''
Name: {name}
Surname: {surname}
Age: {age}
City: {city}
''')


# დავალება 4
# დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ნებისმიერი სამი სხვადასხვა ხილის
# დასახელება ცალცალკე. რეზულტატი კი იბეჭდება შემდეგი სახით: Apple//Peach%%Orange

fruit_1 = input('Enter fruit 1:')
fruit_2 = input('Enter fruit 2:')
fruit_3 = input('Enter fruit 3:')

print(f"{fruit_1}//{fruit_2}%%{fruit_3}")


# დავალება 5
# დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ტექსტი, დათვლის მასში არსებული
# სიმბოლოების რაოდენობას და გამოიტანს შედეგს შემდეგნაირად: Number of symbols: 50

text = input('Type some text:')
print(f"Number of symbols: {len(text)}")