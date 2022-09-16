import re
from random import randint

name = 'muhammadihsan3011@gmail.com'

def username_generator(name):
    email = re.sub(r'@\S*\s?', '', name)
    username = email + str(randint(0, 999))
    return username

if __name__ == '__main__':
    username_generator(name)
