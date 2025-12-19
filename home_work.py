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

price = float(input("Вартість оренди за день: "))
days = int(input("Кількість днів: "))
deposit = float(input("Сума застави: "))

rent_sum = price * days
total_pay = rent_sum + deposit
return_money = deposit
one_day_price = rent_sum / days

print(f"Загальна вартість оренди (без застави): {rent_sum} грн")
print(f"Сума до оплати з урахуванням застави: {total_pay} грн")
print(f"Сума, яку повернуть після повернення авто: {return_money} грн")
print(f"Вартість оренди за один день: {one_day_price} грн")
