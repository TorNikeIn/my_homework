# 1. შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე სიას,
# თუმცა უნიკალური ელემენტებით (გამოიყენე set მონაცემთა ტიპი).


def unique_list(list_arg):
    result = set(list_arg)
    print(result)
    return result


unique_list([2, 3, 4, 5, 6, 7, 7, 8, 8, 9])




# 2. შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე set ტიპის მონაცემს უნიკალური ელემენტებით,
# რომლის შეცვლაც შეუძლებელი იქნება (გამოიყენე frozenset).


def immutable_set(list_arg):
    result = frozenset(list_arg)
    print(result)
    return result


immutable_set([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9])




# 3. შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის მონაცემს, გააერთიანებს მათ,
# შემდეგ კი გადააქცევს tuple ტიპის მონაცემად და დააბრუნებს შედეგს.


def set_to_tuple(set1, set2):
    set1.update(set2)
    result = tuple(set1)
    print(result)
    return result


set_to_tuple({2, 3, 5, 6, 7, 8}, {3, 5, 10, 12, 13})
