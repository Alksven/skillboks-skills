import os

file = None
try:
    file = open("23.3.txt", "w", encoding="utf8")
    number = int(input("Введите текст: "))
    file.write(str(number))
except (FileNotFoundError, PermissionError) as exc:
    print(type(exc), exc)
except ValueError as exc:
    print(type(exc), exc)
except Exception as exc:
    print(type(exc), exc)
else:
    print("Запись прошла без ошибок")
finally:
    if file and not file.closed:
        file.close()