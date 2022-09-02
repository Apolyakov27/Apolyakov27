import time
birthdays = {}
def f(x):
    with open(u"/Users/alexey/Desktop/Разное/Учеба/Python/List of bdays.txt", "r+") as bdays_list:
        x = bdays_list.read().strip()
        sp = x.split("\n")
        sp.sort()
        spstr = ("\n").join(sp)
        time.sleep(1)
    with open(u"/Users/alexey/Desktop/Разное/Учеба/Python/List of bdays.txt", "w") as bdays_list:
        bdays_list.write(spstr)
pass
print("Справочник дней рождения")
time.sleep(1)
print("Для поиска нажмите 1, для ввода новых имен нажмите 2. \nЧтобы посмотреть весь список, нажмите 3.")
q = input()
if q == "2":
    while True:
        bdays_list = open(u"/Users/alexey/Desktop/Разное/Учеба/Python/List of bdays.txt", "r+")
        x = bdays_list.read().strip()
        sp = x.split("\n")
        list = []
        time.sleep(0.5)
        friend = input("Введите имя: ")
        if friend == "":
            break
        if friend not in x:
            friends_list = list.append(friend)
            list.sort()
            time.sleep(0.5)
            birthdays[friend] = input("Введите дату рождения: ")
            for x in list:
                bdays_list.write("\n" + x + " - " + birthdays[x] + "\n")
            time.sleep(0.5)
            print(friend + " теперь в списке!")
            bdays_list.close()
            f(friend)
            time.sleep(0.5)
            print("Ввести новое имя? 1 - да, 2 - нет")
            if input() == "1":
                continue
            else:
                break
        else:
            for i in sp:
                g = i.find(friend)
                if g != -1:
                    time.sleep(1)
                    print(friend + " уже есть в списке")
                    print(i)
            print("Попробовать снова? Да - 1, нет - любая клавиша")
            if input() != "1":
                break
            else:
                continue
if q == "1":
    with open(u"/Users/alexey/Desktop/Разное/Учеба/Python/List of bdays.txt", "r+") as bdays_list:
        x = bdays_list.read().strip()
        sp = x.split("\n")
        while True:
            list = []
            time.sleep(0.5)
            friend = input("Введите имя: ")
            if friend == "":
                break
            if friend not in x:
                time.sleep(0.5)
                print(friend + " не находится в списке. Нажмите 1, чтобы добавить или любую клавишу, чтобы пропустить")
                if input() == "1":
                    friends_list = list.append(friend)
                    time.sleep(0.5)
                    birthdays[friend] = input("Введите дату рождения: ")
                    for x in list:
                        bdays_list.write(x + " - " + birthdays[x] + "\n")
                    #f(q)
                    time.sleep(0.5)
                    print(friend + " теперь в списке!")
                    time.sleep(0.5)
                    print("Продолжить поиск? 1 - да, 2 - нет")
                    if input() == "1":
                        continue
                    else:
                        break
                else:
                    time.sleep(1)
                    print("Продолжить поиск? 1 - да, 2 - нет")
                    if input() == "1":
                        continue
                    else:
                        break
            if friend in x:
                for i in sp:
                    f = i.find(friend)
                    if f != -1:
                        print(friend + " уже есть в списке")
                        print(i)
                time.sleep(1)
                print("Продолжить поиск? 1 - да, 2 - нет")
                if input() == "1":
                    continue
                else:
                    break
if q == "3":
    f(q)

