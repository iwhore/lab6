import random

# Генеруємо список із 25 елементів у діапазоні від -50 до 50
random_list = [random.randint(-50, 50) for _ in range(25)]

# Додатні елементи у список А1
A1 = [x for x in random_list if x > 0]

# Від'ємні елементи у список А2
A2 = [x for x in random_list if x < 0]

# Виводимо результати
print("Список A1 (додатні):", A1)
print("Список A2 (від'ємні):", A2)