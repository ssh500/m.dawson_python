# Проигранное сражение
# Демонстрирует бесконечный цикл, while
print("Вашего героя окружила огромная армия троллей.")
print("Одинокий герой достаёт меч из ножен, готовясь к последней битве\n")
health = 10
trolls = 0
damage = 3
while health > 0:
    trolls += 1
    health -= damage
    print("Взмахнув мечом, ваш герой истребляет злобного тролля," \
            "но сам получает повреждений на", damage, "очков.\n")
    print("Ваш герой доблестно сражался и убил", trolls, "троллей.")
print("Но увы! Он пал на поле боя.")
#input("\n\nНажмите Enter, чтобы выйти.")

