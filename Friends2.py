while True:
    list = []
    friends = [input("Добавьте трех друзей: ").capitalize(), input().capitalize(), input().capitalize()]
    for s in friends:
        list.append(s)
    friend = input("Введите имя друга из списка")
    try:
        list.index(friend)
    except ValueError:
        print("Такого пользователя нет в списке")
        break
    answer = input("Хотите, чтобы этот человек присутсвовал на вечеринке?").capitalize()
    if answer == "Нет" or answer == 'No':
        list.remove(friend)
        print(list)
    else:
        print(list)
    break