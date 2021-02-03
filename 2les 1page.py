# 1 Задание. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type()
text = [12345, 'Who are you', 3.14, False]
count = 0
while count < len(text):
    print(text[count])
    print(type(text[count]))
    count += 1
#через цикл for
for element in text:
    print(element)
    print(type(element))









