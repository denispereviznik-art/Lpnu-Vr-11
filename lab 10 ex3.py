import matplotlib.pyplot as plt
import os

# Визначаємо голосні літери українського алфавіту
vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"

# Якщо файлу немає — створюємо з прикладом тексту
if not os.path.exists("text.txt"):
    with open("text.txt", "w", encoding="utf-8") as file:
        file.write("Це приклад тексту для побудови гістограми голосних літер. Програма працює коректно.")
    print("Створено файл 'text.txt' із прикладом тексту.")

# Зчитуємо текст із файлу
with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Підрахунок частоти голосних
counts = {}
for char in text:
    if char in vowels:
        counts[char.lower()] = counts.get(char.lower(), 0) + 1

# Побудова гістограми
plt.bar(counts.keys(), counts.values(), color='skyblue', edgecolor='black')
plt.title("Частота появи голосних літер у тексті", fontsize=14)
plt.xlabel("Голосні літери", fontsize=12)
plt.ylabel("Кількість появ", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Збереження графіка у файл
plt.savefig("histogram.png", dpi=300)
plt.show()

print("Гістограму збережено у файл 'histogram.png'.")
