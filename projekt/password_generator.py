import random


class PasswordGenerator:
    def __init__(self, password_len):
        self._password_len = password_len
        self._password = []

    def add(self, what, number_of_characters):
        if self._character_left() >= number_of_characters:
            self._password += random.choices(what, k=number_of_characters)
            random.shuffle(self._password)
            return True

        return False

    def ready(self):
        return self._character_left() == 0

    def _character_left(self):
        return self._password_len - len(self._password)
    def password(self):

        if self.ready():
            return ''.join(self._password)
