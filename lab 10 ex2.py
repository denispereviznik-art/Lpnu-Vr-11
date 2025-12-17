# створюємо та відкриваємо файл для запису
with open("letters.txt", "w", encoding="utf-8") as file:
    for i in range(1, 10):  # 9 рядків
        line = "a" * i      # у 1 рядку — 1 літера, у 2 — 2 і т.д.
        file.write(line + "\n")

print("Файл 'letters.txt' успішно створено!")
