# Привередливая считалка.
# Демонстрирует работу break и continue
count = 0
while True:
    count += 1
    # Завершить цикл, если он принимает значение больше 10
    if count > 10:
        break
    # Пропустить 5
    if count == 5:
        continue
    print(count)
