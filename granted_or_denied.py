# Open or Closed
# Демонстрирует использование условия else
print('Добро пожаловать к нам в ООО "Системы безопасности".')
print('-- Безопасность - наше второе имя.\n')
password = input("Введите пароль: ")
if password == "secret":
    print("Доступ открыт.")
else:
    print("Доступ закрыт.")
input("\n\nНажмите Enter, чтобы выйти.")