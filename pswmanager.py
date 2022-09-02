# менеджер учетных записей для личного пользования с заделом под дальнейшее редактирование, не залезая под капот 
accountsData = {"Gosuslugi":{"8 9xx 9xx xx xx": "!xxxxxxxxx"},
                "Госуслуги":{"8 9xx 9xx xx xx": "!xxxxxxxxx"},
                "Гос услуги":{"8 9xx 9xx xx xx": "!xxxxxxxx"},
                "Почта mail.ru":{"xxx@xxxx.ru":"xxxxxxxxxx"},
                'Работа':{"xxx@xxxx.ru":"xxxxxxx"}}

import sys

def show(list):
 while True:
    print("Введите название аккаунта")
    query = input()
    for i in list.keys():
        if query.lower() in str(i).lower():
            query = i
            b = 1
            break
        else:
            b = 0

    if b > 0:
        i = list[query]
        for k,v in i.items():
            print("Аккаунт: " + query + "\nЛогин: " + k + "\nПароль: " + v)
        print("Продолжить?")
        answ1 = input()
        if answ1.lower() == "да":
            continue
        else:
            print("Программа завершена, спасибо!")
        break

    elif b == 0:
        print("Аккаунт " + query + " не найден. \nХотите добавить?")
        answ = input()
        if answ.lower() == "да":
            print("Введите название аккаанта:")
            accountNew = input()
            print("Введите логин")
            loginNew = input()
            print("Введите пароль")
            pswNew = input()
            newLoginPsw = {loginNew:pswNew}
            list[accountNew]=newLoginPsw
            print("Аккаунт успешно добавлен!")
            print("Продолжить?")
            answ1 = input()
            if answ1.lower() == "да":
                continue
            else:
                print("Программа завершена, спасибо!")
                break
        else:
            print("Хотите продолжить?")
            reply = input()
            if reply.lower() == 'да':
                continue
            else:
                print("Программа завершена, спасибо!")
            break

show(accountsData)
