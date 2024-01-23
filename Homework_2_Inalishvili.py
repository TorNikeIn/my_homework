# 1. ვიქტორინა
# შეადგინე ვიქტორინის პროგრამა. მომხმარებელს უნდა დავუსვათ კითხვა: “რომელი
# იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს დღესაც?”
# სავარაუდო პასუხები:
# 1. შუმერთა
# 2. სელჩუკთა
# 3. რომის
# 4. მონღოლთა
# მომხმარებელმა უნდა შეიყვანოს სწორი პასუხის ნომერი ან თავად სწორი პასუხი.
# შეცდომის შემთხვევაში იბეჭდება: „არა! სწორი პასუხია რომის!“
# სწორი პასუხის შემთხვევაში იბეჭდება: „სწორია!“


quiz_question = input('''რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს დღესაც?
1. შუმერთა
2. სელჩუკთა
3. რომის
4. მონღოლთა
შეიყვანეთ პასუხი: ''')

if quiz_question == "3" or quiz_question == "რომის" or quiz_question == "რომი":
    print("სწორია!")
else:
    print("არა! სწორი პასუხია რომის!")




# 2. ონლაინ მაღაზია
# პროგრამა გთავაზობს პროდუქტის სამ კატეგორიას.
# მაგ.
# 1. ლეპტოპები
# 2. პერსონალური კომპიუტერები
# 3. მობილურები
# მომხმარებელი ირჩევს ერთ-ერთს.
# პროგრამა ითხოვს მაქსიმალურ ბიუჯეტს და ბიუჯეტის მიხედვით სთავაზობს
# მომხმარებელს კონკრეტულ მოდელს არჩეულ კატეგორიაში. (თითო კატეგორიაში მინიმუმ 3 პროდუქტი მაინც უნდა იყოს)
# თუ ბიუჯეტი ძალიან მცირეა, პროგრამა ბეჭდავს, რომ ამ თანხაში არ გააჩნია შემოთავაზება.


laptop_1 = 750
laptop_2 = 970
laptop_3 = 1550
laptop_4 = 1700

pc_1 = 980
pc_2 = 1100
pc_3 = 1350
pc_4 = 1720

smartphone_1 = 350
smartphone_2 = 400
smartphone_3 = 630
smartphone_4 = 1220

category = input("Please choose category (laptop, pc or smartphone): ")
budget = int(input("Please Enter your budget: "))

if category == "laptop":
    if budget < laptop_1:
        print("Sorry, we don't have any offer for this budget.")
    elif budget < laptop_2:
        print("We have a laptop_1 for you")
    elif budget < laptop_3:
        print("We have two options for you: laptop_1 and laptop_2.")
    elif budget < laptop_4:
        print("We have three options for you: laptop_1, laptop_2 and laptop_3")
    else:
        print("We have four options for you: laptop_1, laptop_2, laptop_3 and laptop_4")
elif category == "pc":
    if budget < pc_1:
        print("Sorry, we don't have any offer for this budget.")
    elif budget < pc_2:
        print("We have a pc_1 for you")
    elif budget < pc_3:
        print("We have two options for you: pc_1 and pc_2.")
    elif budget < pc_4:
        print("We have three options for you: pc_1, pc_2 and pc_3")
    else:
        print("We have four options for you: pc_1, pc_2, pc_3 and pc_4")
elif category == "smartphone":
    if budget < smartphone_1:
        print("Sorry, we don't have any offer for this budget.")
    elif budget < smartphone_2:
        print("We have a smartphone_1 for you")
    elif budget < smartphone_3:
        print("We have two options for you: smartphone_1 and smartphone_2.")
    elif budget < smartphone_4:
        print("We have three options for you: smartphone_1, smartphone_2 and smartphone_3")
    else:
        print("We have four options for you: smartphone_1, smartphone_2, smartphone_3 and smartphone_4")
else:
    print("Please enter correct category name.")




# 3. ქუესთის შედგენა (Text Based Adventure Game)
# დაწერე ერთმანეთში ჩასმული if-else კონსტრუქციების
# გამოყენებით მარტივი ტექსტზე დაფუძნებული სათავგადასავლო თამაში.
# მაგ. თავიდან პროგრამა ბეჭდავს მომხმარებლის ადგილსამყოფელს და სთავაზობს
# მქომედების რამდენიმე ვარიანტს. სხვადასხვა არჩევანის შემთხვევაში თამაშ
# სხვადასხვანაირად ვითარდება.


print('''Welcome to the Paths subject of the Earth!
You are about to born again my proud atma...
But what will you be?..
Choose wisely...''')

path_to_kingdoms = int(input('''Gate 1, the writing says:
You bury me when I'm alive,
and dig me up only when I die.

Gate 2, the writing says:
Lot of drama, lot of hate - but mostly
the drive to survive.

Which gate to enter? 1 or 2 : '''))

if path_to_kingdoms == 1:
    path_to_plants = int(input('''More Gates to choose...
    Gate 1, the writing says:
    Wear rings without having fingers, and leave
    without going anywhere.

    Gate 2, the writing says:
    Fill the ground with color as
    a cloud hides the sun.

    Which Gate to enter? 1, or 2 : '''))
    if path_to_plants == 1:
        path_to_trees = int((input('''The Gates again
        Gate 1, the writing says:
        Into paper and sheets you're often cast
        you think you're tree but you're grass.

        Gate 2, the writing says:
        You with branches and all green
        in December you will be seen.

        Gate 3, the writing says:
        The sap from beneath your bark
        will be a breakfast time staple.

        Which Gate to enter? 1, 2, or 3? : ''')))
        if path_to_trees == 1:
            print("You will be a bamboo!! You will grow lightning fast!")
        elif path_to_trees == 2:
            print("You will be a christmas tree. Shine and twinkle!")
        elif path_to_trees == 3:
            print("You will be a maple tree. Be sweet dress warmly, it's cold outside in Canada.")
        else:
            print("Enter only 1, 2, or 3. Try again.")

    elif path_to_plants == 2:
        path_to_flowers = int(input('''The Gates again...
        Gate 1, the writing says:
        Delicate and bright,
        petals unfold in delight.

        Gate 2, the writing says:
        Yellow-golden, like a chick, fluffy
        immediately wither from the cold sissy.

        Gate 3, the writing says:
        The sun is your friend, truly best friend
        stare at it all day until the night rests.

        Which gate to enter? 1, 2, or 3 : '''))
        if path_to_flowers == 1:
            print("You will be a daisy.")
        elif path_to_flowers == 2:
            print("You will be a mimosa.")
        elif path_to_flowers == 3:
            print("You will be a sunflower")
        else:
            print("Enter only 1, 2, or 3. Try again.")
    else:
        print("Enter only 1 or 2. Try again.")
elif path_to_kingdoms == 2:
    path_to_animals = int(input('''More Gates to choose...
    Gate 1, the writing says:
    So weak, a little wind can move
    so strong, no shore too proof.

    Gate 2, the writing says:
    Heavy grey, pure white
    a drama of changing blinding silver, blue

    Gate 3, the writing says:
    My feet are on solid,
    for to the earth I am bound.

    Which Gate to enter? 1, 2, or 3 : '''))
    if path_to_animals == 1:
        path_to_water_animals = int(input('''More Gates to choose...
        Gate 1, the writing says:
        Hop around tadpole when young
        croak and catch flies with long long tongue.

        Gate 2, the writing says:
        Clangs, clicks and codas,
        massive predator feeds, vulnerable might.

        Gate 3, the writing says:
        Glowing jellies sink or swim
        almost all water dance and twirl.

        Which gate to enter? 1, 2, or 3 : '''))
        if path_to_water_animals == 1:
            print("You will be a frog.")
        elif path_to_water_animals == 2:
            print("You will be a whale.")
        elif path_to_water_animals == 3:
            print("You will be a jellyfish.")
        else:
            print("Enter only 1, 2, or 3. Try again.")
    elif path_to_animals == 2:
        path_to_sky_animals = int(input('''More Gates to choose...
        Gate 1, the writing says:
        Begin the life in a different state -
        hatch, eat, then pupa up and wait.

        Gate 2, the writing says:
        Can fly backwards
        buzz as you roam.

        Gate 3, the writing says:
        Upside down you big surprise
        see with your ears, hid from sunrise.

        Which gate to enter? 1, 2, or 3 : '''))
        if path_to_sky_animals == 1:
            print("You will be a butterfly.")
        elif path_to_sky_animals == 2:
            print("You will be a hummingbird.")
        elif path_to_sky_animals == 3:
            print("You will be a bat.")
        else:
            print("Enter only 1, 2, or 3. Try again.")
    elif path_to_animals == 3:
        path_to_land_animals = int(input('''More Gates to choose...
        Gate 1, the writing says:
        Eat fish and berries
        you huge and furry.

        Gate 2, the writing says:
        Day or night, homeward-bound
        no hooves to beat, yet running free.

        Gate 3, the writing says:
        Try to think about others first
        but fail sometimes to quench selfish thirst.

        Which gate to enter? 1, 2, or 3 : '''))
        if path_to_land_animals == 1:
            print("You will be a bear.")
        elif path_to_land_animals == 2:
            print("You will be a horse.")
        elif path_to_land_animals == 3:
            print('''Hooray! You manage to rebirth as a human again.
            You are blessed... or cursed! Who knows...''')
        else:
            print("Enter only 1, 2, or 3. Try again.")
    else:
        print("Enter only 1, 2, or 3. Try again.")
else:
    print("Enter only 1 or 2. Try again.")




# 4. მომხმარებლისთვის კარიერის შერჩევა (არასავალდებულო)
# პროგრამა უსვამს მომხმარებელს რამდენიმე კითხვას
# (თქვენი იმპროვიზაციით) და ურჩევს მისთვის შესაფერისპროფესიას.

print('''Please answer questions to get the career advise.
Enter only numbers according to your answer.''')

question_1 = int(input('''What type of intelligence are you strongest at?

1. Logical-mathematical intelligence.
2. Interpersonal intelligence.
3. Linguistic intelligence.'''))

question_2 = int(input('''What factor is the most important for you?

1. Influence on the World.
2. Flexible work hours.
3. To be your own boss.'''))

if question_1 == 1 and question_2 == 1:
    print('''Your career choice might be:
    Scientist''')
elif question_1 == 1 and question_2 == 2:
    print('''Your career choice might be:
    Computer programmer''')
elif question_1 == 1 and question_2 == 3:
    print('''Your career choice might be:
    Economist''')
elif question_1 == 2 and question_2 == 1:
    print('''Your career choice might be:
    Politician''')
elif question_1 == 2 and question_2 == 2:
    print('''Your career choice might be:
    Publicist''')
elif question_1 == 2 and question_2 == 3:
    print('''Your career choice might be:
    Psychologist''')
elif question_1 == 3 and question_2 == 1:
    print('''Your career choice might be:
    Journalist''')
elif question_1 == 3 and question_2 == 2:
    print('''Your career choice might be:
    Editor''')
else:
    print('''Your career choice might be:
    Lawyer''')
