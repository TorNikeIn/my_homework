# 1. რეკურსიის დახმარებით შექმენი ფუნქცია, რომელიც იმდენჯერ დაბეჭდავს მისალმებას,
# რა რიცხვსაც გადასცემ არგუმენტად. (ციკლის გამოყენება არ შეიძლება)


def hello_printer(a):
    if a == 1:
        print("Hello there!")
        return
    else:
        print("Hello there!")
        return hello_printer(a-1)


hello_printer(4)




# 2. შექმენი ფუნქცია, რომელიც მიიღებს შეკვეთას, ანუ კერძის სახელს და რაოდენობას
# და დაბეჭდავს მას, თუმცა რაოდენობას თუ არ მივუთითებთ შეცდომას არ ამოაგდებს და 1_ად ჩათვლის.


def cook(dish, quantity=1):
    print(f"{dish} : {quantity}.")


cook("Khinkali")




# 3. შექმენი ფუნქცია, რომელიც მიიღებს მინიმუმ 3 რიცხვს,  და დააბრუნებს და დაბეჭდავს ნარმავლს.


def multi(a,b,c,*args):
    result = a*b*c
    for i in args:
        result *= i
    print(result)
    return result

multi(2, 2,2, 3, 3, 3)