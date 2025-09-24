import random

def pass_gen():
    char = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0 ! @'
    usable_char = char.split(' ')
    password_part = random.sample(usable_char, 4)
    final = ''.join(password_part)
    return final

password = f'{pass_gen()}-{pass_gen()}-{pass_gen()}'
print(password)

def test_password():
    points = 0
    for i in password:
        if i.isalnum():
            points += 1
        elif i.isalpha() == False:
            points += 1
        else:
            points -= 1

    return 'Strong' if points == 14 else 'Weak'

test = test_password()
print(test)