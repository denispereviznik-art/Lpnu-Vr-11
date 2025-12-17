# зчитування вхідних даних
x1 = int(input())
y1 = int(input())
a1 = int(input())
b1 = int(input())
x2 = int(input())
y2 = int(input())

# переводимо час у хвилини
clock_start = x1 * 60 + y1
clock_end = x2 * 60 + y2
real_start = a1 * 60 + b1

# якщо час "перейшов через добу"
if clock_end <= clock_start:
    clock_end += 24 * 60

# скільки хвилин пройшло на годиннику
clock_diff = clock_end - clock_start
# wewee
# реальний час іде вдвічі швидше
real_diff = clock_diff * 2

# реальний час у хвилинах
real_time = real_start + real_diff

# переводимо назад у години і хвилини
a2 = (real_time // 60) % 24
b2 = real_time % 60

print(a2, b2)
