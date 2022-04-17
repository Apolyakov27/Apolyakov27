print("Добрый день. Вам будут предложены 5 предложений с пропусками и вариантами ответов.\nВам надо ввести правильный вариант ответа и нажать Enter.")
print("Пожалуйста, введите Ваше имя")
name = input()
print("Для начала теста нажмите Enter")
correct = 0
total = 0
answers = []
start = input()
if start == "":
    with open(u"/Users/alexey/Desktop/Разное/Python/Экзаменатор/Test copy.txt", "r") as a:
        while True:
            task = a.readline().strip()
            if not task or task == "":
                break
            for i in range(3):
                answers.append(a.readline().strip())
            true = a.readline().strip().lower()
            omit = a.readline().strip()
            with open(u"/Users/alexey/Desktop/Разное/Python/Экзаменатор/"+name+".txt", "a") as b:
                print(task)
                taskb = b.write(task + "\n")
                for x in answers:
                    print(x)
                    xb = b.write(x + "\n")
                answers = []
                reply = input().lower()
                replyb = b.write("Ваш ответ: " + reply + "\n")
                total += 1
                if reply == true:
                    correct += 1
                    correct_response = "Правильно!\n"
                    correct_responseb = b.write(correct_response + "\n")
                else:
                    wrong_response = "Неверно. Правильный ответ: " + true + "\n\n"
                    wrong_responseb = b.write(wrong_response)
result = f"Вы ответили правильно на {correct} вопросов из {total}."
print(result)
with open(u"/Users/alexey/Desktop/Разное/Python/Экзаменатор/"+name+".txt", "a") as b:
    resultb = b.write(result)

