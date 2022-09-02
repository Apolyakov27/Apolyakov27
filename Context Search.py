#программа контекстного поиска по тексту
import re
import pyperclip
def func(text, query):
    phoneNum = re.compile(r"[^.?!]*?"+query+r"[^.!?]*", re.I)
    mo = phoneNum.findall(text)
    #print("Number found: " + str(mo))
    for i in mo:
        i = i.strip()+"."
        print(i)
#a = "Росатом вперед! Мы за Росатом! Это инновационное предприятие России. Росатом Латинская Америка. Мы лучшие."
print("Что ищем?")
query = input()
print("Где ищем?")
b = input()
func(b, query)
