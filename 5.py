info = """Мене звати Ігор. Я студент. Мені подобається програмування. 
Я вивчаю Python. Моє хобі — читання книг. Я люблю подорожувати.
Моя улюблена страва — піца. Я люблю слухати музику. Мені подобаються тварини.
Я планую стати програмістом."""

# Підраховуємо кількість символів 'а'
count_a = info.count('а')

# Виводимо речення по одному в рядок
sentences = info.split('. ')
for sentence in sentences:
    print(sentence)

# Виводимо кількість символів 'а'
print(f"Кількість символів 'а' у тексті: {count_a}")