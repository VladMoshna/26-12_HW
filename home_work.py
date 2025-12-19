# 1 завдання

num1 = float(input("Введіть друге число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть друге число: "))

print(f"Сума чисел: {num1 + num2 + num3}\nДобуток чисел: {num1 * num2 * num3}")

# 2 завдання

d1 = float(input("Введіть першу діагональ ромба: "))
d2 = float(input("Введіть другу діагональ ромба: "))
p = (d1 / 2) ** 2 + (d2 / 2) ** 2
print(f"Периметр ромба: {p}")

# 3 завдання

salary = float(input("Введіть зарплату за місяць: "))
credit = float(input("Введіть суму кредиту: "))
duty = float(input("Введіть заборгованіть за комунальні послуги: "))

print(f"Після всіх виплат у вас залишиться: {salary - (credit + duty)}")

# 4 завдання 

kilometr = float(input("Введіть відстань(км): "))
cost = float(input("Введіть витрату палива(л/100 км): "))
price = float("Введіть ціну палива(грн/1 л): ")

result = ((kilometr / 100) * cost) * price

print(f"Загальна вартість поїздки: {result}")

# 5 завдання

total_amount = float(input("Введіть загальну суму рахунку: "))
number_of_people = int(input("Введіть кількість осіб: "))

tips = (total_amount / 100) * 15
total_amount += tips

print(f"Кожна людина повинна заплатити: {total_amount / number_of_people}")

# 6 завдання

rent_cost = float(input("Введіть вартість оренди за день: "))
number_of_days = int(input("Введіть на скільки днів ви арендували автомобіль: "))
sum_outpost = float(input("Введіть суму застави: "))

res = rent_cost * number_of_days

print(f"Вам треба заплатити(застава повертається): {res}")
print(f"Вартість оренди за один день: {res / number_of_days}")
