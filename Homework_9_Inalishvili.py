# 1. დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sort() მეთოდის გამოყენებით (ზრდადობით).


from random import randint
sort_list = []
for i in range(10):
    random_num = randint(1,1000)
    sort_list.append(random_num)
sort_list.sort()

print(sort_list)




# 2. დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sorted() ფუნქციის გამოყენებით (კლებადობით).


from random import randint
sort_list_reverse = []
for i in range(10):
    random_num = randint(1,1000)
    sort_list_reverse.append(random_num)
sort_list_reverse.sort(reverse=True)

print(sort_list_reverse)




# 3. დაწერე პროგრამა რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას და შექმნილი სიის სორტირებასცადე ორი განსხვავებული
# მეთოდით(მაგ. Bubble და Selection). დათვალე თითოეული მეთოდისთვის სორტირებისთვის საჭირო დრო და დააკვირდი,
# რომელი უფრო ეფექტურია მცირე(1000 ელემენტი), საშუალო(2000 ელემენტი) და გრძელი(3000 ელემენტი) სიის შემთხვევებში.


from random import randint
import time
def sort_method_comparison():

    def list_generator(size):
        unsorted_list = []
        for i in range(size):
            random_num = randint(1,100000)
            unsorted_list.append(random_num)
        return unsorted_list

    small_bubble = list_generator(1000)
    medium_bubble = list_generator(3000)
    large_bubble = list_generator(10000)
    small_insertion = list_generator(1000)
    medium_insertion = list_generator(3000)
    large_insertion = list_generator(10000)

    def timing_decorator(func):
        def wrapper(*args):
            start_time = time.time()
            func(*args)
            end_time = time.time()
            sort_time = end_time - start_time
            print(f"Time taken for {func.__name__}: {sort_time} seconds")
            return sort_time

        return wrapper

    @timing_decorator
    def bubble_sort(num_list):
        indexing_length = len(num_list) - 1
        list_sorted = False

        while not list_sorted:
            list_sorted = True
            for i in range(0, indexing_length):
                if num_list[i] > num_list[i + 1]:
                    list_sorted = False
                    num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
        return num_list

    @timing_decorator
    def insertion_sort(num_list):
        arr = num_list
        indexing_length = range(1, len(arr))

        for i in indexing_length:
            value_to_sort = arr[i]

            while arr[i-1] > value_to_sort and i > 0:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                i = i - 1
        return arr

    print("Sorting time on small lists:")
    small_bubble_time = bubble_sort(small_bubble)
    small_insertion_time = insertion_sort(small_insertion)
    if small_bubble_time < small_insertion_time:
        print("Bubble sort method is faster on small lists.", "\n")
    else:
        print("Insertion sort method is faster on small lists.", "\n")

    print("Sorting time on medium size lists:")
    medium_bubble_time = bubble_sort(medium_bubble)
    medium_insertion_time = insertion_sort(medium_insertion)
    if medium_bubble_time < medium_insertion_time:
        print("Bubble sort method is faster on medium size lists.", "\n")
    else:
        print("Insertion sort method is faster on medium size lists.", "\n")

    print("Sorting time on large lists:")
    large_bubble_time = bubble_sort(large_bubble)
    large_insertion_time = insertion_sort(large_insertion)
    if large_bubble_time < large_insertion_time:
        print("Bubble sort method is faster on large lists.")
    else:
        print("Insertion sort method is faster on large lists.")

sort_method_comparison()