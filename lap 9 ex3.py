s = input().strip()

parts = s.split('.')

# перевірка кількості частин
if len(parts) != 4:
    print("No")
else:
    ok = True
    for part in parts:
        if not part.isdigit():
            ok = False
            break
        num = int(part)
        if num < 0 or num > 255:
            ok = False
            break

    if ok:
        print("Yes")
    else:
        print("No")
