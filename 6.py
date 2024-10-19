str_info = "Ігор, група КН-4, спеціальність Ком'ютерні науки"

group = str_info.split(", ")[1]
print("Назва групи:", group)

str_info_updated = str_info.replace("Ігор", "Яремко")
print("Змінений рядок:", str_info_updated)

words = str_info.split()
print("Кількість слів у рядку:", len(words))