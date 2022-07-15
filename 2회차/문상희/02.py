with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruits = list(map(str, text.split('\n')))
    cnt = 0
    new_fruit = []
    for fruit in fruits:
        if fruit.endswith('berry'):
            if fruit not in new_fruit:
                new_fruit.append(fruit)
                cnt += 1
    print(cnt)
    
for fruit2 in new_fruit:
    print(fruit2)
    