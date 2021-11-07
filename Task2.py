list = ['Новости', 'Россия!!!', 'АмерикаГовно!', 'ПендосыТупые!']
for i in list:
    print(i)
list.insert(int(input("Введите позицию: ")), input('Введите название передачи: '))
for i in list:
    print(i)