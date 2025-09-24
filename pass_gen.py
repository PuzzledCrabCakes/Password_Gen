import random


char = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0 ! @'

usable_char = char.split(' ')

password_part_1 = random.sample(usable_char, 4)
password_part_2 = random.sample(usable_char, 4)
password_part_3 = random.sample(usable_char, 4)

final_1 = ''.join(password_part_1)
final_2 = ''.join(password_part_2)
final_3 = ''.join(password_part_3)


password = f'{final_1}-{final_2}-{final_3}'
print(password)
