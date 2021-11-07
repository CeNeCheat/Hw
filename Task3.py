nums = [int(input("Введите числа")),int(input()),int(input())]
print(nums)
answer = input("Вы хотите оставить последнее число в списке? ").capitalize()
if answer == "No" or answer == "Нет":
    nums.remove(nums[2])
    for i in nums:
        print(i)
elif answer == "Yes" or answer == "Да":
    for i in nums:
        print(i)
else:
    print("Неправильно ответили")