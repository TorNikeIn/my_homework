# 1. დაწერე ფუნქცია რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას.

from random import randint
import time
def list_generator(size, max_range):
    my_list = []
    for _ in range(size):
        random_num = randint(0, max_range)
        my_list.append(random_num)
    return my_list


my_list = list_generator(50, 1000)


# 2. დაასორტირე შექმნილი სია რომელიმე ოპტიმალური მეთოდით.

my_list.sort()




# 3. დასორტირებულ სიაში ელემენტის მოსაძებნად გამოიყენე ხაზობრივი და ბინარული ძიება.

def linear(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


num_searched_linear = linear(my_list, 456)
print("Linear search result:", num_searched_linear)

def binary(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary(arr, low, mid-1, x)

        else:
            return binary(arr, mid+1, high, x)
    else:
        return -1


num_searched_binary = binary(my_list, 0, 49, 243)
print("Binary search result:", num_searched_binary, "\n")




# 4. დათვალე ძიების თითოეული მეთოდისთვის საჭირო დრო (დეკორატორის გამოყენებით)
# და დააკვირდი დროში სხვაობას მცირე, საშუალო და გრძელი სიის შემთხვევებში.


def search_method_comparison():

    short_list = list_generator(100, 10000)
    medium_list = list_generator(1000, 100000)
    long_list = list_generator(10000, 1000000)

    short_list.sort()
    medium_list.sort()
    long_list.sort()

    def timing_decorator(func):
        def wrapper(*args):
            start_time = time.time()
            func(*args)
            end_time = time.time()
            search_time = end_time - start_time
            return search_time

        return wrapper

    @timing_decorator
    def binary_search(arr, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid

            elif arr[mid] > x:
                return binary_search(arr, low, mid - 1, x)

            else:
                return binary_search(arr, mid + 1, high, x)
        else:
            return -1

    @timing_decorator
    def linear_search(arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1

    short_linear_time = linear_search(short_list, 78)
    short_binary_time = binary_search(short_list,0, 99, 78)
    if short_linear_time < short_binary_time:
        print("Linear search method is faster on short lists.", "\n")
    else:
        print("Binary search method is faster on short lists.", "\n")

    medium_linear_time = linear_search(medium_list, 856)
    medium_binary_time = binary_search(medium_list, 0, 999, 856)
    if medium_linear_time < medium_binary_time:
        print("Linear search method is faster on medium size lists.", "\n")
    else:
        print("Binary search method is faster on medium size lists.", "\n")

    long_linear_time = linear_search(long_list, 7568)
    long_binary_time = binary_search(long_list, 0, 9999, 7568)
    if long_linear_time < long_binary_time:
        print("Linear search method is faster on long lists.")
    else:
        print("Binary search method is faster on long lists.")


search_method_comparison()
