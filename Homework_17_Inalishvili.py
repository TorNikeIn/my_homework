# 1. შექმენი კლასი, რომელსაც ექნება public, protected და private პარამეტრები.
# გამოიყენე @ property დეკორატორი და ასევე შექმენი setter და getter დეკორატორებიანი ფუნქციები
# პარამეტრებზე წვდომისა და რედაქტირებისთვის.


class Diary:
    def __init__(self, diary_user, public_note, private_note):
        assert type(diary_user) is str, "All parameters must be strings."
        assert type(public_note) is str, "All parameters must be strings."
        assert type(private_note) is str, "All parameters must be strings."

        self._diary_user = diary_user
        self.public_note = public_note
        self.__private_note = private_note

    @property
    def private_note(self):
        return self.__private_note

    @private_note.setter
    def private_note(self, value):
        assert type(value) is str, "Note must be a string."
        self.__private_note = value

    @private_note.getter
    def private_note(self):
        return self.__private_note

    def public_editor(self, new_note):
        assert type(new_note) is str, "Note must be a string."
        self.public_note = new_note
        return self.public_note


# my_note = Diary( "Emo Teen", "First public note", "First private note")
# print(my_note.private_note)
# my_note.private_note = "Second private note"
# print(my_note.public_note)
# my_note.public_editor("Second public note")
# print(my_note.private_note)
# print(my_note.public_note)




# 2. შექმენი მისი შვილობილი კლასი და შეუცვალე რაიმე არსებული მეთოდი.


class AdvancedDiary(Diary):
    def __init__(self, diary_user, public_note, private_note):
        super().__init__(diary_user, public_note, private_note)
        assert type(public_note) is str, "Note must be a string."
        self.advanced_public_note = public_note

    def public_editor(self, new_note):
        assert type(new_note) is str, "Note must be a string."
        self.public_note += " / " + new_note
        return self.public_note


my_advanced_note = AdvancedDiary("Emo Teen", "First public note", "First Private note")
print(my_advanced_note.private_note)
my_advanced_note.private_note = "Second private note"
print(my_advanced_note.public_note)
my_advanced_note.public_editor("Second public note")
print(my_advanced_note.private_note)
print(my_advanced_note.public_note)
