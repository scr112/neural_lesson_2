# putin_birthdate_year = 1952
# elcin_birthdate_year = 1931
# gorbachev_birthdate_year = 1931
# brezhnev_birthdate_year = 1906
# andropov_birthdate_year = 1914
error_answer = 0
accept_answer = 0

putin_birthdate_year = int(input("какой год рождения В. В. Путина: ", ))
if putin_birthdate_year == 1952:
    print("Правильно")
    accept_answer += 1
else:
    print("неправильно")
    error_answer += 1
elcin_birthdate_year = int(input("какой год рождения Б. Н. Ельцина: ", ))
if elcin_birthdate_year == 1931:
    print("Правильно")
    accept_answer += 1
else:
    print("неправильно")
    error_answer += 1
gorbachev_birthdate_year = int(input("какой год рождения М. С. Горбаче: ", ))
if gorbachev_birthdate_year == 1931:
    print("Правильно")
    accept_answer += 1
else:
    print("неправильно")
    error_answer += 1
brezhnev_birthdate_year = int(input("какой год рождения Л. И. Брежнев: ", ))
if brezhnev_birthdate_year == 1906:
    print("Правильно")
    accept_answer += 1
else:
    print("неправильно")
    error_answer += 1
andropov_birthdate_year = int(input("какой год рождения В. А. Андропова: ", ))
if andropov_birthdate_year == 1914:
    print("Правильно")
    accept_answer += 1
else:
    print("неправильно")
    error_answer += 1
error_percent = (error_answer / 5) * 100
accept_percent = (accept_answer / 5) * 100
print("Отлично, вы закончили викторину!!!, \n , процент ваших правильных ответов: ", accept_percent, "%\n",
      "Количество не правильных ответов: ", error_percent, "%")
