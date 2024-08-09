# Бесполезные факты
#
# Узнаёт у пользователя его / её личные данные и выдаёт несколько фактов.
# о нём /ней. Эти факты истинны, но совершенно бесполезны.

name = input("Hello. What's yor name? ")
age = input("How old is you? ")
age = int(age)
seconds = age * 365 * 24 * 60 * 60
weight = int(input("Good, and last question. What's your weight in kilogramms. "))
moon_weight = weight / 6
print(name.title(), "you are:", age, "years", ",", weight, "killogramms")
print("Your age more than", seconds, "seconds")
print("\nЗнаете ли вы, что на Луне вы весили бы всего", moon_weight, "kg")
sun_weight = weight * 27.1
print("А вот находясь на Солнце, вы бы весили", sun_weight, "kg (Но увы это продолжалось бы недолго...)")
input("\n\nPress Enter, to exit.")