import string

from password_generator import PasswordGenerator

pg = PasswordGenerator(10)
print(pg._password_len)
print(pg._password)
pg.add(string.digits, 9)
print(pg._password)
print(pg.ready())
print(pg.password())
pg.add(string.ascii_lowercase, 1)
print(pg.ready())
print(pg.password())
