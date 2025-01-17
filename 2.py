C = ["Товар1", "Товар2", "Товар3", "Товар4", "Товар5", "Товар6", "Товар7", "Товар8", "Товар9", "Товар10", 
     "Товар11", "Товар12", "Товар13", "Товар14", "Товар15", "Товар16", "Товар17", "Товар18", "Товар19", "Товар20"]
A = [5, 8, 10, 3, 6, 12, 9, 7, 15, 4, 11, 6, 14, 2, 1, 13, 8, 10, 7, 9]
B = [100, 200, 150, 300, 250, 400, 50, 60, 80, 90, 500, 120, 70, 110, 130, 140, 160, 170, 180, 190]

# Обчислюємо загальну вартість товарів на складі
total_value = sum(A[i] * B[i] for i in range(len(A)))

# Обчислюємо середню ціну товарів
average_price = sum(B) / len(B)

# Знаходимо товар, якого найбільше на складі
max_quantity_index = A.index(max(A))
most_stocked_item = C[max_quantity_index]

# Виводимо результати
print("Загальна вартість товарів:", total_value)
print("Середня ціна товарів:", average_price)
print("Товар, якого найбільше на складі:", most_stocked_item)
