pushkin_birth_year = int(input("какой год рождения А.С Пушкина: ", ))

if pushkin_birth_year == 1799:
    print("верно")
    pushkin_birth_day = int(input("какого числа родился А.С Пушкина: ", ))
    if pushkin_birth_day == 26:
        print("верно")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год")
