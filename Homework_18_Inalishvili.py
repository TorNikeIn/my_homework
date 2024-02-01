# შექმენი საბანკო ანგარიშის კლასი, მომხმარებლის, პაროლის და საწყისი თანხის პარამეტრებით. თანხის შეტანის,
# გამოტანის და გადარიცხვის, დარჩენილი ნაშთის ჩვენების მეთოდებით. __repr__ მეჯიქ მეთოდით.
# პაროლის ცვლადი უნდა იყოს private _ ცვლადი და საჭიროა აკმაყოფილებდეს პირობას: მინიმალური სიმბოლოების ოდენობა _ 8.


class Bank:
    def __init__(self, user_name, password, starting_amount):
        assert type(user_name) is str, "Username must be a string."
        assert len(user_name) > 0, "Username can not be empty."
        assert type(password) is str, "Password must be a string."
        assert type(starting_amount) is int or float, "Starting amount must be integer or float number."
        assert len(password) >= 8, "Password must be at least 8 character long."
        assert starting_amount >= 0, "Amount on the account can't be negative."
        self.user_name = user_name
        self.__password = password
        self.starting_amount = starting_amount

    @property
    def password_func(self):
        return self.__password

    @password_func.setter
    def password_func(self, new_password):
        assert type(new_password) is str, "Password must be a string."
        assert len(new_password) >= 8, "Password must be at least 8 character long."
        self.__password = new_password

    @password_func.getter
    def password_func(self):
        return self.__password

    def deposit(self, deposit_amount):
        assert type(deposit_amount) is int or float, "Deposit amount must be integer or float number."
        assert deposit_amount > 0, "Deposit amount must be positive."
        self.starting_amount += deposit_amount
        print(f"US$ {deposit_amount} was credited to the account.")

    def withdraw(self, withdraw_amount):
        assert type(withdraw_amount) is int or float, "Amount to withdraw must be integer or float number."
        assert withdraw_amount > 0, "Withdrawal amount must be positive."
        assert withdraw_amount <= self.starting_amount, "Not enough money on the account."
        self.starting_amount -= withdraw_amount
        print(f"US$ {withdraw_amount} was withdrawn from the account.")

    def transfer(self, recipient_name, recipient_number, transfer_amount):
        assert type(transfer_amount) is int or float, "Transfer amount must be integer or float number."
        assert transfer_amount <= self.starting_amount, "Not enough money to transfer."
        assert type(recipient_name) is str, "Recipient's name must be a string."
        assert len(recipient_name) > 0, "Recipient's name can not be empty."
        assert type(recipient_number) is int, "Recipient's card number must be an integer."
        assert len(str(recipient_number)) == 12, "Recipient's card number must be 12 symbols long."
        self.starting_amount -= transfer_amount
        print(f"""US$ {transfer_amount} transferred to {recipient_name}
                Recipient Card Number: {recipient_number}
                Amount left on the account: US$ {self.starting_amount}""")

    def __repr__(self):
        return f"Username: {self.user_name}\nAvailable amount: US$ {self.starting_amount}"


user1 = Bank("Trulaila", "needs_no_money", 1500)
print(user1.password_func)
user1.password_func = "needs_little_money"
print(user1.password_func)
user1.deposit(425.5)
user1.withdraw(106.5)
user1.transfer("Givi", 123456789123, 590.5)
print(repr(user1))
