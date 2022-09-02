#программа поиска номеров телефона и адресов электронной почты через буффер обмена
import pyperclip, re

#создаем объект регулярного выражения номеров телефонов
phones = re.compile(r'''(
(\+\s?7\s?|8\s?)?
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)?
(\d{2}(-|\s)?\d{2})
(\s*?(ext|ext.|д.|доб.|доб|д)?\s*?(\d{2,5}))?
)''', re.VERBOSE)

#создаем объект регулярного выражения адресов почты
emails = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z0-9]{2,5})
)''', re.VERBOSE)

#тело программы
text = str(pyperclip.paste())
matches=[] #создаем список, в который будем добавлять все совпадения по итогам поиска
for groups in phones.findall(text):
    phoneNum = "-".join([groups[1], groups[2], groups[4], groups[6]]) #объединяем в одну строку список кортежей каждого из совпадений (groups[0])
    if groups[10] != '': #проверяем наличие добавочного номера
        phoneNum += " доб. " + groups[10]
    matches.append(phoneNum) #добавляем сформированную строку с результатом поиска в список
for groups in emails.findall(text):
    matches.append(groups[0])

if len(matches) > 0: #проверяем, что в списке есть хотя бы один результат
    pyperclip.copy('\n'.join(matches))
    print("Скопировано в буфер обмена")
    print('\n'.join(matches))
else:
    print("Телефонные номера и адреса электронной почты не найдены")

