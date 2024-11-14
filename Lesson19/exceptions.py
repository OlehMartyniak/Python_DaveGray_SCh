# 1. Створити  невизначену змінну та вивести відповідну помилку
try:
    print(x)
except NameError:
    print("You have an indefined variable")

# 2. Створити try / except / else / finally exception

x = 2

try:
    print(x/0)
except NameError:
    print("You have an indefined variable")
except ZeroDivisionError:
    print("You cannot divide by 0")
else:
    print("You have no errors")
finally:
    print("Finally prints this message anyways")

# 3. Створити Еxception as an error що виводитиме помилку типу даних

try:
    if not type(x) is str:
        raise TypeError("Only strings are allowed")
except Exception as error:
    print(error)

