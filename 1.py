numbers = [10, 20, 30, 40, 50, 60]

numbers.insert(1, -5)

# Знаходимо мінімальний та максимальний елемент списку
min_number = min(numbers)
max_number = max(numbers)

# Додаємо список [1, 2, 3] починаючи з третього елемента
numbers[2:2] = [1, 2, 3]

# Додаємо новий елемент із прізвищем та ім'ям
numbers.append(["Прізвище", "Ім'я"])

# Визначаємо кількість елементів у списку
element_count = len(numbers)

# Виводимо результати
print("Оновлений список:", numbers)
print("Мінімальний елемент:", min_number)
print("Максимальний елемент:", max_number)
print("Кількість елементів у списку:", element_count)
