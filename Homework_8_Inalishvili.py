# 1. დაწერე პროგრამა, რომელიც გადაამრავლებს სიის ყველა
# წევრს კონკრეტულ რიცხვზე ლამბდას გამოყენებით.


def multi_list(nums, a):
    multi_by_a = lambda x: x * a
    new_list = list(map(multi_by_a, nums))
    print(new_list)
    return new_list

multi_list([1,2,3,4], 5)




# 2. დაწერე პროგრამა ლამბდას გამოყენებით, რომელიც გადაცემული სიის სიგრძეს დააბრუნებს,
# მას შემდეგ რაც წაშლის სიიდან ყველა სახელს რომელიც პატარა სიმბოლოთი იწყება.
# (გამოიყენე .isupper() მეთოდი)


def modified_list_length(names):
    modified_list = [x for x in names if (lambda s: s[0].isupper())(x)]
    print(len(modified_list))
    return len(modified_list)

modified_list_length(["asdr", "Adf"])




# 3. დაწერე პროგრამა რომელიც დააჯამებს სიაში არსებულ დადებით და უარყოფით რიცხვებს ცალცალკე.
# გამოიყენე ლამბდა ფუნქცია და filter.


def positives_and_negatives(nums):
    positives = list(filter(lambda x: x > 0, nums))
    negatives = list(filter(lambda x: x < 0, nums))

    sum_of_positives = sum(positives)
    sum_of_negatives = sum(negatives)

    print(f"""Sum of positive numbers is: {sum_of_positives}.
Sum of negative numbers is: {sum_of_negatives}.""")
    return sum_of_positives, sum_of_negatives

positives_and_negatives([3,5,6,22,-8,-12])




# 4. დაწერე ბანკის ექაუნთის შექმნის, ანგარიშზე თანხის განთავსების და შემდგომ ექაუნთში შესვლის პროგრამა,
# არასწორი ინფორმაციის შეყვანა მომხმარებლისგან დააზღვიე try და except ბლოკის მეშვეობით.

def bank_account():
    try:
        username = input("Create an username: ")
        password = input("Create a password(must contain at least 8 symbols): ")
        amount = int(input("Enter amount to place on your account: "))

        if username and len(password) >= 8:
            log_username = input("Please enter your username: ")
            log_password = input("Please enter your password: ")

            try:
                if log_username == username and log_password == password:
                    print(f"""You are logged in.
                            Amount on your account: {amount}""")
            except:
                print("Username or password is not correct!")
    except:
        print("Username can't be empty or password is shorter than 8 symbols.")

bank_account()