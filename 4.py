users = ["Mark", "Tom", "Bob", "Alice", "Tom", "Bill", "Tom", "Alex", "Shaun", "Mark"]

# Підраховуємо кількість разів, коли зустрічаються елементи
tom_count = users.count("Tom")
mark_count = users.count("Mark")
alice_count = users.count("Alice")
john_count = users.count("John")  


users.pop(2)  # Вилучаємо індекс 2
users.remove("Tom")

print(f"Tom зустрічається {tom_count} раз(ів)")
print(f"Mark зустрічається {mark_count} раз(ів)")
print(f"Alice зустрічається {alice_count} раз(ів)")
print(f"John зустрічається {john_count} раз(ів)")
print("Оновлений список:", users)