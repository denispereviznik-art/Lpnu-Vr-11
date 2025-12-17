n = int(input())

square = n * n

if str(square).endswith(str(n)):
    print("Правда")
else:
    print("Хибно")
