with open('CoocBook.txt', 'w', encoding='utf-8') as file:
    file.write('Омлет \n 3 \n яйцо | 2 | шт \n Молоко | 100 | мл \n Помидор | 2 | шт. \n')
with open('CoocBook.txt', 'a', encoding='utf-8') as file:
    file.write('\n')
with open('CoocBook.txt', 'a', encoding='utf-8') as file:
    file.write('\n')
with open('CoocBook.txt', 'a', encoding='utf-8') as file:
    file.write('Утка по пекински \n 4 \n Утка | 1 | шт. \n Вода | 2 | ст.л. \n Мёд |3|ст.л. \n Соевый соус | 60 | мл. \n')
with open('CoocBook.txt', 'a', encoding='utf-8') as file:
    file.write(' \n')
with open('CoocBook.txt', 'a', encoding='utf-8') as file:
    file.write(' \n')   
with open('CoocBook.txt', 'a', encoding='utf-8') as file:
    file.write('Зпеченый картофель \n 3 \n Картофель | 1 | кг. \n Чеснок | 3 | зуб. \n Сыр гауда | 100| гр.')
file.close()

with open('CoocBook.txt', encoding='utf-8') as file:
    data = file.read()
    print(type(data))
    print(data)

file.close()

