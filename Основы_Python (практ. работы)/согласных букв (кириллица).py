letter = input ('Введите букву (кириллицей)')
if letter == 'а' or letter == 'е' or letter == 'и' or letter == 'о' or letter == 'у':
    print ('Гласная буква')
elif letter == 'Ъ' or letter == 'Ь':
    print ('Не относится ни к гласным, ни к согласным')
else:
    print ('Согласная буква')