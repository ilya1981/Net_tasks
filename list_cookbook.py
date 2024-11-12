import json
with open('Receipt.txt', encoding='utf-8') as file:
    cook_book = {}
    for item in file:
        receipt = item.strip()
        count = file.readline()
        ingredients = []
        for p in range(int(count)):
            rec = file.readline().strip().split('|')
            product, quantity, name = rec
            ingredients.append({'ingridient_name': product, 'quantity': quantity, 'measure': name })
            cook_book[receipt] = ingredients
        file.readline()
    print(cook_book)

    
