with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruits = list(map(str, text.split('\n')))
    result = {}
    for fruit in fruits:
        result[fruit] = result.get(fruit, 0) + 1
    for key in result:
        print(key, result[key])