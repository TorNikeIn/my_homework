# 1. დაწერე ფუნქცია რომელიც ლექსიკონიდან დუბლიკატებს ამოშლის და ყველა უნიკალური value_ს მქონე ლექსიკონს დააბრუნებს.


def unique_dict(dict_arg):
    result = dict()
    for key, value in dict_arg.items():
        if value not in result.values():
            result[key] = value
    print(str(result))
    return result


unique_dict({"a": 2, "b": 3, "c": 4, "d": 3})




# 2.დაწერე ფუნქცია რომელიც შეამოწმებს გადაცემული ლექსიკონი ცარიელია თუ არა და დააბრუნებს შესაბამის პასუხს.


def empty_dict_status(dict_arg):
    if dict_arg.items():
        print("The dictionary is not empty.")
    else:
        print("The dictionary is empty.")


empty_dict_status({})




# 3. დაწერე ფუნქცია, რომელიც გადაცემული სტრიქონისგან ლექსიკონს შექმნის და დააბრუნებს.
# ვთქვათ გადავეცით ფუნქციას სტრიქონი, უნდა დააბრუნოს სიმბოლოები key_ს ადგილას და მათი რაოდენობა value_ს ადგილას.
# მაგალითად გადავეცით სტრიქონი : 'racoon'
# უნდა დააბრუნოს ლექსიკონი: {'r': 1, 'a': 1, ‘c': 1, 'o': 2, ‘n': 1}


def dict_from_str(string):
    result = {}
    char_list = []
    for i in string:
        char_list.append(i)
    char_set = set(char_list)
    filtered_char_list = list(char_set)
    for j in filtered_char_list:
        if j != " ":
            result[j] = string.count(j)
    print(result)
    return result


dict_from_str("abcddddd eeee")
