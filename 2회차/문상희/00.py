with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('2회차 문상희\n')
    f.write('Happy, Python!\n')
    for i in range(1, 6):
        f.write(f'{i}일차 파이썬 공부 중\n')
