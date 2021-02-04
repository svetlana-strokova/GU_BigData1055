# 4 Задание Строка с пробелами, выводим каждое слово с новой строки, берем первые 10 букв в длинном слове

text = input('Введите произвольные слова через символ пробел - ')
text.split( )
text = text.split( )
#for element in text:
#    print(element)
i = 0
while i < len(text) :
    print( str(i + 1) + '. ' + str(text[i]) )
    i += 1



